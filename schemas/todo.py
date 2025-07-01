from pydantic import BaseModel
from datetime import datetime


class Todo(BaseModel):
    title: str
    description: str
    priority: int = 1
    completed: bool = False


class TodoResponse(Todo):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
