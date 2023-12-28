from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional



class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class User(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    title: str
    content: str
    published: bool
    owner_id: int
    owner: UserResponse
    class Config:
        orm_mode = True    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)