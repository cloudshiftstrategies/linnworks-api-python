# coding: utf-8

"""
    Import and Export API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: importexport
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.importexport.models.execution_option_type import ExecutionOptionType
from typing import Optional, Set
from typing_extensions import Self

class ExecutionOption(BaseModel):
    """
    ExecutionOption
    """ # noqa: E501
    option_details: Optional[ExecutionOptionType] = Field(default=None, alias="OptionDetails")
    display_name: Optional[StrictStr] = Field(default=None, alias="DisplayName")
    value: Optional[Dict[str, Any]] = Field(default=None, alias="Value")
    __properties: ClassVar[List[str]] = ["OptionDetails", "DisplayName", "Value"]

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
        """Create an instance of ExecutionOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of option_details
        if self.option_details:
            _dict['OptionDetails'] = self.option_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExecutionOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OptionDetails": ExecutionOptionType.from_dict(obj["OptionDetails"]) if obj.get("OptionDetails") is not None else None,
            "DisplayName": obj.get("DisplayName"),
            "Value": obj.get("Value")
        })
        return _obj


