from operator import attrgetter

from repository.car_repository import insert_car, find_car_by_brand
from repository.customer_repository import insert_customer, add_product_to_customer, remove_product_from_customer
from repository.database import create_tables
from model import User, Car, Product, Customer, CustomerProducts
import logging

from repository.product_repository import insert_product
from repository.user_repository import insert_user

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    create_tables()
