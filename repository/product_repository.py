from returns.maybe import Maybe
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import Product


def insert_product(product: Product) -> Result[Product, str]:
    with session_factory() as session:
        try:
            session.add(product)
            session.commit()
            session.refresh(product)
            return Success(product)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_product_by_id(p_id: int) -> Maybe[Product]:
    with session_factory() as session:
        return Maybe.from_optional(session.query(Product).get(p_id))