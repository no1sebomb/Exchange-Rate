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
    date = fields.Date(format="%Y-%m-%d")
    cached = fields.Bool(missing=True)
