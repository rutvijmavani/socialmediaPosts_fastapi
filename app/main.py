from typing import Optional , List
from warnings import deprecated
from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from .routers import post , user , auth

import time
from sqlalchemy.orm import Session
from . import models , schemas , utils
from . database import engine , get_db


models.Base.metadata.create_all(bind = engine) 

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
 
@app.get("/")
def root():
    return {"message" : "Welcome to my API."}


