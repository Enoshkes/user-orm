from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

from config.base import Base
from model.CustomerProducts import customer_products


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    title = Column(String(100), nullable=False)

    customers = relationship("Customer", secondary=customer_products, back_populates="products")