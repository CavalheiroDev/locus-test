from fastapi.params import Depends
from app.db import SessionLocal
from app.api.models import User
from faker import Faker
from random import choice

status = ['Esperando documentação', 'Ativo',
          'Em análise', 'Negado', 'Cancelado']


def factory_database():
    fake = Faker('pt_BR')
    db = SessionLocal()

    for _ in range(50):

        fake_user = User(status=choice(status), trading_name=fake.company(
        ), cnpj="12345678901234", cpf="12345678901", partner=fake.name(), email=fake.email())
        db.add(fake_user)
        db.commit()
        db.refresh(fake_user)

    db.close()
