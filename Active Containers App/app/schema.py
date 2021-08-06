from pydantic import BaseModel
from typing import Optional
from datetime import date
from typing import List, Optional

from sqlalchemy.sql.sqltypes import ARRAY

class CreateContainerNumberBookmarks(BaseModel):
    tracking_number: str
    type: str
    shipped_to: str
    final_pod: str
    price_calculation_date: date
    final_pod_eta: Optional[date]
    bill_of_lading_id: str
    
    class Config:
        orm_mode = True
         
class ContainerNumberBookmarksRequest(CreateContainerNumberBookmarks):
    id: str
    
    class Config:
        orm_mode = True

class CreateBillOfLadingBookmarks(BaseModel):
    bill_of_lading_id: str
    departure_date: date
    port_of_discharge: str
    vessel: str
    transhipment: str
    port_of_load: str
    price_calculation_date: date
    
    class Config:
        orm_mode = True
      
class BillOfLadingBookmarksRequest(CreateBillOfLadingBookmarks):
    id: str
    
    class Config:
        orm_mode = True


