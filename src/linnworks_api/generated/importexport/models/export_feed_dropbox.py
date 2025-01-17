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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.importexport.models.dropbox_account import DropboxAccount
from linnworks_api.generated.importexport.models.export_generic_feed import ExportGenericFeed
from typing import Optional, Set
from typing_extensions import Self

class ExportFeedDropbox(ExportGenericFeed):
    """
    ExportFeedDropbox
    """ # noqa: E501
    account: Optional[DropboxAccount] = Field(default=None, alias="Account")
    __properties: ClassVar[List[str]] = ["FeedType", "FileName", "FilePath", "TempFileName", "IfFileExist", "discriminator", "Account"]

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
        """Create an instance of ExportFeedDropbox from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['Account'] = self.account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExportFeedDropbox from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FeedType": obj.get("FeedType"),
            "FileName": obj.get("FileName"),
            "FilePath": obj.get("FilePath"),
            "TempFileName": obj.get("TempFileName"),
            "IfFileExist": obj.get("IfFileExist"),
            "discriminator": obj.get("discriminator"),
            "Account": DropboxAccount.from_dict(obj["Account"]) if obj.get("Account") is not None else None
        })
        return _obj


