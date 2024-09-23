from operator import attrgetter

from returns.result import Failure

from repository.database import create_tables
from model import User
import logging
import toolz as t
from operator import add
from repository.user_repository import insert_user, find_user_by_id, delete_user, update_user

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    create_tables()

    # saved_user = insert_user(User(
    #     username="matanel",
    #     email="enosh@gmail.com",
    #     password="ha-megid123"
    # ))

    updated_user = update_user(18, User(username="Elkana", email="e@walla.com", password="Israel123"))
    logging.info(updated_user)
