# coding=utf-8

import typing as t
from flask import Blueprint

from ..response import *


rate_blueprint = Blueprint("rate", __name__)


@rate_blueprint.get("/currency")
def get_currency() -> APIResponse:
    """
    Get currency

    Returns:
        APIResponse: Currency rates
    """

    return APIResponse(SUCCESS) >> {}
