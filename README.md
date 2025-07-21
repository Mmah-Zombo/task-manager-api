# Todo List API

An API that helps users manage their tasks, built with FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints for user registration, authentication, and CRUD operations on to-do items.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Running the Application](#running-the-application)  
- [API Documentation](#api-documentation)  
- [Authentication](#authentication)  
- [Endpoints](#endpoints)  
  - [Root](#root)  
  - [User Endpoints](#user-endpoints)  
  - [Todo Endpoints](#todo-endpoints)  
- [License](#license)  

---

## Features

- **User Registration & Login** with JWT-based authentication
- **Create, Read, Update, Delete** to-do items scoped to the authenticated user
- **Automatic table creation** on startup via SQLAlchemy’s `Base.metadata.create_all()`
- **Password hashing** with bcrypt and token generation using python-jose
- **Interactive API docs** (Swagger UI) at `/docs`  
- **Summary API docs** (Redoc) at `/redoc`

---

## Prerequisites

- Python 3.8 or newer  
- PostgreSQL database  
- `git`  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Mmah-Zombo/todo-list-api.git
   cd todo-list-api
   ```

2. **Create & activate a virtual environment**

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies**

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt   # fastapi, uvicorn, sqlalchemy, psycopg2-binary, passlib[bcrypt], python-jose[cryptography], dotenv, python-multipart  [oai_citation:4‡GitHub](https://raw.githubusercontent.com/Mmah-Zombo/todo-list-api/main/requirements.txt)
    ```

___

## Configuration

1. Copy the example environment file and fill in your values:

    ```bash
    cp .env.example .env
    ```

    ```bash
    DATABASE_NAME=your_db_name
    DATABASE_HOST=your_db_host
    DATABASE_USER=your_db_user
    DATABASE_PASSWORD=your_db_password
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ```

- The `SECRET_KEY` and `ALGORITHM` are used for JWT token encoding/decoding

---

## Running the Application

Start the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```

- The API will be available at http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc:  http://localhost:8000/redoc

---

## API Documentation

Once the server is running, you can explore all endpoints, request/response models and try them out via the automatically generated Swagger UI at:

http://localhost:8000/docs

- The Swagger UI documentation is available at: http://localhost:8000/docs
- The ReDoc summary documentation is available at:  http://localhost:8000/redoc
---

## Authentication

- The API uses **OAuth2 Password** (JWT Bearer) for protected routes.
- Obtain a token by logging in via POST `/users/login` with form fields username and password.
- Include the returned access_token in the Authorization: Bearer <token> header for all subsequent protected requests.

---

## Endpoints

**Root**

| Method | 	Path	 | Description     |
|--------|:-------|-----------------|
| GET	   | /	     | Welcome message |

**User Endpoints**

| Method	 | Path	            | Description	                                   | Auth |
|---------|------------------|------------------------------------------------|------|
| GET	    | /users	          | List all users.	                               | ✔︎   |
| GET	    | /users/{user_id} | Get a single user by ID.	                      | ✔︎   |
| POST	   | /users	          | Register a new user (no auth required).	       | ✘    |
| POST	   | /users/login	    | Obtain JWT token (form: username, password).   | ✘    |
| POST	   | /users/logout	   | (Stub — currently no operation).	              | ✔︎   |
| DELETE	 | /users/delete	   | Delete the authenticated user’s account.	      | ✔︎   |
| PUT	    | /users	          | Update the authenticated user’s name/password. | 	✔︎  |

_(User schema: name: str, password: str – responses include id, created_at, updated_at)._

**Todo Endpoints**

| Method	 | Path	            | Description	                                 | Auth |
|---------|------------------|----------------------------------------------|------|
| GET	    | /todos	          | List all to-dos for the authenticated user.	 | ✔︎   |
| GET	    | /todos/{todo_id} | Retrieve a single to-do by its ID.	          | ✔︎   |
| POST	   | /todos	          | Create a new to-do.	                         | ✔︎   |
| PUT	    | /todos/{todo_id} | 	Update an existing to-do.	                  | ✔︎   |
| DELETE	 | /todos/{todo_id} | 	Delete a to-do by its ID.	                  | ✔︎   |

_(To-do schema: title: str, description: str, priority: int = 1, completed: bool = False; responses include id, user_id, created_at, updated_at.)._

---

**License**

This project is provided under the MIT License.
