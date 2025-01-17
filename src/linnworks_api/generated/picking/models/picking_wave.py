# coding: utf-8

"""
    Picking API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: picking
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.picking.models.picking_wave_options import PickingWaveOptions
from linnworks_api.generated.picking.models.picking_wave_order import PickingWaveOrder
from typing import Optional, Set
from typing_extensions import Self

class PickingWave(BaseModel):
    """
    PickingWave
    """ # noqa: E501
    location_id: Optional[StrictStr] = Field(default=None, alias="LocationId")
    user_id: Optional[StrictInt] = Field(default=None, alias="UserId")
    email_address: Optional[StrictStr] = Field(default=None, alias="EmailAddress")
    created_date: Optional[datetime] = Field(default=None, alias="CreatedDate")
    order_count: Optional[StrictInt] = Field(default=None, alias="OrderCount")
    item_count: Optional[StrictInt] = Field(default=None, alias="ItemCount")
    items_picked: Optional[StrictInt] = Field(default=None, alias="ItemsPicked")
    orders_picked: Optional[StrictInt] = Field(default=None, alias="OrdersPicked")
    accumulated_in_progress_seconds: Optional[StrictInt] = Field(default=None, alias="AccumulatedInProgressSeconds")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    end_time: Optional[datetime] = Field(default=None, alias="EndTime")
    group_type: Optional[StrictStr] = Field(default=None, alias="GroupType")
    sort_type: Optional[StrictStr] = Field(default=None, alias="SortType")
    orders: Optional[List[PickingWaveOrder]] = Field(default=None, alias="Orders")
    options: Optional[PickingWaveOptions] = Field(default=None, alias="Options")
    picking_wave_id: Optional[StrictInt] = Field(default=None, alias="PickingWaveId")
    state: Optional[StrictStr] = Field(default=None, alias="State")
    __properties: ClassVar[List[str]] = ["LocationId", "UserId", "EmailAddress", "CreatedDate", "OrderCount", "ItemCount", "ItemsPicked", "OrdersPicked", "AccumulatedInProgressSeconds", "StartTime", "EndTime", "GroupType", "SortType", "Orders", "Options", "PickingWaveId", "State"]

    @field_validator('group_type')
    def group_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Items', 'Orders']):
            raise ValueError("must be one of enum values ('Items', 'Orders')")
        return value

    @field_validator('sort_type')
    def sort_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BinPriority', 'OrderView']):
            raise ValueError("must be one of enum values ('BinPriority', 'OrderView')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Unallocated', 'Allocated', 'InProgress', 'Paused', 'Complete', 'Abandoned', 'Packing', 'Shipped']):
            raise ValueError("must be one of enum values ('Unallocated', 'Allocated', 'InProgress', 'Paused', 'Complete', 'Abandoned', 'Packing', 'Shipped')")
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
        """Create an instance of PickingWave from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item_orders in self.orders:
                if _item_orders:
                    _items.append(_item_orders.to_dict())
            _dict['Orders'] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['Options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickingWave from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LocationId": obj.get("LocationId"),
            "UserId": obj.get("UserId"),
            "EmailAddress": obj.get("EmailAddress"),
            "CreatedDate": obj.get("CreatedDate"),
            "OrderCount": obj.get("OrderCount"),
            "ItemCount": obj.get("ItemCount"),
            "ItemsPicked": obj.get("ItemsPicked"),
            "OrdersPicked": obj.get("OrdersPicked"),
            "AccumulatedInProgressSeconds": obj.get("AccumulatedInProgressSeconds"),
            "StartTime": obj.get("StartTime"),
            "EndTime": obj.get("EndTime"),
            "GroupType": obj.get("GroupType"),
            "SortType": obj.get("SortType"),
            "Orders": [PickingWaveOrder.from_dict(_item) for _item in obj["Orders"]] if obj.get("Orders") is not None else None,
            "Options": PickingWaveOptions.from_dict(obj["Options"]) if obj.get("Options") is not None else None,
            "PickingWaveId": obj.get("PickingWaveId"),
            "State": obj.get("State")
        })
        return _obj


