from fastapi import FastAPI
from database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="Todo List API",
    description="An API that helps users to manage their tasks",
    version="0.0.1"
)


@app.get('/')
async def index():
    return {"message": "Welcome to this cool TODO List API built with Python"}
