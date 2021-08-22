from app.api.models import User
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.crud import get_all, post, put, delete, get_pagination
from app.api.schemas import UserDB, UserQuery, UserSchema
from app.db import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/', response_model=List[UserDB], status_code=status.HTTP_200_OK)
def read_all_users(db: Session = Depends(get_db)):

    users = get_all(db=db)
    if not users:
        return HTTPException(404, 'Nenhum item encontrado.')

    return users


@router.get('/page/{number_page}', response_model=List[UserDB], status_code=status.HTTP_200_OK)
def read_users_pagination(number_page: int, db: Session = Depends(get_db), size: int = 10):
    users = get_pagination(
        db=db, number_page=number_page, size=size)
    if not users:
        return HTTPException(404, 'Nenhum item encontrado.')
    return users


@ router.post('/', response_model=UserDB, status_code=status.HTTP_201_CREATED)
def create_user(*, db: Session = Depends(get_db), data: UserSchema):
    user = post(db=db, data=data)
    return user
