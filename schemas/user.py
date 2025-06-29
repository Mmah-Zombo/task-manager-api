from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    password: str


class UserResponse(User):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
