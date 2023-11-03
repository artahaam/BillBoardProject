from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import get_db
import schemas
import crud
from oauth2 import get_current_user

router = APIRouter(tags=['users'],
                #    dependencies=[Depends(get_current_user)]
                   )


@router.post('/user/new', response_model=schemas.UserShow)
async def add_usesr(user:schemas.UserAdd, db: Session = Depends(get_db)):
    return await crud.create_user(db=db, user=user)


@router.get('/admin/user/{id}', response_model=schemas.UserShow)
async def get_user_by_id(id:int, db:Session = Depends(get_db)):
    user = await crud.read_user_by_id(db=db, user_id = id)
    if not user:
        raise HTTPException(404, f'no user found with id:{id}')
    return user    


@router.get('/admin/users/', response_model=list[schemas.UserShow])
async def get_all_users(db:Session = Depends(get_db)):
    users = await crud.read_all_users(db=db)
    if not users:
        raise HTTPException(404, 'no users yet')
    return users   


@router.put('/admin/user/update/{id}', response_model=schemas.UserBase)
async def update_user(user:schemas.UserBase, id:int, db: Session=Depends(get_db)):
    return await crud.update_user(user=user, user_id=id, db=db)


@router.delete('/admin/user/delete/{id}')
async def delete_user(id:int, db:Session=Depends(get_db)):
    await crud.delete_user(db=db, user_id=id)
