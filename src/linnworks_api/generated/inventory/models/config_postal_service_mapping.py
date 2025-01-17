# coding: utf-8

"""
    Inventory API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: inventory
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.inventory.models.channel_postal_service import ChannelPostalService
from linnworks_api.generated.inventory.models.config_postal_service_mapping_item import ConfigPostalServiceMappingItem
from typing import Optional, Set
from typing_extensions import Self

class ConfigPostalServiceMapping(BaseModel):
    """
    ConfigPostalServiceMapping
    """ # noqa: E501
    mapping: Optional[List[ConfigPostalServiceMappingItem]] = Field(default=None, alias="Mapping")
    channel_services: Optional[List[ChannelPostalService]] = Field(default=None, alias="ChannelServices")
    is_changed: Optional[StrictBool] = Field(default=None, alias="IsChanged")
    __properties: ClassVar[List[str]] = ["Mapping", "ChannelServices", "IsChanged"]

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
        """Create an instance of ConfigPostalServiceMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "mapping",
            "channel_services",
            "is_changed",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in mapping (list)
        _items = []
        if self.mapping:
            for _item_mapping in self.mapping:
                if _item_mapping:
                    _items.append(_item_mapping.to_dict())
            _dict['Mapping'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in channel_services (list)
        _items = []
        if self.channel_services:
            for _item_channel_services in self.channel_services:
                if _item_channel_services:
                    _items.append(_item_channel_services.to_dict())
            _dict['ChannelServices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigPostalServiceMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Mapping": [ConfigPostalServiceMappingItem.from_dict(_item) for _item in obj["Mapping"]] if obj.get("Mapping") is not None else None,
            "ChannelServices": [ChannelPostalService.from_dict(_item) for _item in obj["ChannelServices"]] if obj.get("ChannelServices") is not None else None,
            "IsChanged": obj.get("IsChanged")
        })
        return _obj


