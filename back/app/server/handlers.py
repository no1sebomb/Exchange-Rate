# coding=utf-8

from flask import Blueprint
from werkzeug.exceptions import InternalServerError, HTTPException

from .response import APIResponse, Status, INTERNAL_SERVER_ERROR


handlers_blueprint = Blueprint("handlers", __name__)


@handlers_blueprint.app_errorhandler(500)
def handle_internal_error(error: InternalServerError) -> APIResponse:
    """
    Handle 500 Internal Server Error

    Args:
        error (InternalServerError): Occurred error

    Returns:
        APIResponse: Template response for 500 Internal Server Error
    """

    return APIResponse(INTERNAL_SERVER_ERROR)


@handlers_blueprint.app_errorhandler(HTTPException)
def handle_any(error: HTTPException) -> APIResponse:
    """
    Handle any HTTP exception

    Args:
        error (HTTPException): Occurred error

    Returns:
         APIResponse: Template response for exception
    """

    return APIResponse(Status(error.code or 500, error.name.lower().replace(" ", "_")))
