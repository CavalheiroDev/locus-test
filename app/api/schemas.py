from typing import Optional, List
from pydantic import BaseModel, Field


class UserQuery(BaseModel):
    status: Optional[str] = None
    cnpj: Optional[str] = None
    cpf: Optional[str] = None
    ordering: Optional[str] = None
    reverse: Optional[bool] = False


class UserSchema(BaseModel):
    id: int = Field(...)
    status: str = Field(..., min_length=5)
    trading_name: str = Field(..., min_length=3)
    cnpj: str = Field(..., min_length=14, max_length=14)
    cpf: str = Field(..., min_length=11, max_length=11)
    partner: str = Field(..., min_length=4)
    email: str = Field(..., min_length=5)

    class Config:
        orm_mode = True


class UserDB(BaseModel):
    next_page: int
    previous_page: int
    items: List[UserSchema]

    class Config:
        orm_mode = True
