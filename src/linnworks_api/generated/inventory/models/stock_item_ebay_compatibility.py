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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class StockItemEbayCompatibility(BaseModel):
    """
    StockItemEbayCompatibility
    """ # noqa: E501
    fk_stock_item_id: Optional[StrictStr] = Field(default=None, alias="FkStockItemId")
    fk_compatibility_list_id: Optional[StrictStr] = Field(default=None, alias="FkCompatibilityListId")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    compatibility_notes: Optional[StrictStr] = Field(default=None, alias="CompatibilityNotes")
    value: Optional[StrictStr] = Field(default=None, alias="Value")
    include_years: Optional[StrictStr] = Field(default=None, alias="IncludeYears")
    exclude_years: Optional[StrictStr] = Field(default=None, alias="ExcludeYears")
    culture: Optional[StrictStr] = Field(default=None, alias="Culture")
    ebay_compitibility_type: Optional[StrictStr] = Field(default=None, alias="EbayCompitibilityType")
    __properties: ClassVar[List[str]] = ["FkStockItemId", "FkCompatibilityListId", "SKU", "CompatibilityNotes", "Value", "IncludeYears", "ExcludeYears", "Culture", "EbayCompitibilityType"]

    @field_validator('ebay_compitibility_type')
    def ebay_compitibility_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['KType', 'ePID']):
            raise ValueError("must be one of enum values ('KType', 'ePID')")
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
        """Create an instance of StockItemEbayCompatibility from a JSON string"""
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
        """Create an instance of StockItemEbayCompatibility from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FkStockItemId": obj.get("FkStockItemId"),
            "FkCompatibilityListId": obj.get("FkCompatibilityListId"),
            "SKU": obj.get("SKU"),
            "CompatibilityNotes": obj.get("CompatibilityNotes"),
            "Value": obj.get("Value"),
            "IncludeYears": obj.get("IncludeYears"),
            "ExcludeYears": obj.get("ExcludeYears"),
            "Culture": obj.get("Culture"),
            "EbayCompitibilityType": obj.get("EbayCompitibilityType")
        })
        return _obj


