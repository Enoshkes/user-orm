from sqlalchemy import Table, Column, Integer, ForeignKey

from config.base import Base

customer_products = Table('customer_products', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('customer_id', Integer, ForeignKey('customers.id')),
)
