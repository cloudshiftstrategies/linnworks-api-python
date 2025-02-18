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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.stock.models.stock_item_pricing_rule import StockItemPricingRule
from typing import Optional, Set
from typing_extensions import Self

class StockItemPrice(BaseModel):
    """
    StockItemPrice
    """ # noqa: E501
    rules: Optional[List[StockItemPricingRule]] = Field(default=None, alias="Rules")
    pk_row_id: Optional[StrictStr] = Field(default=None, alias="pkRowId")
    source: Optional[StrictStr] = Field(default=None, alias="Source")
    sub_source: Optional[StrictStr] = Field(default=None, alias="SubSource")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Price")
    tag: Optional[StrictStr] = Field(default=None, alias="Tag")
    update_status: Optional[StrictStr] = Field(default=None, alias="UpdateStatus")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="StockItemIntId")
    __properties: ClassVar[List[str]] = ["Rules", "pkRowId", "Source", "SubSource", "Price", "Tag", "UpdateStatus", "StockItemId", "StockItemIntId"]

    @field_validator('update_status')
    def update_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NoChange', 'Pending', 'SentNotConfirmed', 'Success', 'Error']):
            raise ValueError("must be one of enum values ('NoChange', 'Pending', 'SentNotConfirmed', 'Success', 'Error')")
        return value

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
        """Create an instance of StockItemPrice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['Rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemPrice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Rules": [StockItemPricingRule.from_dict(_item) for _item in obj["Rules"]] if obj.get("Rules") is not None else None,
            "pkRowId": obj.get("pkRowId"),
            "Source": obj.get("Source"),
            "SubSource": obj.get("SubSource"),
            "Price": obj.get("Price"),
            "Tag": obj.get("Tag"),
            "UpdateStatus": obj.get("UpdateStatus"),
            "StockItemId": obj.get("StockItemId"),
            "StockItemIntId": obj.get("StockItemIntId")
        })
        return _obj


