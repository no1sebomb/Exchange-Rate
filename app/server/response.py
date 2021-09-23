# coding=utf-8

import typing as t
from json import dumps
from flask import Response as PageResponse
from dataclasses import dataclass


@dataclass(frozen=True)
class Status(object):
    """
    Status class. Stores status code and message
    """

    code: int
    message: str

    def __repr__(self) -> str:
        """
        Status object representation
        Returns:
            str: "<code>_<message>" format
        """

        return f"{self.code}_{self.message}"

    def __iter__(self) -> t.Iterator:
        """
        Iterate status object
        Returns:
            t.Iterator: Status code & message
        """

        return (self.code, self.message).__iter__()


class APIResponse(PageResponse):
    """
    API Response class, defines API response object
    """

    __slots__ = ("__data", "__status")

    def __init__(self, status: Status, data: t.Dict[str, t.Any] = None) -> None:
        """
        Create APIResponse object

        Args:
            status (Status): Response status
            data (t.Dict[str, t.Any]): Response data
        """

        # Save response data
        self.__data: t.Dict[str, t.Any] = data or {}
        self.__status: Status = status

        # Init flask response
        super(APIResponse, self).__init__(
            response=dumps({
                "response": self.__data,
                "message": status.message
            }, ensure_ascii=False),
            mimetype="application/json",
            status=status.code
        )

    def __rshift__(self, data: t.Dict[str, t.Any]) -> "APIResponse":
        """
        Bitwise right shift operator overload (load response data)

        Args:
            data (t.Dict[str, Any]): Response data you want to add

        Returns:
            APIResponse: Response object with given data
        """

        # Save new response
        self.__data = data

        # Set new response JSON data
        self.data = dumps({
            "response": data,
            "message": self.__status.message
        }, ensure_ascii=False)

        return self


# Statuses definition
SUCCESS:               Status = Status(200, "success")
BAD_REQUEST:           Status = Status(400, "bad_request")
INTERNAL_SERVER_ERROR: Status = Status(500, "internal_server_error")
SERVICE_UNAVAILABLE:   Status = Status(503, "service_unavailable")


__all__ = (
    "Status", "APIResponse",
    "SUCCESS", "BAD_REQUEST",
    "INTERNAL_SERVER_ERROR",
    "SERVICE_UNAVAILABLE"
)
