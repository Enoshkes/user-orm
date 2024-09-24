from dataclasses import dataclass
from operator import attrgetter
from typing import Optional

from returns.maybe import Maybe, Some, Nothing
from returns.result import Result, Success, Failure


def divide(num1: int, num2: int) -> Result[float, str]:
    try:
        return Success(num1 / num2)
    except ZeroDivisionError as zde:
        return Failure(str(zde))

res = divide(2, 0).map(lambda x: x + 100).map(lambda x: x + 1000)

print(res)