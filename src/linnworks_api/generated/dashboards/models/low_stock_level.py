# coding: utf-8

"""
    Dashboards API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: dashboards
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LowStockLevel(BaseModel):
    """
    LowStockLevel
    """ # noqa: E501
    item_title: Optional[StrictStr] = Field(default=None, alias="ItemTitle")
    item_number: Optional[StrictStr] = Field(default=None, alias="ItemNumber")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    minimum_level: Optional[StrictInt] = Field(default=None, alias="MinimumLevel")
    in_books: Optional[StrictInt] = Field(default=None, alias="InBooks")
    location: Optional[StrictStr] = Field(default=None, alias="Location")
    __properties: ClassVar[List[str]] = ["ItemTitle", "ItemNumber", "Quantity", "MinimumLevel", "InBooks", "Location"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LowStockLevel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LowStockLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ItemTitle": obj.get("ItemTitle"),
            "ItemNumber": obj.get("ItemNumber"),
            "Quantity": obj.get("Quantity"),
            "MinimumLevel": obj.get("MinimumLevel"),
            "InBooks": obj.get("InBooks"),
            "Location": obj.get("Location")
        })
        return _obj


