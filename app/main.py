from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.middleware import cors
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import mysql.connector
import time
from pydantic_settings import BaseSettings
from sqlalchemy.orm import Session
from app import models, schema, utils, oauth2
from .database import engine, get_db
from .config import settings
##models.Base.metadata.create_all(bind=engine)
from app.routers import auth, post, user, vote

class Post(BaseModel):
    title: str
    content: str
    published: bool = True  

origins = ["*"]

app = FastAPI()
app.add_middleware(
    cors,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message":"Hello"}

