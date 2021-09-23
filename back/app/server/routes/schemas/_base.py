# coding=utf-8

from marshmallow import fields
from marshmallow.exceptions import ValidationError


class DelimitedListField(fields.List):
    """
    DelimitedListField type implementation.
    Deserializes list of strings, separated by commas.
    """

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return value.split(",")
        except AttributeError:
            raise ValidationError(
                f"{attr} is not a delimited list it has a non string value {value}."
            )
