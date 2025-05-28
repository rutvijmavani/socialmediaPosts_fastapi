from pydantic import BaseModel
from datetime import datetime

"""class Post(BaseModel): 
    title : str
    content : str
    published : bool = True

class CreatePost(BaseModel):
    title : str
    content : str
    published : bool = True

class UpdatePost(BaseModel):
    title : str
    content : str
    published : bool"""

class PostBase(BaseModel): #request structure
    title : str
    content : str
    published : bool = True

class PostRequest(PostBase):
    pass 

class PostResponse(PostBase): # for response result structure 
    created_at : datetime
    class Config: #enables reading of orm response from sqlalchemy aprat from dictionary. 
        orm_mode = True

