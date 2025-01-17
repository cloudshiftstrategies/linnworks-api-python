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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.picking.models.picking_wave_item_update import PickingWaveItemUpdate
from typing import Optional, Set
from typing_extensions import Self

class PickingWaveItemUpdateRequest(BaseModel):
    """
    Pickwave item update request.
    """ # noqa: E501
    wave_item_updates: Optional[List[PickingWaveItemUpdate]] = Field(default=None, description="List of pickwave items to update", alias="WaveItemUpdates")
    __properties: ClassVar[List[str]] = ["WaveItemUpdates"]

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
        """Create an instance of PickingWaveItemUpdateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in wave_item_updates (list)
        _items = []
        if self.wave_item_updates:
            for _item_wave_item_updates in self.wave_item_updates:
                if _item_wave_item_updates:
                    _items.append(_item_wave_item_updates.to_dict())
            _dict['WaveItemUpdates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PickingWaveItemUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "WaveItemUpdates": [PickingWaveItemUpdate.from_dict(_item) for _item in obj["WaveItemUpdates"]] if obj.get("WaveItemUpdates") is not None else None
        })
        return _obj


