from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import todo as todo_crud
from database import get_db
from dependencies.auth import get_current_user
from models.user import User
from schemas.todo import Todo as TodoCreate
from schemas.todo import TodoResponse

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=List[TodoResponse])
def list_todos(current_user: User = Depends(get_current_user)):
    return current_user.todos


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_todo = todo_crud.get_by_id(todo_id, db)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Task not found")

    if db_todo.user_id != current_user.id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return db_todo


@router.post("/", response_model=TodoResponse)
def create_todo(
    todo_data: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_id = current_user.id
    new_todo = todo_crud.create(todo_data, user_id, db)
    if not new_todo:
        raise HTTPException(status_code=500, detail="Could not create new task")
    return new_todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    data: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = todo_crud.get_by_id(todo_id, db)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    owner = todo.user_id == current_user.id
    if not owner:
        raise HTTPException(status_code=403, detail="Unauthorized to update this todo")

    todo = todo_crud.update(todo_id, data, db)

    if not todo:
        raise HTTPException(status_code=500, detail="Could not update todo")

    return todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    todo = todo_crud.get_by_id(todo_id, db)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    owner = todo.user_id == current_user.id
    if not owner:
        raise HTTPException(status_code=403, detail="Unauthorized to delete this todo")

    todo_crud.delete(todo_id, db)

    return {"message": f"Todo with id: {todo_id} deleted"}


@router.get('/filter/', response_model=List[TodoResponse])
def filter_todos(completed: bool = None, priority: int = None, description: str = None, current_user: User = Depends(get_current_user)):
    todos = current_user.todos
    filtered_todos = []
    if completed is not None:
        filtered_todos = [todo for todo in todos if todo.completed == completed]

    if priority is not None:
        filtered_todos = [todo for todo in filtered_todos if todo.priority == priority]

    if description is not None:
        filtered_todos = [todo for todo in filtered_todos if todo.description == description]

    return filtered_todos
