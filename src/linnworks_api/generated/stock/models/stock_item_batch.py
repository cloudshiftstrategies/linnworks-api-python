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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.stock.models.stock_item_batch_inventory import StockItemBatchInventory
from typing import Optional, Set
from typing_extensions import Self

class StockItemBatch(BaseModel):
    """
    StockItemBatch
    """ # noqa: E501
    batch_id: Optional[StrictInt] = Field(default=None, alias="BatchId")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    inventory_tracking_type: Optional[StrictInt] = Field(default=None, alias="InventoryTrackingType")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    batch_number: Optional[StrictStr] = Field(default=None, alias="BatchNumber")
    expires_on: Optional[datetime] = Field(default=None, alias="ExpiresOn")
    sell_by: Optional[datetime] = Field(default=None, alias="SellBy")
    inventory: Optional[List[StockItemBatchInventory]] = Field(default=None, alias="Inventory")
    is_deleted: Optional[StrictBool] = Field(default=None, alias="IsDeleted")
    __properties: ClassVar[List[str]] = ["BatchId", "SKU", "InventoryTrackingType", "StockItemId", "BatchNumber", "ExpiresOn", "SellBy", "Inventory", "IsDeleted"]

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
        """Create an instance of StockItemBatch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inventory (list)
        _items = []
        if self.inventory:
            for _item_inventory in self.inventory:
                if _item_inventory:
                    _items.append(_item_inventory.to_dict())
            _dict['Inventory'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemBatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "BatchId": obj.get("BatchId"),
            "SKU": obj.get("SKU"),
            "InventoryTrackingType": obj.get("InventoryTrackingType"),
            "StockItemId": obj.get("StockItemId"),
            "BatchNumber": obj.get("BatchNumber"),
            "ExpiresOn": obj.get("ExpiresOn"),
            "SellBy": obj.get("SellBy"),
            "Inventory": [StockItemBatchInventory.from_dict(_item) for _item in obj["Inventory"]] if obj.get("Inventory") is not None else None,
            "IsDeleted": obj.get("IsDeleted")
        })
        return _obj


