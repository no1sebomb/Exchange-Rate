# coding=utf-8

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import postgresql as pg

from ..db import database


class History(database.Model):
    """
    History model class
    """

    # Meta
    __tablename__ = "history"
    __table_args__ = {},

    # ID
    currency_id = Column(
        pg.SMALLINT,
        ForeignKey("currency.id"),
        primary_key=True
    )
    timestamp = Column(
        pg.TIMESTAMP,
        primary_key=True
    )

    # Relations
    currency = relationship(
        "Currency",
        back_populates="history"
    )

    # Info
    value = Column(
        pg.NUMERIC(10, 3),
    )
