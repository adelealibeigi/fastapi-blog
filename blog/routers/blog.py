from typing import List

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

import database
from oath2 import get_current_user
from helper import blog
import schemas

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def blog_list(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogBase, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db,current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def blog_detail(id: int, response: Response, db: Session = Depends(database.get_db)):
    return blog.detail(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, )
def destroy_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)
