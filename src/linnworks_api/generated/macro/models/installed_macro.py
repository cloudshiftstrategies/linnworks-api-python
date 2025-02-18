# coding: utf-8

"""
    Macros API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: macro
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.macro.models.parameter_definition import ParameterDefinition
from typing import Optional, Set
from typing_extensions import Self

class InstalledMacro(BaseModel):
    """
    InstalledMacro
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, alias="ApplicationName")
    application_logo: Optional[StrictStr] = Field(default=None, alias="ApplicationLogo")
    macro_name: Optional[StrictStr] = Field(default=None, alias="MacroName")
    macro_description: Optional[StrictStr] = Field(default=None, alias="MacroDescription")
    execution_type: Optional[StrictStr] = Field(default=None, alias="ExecutionType")
    source_code_type: Optional[StrictStr] = Field(default=None, alias="SourceCodeType")
    parameters: Optional[List[ParameterDefinition]] = Field(default=None, alias="Parameters")
    __properties: ClassVar[List[str]] = ["ApplicationName", "ApplicationLogo", "MacroName", "MacroDescription", "ExecutionType", "SourceCodeType", "Parameters"]

    @field_validator('execution_type')
    def execution_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['API', 'Scheduled', 'RulesEngine_Order']):
            raise ValueError("must be one of enum values ('API', 'Scheduled', 'RulesEngine_Order')")
        return value

    @field_validator('source_code_type')
    def source_code_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['netcore10', 'netcore21', 'netcore31', 'net6']):
            raise ValueError("must be one of enum values ('netcore10', 'netcore21', 'netcore31', 'net6')")
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
        """Create an instance of InstalledMacro from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item_parameters in self.parameters:
                if _item_parameters:
                    _items.append(_item_parameters.to_dict())
            _dict['Parameters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstalledMacro from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ApplicationName": obj.get("ApplicationName"),
            "ApplicationLogo": obj.get("ApplicationLogo"),
            "MacroName": obj.get("MacroName"),
            "MacroDescription": obj.get("MacroDescription"),
            "ExecutionType": obj.get("ExecutionType"),
            "SourceCodeType": obj.get("SourceCodeType"),
            "Parameters": [ParameterDefinition.from_dict(_item) for _item in obj["Parameters"]] if obj.get("Parameters") is not None else None
        })
        return _obj


