from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    status: str = Field(..., min_length=5)
    trading_name: str = Field(..., min_length=3)
    cnpj: int = Field(..., min_length=14)
    cpf: int = Field(..., min_length=11)
    partner: str = Field(..., min_length=4)
    email: str = Field(..., min_length=5)


class UserDB(UserSchema):
    id: int

    class Config:
        orm_mode = True
