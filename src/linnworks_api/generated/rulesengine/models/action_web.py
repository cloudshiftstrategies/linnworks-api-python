# coding: utf-8

"""
    Rules Engine API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: rulesengine
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.rulesengine.models.action_web_property import ActionWebProperty
from typing import Optional, Set
from typing_extensions import Self

class ActionWeb(BaseModel):
    """
    ActionWeb
    """ # noqa: E501
    pk_action_id: Optional[StrictInt] = Field(default=None, alias="pkActionId")
    fk_condition_id: Optional[StrictInt] = Field(default=None, alias="fkConditionId")
    action_name: Optional[StrictStr] = Field(default=None, alias="ActionName")
    action_type: Optional[StrictStr] = Field(default=None, alias="ActionType")
    properties: Optional[List[ActionWebProperty]] = Field(default=None, alias="Properties")
    __properties: ClassVar[List[str]] = ["pkActionId", "fkConditionId", "ActionName", "ActionType", "Properties"]

    @field_validator('action_type')
    def action_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AssignShippingService', 'AssignToFolder', 'AssignToLocation', 'SplitOrderByWeight', 'SplitOrderByValue', 'SplitOrderSingle', 'AssignOrderExtendedProperty', 'ChangeOrderLockStatus', 'ChangeOrderParkStatus', 'AssignTagToOrder', 'ExecuteMacro', 'AssignIdentifierToOrder', 'BlockOrderFromMerging', 'SendToFulfillmentNetwork']):
            raise ValueError("must be one of enum values ('AssignShippingService', 'AssignToFolder', 'AssignToLocation', 'SplitOrderByWeight', 'SplitOrderByValue', 'SplitOrderSingle', 'AssignOrderExtendedProperty', 'ChangeOrderLockStatus', 'ChangeOrderParkStatus', 'AssignTagToOrder', 'ExecuteMacro', 'AssignIdentifierToOrder', 'BlockOrderFromMerging', 'SendToFulfillmentNetwork')")
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
        """Create an instance of ActionWeb from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in properties (list)
        _items = []
        if self.properties:
            for _item_properties in self.properties:
                if _item_properties:
                    _items.append(_item_properties.to_dict())
            _dict['Properties'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActionWeb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkActionId": obj.get("pkActionId"),
            "fkConditionId": obj.get("fkConditionId"),
            "ActionName": obj.get("ActionName"),
            "ActionType": obj.get("ActionType"),
            "Properties": [ActionWebProperty.from_dict(_item) for _item in obj["Properties"]] if obj.get("Properties") is not None else None
        })
        return _obj


