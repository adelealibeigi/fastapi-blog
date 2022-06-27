from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import database
import generate_token
import models
from hashing import Hash

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Invalid Credentials.')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Incorrect Password.')

    access_token = generate_token.create_access_token(
        data={'id': user.id, "email": user.email}
    )
    return {'access_token': access_token,
            'token_type': 'bearer'
            }
