# coding: utf-8

"""
    Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: orders
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

class OrdersGetOrdersRequest(BaseModel):
    """
    OrdersGetOrdersRequest
    """ # noqa: E501
    orders_ids: Optional[List[StrictStr]] = Field(default=None, description="Orders ids", alias="ordersIds")
    fulfilment_location_id: Optional[StrictStr] = Field(default=None, description="Current fulfilment center", alias="fulfilmentLocationId")
    load_items: Optional[StrictBool] = Field(default=None, description="Load or not the orders items information", alias="loadItems")
    load_additional_info: Optional[StrictBool] = Field(default=None, description="Load or not the orders additional info", alias="loadAdditionalInfo")
    __properties: ClassVar[List[str]] = ["ordersIds", "fulfilmentLocationId", "loadItems", "loadAdditionalInfo"]

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
        """Create an instance of OrdersGetOrdersRequest from a JSON string"""
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
        """Create an instance of OrdersGetOrdersRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ordersIds": obj.get("ordersIds"),
            "fulfilmentLocationId": obj.get("fulfilmentLocationId"),
            "loadItems": obj.get("loadItems"),
            "loadAdditionalInfo": obj.get("loadAdditionalInfo")
        })
        return _obj


