from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.sql.sqltypes import ARRAY
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models
from .schema import CreateBillOfLadingBookmarks, CreateContainerNumberBookmarks
from .models import BillOfLadingBookmarks, ContainerNumberBookmarks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return { 
        "message": "Welcome!",
    }
    
    
@app.post("/add-bill-of-lading")
def add_bill_of_lading(data: CreateBillOfLadingBookmarks, db: Session = Depends(get_db)):
    id_already_exist = (db.query(BillOfLadingBookmarks).filter(BillOfLadingBookmarks.bill_of_lading_id == data.bill_of_lading_id).first() 
                                          or db.query(ContainerNumberBookmarks).filter(ContainerNumberBookmarks.tracking_number == data.bill_of_lading_id).first())

    if id_already_exist:
        raise HTTPException(404, {"message": "Tracking Number Already exist!"})
    else:
        to_create = BillOfLadingBookmarks(
            bill_of_lading_id= data.bill_of_lading_id,
            departure_date = data.departure_date,
            port_of_discharge =  data.port_of_discharge,
            vessel =  data.vessel,
            transhipment =  data.transhipment,
            port_of_load =  data.port_of_discharge,
            price_calculation_date =  data.price_calculation_date 
        )
        db.add(to_create)
        db.commit()
        db.refresh(to_create)
        return { 
            "success": True
        }
    
@app.post("/add-container")
def container_data(container_data: CreateContainerNumberBookmarks, db: Session =Depends(get_db)):

    id_already_exist = (db.query(ContainerNumberBookmarks).filter(ContainerNumberBookmarks.tracking_number == container_data.tracking_number).first()
                           or db.query(BillOfLadingBookmarks).filter(BillOfLadingBookmarks.bill_of_lading_id == container_data.tracking_number).first())
    
    if id_already_exist:
        raise HTTPException(404, {"message": "Tracking Number Already exist!"})
    else:
        bill_of_lading_exist = db.query(BillOfLadingBookmarks).filter(BillOfLadingBookmarks.bill_of_lading_id == container_data.bill_of_lading_id).first()
        if bill_of_lading_exist:
            
            to_create = ContainerNumberBookmarks(
                bill_of_lading_id = container_data.bill_of_lading_id,
                tracking_number = container_data.tracking_number,
                type = container_data.type,
                shipped_to = container_data.shipped_to,
                final_pod = container_data.final_pod,
                price_calculation_date = container_data.price_calculation_date,
                final_pod_eta = container_data.final_pod_eta,
            )
            db.add(to_create)
            db.commit()
            db.refresh(to_create)
            return { 
                "success": True,
            }
        else:
            raise HTTPException(404, {"message": "No Bill of lading found"})
            
    
@app.get("/track/{tracking_no}")
def get_containers_details(tracking_no: str, db: Session =Depends(get_db)):
    bill_of_lading = db.query(BillOfLadingBookmarks).filter(BillOfLadingBookmarks.bill_of_lading_id == tracking_no).first()
    if bill_of_lading:
        all_containers = db.query(ContainerNumberBookmarks).filter(ContainerNumberBookmarks.bill_of_lading_id == tracking_no).all()
        return {
            'bill_of_lading': bill_of_lading,
            'container': all_containers
            }
    else:
        container = db.query(ContainerNumberBookmarks).filter(ContainerNumberBookmarks.tracking_number == tracking_no).first()
        if container:
            return container
        else:
            raise HTTPException(404, {"message": "INVALID TRACKING NUMBER"})
