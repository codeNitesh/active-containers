from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import ARRAY
from .database import Base
from sqlalchemy import Date, Column, String, Boolean, Integer

class BillOfLadingBookmarks(Base):
    __tablename__ = 'bill_of_lading_bookmarks'

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    
    bill_of_lading_id = Column(String, unique=True, index=True)
    departure_date = Column(Date)
    port_of_discharge = Column(String)
    vessel = Column(String)
    transhipment = Column(String)
    port_of_load = Column(String)
    price_calculation_date = Column(Date)
                
class ContainerNumberBookmarks(Base):
    __tablename__ = 'container_no_bookmarks'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
        
    tracking_number = Column(String, unique=True, index=True)
    
    type = Column(String)
    shipped_to = Column(String)
    final_pod = Column(String)
    price_calculation_date = Column(Date)
    final_pod_eta = Column(Date, nullable=true)
        
    bill_of_lading_id = Column(String)
    
  
