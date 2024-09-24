from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from config.base import Base

class CustomerProducts(Base):
    __tablename__ = "customer_products"
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('customer_id', 'product_id'),
    )

    def __repr__(self):
        return f"<CustomerProducts(customer_id={self.customer_id}, product_id={self.product_id})>"
