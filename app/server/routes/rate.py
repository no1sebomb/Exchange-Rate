# coding=utf-8

import typing as t
from flask import Blueprint


rate_blueprint = Blueprint("rate", __name__)


@rate_blueprint.get("/currency")
def get_currency() -> t.Tuple[t.Dict[str, t.Any], int]:
    """
    Get currency
    """

    return {"message": "ok"}, 200
