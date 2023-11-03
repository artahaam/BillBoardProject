from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from databases import get_db
import schemas
import crud
import oauth2
import models
router = APIRouter(prefix='/admin', tags=['billboards',])


@router.post('/billboards/add', response_model=schemas.BillBoardRead)
async def add_billboard(billboard:schemas.BillBoardAdd, db: Session = Depends(get_db)):
        return await crud.create_billboard(db=db, billboard=billboard)


@router.get('/billboard/{id}/', response_model=schemas.BillBoardRead)
async def get_billboard_by_id(id:int, db: Session = Depends(get_db)):
    billboard = await crud.read_billboard_by_id(db=db, billboard_id=id)
    if not billboard:
        raise HTTPException(404, f'no billboard found with id:{id}')
    return billboard


@router.get('/billboards/', response_model=list[schemas.BillBoardRead])
async def get_all_billboards(db: Session = Depends(get_db),
                            #  current_user: str = Depends(oauth2.get_current_user)
                             ):
    billboards = await crud.read_all_billboards(db=db)
    if not billboards:
        raise HTTPException(404, 'no billboards yet')
    # user = db.query(models.User).filter(models.User.phone_number==current_user.phone_number).first()
    # if user.phone_number == '09162456790':
    #     return billboards 
    # else:
    #     raise HTTPException(status.HTTP_403_FORBIDDEN, 'You are not allowd')
    return billboards 


@router.put('/billboard/update/{id}', response_model=schemas.BillBoardAdd)
async def update_billboard(billboard:schemas.BillBoardAdd, id:int, db: Session=Depends(get_db)):
    return await crud.update_billboard(billboard=billboard, billboard_id=id, db=db)


@router.delete('/billboard/delete/{id}')
async def delete_billboard(id:int, db:Session=Depends(get_db)):
    await crud.delete_billboard(db=db, billboard_id=id)

