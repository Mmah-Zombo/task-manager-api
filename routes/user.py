from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from schemas.user import User as UserCreate, UserResponse
from sqlalchemy.orm import Session
from typing import List
from crud import user as user_crud
from utils.auth import hash_password, verify_password, generate_token
from dependencies.auth import get_current_user
from models.user import User


router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user:
        return HTTPException(status_code=401, detail="Unauthorized")
    return user_crud.get_all(db)


@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = user_crud.get_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post('/', response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_by_username(user_data.name, db)
    if db_user:
        raise HTTPException(status_code=403, detail="Username already exists")

    hashed_password = hash_password(user_data.password)
    if not hashed_password:
        raise HTTPException(status_code=500, detail="Could not hash password")

    user = UserCreate(name=user_data.name, password=hashed_password)
    new_user = user_crud.create(user, db)
    if not new_user:
        raise HTTPException(status_code=500, detail="Could not create user")

    return new_user


@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = user_crud.get_by_username(form_data.username, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user_password = verify_password(form_data.password, db_user.password)
    if not db_user_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    new_token = generate_token({"sub": form_data.username})
    if not new_token:
        raise HTTPException(status_code=500, detail="Could not generate token")

    return {"access_token": new_token, "token_type": "bearer"}


@router.post('/logout')
def logout(current_user: User = Depends(get_current_user)):
    pass


@router.delete('/delete')
def delete_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_user = user_crud.delete(current_user.id, db)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User account deleted"}
