# coding=utf-8

import datetime
import requests
import typing as t

from app.config import CONFIG


def get_exchange_rates(
        codes: t.Iterable[str],
        base: str = CONFIG["currency"]["base"],
        date: t.Optional[datetime.date] = None,
        **kwargs: t.Any
) -> t.Generator[t.Tuple[str, float], None, None]:
    """
    Get exchange rate for specified currencies (and date) to base currency

    Args:
        codes (t.Iterable[str]): Currency codes (3-letter)
        base (str): Base currency code (3-letter)
        date (t.Optional[datetime.date]): Requested date.
            If no date is specified, returns latest exchange rate

    Yields:
        float: Currency rate

    Raises:
        ValueError: If specified date is unavailable
        requests.exceptions.RequestException: Request failed

    Notes:
        Changing the API `base` currency is available for
        Developer, Enterprise and Unlimited plan clients
    """

    def _check_date() -> None:
        """
        Check if date is available
        """

        if not datetime.datetime(year=1999, day=1, month=1) <= date <= datetime.datetime.utcnow():
            # Invalid date
            raise ValueError(f"Specified date '{date.strftime('%Y-%m-%d')}' is not available")

    if date is None:
        # Latest rate
        rate_request_link = (
            f'https://openexchangerates.org/api/latest.json?'
            f'app_id={CONFIG["exchange_rate_api"]["app_id"]}&'
            f'symbols={",".join(codes)}&'
            f'currency={base}'
        )

    else:
        # Rate by date
        _check_date()

        rate_request_link = (
            f'https://openexchangerates.org/api/historical/'
            f'{date.strftime("%Y-%m-%d")}.json?'
            f'app_id={CONFIG["exchange_rate_api"]["app_id"]}&'
            f'symbols={",".join(codes)}&'
            f'currency={base}'
        )

    try:
        rate_request = requests.get(
            rate_request_link,
            **CONFIG["exchange_rate_api"]["request_options"]
        )

        # Validate request status
        assert rate_request.status_code == 200

    except (requests.exceptions.RequestException, AssertionError):
        # Request failed
        raise requests.exceptions.RequestException("Exchange rate request is failed")

    else:
        # Success
        rates: t.Dict[str, float] = rate_request.json().get("rates", {})

        for currency in codes:
            # Yield rate for specified currencies (if exists)
            if currency in rates:
                yield currency, rates[currency]
