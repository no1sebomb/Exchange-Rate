# coding=utf-8

import datetime
import typing as t
from sqlalchemy import func
from flask import request
from flask_smorest import Blueprint
from flask_sqlalchemy import BaseQuery
from requests.exceptions import RequestException
from marshmallow.exceptions import ValidationError

from ..response import *
from .schemas import GetCurrency
from app.config import CONFIG
from app.utils import get_exchange_rates
from app.database import database
from app.database.models import History


rate_blueprint = Blueprint("rate", "rate", description="Currency rate operations")


@rate_blueprint.get("/currency")
# @rate_blueprint.arguments(GetCurrency, location="query")
def get_currency() -> APIResponse:
    """
    Get exchange rate for specified currencies to USD
    """

    try:
        # Get request args
        query: t.Dict[str, t.Any] = GetCurrency().load(request.args)

        if "date" in query:
            # Date specified => convert to datetime
            query["date"] = datetime.datetime.combine(
                query["date"],
                datetime.datetime.min.time()
            )

        else:
            # Set current
            query["date"] = datetime.datetime.now()

    except ValidationError:
        # Invalid args
        return APIResponse(BAD_REQUEST)

    # Define results
    results: t.Dict[str, float] = {}

    # Split saved & non-saved currencies
    saved_currencies: t.List[str] = [
        code.upper() for code in query["codes"] if (
                code in CONFIG["saved_currencies"] and query["cached"]
        )
    ]
    requested_currencies: t.List[str] = [
        code.upper() for code in query["codes"] if (
                code not in saved_currencies
        )
    ]

    if saved_currencies:
        # Select currency rates for specified date (or today)
        currency_query: BaseQuery = History.query.filter(
            History.code.in_(saved_currencies),
            func.date(History.date) == query["date"].date()
        )

        # Save to results
        results.update({
            currency.code: currency.value for currency in currency_query.all()
        })

        # Add unavailable currencies to request list
        requested_currencies += [
            currency for currency in saved_currencies if currency not in results
        ]

    if requested_currencies:
        # Replace requested currencies and set date
        query["codes"] = requested_currencies

        try:
            # Request exchange rates
            for currency_code, rate in get_exchange_rates(**query):
                # Save result
                results[currency_code] = rate

                if currency_code in CONFIG["saved_currencies"]:
                    # Save new value to database
                    database.session.add(
                        History(
                            code=currency_code,
                            date=query["date"],
                            value=rate
                        )
                    )

        except RequestException:
            # Request failed
            return APIResponse(SERVICE_UNAVAILABLE)

        else:
            # Save changes
            database.session.commit()

    return APIResponse(SUCCESS) >> results  # TODO: Serialize with Marshmallow
