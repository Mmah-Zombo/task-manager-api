from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    todos = Relationship("Todo", back_populates="user", cascade="all, delete-orphan")
