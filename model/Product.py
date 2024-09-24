from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship

from config.base import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    title = Column(String(100), nullable=False)

    customers = relationship(
        "Customer",
        secondary="customer_products",
        back_populates="products"
    )

    def __repr__(self):
        return f"<Product(id={self.id} price={self.price}, title={self.title})>"