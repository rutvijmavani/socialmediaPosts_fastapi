from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel): #request structure
    title : str
    content : str
    published : bool = True

class PostRequest(PostBase):
    pass 

class UserResponse(BaseModel):
    id : int 
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True
        
class PostResponse(PostBase):
    # for response result structure 
    id : int
    created_at : datetime
    owner_id : int 
    owner : UserResponse
    class Config: #enables reading of orm response from sqlalchemy aprat from dictionary. 
        orm_mode = True

class PostOut(BaseModel):
    Post : PostResponse
    votes : int
    class Config: #enables reading of orm response from sqlalchemy aprat from dictionary. 
        orm_mode = True


class UserCreate(BaseModel):
    email : EmailStr 
    password : str 

 

class UserLogin(BaseModel):
    email : EmailStr
    password : str 

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(ge = 0 , le = 1) # type: ignore