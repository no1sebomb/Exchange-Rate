# coding=utf-8

import typing as t
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator
from sqlalchemy.dialects import postgresql as pg

from ..db import database


class _CURRENCY(TypeDecorator):
    """
    Currency column type (3 upper letters)
    """

    impl = pg.VARCHAR(3)

    def process_bind_param(self, value, dialect):
        """
        Switch value to upper case
        """

        return value.upper()


class History(database.Model):
    """
    History model class
    """

    # Meta
    __tablename__ = "history"
    __table_args__: t.Tuple[t.Dict[str, t.Any]] = {
        "schema": "currency"
    },

    # ID
    code = Column(
        _CURRENCY,
        primary_key=True
    )
    date = Column(
        pg.TIMESTAMP,
        primary_key=True
    )

    # Info
    value = Column(
        pg.REAL
    )
