# coding=utf-8

import typing as t
from flask import Flask

from app.config import CONFIG


if t.TYPE_CHECKING:
    # Must define types
    from flask import Blueprint


class RateAPIServer(Flask):
    """
    Currencies rate API server class
    """

    __slots__ = ()

    def register_blueprint(self, blueprint: "Blueprint", **options: t.Any) -> None:
        """
        Register API blueprint with default prefix (Flask.register_blueprint overriding).

        Args:
            blueprint (Blueprint): Blueprint, you want to register
            **options (Any): Blueprint options
        """

        # Set default API prefix
        options.setdefault("url_prefix", CONFIG["server"]["api_prefix"])

        super(RateAPIServer, self).register_blueprint(blueprint, **options)
