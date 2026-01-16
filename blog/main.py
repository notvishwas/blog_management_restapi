from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user,authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)     #importtant line, uses model we created in database to make shit happens

app.include_router(authentication.router) 
app.include_router(blog.router) 
app.include_router(user.router)






# def get_db():
#     db = sessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()





# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
# def destroy(id, db: Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
    
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {'done'}
    

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)     #query me request ko as a dictionary pass kra
    
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    
#     blog.update(request.dict())
#     db.commit()
#     return 'updated yara'


# @app.get('/blog', status_code=status.HTTP_200_OK, response_model=list[schemas.showblog], tags=['Blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showblog, tags=['Blogs'])  #show full blog, using showblog schema (Blog class inherited)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {'detail': f'blog with the id {id} is not available'}
#         #or
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')

#     return blog


# @app.get('/blog_title/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showblogtitle, tags=['Blogs'])  #show only title, using different schema (baseclass title inherited)
# def show_title_only(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {id} is not available')

#     return blog


#from passlib.context import CryptContext                                    line 80, 81, 86, 90
#pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')              

# @app.post('/user', response_model=schemas.showuser, tags=['Users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
#     #hashed_pass = pwd_cxt.hash(request.password)  



#     new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))      #new_user = models.User(name = request.name, email = request.email, password = hashed_pass)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model=schemas.showuser, tags=['Users'])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} not found')
    
#     return user