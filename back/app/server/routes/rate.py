# coding=utf-8

import typing as t
from flask import request
from requests.exceptions import RequestException
from marshmallow.exceptions import ValidationError
from flask_smorest import Blueprint

from ..response import *
from .schemas import GetCurrency
from app.utils import get_exchange_rates


rate_blueprint = Blueprint("rate", "rate", description="Currency rate operations")


@rate_blueprint.get("/currency")
@rate_blueprint.arguments(GetCurrency, location="query")
def get_currency() -> APIResponse:
    """
    Get exchange rate for specified currencies to USD
    """

    try:
        # Get request args
        query: t.Dict[str, t.Any] = GetCurrency().load(request.args)

    except ValidationError:
        # Invalid args
        return APIResponse(BAD_REQUEST)

    try:
        # Request exchange rates
        exchange_rates = dict(get_exchange_rates(**query))

    except KeyError:
        # Invalid currency
        return APIResponse(BAD_REQUEST)

    except RequestException:
        # Request failed
        return APIResponse(SERVICE_UNAVAILABLE)

    return APIResponse(SUCCESS) >> exchange_rates  # TODO: Serialize with Marshmallow
