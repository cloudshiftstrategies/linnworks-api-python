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
from typing import Optional, Set
from typing_extensions import Self

class GetBinrackZonesByZoneIdOrNameResponse(BaseModel):
    """
    GetBinrackZonesByZoneIdOrNameResponse
    """ # noqa: E501
    warehouse_zones: Optional[List[WarehouseZone]] = Field(default=None, alias="WarehouseZones")
    __properties: ClassVar[List[str]] = ["WarehouseZones"]

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
        """Create an instance of GetBinrackZonesByZoneIdOrNameResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in warehouse_zones (list)
        _items = []
        if self.warehouse_zones:
            for _item_warehouse_zones in self.warehouse_zones:
                if _item_warehouse_zones:
                    _items.append(_item_warehouse_zones.to_dict())
            _dict['WarehouseZones'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetBinrackZonesByZoneIdOrNameResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "WarehouseZones": [WarehouseZone.from_dict(_item) for _item in obj["WarehouseZones"]] if obj.get("WarehouseZones") is not None else None
        })
        return _obj


