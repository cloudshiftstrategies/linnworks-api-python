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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BatchPickingWaveStockItems(BaseModel):
    """
    BatchPickingWaveStockItems
    """ # noqa: E501
    picking_wave_items_row_id: Optional[StrictInt] = Field(default=None, alias="PickingWaveItemsRowId")
    picking_wave_id: Optional[StrictInt] = Field(default=None, alias="PickingWaveId")
    user_name: Optional[StrictStr] = Field(default=None, alias="UserName")
    to_pick_quantity: Optional[StrictInt] = Field(default=None, alias="ToPickQuantity")
    picked_quantity: Optional[StrictInt] = Field(default=None, alias="PickedQuantity")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    order_id: Optional[StrictInt] = Field(default=None, alias="OrderId")
    user_id: Optional[StrictInt] = Field(default=None, alias="UserId")
    __properties: ClassVar[List[str]] = ["PickingWaveItemsRowId", "PickingWaveId", "UserName", "ToPickQuantity", "PickedQuantity", "StockItemId", "OrderId", "UserId"]

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
        """Create an instance of BatchPickingWaveStockItems from a JSON string"""
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
        """Create an instance of BatchPickingWaveStockItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PickingWaveItemsRowId": obj.get("PickingWaveItemsRowId"),
            "PickingWaveId": obj.get("PickingWaveId"),
            "UserName": obj.get("UserName"),
            "ToPickQuantity": obj.get("ToPickQuantity"),
            "PickedQuantity": obj.get("PickedQuantity"),
            "StockItemId": obj.get("StockItemId"),
            "OrderId": obj.get("OrderId"),
            "UserId": obj.get("UserId")
        })
        return _obj


