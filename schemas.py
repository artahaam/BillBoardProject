from pydantic import BaseModel


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
    # owner : OwnerBase
    pass


class BillBoardResponse(BillBoardBase):
    pass


class OwnerRead(OwnerAdd):
    # billboards : list[BillBoardAdd]
    pass


class UserBase(BaseModel):
    phone_number : str
    class Config:
        orm_mode = True


class UserAdd(UserBase):
    password : str
    

class UserShow(UserBase):
    id : int
    pass