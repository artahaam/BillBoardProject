from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models 
import schemas
import crud
from databases import SessionLocal, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/admin/owners/add', response_model=schemas.OwnerAdd)
async def add_owners(owner:schemas.OwnerAdd, db:Session = Depends(get_db)):
    return await crud.create_owner(owner=owner, db=db)


@app.post('/admin/billboards/add', response_model=schemas.BillBoardAdd)
async def add_billboard(billboard:schemas.BillBoardAdd, db: Session = Depends(get_db)):
        return await crud.create_billboard(db=db, billboard=billboard)


@app.post('/user/new', response_model=schemas.UserShow)
async def add_usesr(user:schemas.UserAdd, db: Session = Depends(get_db)):
    return await crud.create_user(db=db, user=user)


@app.get('/admin/billboard/{id}/', response_model=schemas.BillBoardRead)
async def get_billboard_by_id(id:int, db: Session = Depends(get_db)):
    billboard = await crud.read_billboard_by_id(db=db, billboard_id=id)
    if not billboard:
        raise HTTPException(404, f'no billboard found with id:{id}')
    return billboard


@app.get('/admin/billboards/', response_model=list[schemas.BillBoardRead])
async def get_all_billboards(db: Session = Depends(get_db)):
    billboards = await crud.read_all_billboards(db=db)
    if not billboards:
        raise HTTPException(404, 'no billboards yet')
    return billboards 


@app.get('/admin/owners/', response_model=list[schemas.OwnerRead])
async def get_all_owners(db:Session = Depends(get_db)):
    owners = await crud.read_all_owners(db=db)
    if not owners:
        raise HTTPException(404, 'no owners yet')
    return owners


@app.get('/admin/owner/{id}', response_model=schemas.OwnerRead)
async def get_owner_by_id(id:int, db:Session = Depends(get_db)):
    owner =  await crud.read_owner_by_id(db=db, owner_id = id)
    if not owner:
        raise HTTPException(404, f'no owner found with id:{id}')
    return owner    


@app.get('/admin/user/{id}', response_model=schemas.UserShow)
async def get_user_by_id(id:int, db:Session = Depends(get_db)):
    user = await crud.read_user_by_id(db=db, user_id = id)
    if not user:
        raise HTTPException(404, f'no user found with id:{id}')
    return user    


@app.get('/admin/users/', response_model=list[schemas.UserShow])
async def get_all_users(db:Session = Depends(get_db)):
    users = await crud.read_all_users(db=db)
    if not users:
        raise HTTPException(404, 'no users yet')
    return users   
