# coding: utf-8

"""
    Warehouse Transfer

    Warehouse Transfer v1

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.warehousetransfer_new.models.bin_rack_response import BinRackResponse
from typing import Optional, Set
from typing_extensions import Self

class StockItemBatchResponse(BaseModel):
    """
    StockItemBatchResponse
    """ # noqa: E501
    fk_bin_rack_id: Optional[StrictInt] = Field(default=None, alias="fkBinRackId")
    batch_id: Optional[StrictInt] = Field(default=None, alias="batchId")
    batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="batchInventoryId")
    bin_rack_type: Optional[BinRackResponse] = Field(default=None, alias="binRackType")
    bin_rack: Optional[StrictStr] = Field(default=None, alias="binRack")
    expires_on: Optional[datetime] = Field(default=None, alias="expiresOn")
    number: Optional[StrictStr] = None
    priority_sequence: Optional[StrictInt] = Field(default=None, alias="prioritySequence")
    available: Optional[StrictInt] = None
    quantity: Optional[StrictInt] = None
    sell_by: Optional[datetime] = Field(default=None, alias="sellBy")
    status: Optional[StrictStr] = None
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="stockItemIntId")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="stockItemId")
    stock_location_id: Optional[StrictStr] = Field(default=None, alias="stockLocationId")
    stock_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="stockValue")
    __properties: ClassVar[List[str]] = ["fkBinRackId", "batchId", "batchInventoryId", "binRackType", "binRack", "expiresOn", "number", "prioritySequence", "available", "quantity", "sellBy", "status", "stockItemIntId", "stockItemId", "stockLocationId", "stockValue"]

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
        """Create an instance of StockItemBatchResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bin_rack_type
        if self.bin_rack_type:
            _dict['binRackType'] = self.bin_rack_type.to_dict()
        # set to None if fk_bin_rack_id (nullable) is None
        # and model_fields_set contains the field
        if self.fk_bin_rack_id is None and "fk_bin_rack_id" in self.model_fields_set:
            _dict['fkBinRackId'] = None

        # set to None if bin_rack (nullable) is None
        # and model_fields_set contains the field
        if self.bin_rack is None and "bin_rack" in self.model_fields_set:
            _dict['binRack'] = None

        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemBatchResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkBinRackId": obj.get("fkBinRackId"),
            "batchId": obj.get("batchId"),
            "batchInventoryId": obj.get("batchInventoryId"),
            "binRackType": BinRackResponse.from_dict(obj["binRackType"]) if obj.get("binRackType") is not None else None,
            "binRack": obj.get("binRack"),
            "expiresOn": obj.get("expiresOn"),
            "number": obj.get("number"),
            "prioritySequence": obj.get("prioritySequence"),
            "available": obj.get("available"),
            "quantity": obj.get("quantity"),
            "sellBy": obj.get("sellBy"),
            "status": obj.get("status"),
            "stockItemIntId": obj.get("stockItemIntId"),
            "stockItemId": obj.get("stockItemId"),
            "stockLocationId": obj.get("stockLocationId"),
            "stockValue": obj.get("stockValue")
        })
        return _obj


