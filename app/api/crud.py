from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import column
from app.api.models import User
from app.api.schemas import UserSchema


def get_all(db: Session):
    return db.query(User).all()


def get_pagination(db: Session, number_page: int, size: int):
    offset = size * (number_page - 1)
    query = db.query(User).offset(offset).limit(size).all()
    total_rows = db.query(User.id).count()
    return {'users': query, 'total_rows': total_rows}


def post(db: Session, data: UserSchema):
    user = User(data.status, data.trading_name, data.cnpj,
                data.cpf, data.partner, data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def put(db: Session, user: User, status: str = None, trading_name: str = None, cnpj: int = None,
        cpf: int = None, partner: str = None, email: str = None):
    if status:
        user.status = status
    if trading_name:
        user.trading_name = trading_name
    if cnpj:
        user.cnpj = cnpj
    if cpf:
        user.cpf = cpf
    if partner:
        user.partner = partner
    if email:
        user.email = email
    db.commit()
    return user


def delete(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user
