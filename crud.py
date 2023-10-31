from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
async def hash(password):
    return pwd_context.hash(password)


async def password_verify(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)


async def read_billboard_by_id(db:Session, billboard_id:int):
    return db.query(models.BillBoard).filter(models.BillBoard.id == billboard_id).first()


async def read_all_billboards(db:Session):
    billboards = db.query(models.BillBoard).all()
    return billboards


async def read_all_owners(db:Session):
    owners = db.query(models.Owner).all()
    return owners


async def create_billboard(db:Session, billboard:schemas.BillBoardAdd):
    new_billboard = models.BillBoard(**billboard.dict())
    db.add(new_billboard)
    db.commit()
    db.refresh(new_billboard)
    return new_billboard


async def create_owner(db:Session, owner:schemas.OwnerBase):
    new_owner = models.Owner(**owner.dict())
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner


async def create_user(db:Session, user:schemas.UserAdd):
    user.password = await hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def read_user_by_id(db:Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def read_owner_by_id(owner_id:int, db=Session):
    return db.query(models.Owner).filter(models.Owner.id == owner_id).first()


async def read_all_users(db=Session):
    users = db.query(models.User).all()
    return users 