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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ActionTypeDescriptorProperties(BaseModel):
    """
    ActionTypeDescriptorProperties
    """ # noqa: E501
    display_name: Optional[StrictStr] = Field(default=None, alias="DisplayName")
    display_type: Optional[StrictStr] = Field(default=None, alias="DisplayType")
    field_type: Optional[StrictStr] = Field(default=None, alias="FieldType")
    __properties: ClassVar[List[str]] = ["DisplayName", "DisplayType", "FieldType"]

    @field_validator('display_type')
    def display_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FreeText', 'AutoComplete', 'Dropdown', 'None']):
            raise ValueError("must be one of enum values ('FreeText', 'AutoComplete', 'Dropdown', 'None')")
        return value

    @field_validator('field_type')
    def field_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Default', 'String', 'Int', 'Bool', 'Guid', 'Float', 'Double']):
            raise ValueError("must be one of enum values ('Default', 'String', 'Int', 'Bool', 'Guid', 'Float', 'Double')")
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
        """Create an instance of ActionTypeDescriptorProperties from a JSON string"""
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
        """Create an instance of ActionTypeDescriptorProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DisplayName": obj.get("DisplayName"),
            "DisplayType": obj.get("DisplayType"),
            "FieldType": obj.get("FieldType")
        })
        return _obj


