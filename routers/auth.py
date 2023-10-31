from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from databases import get_db
import schemas, models
from crud import password_verify
import oauth2


router = APIRouter(tags=['login',])


@router.post('/login', response_model=schemas.Token)
async def login(user_credentials:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.phone_number == user_credentials.username).first()
    if not user:
        raise  HTTPException(status.HTTP_403_FORBIDDEN, 'Invalid credentials')
    if not await password_verify(user_credentials.password, user.password):
        raise  HTTPException(status.HTTP_403_FORBIDDEN, 'Invalid credentials')
    access_token = await oauth2.create_acces_token(data={'phone_number':user.phone_number,})
    token = schemas.Token(access_token=access_token, token_type='bearer')    
    # return {"access_token" : access_token, "token_type" : "bearer"}
    return token
