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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.returnsrefunds.models.exchange_item import ExchangeItem
from linnworks_api.generated.returnsrefunds.models.resend_item import ResendItem
from linnworks_api.generated.returnsrefunds.models.return_item import ReturnItem
from typing import Optional, Set
from typing_extensions import Self

class CreateRMABookingRequest(BaseModel):
    """
    CreateRMABookingRequest
    """ # noqa: E501
    channel_initiated: Optional[StrictBool] = Field(default=None, description="Determines whether the RMA request was initiated on the channel, or within Linnworks", alias="ChannelInitiated")
    order_id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the order a return booking is being created for", alias="OrderId")
    return_items: Optional[List[ReturnItem]] = Field(default=None, description="A collection of items to be returned as part of this booking", alias="ReturnItems")
    exchange_items: Optional[List[ExchangeItem]] = Field(default=None, description="A collection of items to be exchanged as part of this booking", alias="ExchangeItems")
    resend_items: Optional[List[ResendItem]] = Field(default=None, description="A collection of items to be resent as part of this booking", alias="ResendItems")
    reference: Optional[StrictStr] = Field(default=None, description="(Optional) If provided, sets the External Reference of the RMA header to the provided value. Otherwise, this value is automatically generated", alias="Reference")
    __properties: ClassVar[List[str]] = ["ChannelInitiated", "OrderId", "ReturnItems", "ExchangeItems", "ResendItems", "Reference"]

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
        """Create an instance of CreateRMABookingRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in return_items (list)
        _items = []
        if self.return_items:
            for _item_return_items in self.return_items:
                if _item_return_items:
                    _items.append(_item_return_items.to_dict())
            _dict['ReturnItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exchange_items (list)
        _items = []
        if self.exchange_items:
            for _item_exchange_items in self.exchange_items:
                if _item_exchange_items:
                    _items.append(_item_exchange_items.to_dict())
            _dict['ExchangeItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resend_items (list)
        _items = []
        if self.resend_items:
            for _item_resend_items in self.resend_items:
                if _item_resend_items:
                    _items.append(_item_resend_items.to_dict())
            _dict['ResendItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRMABookingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChannelInitiated": obj.get("ChannelInitiated"),
            "OrderId": obj.get("OrderId"),
            "ReturnItems": [ReturnItem.from_dict(_item) for _item in obj["ReturnItems"]] if obj.get("ReturnItems") is not None else None,
            "ExchangeItems": [ExchangeItem.from_dict(_item) for _item in obj["ExchangeItems"]] if obj.get("ExchangeItems") is not None else None,
            "ResendItems": [ResendItem.from_dict(_item) for _item in obj["ResendItems"]] if obj.get("ResendItems") is not None else None,
            "Reference": obj.get("Reference")
        })
        return _obj


