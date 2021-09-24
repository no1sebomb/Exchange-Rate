# coding=utf-8

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql as pg

from ..db import database


class Currency(database.Model):
    """
    Currency model class
    """

    # Meta
    __tablename__ = "currency"

    # ID
    id = Column(
        pg.SMALLINT,
        primary_key=True,
        autoincrement=True
    )
    name = Column(
        pg.VARCHAR(3),
        unique=True
    )

    # Relations
    history = relationship(
        "History",
        back_populates="currency"
    )

    # Info
    value = Column(
        pg.REAL
    )
    updated_at = Column(
        pg.TIMESTAMP
    )
