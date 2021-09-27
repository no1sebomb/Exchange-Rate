# coding=utf-8

import typing as t
from marshmallow import Schema, fields


class ResponseSchema(Schema):
    """
    Response object schema
    """

    message = fields.Str()
    response = fields.Dict()

    def __class_getitem__(cls, response: t.Type[Schema]) -> t.Type:
        """
        Get response schema for specified response schema

        Args:
            response (Schema): Response schema

        Returns:
            t.Type[ResponseSchema]: ResponseSchema with specified response
        """

        return type(
            f"{cls.__name__}_{response.__name__}",
            (cls, ),
            {"response": fields.Nested(response)}
        )
