from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError
from toolz import excepts

from config.base import session_factory
from model import Customer, Product
from repository.product_repository import find_product_by_id


def insert_customer(customer: Customer) -> Result[Customer, str]:
    with session_factory() as session:
        try:
            session.add(customer)
            session.commit()
            session.refresh(customer)
            return Success(customer)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def find_customer_by_id(c_id: int) -> Maybe[Customer]:
    with session_factory() as session:
        return Maybe.from_optional(session.query(Customer).get(c_id))

def add_product_to_customer(c_id: int, product: Product) -> Result[Customer, str]:
    with session_factory() as session:
        try:
            maybe_customer = find_customer_by_id(c_id)
            if maybe_customer is Nothing:
                return Failure(f"No customer with the id {c_id}")
            session.add(product)
            session.commit()
            session.refresh(product)
            customer_to_save = session.merge(maybe_customer.unwrap())
            customer_to_save.products.append(product)
            session.commit()
            session.refresh(customer_to_save)
            return Success(customer_to_save)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def remove_product_from_customer(c_id: int, p_id: int) -> Result[Product, str]:
    with session_factory() as session:
        try:
            maybe_customer = find_customer_by_id(c_id)
            maybe_product = find_product_by_id(p_id)
            if any(x is Nothing for x in [maybe_product, maybe_customer]):
                return Failure("Missing customer or product")
            customer = session.merge(maybe_customer.unwrap())
            product = session.merge(maybe_product.unwrap())
            customer.products.remove(product)
            session.commit()
            session.refresh(customer)
            return Success(customer)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
