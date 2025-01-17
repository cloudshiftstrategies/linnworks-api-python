# coding: utf-8

"""
    Rules Engine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: rulesengine
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FieldDescriptor(BaseModel):
    """
    FieldDescriptor
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    field_name: Optional[StrictStr] = Field(default=None, alias="FieldName")
    field_group: Optional[StrictStr] = Field(default=None, alias="FieldGroup")
    is_a_set: Optional[StrictBool] = Field(default=None, alias="IsASet")
    valid_evaluator_groups: Optional[List[StrictStr]] = Field(default=None, alias="ValidEvaluatorGroups")
    key: Optional[StrictStr] = Field(default=None, alias="Key")
    key_display_name: Optional[StrictStr] = Field(default=None, alias="KeyDisplayName")
    has_key_options: Optional[StrictBool] = Field(default=None, alias="HasKeyOptions")
    has_attribute_key: Optional[StrictBool] = Field(default=None, alias="HasAttributeKey")
    has_options: Optional[StrictBool] = Field(default=None, alias="HasOptions")
    display_type: Optional[StrictStr] = Field(default=None, alias="DisplayType")
    exact_match_required: Optional[StrictBool] = Field(default=None, alias="ExactMatchRequired")
    __properties: ClassVar[List[str]] = ["Name", "FieldName", "FieldGroup", "IsASet", "ValidEvaluatorGroups", "Key", "KeyDisplayName", "HasKeyOptions", "HasAttributeKey", "HasOptions", "DisplayType", "ExactMatchRequired"]

    @field_validator('valid_evaluator_groups')
    def valid_evaluator_groups_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BasicEquality', 'Range', 'Set', 'NumberEquality', 'StringEquality']):
                raise ValueError("each list item must be one of ('BasicEquality', 'Range', 'Set', 'NumberEquality', 'StringEquality')")
        return value

    @field_validator('display_type')
    def display_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FreeText', 'AutoComplete', 'Dropdown', 'None']):
            raise ValueError("must be one of enum values ('FreeText', 'AutoComplete', 'Dropdown', 'None')")
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
        """Create an instance of FieldDescriptor from a JSON string"""
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
            "has_attribute_key",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FieldDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "FieldName": obj.get("FieldName"),
            "FieldGroup": obj.get("FieldGroup"),
            "IsASet": obj.get("IsASet"),
            "ValidEvaluatorGroups": obj.get("ValidEvaluatorGroups"),
            "Key": obj.get("Key"),
            "KeyDisplayName": obj.get("KeyDisplayName"),
            "HasKeyOptions": obj.get("HasKeyOptions"),
            "HasAttributeKey": obj.get("HasAttributeKey"),
            "HasOptions": obj.get("HasOptions"),
            "DisplayType": obj.get("DisplayType"),
            "ExactMatchRequired": obj.get("ExactMatchRequired")
        })
        return _obj


