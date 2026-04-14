from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from .UserSchema import UserSchema, UserPublicSchema, UserDB, UserListSchema

app = FastAPI()

database = []

@app.get("/")
def root():
    return {"message": "Olá Mundo!"}

@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: UserSchema):
    use_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(use_with_id)
    return use_with_id

@app.get("/users/", response_model=UserListSchema)
def read_users():
    return {'users': database}

@app.put('/users/{user_id}', response_model=UserPublicSchema)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    use_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = use_with_id
    return use_with_id

@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    del database[user_id - 1]
    return {'message': 'User deleted'}

@app.post('/users/test', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def crate_user_test(user: UserSchema):
    use_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(use_with_id)
    print("PRINT FUNCIONANDO:", user)
    return use_with_id