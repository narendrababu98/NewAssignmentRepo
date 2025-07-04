from sqlalchemy import Column, Integer, String, Float
from database import Base


class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    pincode = Column(String(6))
    latitude = Column(Float)
    longitude = Column(Float)


