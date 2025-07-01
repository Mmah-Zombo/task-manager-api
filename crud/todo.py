from sqlalchemy.orm import Session
from models.todo import Todo
from schemas.todo import Todo as TodoCreate
from datetime import datetime


def get_all(db: Session):
    return db.query(Todo).all()


def get_by_id(todo_id: int, db: Session):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create(todo_data: TodoCreate, db: Session):
    new_todo = Todo(**todo_data.dict())
    new_todo.created_at = datetime.utcnow()
    new_todo.updated_at = datetime.utcnow()
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update(todo_id: int, todo_data: TodoCreate, db: Session):
    db_todo = get_by_id(todo_id, db)
    if db_todo:
        for key, value in todo_data.dict().items():
            setattr(db_todo, key, value)
        db_todo.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_todo)
    return db_todo


def delete(todo_id: int, db: Session):
    db_todo = get_by_id(todo_id, db)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
