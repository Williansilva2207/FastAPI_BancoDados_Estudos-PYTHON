from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ORM.FastAPI.Fast_zero.models import User
from ORM.FastAPI.Fast_zero.UserSchema import UserSchema, UserPublicSchema, UserListSchema, Message
from ORM.FastAPI.Fast_zero.database import get_session

app = FastAPI()

@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.name == user.name) | (User.email == user.email)
            )
    )

    if db_user:
        if db_user.name == user.name:
            raise HTTPException(
                status_code = HTTPStatus.CONFLICT,
                detail = 'Username already exists',
            )
                
        elif db_user.email == user.email:
            raise HTTPException(
                status_code = HTTPStatus.CONFLICT,
                detail = 'Email already exists',
            )
        
    db_user = User(
        name = user.name, password = user.password, email= user.email
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.get('/users/', response_model=UserListSchema)
def read_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users= session.scalars(select(User).offset(skip).limit(limit)).all()
    return{'users':users}

@app.put('/users/{user_id}', response_model=UserPublicSchema)
def update_user(
    user_id:int, user:UserSchema, session: Session = Depends(get_session)
):
    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    try:
        db_user.name = user.name
        db_user.password = user.password
        db_user.email = user.email
        session.commit()
        session.refresh(db_user)
        return db_user
    except IntegrityError:
        raise HTTPException(
            status_code = HTTPStatus.CONFLICT,
            detail = 'Username or email already exists'
        )

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}