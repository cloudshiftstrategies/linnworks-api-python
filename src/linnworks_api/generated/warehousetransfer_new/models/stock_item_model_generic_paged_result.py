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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer_new.models.stock_item_model import StockItemModel
from typing import Optional, Set
from typing_extensions import Self

class StockItemModelGenericPagedResult(BaseModel):
    """
    Order item object
    """ # noqa: E501
    page_number: Optional[StrictInt] = Field(default=None, description="Result page number", alias="pageNumber")
    entries_per_page: Optional[StrictInt] = Field(default=None, description="Result page size, quantity of records per page", alias="entriesPerPage")
    total_entries: Optional[StrictInt] = Field(default=None, description="Total records", alias="totalEntries")
    total_pages: Optional[StrictInt] = Field(default=None, description="Total pages", alias="totalPages")
    data: Optional[List[StockItemModel]] = None
    __properties: ClassVar[List[str]] = ["pageNumber", "entriesPerPage", "totalEntries", "totalPages", "data"]

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
        """Create an instance of StockItemModelGenericPagedResult from a JSON string"""
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
            "total_pages",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemModelGenericPagedResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pageNumber": obj.get("pageNumber"),
            "entriesPerPage": obj.get("entriesPerPage"),
            "totalEntries": obj.get("totalEntries"),
            "totalPages": obj.get("totalPages"),
            "data": [StockItemModel.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None
        })
        return _obj


