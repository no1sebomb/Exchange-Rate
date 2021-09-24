# coding=utf-8

import typing as t
from sqlalchemy import Column
from sqlalchemy.dialects import postgresql as pg

from ..db import database
from .types import CURRENCY


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
        CURRENCY,
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
