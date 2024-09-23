from returns.maybe import Nothing, Maybe
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError
from typing import  Optional
from config.base import session_factory
from model import Car
from repository.user_repository import find_user_by_id


def find_car_by_brand(brand: str) -> Maybe[Car]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(Car).filter(Car.brand == brand).first()
        )


def insert_car(car: Car) -> Result[Car, str]:
    maybe_user = find_user_by_id(car.user_id)
    if maybe_user is Nothing:
        return Failure("Missing user")
    with session_factory() as session:
        try:
            session.add(car)
            session.commit()
            session.refresh(car)
            return Success(car)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))