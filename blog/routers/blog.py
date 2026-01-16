from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schemas, models, database
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Blogs']
)
get_db = database.get_db


@router.get('/blog', status_code=status.HTTP_200_OK, response_model=list[schemas.showblog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs 

@router.post('/blog', status_code=status.HTTP_201_CREATED)   #type status. then created -.> will autocomplete to HTTP_201.....
def create(request: schemas.Blog, db: Session = Depends(get_db)):       #use Blog -> schemas.Blog 
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}
    

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)     #query me request ko as a dictionary pass kra
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    
    blog.update(request.dict())
    db.commit()
    return 'updated yara'



@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showblog)  #show full blog, using showblog schema (Blog class inherited)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'blog with the id {id} is not available'}
        #or
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')

    return blog


@router.get('/blog_title/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showblogtitle)  #show only title, using different schema (baseclass title inherited)
def show_title_only(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')

    return blog