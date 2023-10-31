from pydantic import BaseModel
from datetime import datetime


class OwnerBase(BaseModel):
    name : str
    phone_number : str
    
    class Config:
        orm_mode = True

class OwnerAdd(OwnerBase):
    pass
    

class BillBoardBase(BaseModel):
    location : str
    width : int
    height : int
    is_available : bool
    
    class Config:
        orm_mode = True


class BillBoardAdd(BillBoardBase):
    code : str
    rent : int
    reserved_at : str
    reserved_until : str
    owner_id : int


class BillBoardRead(BillBoardAdd):
    id : int
    created_at : datetime
    # owner : OwnerBase
    


class BillBoardResponse(BillBoardBase):
    pass


class OwnerRead(OwnerAdd):
    id : int
    created_at : datetime
    # billboards : list[BillBoardAdd]
    


class UserBase(BaseModel):
    phone_number : str
    class Config:
        orm_mode = True


class UserAdd(UserBase):
    password : str
    
class UserLogin(UserAdd):
    pass
    
class UserShow(UserBase):
    id : int
    created_at : datetime

    
class Token(BaseModel):
    access_token : str
    token_type : str
    # class Config:
    #     orm_mode = True


class TokenData(BaseModel):
    phone_number : str | None = None
    # class Config:
    #     orm_mode = True