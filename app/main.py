from fastapi import FastAPI
from app.api.routesUser import router as UserRouter
from app.api.routesAdmin import router as AdminRouter
from app.api.models import Base
from app.db import engine
from app.api.factory import factory_database


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(UserRouter, prefix='/users', tags=['users'])
app.include_router(AdminRouter, prefix='', tags=['admin'])
app.add_event_handler('startup', factory_database)
