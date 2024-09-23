from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base

class Car(Base):
    __tablename__ = "cars"
    id  = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(100), nullable=False)
    color = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="cars")

    def __repr__(self):
        return f"<Car(id={self.id} brand={self.brand}, color={self.color} user_id={self.user_id})>"