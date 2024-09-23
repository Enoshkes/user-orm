from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base
from model.CustomerProducts import customer_products


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    products = relationship("Product", secondary=customer_products, back_populates="customers")