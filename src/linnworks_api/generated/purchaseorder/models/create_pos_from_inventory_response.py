# coding: utf-8

"""
    Purchase Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: purchaseorder
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.purchaseorder.models.tuple_guid_string import TupleGuidString
from typing import Optional, Set
from typing_extensions import Self

class CreatePOsFromInventoryResponse(BaseModel):
    """
    CreatePOsFromInventoryResponse
    """ # noqa: E501
    purchase_orders: Optional[Dict[str, TupleGuidString]] = Field(default=None, description="A dictionary where the key is supplier Id and the tuple represents the purchase order id and the external invoice number for that PO", alias="PurchaseOrders")
    skipped_stock_items: Optional[List[StrictStr]] = Field(default=None, alias="SkippedStockItems")
    __properties: ClassVar[List[str]] = ["PurchaseOrders", "SkippedStockItems"]

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
        """Create an instance of CreatePOsFromInventoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in purchase_orders (dict)
        _field_dict = {}
        if self.purchase_orders:
            for _key_purchase_orders in self.purchase_orders:
                if self.purchase_orders[_key_purchase_orders]:
                    _field_dict[_key_purchase_orders] = self.purchase_orders[_key_purchase_orders].to_dict()
            _dict['PurchaseOrders'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePOsFromInventoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PurchaseOrders": dict(
                (_k, TupleGuidString.from_dict(_v))
                for _k, _v in obj["PurchaseOrders"].items()
            )
            if obj.get("PurchaseOrders") is not None
            else None,
            "SkippedStockItems": obj.get("SkippedStockItems")
        })
        return _obj


