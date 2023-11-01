from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from databases import get_db
import models
from schemas import Token, TokenData

oauth2_scheme  = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = 'hjdfh2938283cnsljdckdl;asj?S?DLSWDJ22'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def create_acces_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        phone_number = payload.get("phone_number")
        if not phone_number:
            raise credentials_exception
        token_data = TokenData(phone_number=phone_number)
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_user(token:str = Depends(oauth2_scheme), db:Session=Depends(get_db)):
    credentials_exception = HTTPException(401, detail='could not validate credentials',
                                          headers={'WWW-Authenticate':'Bearer'})
    token = await verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.phone_number==token.phone_number).first()
    return user

    