from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    products = relationship(
        "Product",
        lazy="joined",
        secondary="customer_products",
        back_populates="customers"
    )

    def __repr__(self):
        return f"<Customer(id={self.id} name={self.name})>"