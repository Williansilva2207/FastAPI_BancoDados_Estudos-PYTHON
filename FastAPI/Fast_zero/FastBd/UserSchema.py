from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

class UserDB(UserSchema):
    id: int

class UserListSchema(BaseModel):
    users: list[UserPublicSchema]