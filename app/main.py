from typing import Optional
from fastapi import FastAPI , Response , status , HTTPException , Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from . database import engine , get_db

models.Base.metadata.create_all(bind = engine) 

app = FastAPI()


class Post(BaseModel): 
    title : str
    content : str
    published : bool = True
    #rating : Optional[int] = None
 
@app.get("/")
def root():
    return {"message" : "Welcome to my API."}

@app.get("/posts")
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data" : posts}


@app.post("/posts" , status_code = status.HTTP_201_CREATED)
def create_posts(post : Post , db : Session = Depends(get_db)):
    print(post.dict())
    #new_post = models.Post(
    #    title = post.title , content = post.content , published = post.published
    #) this is one way of inserting data
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data" :  new_post}
 
@app.get("/posts/{id}")
def get_posts(id : int , db : Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"Post with id: {id} was not found")

    return{"post_detail" : post}

@app.delete("/posts/{id}" , status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int , db : Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"post with id: {id} does not exist!")
    
    post.delete(synchronize_session = False)
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT )

@app.put("/posts/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
        
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} does not exist")
    
    post_query.update(post.dict() , synchronize_session = False)
    db.commit()
    return{"data": post_query.first()}