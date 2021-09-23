# coding=utf-8

import typing as t
from flask import Blueprint, request
from requests.exceptions import RequestException
from marshmallow.exceptions import ValidationError

from ..response import *
from .schemas import GetCurrency
from app.utils import get_exchange_rates


rate_blueprint = Blueprint("rate", __name__)


@rate_blueprint.get("/currency")
def get_currency() -> APIResponse:
    """
    Get currency

    Returns:
        APIResponse: Currency rates
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
