from returns.result import Result

from config.base import session_factory
from model import Product


# def insert_product(product: Product) -> Result[Product, str]:
#     with session_factory() as session:
#