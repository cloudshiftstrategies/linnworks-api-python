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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class StockItemBatchAudit(BaseModel):
    """
    StockItemBatchAudit
    """ # noqa: E501
    batch_id: Optional[StrictInt] = Field(default=None, alias="BatchId")
    batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="BatchInventoryId")
    quantity_delta: Optional[StrictInt] = Field(default=None, alias="QuantityDelta")
    stock_value_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StockValueDelta")
    change_note: Optional[StrictStr] = Field(default=None, alias="ChangeNote")
    username: Optional[StrictStr] = Field(default=None, alias="Username")
    change_date: Optional[datetime] = Field(default=None, alias="ChangeDate")
    bin_rack: Optional[StrictStr] = Field(default=None, alias="BinRack")
    batch_number: Optional[StrictStr] = Field(default=None, alias="BatchNumber")
    location: Optional[StrictStr] = Field(default=None, alias="Location")
    fk_job_id: Optional[StrictInt] = Field(default=None, alias="fkJobId")
    order_id: Optional[StrictInt] = Field(default=None, alias="OrderId")
    __properties: ClassVar[List[str]] = ["BatchId", "BatchInventoryId", "QuantityDelta", "StockValueDelta", "ChangeNote", "Username", "ChangeDate", "BinRack", "BatchNumber", "Location", "fkJobId", "OrderId"]

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
        """Create an instance of StockItemBatchAudit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "batch_id",
            "batch_inventory_id",
            "quantity_delta",
            "stock_value_delta",
            "change_note",
            "username",
            "change_date",
            "bin_rack",
            "batch_number",
            "location",
            "fk_job_id",
            "order_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemBatchAudit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "BatchId": obj.get("BatchId"),
            "BatchInventoryId": obj.get("BatchInventoryId"),
            "QuantityDelta": obj.get("QuantityDelta"),
            "StockValueDelta": obj.get("StockValueDelta"),
            "ChangeNote": obj.get("ChangeNote"),
            "Username": obj.get("Username"),
            "ChangeDate": obj.get("ChangeDate"),
            "BinRack": obj.get("BinRack"),
            "BatchNumber": obj.get("BatchNumber"),
            "Location": obj.get("Location"),
            "fkJobId": obj.get("fkJobId"),
            "OrderId": obj.get("OrderId")
        })
        return _obj


