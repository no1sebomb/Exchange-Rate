# coding=utf-8

from marshmallow import Schema, fields, validate

from ._base import DelimitedListField


class GetCurrency(Schema):
    """
    Get currency request schema
    """

    codes = DelimitedListField(
        fields.Str(validate=validate.Length(min=1, max=3)),
        validate=validate.Length(min=1),
        required=True
    )
    base = fields.Str(validate=validate.Length(min=1, max=3))
    date = fields.Date(format="%Y-%m-%d")
    cached = fields.Bool(missing=True)


class CurrencyResponse(Schema):
    """
    Currency response schema (used for OpenAPI response definition)
    """

    currency_code1 = fields.Float()
    currency_code2 = fields.Float()
    ...
    currency_codeN = fields.Float()
