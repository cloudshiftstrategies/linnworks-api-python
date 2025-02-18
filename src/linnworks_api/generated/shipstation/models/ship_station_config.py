# coding: utf-8

"""
    ShipStation API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: shipstation
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.shipstation.models.ship_service import ShipService
from typing import Optional, Set
from typing_extensions import Self

class ShipStationConfig(BaseModel):
    """
    ShipStationConfig
    """ # noqa: E501
    config_v: Optional[StrictInt] = Field(default=None, alias="ConfigV")
    config_id: Optional[StrictStr] = Field(default=None, alias="ConfigId")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    enabled: Optional[StrictBool] = Field(default=None, alias="Enabled")
    export_locations: Optional[List[StrictStr]] = Field(default=None, alias="ExportLocations")
    export_folder: Optional[StrictStr] = Field(default=None, alias="ExportFolder")
    last_sync: Optional[datetime] = Field(default=None, alias="LastSync")
    auto_process_orders_location: Optional[StrictStr] = Field(default=None, alias="AutoProcessOrdersLocation")
    export_child_items: Optional[StrictBool] = Field(default=None, alias="ExportChildItems")
    imported_order_tag: Optional[StrictInt] = Field(default=None, alias="ImportedOrderTag")
    default_ship_service_ship_station: Optional[StrictStr] = Field(default=None, alias="DefaultShipServiceShipStation")
    default_ship_service_linnworks: Optional[StrictStr] = Field(default=None, alias="DefaultShipServiceLinnworks")
    use_channel_data: Optional[StrictBool] = Field(default=None, alias="UseChannelData")
    ship_services: Optional[List[ShipService]] = Field(default=None, alias="ShipServices")
    weight_unit: Optional[StrictStr] = Field(default=None, alias="WeightUnit")
    custom_order_field1: Optional[StrictStr] = Field(default=None, alias="CustomOrderField1")
    custom_order_field2: Optional[StrictStr] = Field(default=None, alias="CustomOrderField2")
    custom_order_field3: Optional[StrictStr] = Field(default=None, alias="CustomOrderField3")
    __properties: ClassVar[List[str]] = ["ConfigV", "ConfigId", "Name", "Enabled", "ExportLocations", "ExportFolder", "LastSync", "AutoProcessOrdersLocation", "ExportChildItems", "ImportedOrderTag", "DefaultShipServiceShipStation", "DefaultShipServiceLinnworks", "UseChannelData", "ShipServices", "WeightUnit", "CustomOrderField1", "CustomOrderField2", "CustomOrderField3"]

    @field_validator('weight_unit')
    def weight_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'oz', 'lb', 'gm', 'kg']):
            raise ValueError("must be one of enum values ('none', 'oz', 'lb', 'gm', 'kg')")
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
        """Create an instance of ShipStationConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ship_services (list)
        _items = []
        if self.ship_services:
            for _item_ship_services in self.ship_services:
                if _item_ship_services:
                    _items.append(_item_ship_services.to_dict())
            _dict['ShipServices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipStationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ConfigV": obj.get("ConfigV"),
            "ConfigId": obj.get("ConfigId"),
            "Name": obj.get("Name"),
            "Enabled": obj.get("Enabled"),
            "ExportLocations": obj.get("ExportLocations"),
            "ExportFolder": obj.get("ExportFolder"),
            "LastSync": obj.get("LastSync"),
            "AutoProcessOrdersLocation": obj.get("AutoProcessOrdersLocation"),
            "ExportChildItems": obj.get("ExportChildItems"),
            "ImportedOrderTag": obj.get("ImportedOrderTag"),
            "DefaultShipServiceShipStation": obj.get("DefaultShipServiceShipStation"),
            "DefaultShipServiceLinnworks": obj.get("DefaultShipServiceLinnworks"),
            "UseChannelData": obj.get("UseChannelData"),
            "ShipServices": [ShipService.from_dict(_item) for _item in obj["ShipServices"]] if obj.get("ShipServices") is not None else None,
            "WeightUnit": obj.get("WeightUnit"),
            "CustomOrderField1": obj.get("CustomOrderField1"),
            "CustomOrderField2": obj.get("CustomOrderField2"),
            "CustomOrderField3": obj.get("CustomOrderField3")
        })
        return _obj


