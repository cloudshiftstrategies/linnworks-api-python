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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BatchStockLevelDelta(BaseModel):
    """
    BatchStockLevelDelta
    """ # noqa: E501
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    batch_number: Optional[StrictStr] = Field(default=None, alias="BatchNumber")
    bin_rack: Optional[StrictStr] = Field(default=None, alias="BinRack")
    delta_quantity: Optional[StrictInt] = Field(default=None, alias="DeltaQuantity")
    reason: Optional[StrictStr] = Field(default=None, alias="Reason")
    pk_batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="pkBatchInventoryId")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    stock_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StockValue")
    errors: Optional[List[StrictStr]] = Field(default=None, alias="Errors")
    new_level: Optional[StrictInt] = Field(default=None, alias="NewLevel")
    batch_status: Optional[StrictStr] = Field(default=None, alias="BatchStatus")
    __properties: ClassVar[List[str]] = ["SKU", "BatchNumber", "BinRack", "DeltaQuantity", "Reason", "pkBatchInventoryId", "Quantity", "StockValue", "Errors", "NewLevel", "BatchStatus"]

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
        """Create an instance of BatchStockLevelDelta from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "pk_batch_inventory_id",
            "quantity",
            "stock_value",
            "new_level",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchStockLevelDelta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "SKU": obj.get("SKU"),
            "BatchNumber": obj.get("BatchNumber"),
            "BinRack": obj.get("BinRack"),
            "DeltaQuantity": obj.get("DeltaQuantity"),
            "Reason": obj.get("Reason"),
            "pkBatchInventoryId": obj.get("pkBatchInventoryId"),
            "Quantity": obj.get("Quantity"),
            "StockValue": obj.get("StockValue"),
            "Errors": obj.get("Errors"),
            "NewLevel": obj.get("NewLevel"),
            "BatchStatus": obj.get("BatchStatus")
        })
        return _obj


