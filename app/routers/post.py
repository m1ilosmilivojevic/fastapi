from typing import List, Optional
from app import models, schema, utils, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, get_db
from random import randrange

router = APIRouter(
    prefix="/posts"
)  
        
@router.get("/get/{id}", response_model=schema.Post)
def get_post(id: int, db: Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post
   ## if not post:
      ##  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
               ##             detail=f"post with id: {id} was not found" )
      ##  response.status_code = status.HTTP_404_NOT_FOUND
       ## return {'message': f"post with id: {id} was not found"}
  ##  return {"post data": post}

@router.get("/getall", response_model=List[schema.Post])
def get_post(db: Session=Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return post


@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/patchpost/{id}")
def update_post(id: int, updated_post: schema.Post,  db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"not authorized to perform requested action")
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}
    
@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_post(post: schema.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/schemaget/{id}", response_model=schema.Post)
def schema_get(id: int, db: Session = Depends(get_db)):
    get_post= db.query(models.Post).filter(models.Post.id == id).first()
    if get_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    return get_post