from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

import database
import schemas
# pwd_cxd = CryptContext(schemes=['bcrypt'], deprecated='auto')
from helper import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def user_detail(id: int, db: Session = Depends(database.get_db)):
    return user.detail(id, db)
