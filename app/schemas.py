from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import Optional

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

class UserCreate(BaseModel):
    email : EmailStr 
    password : str 

class UserResponse(BaseModel):
    id : int 
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True 

class UserLogin(BaseModel):
    email : EmailStr
    password : str 

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None