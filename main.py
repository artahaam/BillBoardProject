from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from databases import engine, get_db
from routers import billboards, owners, users, auth
import models 


app = FastAPI()
app.include_router(owners.router)
app.include_router(users.router)
app.include_router(billboards.router)
app.include_router(auth.router)


models.Base.metadata.create_all(bind=engine)

