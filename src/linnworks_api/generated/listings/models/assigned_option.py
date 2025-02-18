# coding: utf-8

"""
    Listings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: listings
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.listings.models.option_value import OptionValue
from typing import Optional, Set
from typing_extensions import Self

class AssignedOption(BaseModel):
    """
    AssignedOption
    """ # noqa: E501
    id_v3: Optional[StrictInt] = Field(default=None, alias="IdV3")
    id: Optional[StrictInt] = Field(default=None, alias="Id")
    values: Optional[List[OptionValue]] = Field(default=None, alias="Values")
    option_display_name: Optional[StrictStr] = Field(default=None, alias="OptionDisplayName")
    option_name: Optional[StrictStr] = Field(default=None, alias="OptionName")
    mapped_from_bc: Optional[StrictBool] = Field(default=None, alias="MappedFromBC")
    assignment_id: Optional[StrictInt] = Field(default=None, alias="AssignmentId")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    __properties: ClassVar[List[str]] = ["IdV3", "Id", "Values", "OptionDisplayName", "OptionName", "MappedFromBC", "AssignmentId", "Type"]

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
        """Create an instance of AssignedOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item_values in self.values:
                if _item_values:
                    _items.append(_item_values.to_dict())
            _dict['Values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssignedOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IdV3": obj.get("IdV3"),
            "Id": obj.get("Id"),
            "Values": [OptionValue.from_dict(_item) for _item in obj["Values"]] if obj.get("Values") is not None else None,
            "OptionDisplayName": obj.get("OptionDisplayName"),
            "OptionName": obj.get("OptionName"),
            "MappedFromBC": obj.get("MappedFromBC"),
            "AssignmentId": obj.get("AssignmentId"),
            "Type": obj.get("Type")
        })
        return _obj


