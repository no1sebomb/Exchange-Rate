# coding=utf-8

from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects.postgresql import VARCHAR


class CURRENCY(TypeDecorator):
    """
    Currency column type (3 upper letters)
    """

    impl = VARCHAR(3)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        """
        Switch value to upper case
        """

        return value.upper()
