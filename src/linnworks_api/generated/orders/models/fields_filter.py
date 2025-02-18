# coding: utf-8

"""
    Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: orders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.orders.models.boolean_field_filter import BooleanFieldFilter
from linnworks_api.generated.orders.models.date_field_filter import DateFieldFilter
from linnworks_api.generated.orders.models.field_visibility import FieldVisibility
from linnworks_api.generated.orders.models.list_field_filter import ListFieldFilter
from linnworks_api.generated.orders.models.numeric_field_filter import NumericFieldFilter
from linnworks_api.generated.orders.models.text_field_filter import TextFieldFilter
from typing import Optional, Set
from typing_extensions import Self

class FieldsFilter(BaseModel):
    """
    FieldsFilter
    """ # noqa: E501
    text_fields: Optional[List[TextFieldFilter]] = Field(default=None, alias="TextFields")
    boolean_fields: Optional[List[BooleanFieldFilter]] = Field(default=None, alias="BooleanFields")
    numeric_fields: Optional[List[NumericFieldFilter]] = Field(default=None, alias="NumericFields")
    date_fields: Optional[List[DateFieldFilter]] = Field(default=None, alias="DateFields")
    list_fields: Optional[List[ListFieldFilter]] = Field(default=None, alias="ListFields")
    field_visibility: Optional[List[FieldVisibility]] = Field(default=None, alias="FieldVisibility")
    __properties: ClassVar[List[str]] = ["TextFields", "BooleanFields", "NumericFields", "DateFields", "ListFields", "FieldVisibility"]

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
        """Create an instance of FieldsFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in text_fields (list)
        _items = []
        if self.text_fields:
            for _item_text_fields in self.text_fields:
                if _item_text_fields:
                    _items.append(_item_text_fields.to_dict())
            _dict['TextFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in boolean_fields (list)
        _items = []
        if self.boolean_fields:
            for _item_boolean_fields in self.boolean_fields:
                if _item_boolean_fields:
                    _items.append(_item_boolean_fields.to_dict())
            _dict['BooleanFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in numeric_fields (list)
        _items = []
        if self.numeric_fields:
            for _item_numeric_fields in self.numeric_fields:
                if _item_numeric_fields:
                    _items.append(_item_numeric_fields.to_dict())
            _dict['NumericFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in date_fields (list)
        _items = []
        if self.date_fields:
            for _item_date_fields in self.date_fields:
                if _item_date_fields:
                    _items.append(_item_date_fields.to_dict())
            _dict['DateFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in list_fields (list)
        _items = []
        if self.list_fields:
            for _item_list_fields in self.list_fields:
                if _item_list_fields:
                    _items.append(_item_list_fields.to_dict())
            _dict['ListFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in field_visibility (list)
        _items = []
        if self.field_visibility:
            for _item_field_visibility in self.field_visibility:
                if _item_field_visibility:
                    _items.append(_item_field_visibility.to_dict())
            _dict['FieldVisibility'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FieldsFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TextFields": [TextFieldFilter.from_dict(_item) for _item in obj["TextFields"]] if obj.get("TextFields") is not None else None,
            "BooleanFields": [BooleanFieldFilter.from_dict(_item) for _item in obj["BooleanFields"]] if obj.get("BooleanFields") is not None else None,
            "NumericFields": [NumericFieldFilter.from_dict(_item) for _item in obj["NumericFields"]] if obj.get("NumericFields") is not None else None,
            "DateFields": [DateFieldFilter.from_dict(_item) for _item in obj["DateFields"]] if obj.get("DateFields") is not None else None,
            "ListFields": [ListFieldFilter.from_dict(_item) for _item in obj["ListFields"]] if obj.get("ListFields") is not None else None,
            "FieldVisibility": [FieldVisibility.from_dict(_item) for _item in obj["FieldVisibility"]] if obj.get("FieldVisibility") is not None else None
        })
        return _obj


