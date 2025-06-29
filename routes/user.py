from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schemas.user import User, UserResponse
from sqlalchemy.orm import Session
from typing import List
from crud import user as user_crud


router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all(db)


@router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post('/', response_model=UserResponse)
def create_user(user_data: User, db: Session = Depends(get_db)):
    pass
