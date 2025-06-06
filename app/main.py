from fastapi import FastAPI
from .routers import post , user , auth , vote
from . import models
from . database import engine
from .config import settings
from fastapi.middleware.cors import CORSMiddleware




#models.Base.metadata.create_all(bind = engine) 
# above command tells sqlalchemy to run the create statement so that it generates all the tables when it first started up

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
 
@app.get("/")
def root():
    return {"message" : "Welcome to my API."}


