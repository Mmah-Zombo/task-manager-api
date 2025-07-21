from fastapi import FastAPI

from database import Base, engine
from routes import todo, user

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="Todo List API",
    description="An API that helps users to manage their tasks",
    version="0.0.1",
)


app.include_router(user.router)
app.include_router(todo.router)


@app.get("/")
async def index():
    return {"message": "Welcome to this cool TODO List API built with Python"}
