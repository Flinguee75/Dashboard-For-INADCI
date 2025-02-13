from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.sql import func
from models import db

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Clé primaire auto-incrémentée
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(String(50), nullable=False)
    date_created = Column(DateTime, default=func.current_timestamp(), nullable=True)
