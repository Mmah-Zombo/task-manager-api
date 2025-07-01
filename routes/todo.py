from fastapi import APIRouter, Depends, HTTPException
from typing import List
from crud import todo as todo_crud
from database import get_db
from dependencies.auth import get_current_user
from models.todo import Todo
from models.user import User
from schemas.todo import TodoResponse, Todo as TodoCreate
from sqlalchemy.orm import Session


router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get('/', response_model=List[TodoResponse])
def list_todos(current_user: User = Depends(get_current_user)):
    return current_user.todos


@router.get('/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = todo_crud.get_by_id(todo_id, db)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")

    if db_todo.user_id != current_user.id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return db_todo


@router.post('/', response_model=TodoResponse)
def create_todo(todo_data: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_id = current_user.id
    new_todo = todo_crud.create(todo_data, user_id, db)
    if not new_todo:
        raise HTTPException(status_code=500, detail="Could not create new task")
    return new_todo
