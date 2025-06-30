import os

from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def generate_token(data: dict):
    data_to_encode = data.copy()
    expiration_date = datetime.utcnow() + timedelta(minutes=15)
    data_to_encode.update({"exp": expiration_date})
    return jwt.encode(data_to_encode, key=secret_key, algorithm=algorithm)


def decode_token(token: str):
    try:
        payload = jwt.decode(token, key=secret_key, algorithms=algorithm)
        return payload
    except JWTError:
        return None
