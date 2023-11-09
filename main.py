from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from databases import engine, get_db
from routers import billboards, owners, users, auth
import models 
from config import settings

app = FastAPI()
app.include_router(owners.router)
app.include_router(users.router)
app.include_router(billboards.router)
app.include_router(auth.router)

# origins = ['*']
origins = [
    "http://localhost",
    "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

