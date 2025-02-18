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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FailedShippingItem(BaseModel):
    """
    FailedShippingItem
    """ # noqa: E501
    sku: Optional[StrictStr] = None
    stock_item_id: Optional[StrictInt] = Field(default=None, alias="stockItemId")
    batch_number: Optional[StrictStr] = Field(default=None, alias="batchNumber")
    batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="batchInventoryId")
    fail_message: Optional[StrictStr] = Field(default=None, alias="failMessage")
    __properties: ClassVar[List[str]] = ["sku", "stockItemId", "batchNumber", "batchInventoryId", "failMessage"]

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
        """Create an instance of FailedShippingItem from a JSON string"""
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
        # set to None if sku (nullable) is None
        # and model_fields_set contains the field
        if self.sku is None and "sku" in self.model_fields_set:
            _dict['sku'] = None

        # set to None if batch_number (nullable) is None
        # and model_fields_set contains the field
        if self.batch_number is None and "batch_number" in self.model_fields_set:
            _dict['batchNumber'] = None

        # set to None if fail_message (nullable) is None
        # and model_fields_set contains the field
        if self.fail_message is None and "fail_message" in self.model_fields_set:
            _dict['failMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FailedShippingItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sku": obj.get("sku"),
            "stockItemId": obj.get("stockItemId"),
            "batchNumber": obj.get("batchNumber"),
            "batchInventoryId": obj.get("batchInventoryId"),
            "failMessage": obj.get("failMessage")
        })
        return _obj


