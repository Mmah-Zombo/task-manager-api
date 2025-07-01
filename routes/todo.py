from fastapi import APIRouter, Depends
from typing import List
from models.todo import Todo
from models.user import User
from schemas.todo import TodoResponse
from sqlalchemy.orm import Session
from database import get_db
from dependencies.auth import get_current_user


router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get('/', response_model=List[TodoResponse])
def list_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return current_user.todos
