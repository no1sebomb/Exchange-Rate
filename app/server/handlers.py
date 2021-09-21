# coding=utf-8

import typing as t
from flask import Blueprint
from werkzeug.exceptions import InternalServerError, HTTPException


handlers_blueprint = Blueprint("handlers", __name__)


@handlers_blueprint.app_errorhandler(500)
def handle_internal_error(error: InternalServerError) -> t.Tuple[t.Dict[str, t.Any], int]:
    """
    Handle 500 Internal Server Error

    Args:
        error (InternalServerError): Occurred error

    Returns:
        t.Tuple[t.Dict[str, t.Any], int]: Template response for 500 Internal Server Error
    """

    return {"message": "internal_server_error"}, 500


@handlers_blueprint.app_errorhandler(HTTPException)
def handle_any(error: HTTPException) -> t.Tuple[t.Dict[str, t.Any], int]:
    """
    Handle any HTTP exception

    Args:
        error (HTTPException): Occurred error

    Returns:
         t.Tuple[t.Dict[str, t.Any], int]: Template response for exception
    """

    return {"message": error.name.lower().replace(" ", "_")}, error.code or 500
