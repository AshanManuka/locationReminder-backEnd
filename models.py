from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Place(Base):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True, index=True)
    placename = Column(String(50))
    
    