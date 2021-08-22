from fastapi import FastAPI
from app.api.routesUser import router as UserRouter
from app.api.routesAdmin import router as AdminRouter
from app.api.models import Base
from app.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(UserRouter, prefix='/users', tags=['users'])
app.include_router(AdminRouter, prefix='', tags=['admin'])
