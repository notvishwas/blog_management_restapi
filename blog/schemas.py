
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class showblog(Blog):   #inherit all from Blog, which is title and body
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

    

