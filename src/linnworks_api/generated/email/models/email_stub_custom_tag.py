# coding: utf-8

"""
    Email API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: email
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EmailStubCustomTag(BaseModel):
    """
    EmailStubCustomTag
    """ # noqa: E501
    pk_email_stub_tag_id: Optional[StrictInt] = Field(default=None, alias="pkEmailStubTagId")
    fk_email_stub_id: Optional[StrictInt] = Field(default=None, alias="fkEmailStubId")
    tag_name: Optional[StrictStr] = Field(default=None, alias="TagName")
    tag_value: Optional[StrictStr] = Field(default=None, alias="TagValue")
    __properties: ClassVar[List[str]] = ["pkEmailStubTagId", "fkEmailStubId", "TagName", "TagValue"]

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
        """Create an instance of EmailStubCustomTag from a JSON string"""
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
        """Create an instance of EmailStubCustomTag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkEmailStubTagId": obj.get("pkEmailStubTagId"),
            "fkEmailStubId": obj.get("fkEmailStubId"),
            "TagName": obj.get("TagName"),
            "TagValue": obj.get("TagValue")
        })
        return _obj


