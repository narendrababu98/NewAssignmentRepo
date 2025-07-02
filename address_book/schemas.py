from pydantic import BaseModel, condecimal, constr


class AddressBase(BaseModel):
    name: str
    street: str
    city: str
    state: str
    pincode: constr(min_length=6, max_length=6)
    latitude: condecimal(ge=-90, le=90)
    longitude: condecimal(ge=-180, le=180)


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    pass


class AddressOut(AddressBase):
    id: int

    class Config:
        orm_mode = True
