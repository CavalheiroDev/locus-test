from sqlalchemy import Column, Text, Integer, VARCHAR
from app.db import Base


class User(Base):

    __tablename__ = 'users'

    id = Column('id', Integer, autoincrement=True,
                primary_key=True, unique=True)
    status = Column('status', Text(125), nullable=False)
    trading_name = Column('nome_fantasia', Text(125), nullable=False)
    cnpj = Column('cnpj', VARCHAR(14), nullable=False)
    cpf = Column('cpf', VARCHAR(11), nullable=False)
    partner = Column('socio', Text(60), nullable=False)
    email = Column('email', VARCHAR(45), nullable=False)

    def __init__(self, status, trading_name, cnpj, cpf, partner, email):
        self.status = status
        self.trading_name = trading_name
        self.cnpj = cnpj
        self.cpf = cpf
        self.partner = partner
        self.email = email
