from typing import List
from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        from_attributes = True


class showblogtitle(BaseModel):  #inherit only title from basemodel,
    title: str

    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str

class creatorshowuser(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

class showuser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        from_attributes = True


class showblog(Blog):   #inherit all from Blog, which is title and body    
    creator: creatorshowuser
    
    class Config:
        from_attributes = True    #orm mode True


class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    
    
    