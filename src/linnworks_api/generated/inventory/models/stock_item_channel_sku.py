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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class StockItemChannelSKU(BaseModel):
    """
    StockItemChannelSKU
    """ # noqa: E501
    channel_sku_row_id: Optional[StrictStr] = Field(default=None, alias="ChannelSKURowId")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    source: Optional[StrictStr] = Field(default=None, alias="Source")
    sub_source: Optional[StrictStr] = Field(default=None, alias="SubSource")
    update_status: Optional[StrictStr] = Field(default=None, alias="UpdateStatus")
    channel_reference_id: Optional[StrictStr] = Field(default=None, alias="ChannelReferenceId")
    last_update: Optional[datetime] = Field(default=None, alias="LastUpdate")
    max_listed_quantity: Optional[StrictInt] = Field(default=None, alias="MaxListedQuantity")
    end_when_stock: Optional[StrictInt] = Field(default=None, alias="EndWhenStock")
    submitted_quantity: Optional[StrictInt] = Field(default=None, alias="SubmittedQuantity")
    listed_quantity: Optional[StrictInt] = Field(default=None, alias="ListedQuantity")
    stock_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="StockPercentage")
    ignore_sync: Optional[StrictBool] = Field(default=None, alias="IgnoreSync")
    ignore_sync_multi_location: Optional[StrictBool] = Field(default=None, alias="IgnoreSyncMultiLocation")
    is_multi_location: Optional[StrictBool] = Field(default=None, alias="IsMultiLocation")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="StockItemIntId")
    __properties: ClassVar[List[str]] = ["ChannelSKURowId", "SKU", "Source", "SubSource", "UpdateStatus", "ChannelReferenceId", "LastUpdate", "MaxListedQuantity", "EndWhenStock", "SubmittedQuantity", "ListedQuantity", "StockPercentage", "IgnoreSync", "IgnoreSyncMultiLocation", "IsMultiLocation", "StockItemId", "StockItemIntId"]

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
        """Create an instance of StockItemChannelSKU from a JSON string"""
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
        """Create an instance of StockItemChannelSKU from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChannelSKURowId": obj.get("ChannelSKURowId"),
            "SKU": obj.get("SKU"),
            "Source": obj.get("Source"),
            "SubSource": obj.get("SubSource"),
            "UpdateStatus": obj.get("UpdateStatus"),
            "ChannelReferenceId": obj.get("ChannelReferenceId"),
            "LastUpdate": obj.get("LastUpdate"),
            "MaxListedQuantity": obj.get("MaxListedQuantity"),
            "EndWhenStock": obj.get("EndWhenStock"),
            "SubmittedQuantity": obj.get("SubmittedQuantity"),
            "ListedQuantity": obj.get("ListedQuantity"),
            "StockPercentage": obj.get("StockPercentage"),
            "IgnoreSync": obj.get("IgnoreSync"),
            "IgnoreSyncMultiLocation": obj.get("IgnoreSyncMultiLocation"),
            "IsMultiLocation": obj.get("IsMultiLocation"),
            "StockItemId": obj.get("StockItemId"),
            "StockItemIntId": obj.get("StockItemIntId")
        })
        return _obj


