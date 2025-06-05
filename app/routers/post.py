from fastapi import FastAPI , Response , status , HTTPException , Depends , APIRouter
from typing import List, Optional
from .. import models , schemas  , oauth2
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter(
    prefix = "/posts",
    tags = ['Posts']
)

#@router.get("/" , response_model = List[schemas.PostOut])
@router.get("/" , response_model = List[schemas.PostOut])
def get_posts(db : Session = Depends(get_db) , 
              current_user : int = Depends(oauth2.get_current_user) , 
              limit : int = 10 , skip : int = 0 ,
              search : Optional[str] = ""):
    # if you only want to fetch the posts of the user who is currently logged in
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    #results = db.query(models.Post).join(models.Vote , models.Vote.post_id == models.Post.id , isouter = True)
    #print(results) 
    #SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content,\
    #posts.published AS posts_published, posts.created_at AS posts_created_at, posts.owner_id AS posts_owner_id

    posts = db.query(models.Post , func.count(models.Vote.post_id).label("votes")).join(
        models.Vote , models.Vote.post_id == models.Post.id , isouter = True).group_by(models.Post.id)\
            .filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
    


@router.post("/" , status_code = status.HTTP_201_CREATED , response_model= schemas.PostResponse)
def create_posts(post : schemas.PostRequest , db : Session = Depends(get_db) ,
                  current_user : int = Depends(oauth2.get_current_user)):
    #new_post = models.Post(
    #    title = post.title , content = post.content , published = post.published
    #) this is one way of inserting data
    new_post = models.Post(owner_id = current_user.id , **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
 
@router.get("/{id}" , response_model = schemas.PostOut)
def get_posts(id : int , db : Session = Depends(get_db) , 
              current_user : int = Depends(oauth2.get_current_user)):
    
    #post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post , func.count(models.Vote.post_id).label("votes")).join(
        models.Vote , models.Vote.post_id == models.Post.id , isouter = True).group_by(models.Post.id)\
        .filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"Post with id: {id} was not found")
    
    # if you only allow the user to fetch the post created by the logged in user
    #if post.owner_id != current_user.id:
    #    raise HTTPException(status_code = status.HTTP_403_FORBIDDEN , detail = "Not authorized to perform requested action!")

    return post

@router.delete("/{id}" , status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int , db : Session = Depends(get_db) , 
                current_user : int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"post with id: {id} does not exist!")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN , detail = "Not authorized to perform requested action!")
    
    post_query.delete(synchronize_session = False)
    db.commit()

    return Response(status_code = status.HTTP_204_NO_CONTENT )

@router.put("/{id}" , response_model = schemas.PostResponse)
def update_post(id: int, post: schemas.PostRequest, db: Session = Depends(get_db) ,
                current_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
        
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} does not exist")
    
    if updated_post.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN , detail = "Not authorized to perform requested action!")
    
    post_query.update(post.dict() , synchronize_session = False)
    db.commit()
    return post_query.first()