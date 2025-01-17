# coding: utf-8

"""
    Returns and Refunds API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: returnsrefunds
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class VerifiedRefundItem(BaseModel):
    """
    VerifiedRefundItem
    """ # noqa: E501
    order_item_row_id: Optional[StrictStr] = Field(default=None, alias="OrderItemRowId")
    return_row_id: Optional[StrictInt] = Field(default=None, alias="ReturnRowId")
    item_sku: Optional[StrictStr] = Field(default=None, alias="ItemSKU")
    channel_sku: Optional[StrictStr] = Field(default=None, alias="ChannelSKU")
    item_title: Optional[StrictStr] = Field(default=None, alias="ItemTitle")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Cost")
    cancelled_quantity: Optional[StrictInt] = Field(default=None, alias="CancelledQuantity")
    __properties: ClassVar[List[str]] = ["OrderItemRowId", "ReturnRowId", "ItemSKU", "ChannelSKU", "ItemTitle", "Cost", "CancelledQuantity"]

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
        """Create an instance of VerifiedRefundItem from a JSON string"""
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
        """Create an instance of VerifiedRefundItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OrderItemRowId": obj.get("OrderItemRowId"),
            "ReturnRowId": obj.get("ReturnRowId"),
            "ItemSKU": obj.get("ItemSKU"),
            "ChannelSKU": obj.get("ChannelSKU"),
            "ItemTitle": obj.get("ItemTitle"),
            "Cost": obj.get("Cost"),
            "CancelledQuantity": obj.get("CancelledQuantity")
        })
        return _obj


