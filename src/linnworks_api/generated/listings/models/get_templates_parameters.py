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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.listings.models.site_filter import SiteFilter
from linnworks_api.generated.listings.models.tuple_int32_int32 import TupleInt32Int32
from typing import Optional, Set
from typing_extensions import Self

class GetTemplatesParameters(BaseModel):
    """
    GetTemplatesParameters
    """ # noqa: E501
    template_ids: Optional[List[StrictStr]] = Field(default=None, alias="TemplateIds")
    only_with_errors: Optional[StrictBool] = Field(default=None, alias="OnlyWithErrors")
    source: Optional[StrictStr] = Field(default=None, alias="Source")
    sub_source: Optional[StrictStr] = Field(default=None, alias="SubSource")
    config_id: Optional[StrictStr] = Field(default=None, alias="ConfigId")
    inventory_item_ids: Optional[List[StrictStr]] = Field(default=None, alias="InventoryItemIds")
    selected_regions: Optional[List[TupleInt32Int32]] = Field(default=None, alias="SelectedRegions")
    token: Optional[StrictStr] = Field(default=None, alias="Token")
    templates_type: Optional[StrictStr] = Field(default=None, alias="TemplatesType")
    page_number: Optional[StrictInt] = Field(default=None, alias="PageNumber")
    entries_per_page: Optional[StrictInt] = Field(default=None, alias="EntriesPerPage")
    is_migrated: Optional[StrictBool] = Field(default=None, alias="IsMigrated")
    site_filter: Optional[SiteFilter] = Field(default=None, alias="SiteFilter")
    __properties: ClassVar[List[str]] = ["TemplateIds", "OnlyWithErrors", "Source", "SubSource", "ConfigId", "InventoryItemIds", "SelectedRegions", "Token", "TemplatesType", "PageNumber", "EntriesPerPage", "IsMigrated", "SiteFilter"]

    @field_validator('templates_type')
    def templates_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Both', 'Simple', 'Variation']):
            raise ValueError("must be one of enum values ('Both', 'Simple', 'Variation')")
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
        """Create an instance of GetTemplatesParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in selected_regions (list)
        _items = []
        if self.selected_regions:
            for _item_selected_regions in self.selected_regions:
                if _item_selected_regions:
                    _items.append(_item_selected_regions.to_dict())
            _dict['SelectedRegions'] = _items
        # override the default output from pydantic by calling `to_dict()` of site_filter
        if self.site_filter:
            _dict['SiteFilter'] = self.site_filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTemplatesParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TemplateIds": obj.get("TemplateIds"),
            "OnlyWithErrors": obj.get("OnlyWithErrors"),
            "Source": obj.get("Source"),
            "SubSource": obj.get("SubSource"),
            "ConfigId": obj.get("ConfigId"),
            "InventoryItemIds": obj.get("InventoryItemIds"),
            "SelectedRegions": [TupleInt32Int32.from_dict(_item) for _item in obj["SelectedRegions"]] if obj.get("SelectedRegions") is not None else None,
            "Token": obj.get("Token"),
            "TemplatesType": obj.get("TemplatesType"),
            "PageNumber": obj.get("PageNumber"),
            "EntriesPerPage": obj.get("EntriesPerPage"),
            "IsMigrated": obj.get("IsMigrated"),
            "SiteFilter": SiteFilter.from_dict(obj["SiteFilter"]) if obj.get("SiteFilter") is not None else None
        })
        return _obj


