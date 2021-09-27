# coding=utf-8

from datetime import date
from unittest import TestCase

from ..config import CONFIG
from ..utils import get_exchange_rates


class TestRateRequests(TestCase):
    """
    Test get_exchange_rates() function from utils subpackage
    """

    _valid = CONFIG["currency"]["cached"]
    _invalid = ["ABC", "123"]

    def test_valid_currencies(self):
        """
        Test existing currency codes
        """

        for index, (code, rate) in enumerate(get_exchange_rates(
            codes=self._valid,
        )):
            # Compare input & output codes
            self.assertEqual(code, self._valid[index])

    def test_invalid_currencies(self):
        """
        Test invalid currency codes
        """

        for _ in get_exchange_rates(
            codes=self._invalid,
        ):
            # Should not run loop body
            self.fail()

    def test_invalid_date(self):
        """
        Test unsupported date
        """

        # Too old date
        with self.assertRaises(ValueError):
            for _ in get_exchange_rates(
                codes=self._valid,
                date=date(year=1990, month=1, day=1)
            ):
                # Start generator and break immediately
                break

        # Date from future
        with self.assertRaises(ValueError):
            for _ in get_exchange_rates(
                codes=self._valid,
                date=date(year=2050, month=1, day=1)
            ):
                # Start generator and break immediately
                break
