from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException
import models
import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def hash(password):
    return pwd_context.hash(password)


async def password_verify(raw_password, hashed_password):
    return pwd_context.verify(raw_password, hashed_password)


async def create_billboard(db: Session, billboard: schemas.BillBoardAdd):
    new_billboard = models.BillBoard(**billboard.dict())
    db.add(new_billboard)
    db.commit()
    db.refresh(new_billboard)
    return new_billboard


async def read_billboard_by_id(db: Session, billboard_id: int):
    return db.query(models.BillBoard).filter(models.BillBoard.id == billboard_id).first()


async def read_all_billboards(db: Session):
    billboards = db.query(models.BillBoard).all()
    return billboards


async def update_billboard(billboard: schemas.BillBoardAdd, billboard_id: int, db=Session):
    query = db.query(models.BillBoard).filter(models.BillBoard.id == billboard_id)
    db_billboard = query.first()
    if db_billboard == None:
        raise HTTPException(404, f'owner with the id:{billboard_id} does not exist')
    query.update(billboard.dict(), synchronize_session=False)
    db.commit()
    print(db_billboard)
    return db_billboard


async def create_owner(db: Session, owner: schemas.OwnerBase):
    new_owner = models.Owner(**owner.dict())
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner


async def read_all_owners(db: Session):
    owners = db.query(models.Owner).all()
    return owners


async def read_owner_by_id(owner_id: int, db=Session):
    return db.query(models.Owner).filter(models.Owner.id == owner_id).first()


async def update_owner(owner: schemas.OwnerAdd, owner_id: int, db=Session):
    query = db.query(models.Owner).filter(models.Owner.id == owner_id)
    db_owner = query.first()
    if db_owner == None:
        raise HTTPException(
            404, f'owner with the id:{owner_id} does not exist')
    query.update(owner.dict(), synchronize_session=False)
    db.commit()
    return db_owner


async def delete_owner(owner_id: int, db=Session):
    query = db.query(models.Owner).filter(models.Owner.id == owner_id)
    db_owner = query.first()
    if db_owner == None:
        raise HTTPException(
            404, f'owner with the id:{owner_id} does not exist')
    query.delete(synchronize_session=False)
    db.commit()


async def create_user(db: Session, user: schemas.UserAdd):
    user.password = await hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def read_all_users(db=Session):
    users = db.query(models.User).all()
    return users


async def read_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def delete_billboard(billboard_id: int, db=Session):
    query = db.query(models.BillBoard).filter(models.BillBoard.id == billboard_id)
    db_billboard = query.first()
    if db_billboard == None:
        raise HTTPException(
            404, f'billboard with the id:{billboard_id} does not exist')
    query.delete(synchronize_session=False)
    db.commit()

