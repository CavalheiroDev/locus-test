from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.api.crud import get_all, post, get_pagination
from app.api.schemas import UserDB, UserQuery, UserSchema
from app.db import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/', response_model=List[UserSchema], status_code=status.HTTP_200_OK)
def read_all_users(db: Session = Depends(get_db)):

    users = get_all(db=db)
    if not users:
        return HTTPException(404, 'Nenhum item encontrado.')

    return users


@router.get('/page/{number_page}', response_model=UserDB, status_code=status.HTTP_200_OK)
def read_users_pagination(number_page: int, db: Session = Depends(get_db), size: int = 10):
    response = get_pagination(
        db=db, number_page=number_page, size=size)

    total_pages = int(response['total_rows']) / 10
    next_page = number_page + 1 if number_page != total_pages else total_pages
    previous_page = number_page - 1 if number_page != total_pages else total_pages - 1
    if not response['users']:
        json_response = {
            'total_pages': total_pages,
            'next_page': next_page,
            'previous_page': previous_page,
            'items': response['users'],

        }
        return json_response

    json_response = {
        'total_pages': total_pages,
        'next_page': next_page,
        'previous_page': previous_page,
        'items': response['users'],

    }

    return json_response


@router.post('/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(*, db: Session = Depends(get_db), data: UserSchema):
    user = post(db=db, data=data)
    return user
