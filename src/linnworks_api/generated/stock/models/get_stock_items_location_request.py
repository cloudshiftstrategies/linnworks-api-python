# coding: utf-8

"""
    Stock API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: stock
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.stock.models.stock_location_stock_item_id import StockLocationStockItemId
from typing import Optional, Set
from typing_extensions import Self

class GetStockItemsLocationRequest(BaseModel):
    """
    GetStockItemsLocationRequest
    """ # noqa: E501
    stock_item_locations: Optional[List[StockLocationStockItemId]] = Field(default=None, alias="StockItemLocations")
    auth_token: Optional[StrictStr] = Field(default=None, alias="AuthToken")
    account_id: Optional[StrictStr] = Field(default=None, alias="AccountId")
    vendor_friendly_name: Optional[StrictStr] = Field(default=None, alias="VendorFriendlyName")
    vendor: Optional[StrictStr] = Field(default=None, alias="Vendor")
    __properties: ClassVar[List[str]] = ["StockItemLocations", "AuthToken", "AccountId", "VendorFriendlyName", "Vendor"]

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
        """Create an instance of GetStockItemsLocationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stock_item_locations (list)
        _items = []
        if self.stock_item_locations:
            for _item_stock_item_locations in self.stock_item_locations:
                if _item_stock_item_locations:
                    _items.append(_item_stock_item_locations.to_dict())
            _dict['StockItemLocations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetStockItemsLocationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "StockItemLocations": [StockLocationStockItemId.from_dict(_item) for _item in obj["StockItemLocations"]] if obj.get("StockItemLocations") is not None else None,
            "AuthToken": obj.get("AuthToken"),
            "AccountId": obj.get("AccountId"),
            "VendorFriendlyName": obj.get("VendorFriendlyName"),
            "Vendor": obj.get("Vendor")
        })
        return _obj


