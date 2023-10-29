from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases import get_db
import schemas
import crud

router = APIRouter(prefix='/admin')

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
async def get_all_billboards(db: Session = Depends(get_db)):
    billboards = await crud.read_all_billboards(db=db)
    if not billboards:
        raise HTTPException(404, 'no billboards yet')
    return billboards 
