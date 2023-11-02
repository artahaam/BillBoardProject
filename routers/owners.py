from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import get_db
import schemas
import crud

router = APIRouter(prefix='/admin',tags=['owners',])


@router.post('/owners/add', response_model=schemas.OwnerAdd)
async def add_owners(owner:schemas.OwnerAdd, db:Session = Depends(get_db)):
    return await crud.create_owner(owner=owner, db=db)


@router.get('/owners/', response_model=list[schemas.OwnerRead])
async def get_all_owners(db:Session = Depends(get_db)):
    owners = await crud.read_all_owners(db=db)
    if not owners:
        raise HTTPException(404, 'no owners yet')
    return owners


@router.get('/owner/{id}', response_model=schemas.OwnerRead)
async def get_owner_by_id(id:int, db:Session = Depends(get_db)):
    owner =  await crud.read_owner_by_id(db=db, owner_id = id)
    if not owner:
        raise HTTPException(404, f'no owner found with id:{id}')
    return owner    


@router.put('/owner/update/{id}', response_model=schemas.OwnerAdd)
async def update_owner(owner:schemas.OwnerAdd, id:int, db:Session=Depends(get_db)):
    return await crud.update_owner(db=db, owner=owner, owner_id=id)


@router.delete('/owner/delete/{id}')
async def delete_owner(id:int, db:Session=Depends(get_db)):
    await crud.delete_owner(db=db, owner_id=id)

