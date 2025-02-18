# coding: utf-8

"""
    WMS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: wms
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.wms.models.warehouse_zone import WarehouseZone
from linnworks_api.generated.wms.models.warehouse_zone_binrack_count import WarehouseZoneBinrackCount
from linnworks_api.generated.wms.models.warehouse_zone_group import WarehouseZoneGroup
from linnworks_api.generated.wms.models.warehouse_zone_group_to_zone import WarehouseZoneGroupToZone
from linnworks_api.generated.wms.models.warehouse_zone_to_zone import WarehouseZoneToZone
from linnworks_api.generated.wms.models.warehouse_zone_type import WarehouseZoneType
from typing import Optional, Set
from typing_extensions import Self

class GetWarehouseZonesByLocationResponse(BaseModel):
    """
    GetWarehouseZonesByLocationResponse
    """ # noqa: E501
    zones: Optional[List[WarehouseZone]] = Field(default=None, description="Warehouse Zones", alias="Zones")
    zone_types: Optional[List[WarehouseZoneType]] = Field(default=None, description="Warehouse Zone types", alias="ZoneTypes")
    zone_groups: Optional[List[WarehouseZoneGroup]] = Field(default=None, description="Zone groups", alias="ZoneGroups")
    zone_groups_to_zones: Optional[List[WarehouseZoneGroupToZone]] = Field(default=None, description="Zone groups to zones.", alias="ZoneGroupsToZones")
    zones_binracks_count: Optional[List[WarehouseZoneBinrackCount]] = Field(default=None, description="Zone binrack counts. Only returns zone if binrack is directly in zone.", alias="ZonesBinracksCount")
    zones_to_zones_hierarchy: Optional[List[WarehouseZoneToZone]] = Field(default=None, description="Zone to zones hierarchy", alias="ZonesToZonesHierarchy")
    __properties: ClassVar[List[str]] = ["Zones", "ZoneTypes", "ZoneGroups", "ZoneGroupsToZones", "ZonesBinracksCount", "ZonesToZonesHierarchy"]

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
        """Create an instance of GetWarehouseZonesByLocationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in zones (list)
        _items = []
        if self.zones:
            for _item_zones in self.zones:
                if _item_zones:
                    _items.append(_item_zones.to_dict())
            _dict['Zones'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zone_types (list)
        _items = []
        if self.zone_types:
            for _item_zone_types in self.zone_types:
                if _item_zone_types:
                    _items.append(_item_zone_types.to_dict())
            _dict['ZoneTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zone_groups (list)
        _items = []
        if self.zone_groups:
            for _item_zone_groups in self.zone_groups:
                if _item_zone_groups:
                    _items.append(_item_zone_groups.to_dict())
            _dict['ZoneGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zone_groups_to_zones (list)
        _items = []
        if self.zone_groups_to_zones:
            for _item_zone_groups_to_zones in self.zone_groups_to_zones:
                if _item_zone_groups_to_zones:
                    _items.append(_item_zone_groups_to_zones.to_dict())
            _dict['ZoneGroupsToZones'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zones_binracks_count (list)
        _items = []
        if self.zones_binracks_count:
            for _item_zones_binracks_count in self.zones_binracks_count:
                if _item_zones_binracks_count:
                    _items.append(_item_zones_binracks_count.to_dict())
            _dict['ZonesBinracksCount'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in zones_to_zones_hierarchy (list)
        _items = []
        if self.zones_to_zones_hierarchy:
            for _item_zones_to_zones_hierarchy in self.zones_to_zones_hierarchy:
                if _item_zones_to_zones_hierarchy:
                    _items.append(_item_zones_to_zones_hierarchy.to_dict())
            _dict['ZonesToZonesHierarchy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetWarehouseZonesByLocationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Zones": [WarehouseZone.from_dict(_item) for _item in obj["Zones"]] if obj.get("Zones") is not None else None,
            "ZoneTypes": [WarehouseZoneType.from_dict(_item) for _item in obj["ZoneTypes"]] if obj.get("ZoneTypes") is not None else None,
            "ZoneGroups": [WarehouseZoneGroup.from_dict(_item) for _item in obj["ZoneGroups"]] if obj.get("ZoneGroups") is not None else None,
            "ZoneGroupsToZones": [WarehouseZoneGroupToZone.from_dict(_item) for _item in obj["ZoneGroupsToZones"]] if obj.get("ZoneGroupsToZones") is not None else None,
            "ZonesBinracksCount": [WarehouseZoneBinrackCount.from_dict(_item) for _item in obj["ZonesBinracksCount"]] if obj.get("ZonesBinracksCount") is not None else None,
            "ZonesToZonesHierarchy": [WarehouseZoneToZone.from_dict(_item) for _item in obj["ZonesToZonesHierarchy"]] if obj.get("ZonesToZonesHierarchy") is not None else None
        })
        return _obj


