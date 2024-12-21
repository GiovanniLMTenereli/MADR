from pydentic import BaseModel, ConfigDict, EmailStr


class AccountSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class ReturnableAccount(AccountSchema):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class AccountsList(BaseModel):
    accounts: list[ReturnableAccount]
