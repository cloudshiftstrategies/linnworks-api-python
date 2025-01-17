# coding: utf-8

"""
    Inventory API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: inventory
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AddImageToInventoryItemRequest(BaseModel):
    """
    AddImageToInventoryItemRequest
    """ # noqa: E501
    item_number: Optional[StrictStr] = Field(default=None, description="SKU number of an item", alias="ItemNumber")
    stock_item_id: Optional[StrictStr] = Field(default=None, description="pkStockItemId of an item", alias="StockItemId")
    is_main: Optional[StrictBool] = Field(default=None, description="Whether you want to set the image as main", alias="IsMain")
    image_url: Optional[StrictStr] = Field(default=None, description="Image URL", alias="ImageUrl")
    __properties: ClassVar[List[str]] = ["ItemNumber", "StockItemId", "IsMain", "ImageUrl"]

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
        """Create an instance of AddImageToInventoryItemRequest from a JSON string"""
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
        """Create an instance of AddImageToInventoryItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ItemNumber": obj.get("ItemNumber"),
            "StockItemId": obj.get("StockItemId"),
            "IsMain": obj.get("IsMain"),
            "ImageUrl": obj.get("ImageUrl")
        })
        return _obj


