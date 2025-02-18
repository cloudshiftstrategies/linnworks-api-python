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
from linnworks_api.generated.listings.models.assigned_option import AssignedOption
from typing import Optional, Set
from typing_extensions import Self

class AssignedOptionSet(BaseModel):
    """
    AssignedOptionSet
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, alias="Id")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    mapped_from_bc: Optional[StrictBool] = Field(default=None, alias="MappedFromBC")
    options: Optional[List[AssignedOption]] = Field(default=None, alias="Options")
    __properties: ClassVar[List[str]] = ["Id", "Name", "MappedFromBC", "Options"]

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
        """Create an instance of AssignedOptionSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['Options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssignedOptionSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Name": obj.get("Name"),
            "MappedFromBC": obj.get("MappedFromBC"),
            "Options": [AssignedOption.from_dict(_item) for _item in obj["Options"]] if obj.get("Options") is not None else None
        })
        return _obj


