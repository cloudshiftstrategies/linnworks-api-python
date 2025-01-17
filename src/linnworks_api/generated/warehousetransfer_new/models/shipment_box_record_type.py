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


class ShipmentBoxRecordType(str, Enum):
    """
    ShipmentBoxRecordType
    """

    """
    allowed enum values
    """
    PALLET = 'Pallet'
    BOX = 'Box'
    SKU = 'Sku'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ShipmentBoxRecordType from a JSON string"""
        return cls(json.loads(json_str))


