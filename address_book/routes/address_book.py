from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from models import Address
from sqlalchemy.orm import Session
from schemas import AddressCreate, AddressBase, AddressOut, AddressUpdate
from database import get_db
from utils import haversine
import asyncio

book = APIRouter(
    tags=["Address"],
)


# post request for creating address
@book.post('/address', response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    await asyncio.sleep(3)
    new_address = Address(**address.dict())
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address


# put request for updating address
@book.put('/address/{address_id}', response_model=AddressOut, status_code=status.HTTP_202_ACCEPTED)
async def update_address(address_id: int, address: AddressUpdate, db: Session = Depends(get_db)):
    await asyncio.sleep(3)
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        raise HTTPException(detail="Address Not Found", status_code=status.HTTP_404_NOT_FOUND)
    for key, value in address.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    return db_address


# delete request for deleting address
@book.delete('/address/{address_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(address_id: int, db: Session = Depends(get_db)):
    await asyncio.sleep(3)
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        raise HTTPException(detail="Address Not Found", status_code=status.HTTP_404_NOT_FOUND)
    db.delete(db_address)
    db.commit()


# get request for getting all addresses
@book.get('/address', response_model=List[AddressOut], status_code=status.HTTP_200_OK)
async def get_all_addresses(db: Session = Depends(get_db)):
    await asyncio.sleep(3)
    addresses = db.query(Address).all()
    return addresses


# get request for getting near by address for given coordinates
@book.get('/address/nearby', response_model=List[AddressOut], status_code=status.HTTP_200_OK)
async def get_neary_by_address(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    await asyncio.sleep(3)
    all_address = db.query(Address).all()
    nearby = [addr for addr in all_address if haversine(lat, lon, addr.latitude, addr.longitude) <= distance]
    return nearby
