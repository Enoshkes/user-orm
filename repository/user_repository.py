from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import User


def insert_user(user: User) -> Result[User, str]:
    with session_factory() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def find_user_by_id(u_id: int) -> Maybe[User]:
    with session_factory() as session:
        return Maybe.from_optional(session.query(User).get(u_id))

def delete_user(u_id: int) -> Result[User, str]:
    with session_factory() as session:
        try:
            maybe_user = find_user_by_id(u_id)
            if maybe_user is Nothing:
                return Failure(f"No user by the id {u_id}")
            user_to_delete = maybe_user.unwrap()
            session.delete(user_to_delete)
            session.commit()
            return Success(user_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def update_user(u_id: int, user: User) -> Result[User, str]:
    with session_factory() as session:
        try:
            maybe_user = find_user_by_id(u_id)
            if maybe_user is Nothing:
                return Failure(f"No user by the id {u_id}")
            user_to_update = session.merge(maybe_user.unwrap())
            user_to_update.username = user.username
            user_to_update.email = user.email
            user_to_update.password = user.password
            session.commit()
            session.refresh(user_to_update)
            return Success(user_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))



