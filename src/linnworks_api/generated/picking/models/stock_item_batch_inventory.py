# coding: utf-8

"""
    Picking API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: picking
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class StockItemBatchInventory(BaseModel):
    """
    StockItemBatchInventory
    """ # noqa: E501
    batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="BatchInventoryId")
    batch_id: Optional[StrictInt] = Field(default=None, alias="BatchId")
    stock_location_id: Optional[StrictStr] = Field(default=None, alias="StockLocationId")
    bin_rack: Optional[StrictStr] = Field(default=None, alias="BinRack")
    priority_sequence: Optional[StrictInt] = Field(default=None, alias="PrioritySequence")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    stock_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StockValue")
    start_quantity: Optional[StrictInt] = Field(default=None, alias="StartQuantity")
    picked_quantity: Optional[StrictInt] = Field(default=None, alias="PickedQuantity")
    batch_status: Optional[StrictStr] = Field(default=None, alias="BatchStatus")
    is_deleted: Optional[StrictBool] = Field(default=None, alias="IsDeleted")
    warehouse_binrack_standard_type: Optional[StrictInt] = Field(default=None, alias="WarehouseBinrackStandardType")
    warehouse_binrack_type_name: Optional[StrictStr] = Field(default=None, alias="WarehouseBinrackTypeName")
    in_transfer: Optional[StrictInt] = Field(default=None, alias="InTransfer")
    bin_rack_id: Optional[StrictInt] = Field(default=None, alias="BinRackId")
    warehouse_binrack_type_id: Optional[StrictInt] = Field(default=None, alias="WarehouseBinrackTypeId")
    __properties: ClassVar[List[str]] = ["BatchInventoryId", "BatchId", "StockLocationId", "BinRack", "PrioritySequence", "Quantity", "StockValue", "StartQuantity", "PickedQuantity", "BatchStatus", "IsDeleted", "WarehouseBinrackStandardType", "WarehouseBinrackTypeName", "InTransfer", "BinRackId", "WarehouseBinrackTypeId"]

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
        """Create an instance of StockItemBatchInventory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "start_quantity",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemBatchInventory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "BatchInventoryId": obj.get("BatchInventoryId"),
            "BatchId": obj.get("BatchId"),
            "StockLocationId": obj.get("StockLocationId"),
            "BinRack": obj.get("BinRack"),
            "PrioritySequence": obj.get("PrioritySequence"),
            "Quantity": obj.get("Quantity"),
            "StockValue": obj.get("StockValue"),
            "StartQuantity": obj.get("StartQuantity"),
            "PickedQuantity": obj.get("PickedQuantity"),
            "BatchStatus": obj.get("BatchStatus"),
            "IsDeleted": obj.get("IsDeleted"),
            "WarehouseBinrackStandardType": obj.get("WarehouseBinrackStandardType"),
            "WarehouseBinrackTypeName": obj.get("WarehouseBinrackTypeName"),
            "InTransfer": obj.get("InTransfer"),
            "BinRackId": obj.get("BinRackId"),
            "WarehouseBinrackTypeId": obj.get("WarehouseBinrackTypeId")
        })
        return _obj


