# coding: utf-8

"""
    Generic Listings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: genericlistings
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.genericlistings.models.inventory_search_parameters import InventorySearchParameters
from linnworks_api.generated.genericlistings.models.pagination_parameters import PaginationParameters
from typing import Optional, Set
from typing_extensions import Self

class CreateTemplatesRequest(BaseModel):
    """
    CreateTemplatesRequest
    """ # noqa: E501
    channel_type: Optional[StrictStr] = Field(default=None, alias="ChannelType")
    channel_name: Optional[StrictStr] = Field(default=None, alias="ChannelName")
    parameters: Optional[InventorySearchParameters] = Field(default=None, alias="Parameters")
    pagination_parameters: Optional[PaginationParameters] = Field(default=None, alias="PaginationParameters")
    configurator_id: Optional[StrictInt] = Field(default=None, alias="ConfiguratorId")
    __properties: ClassVar[List[str]] = ["ChannelType", "ChannelName", "Parameters", "PaginationParameters", "ConfiguratorId"]

    @field_validator('channel_type')
    def channel_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CDiscount', 'Shopify', 'Magento', 'External', 'Walmart', 'TikTok']):
            raise ValueError("must be one of enum values ('CDiscount', 'Shopify', 'Magento', 'External', 'Walmart', 'TikTok')")
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
        """Create an instance of CreateTemplatesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['Parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pagination_parameters
        if self.pagination_parameters:
            _dict['PaginationParameters'] = self.pagination_parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateTemplatesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChannelType": obj.get("ChannelType"),
            "ChannelName": obj.get("ChannelName"),
            "Parameters": InventorySearchParameters.from_dict(obj["Parameters"]) if obj.get("Parameters") is not None else None,
            "PaginationParameters": PaginationParameters.from_dict(obj["PaginationParameters"]) if obj.get("PaginationParameters") is not None else None,
            "ConfiguratorId": obj.get("ConfiguratorId")
        })
        return _obj


