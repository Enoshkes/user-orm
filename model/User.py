from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    cars = relationship("Car", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id} username={self.username}, email={self.email} password={self.password})>"