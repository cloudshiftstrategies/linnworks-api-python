# coding: utf-8

"""
    Warehouse Transfer

    Warehouse Transfer v1

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PrepOwners(str, Enum):
    """
    Values are the same as for field PrepOwner on Amazon
    """

    """
    allowed enum values
    """
    SELLER = 'SELLER'
    AMAZON = 'AMAZON'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrepOwners from a JSON string"""
        return cls(json.loads(json_str))


