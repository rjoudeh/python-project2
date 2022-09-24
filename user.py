from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class User(Base):
    __tablename__ = "app_user"
    _id: int
    name: str
    address: str
    age: str
    email: str

    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    age = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, name, address, age, email):
        self.name = name
        self.address = address
        self.age = age
        self.email = email
