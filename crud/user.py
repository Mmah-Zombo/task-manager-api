from sqlalchemy.orm import Session
from datetime import datetime
from models.user import User
from schemas.user import User as UserCreate


def get_all(db: Session):
    return db.query(User).all()


def get_by_username(username: str, db: Session):
    return db.query(User).filter(User.name == username).first()


def get_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def create(user: UserCreate, db: Session):
    db_user = User(**user.dict())
    db_user.created_at = datetime.utcnow()
    db_user.updated_at = datetime.utcnow()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update(user_id: int, user_data: UserCreate, db: Session):
    db_user = get_by_id(user_id, db)
    if db_user:
        try:
            for key, value in user_data.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        finally:
             pass
    return db_user


def delete(user_id: int, db: Session):
    db_user = get_by_id(user_id, db)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
