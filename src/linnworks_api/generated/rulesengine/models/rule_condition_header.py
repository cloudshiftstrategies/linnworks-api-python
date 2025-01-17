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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.rulesengine.models.rule_action import RuleAction
from typing import Optional, Set
from typing_extensions import Self

class RuleConditionHeader(BaseModel):
    """
    RuleConditionHeader
    """ # noqa: E501
    pk_condition_id: Optional[StrictInt] = Field(default=None, alias="pkConditionId")
    fk_rule_id: Optional[StrictInt] = Field(default=None, alias="fkRuleId")
    run_order: Optional[StrictInt] = Field(default=None, alias="RunOrder")
    enabled: Optional[StrictBool] = Field(default=None, alias="Enabled")
    condition_name: Optional[StrictStr] = Field(default=None, alias="ConditionName")
    fk_parent_condition_id: Optional[StrictInt] = Field(default=None, alias="fkParentConditionId")
    conditions: Optional[List[Dict[str, Any]]] = Field(default=None, alias="Conditions")
    action: Optional[RuleAction] = Field(default=None, alias="Action")
    subrules: Optional[List[RuleConditionHeader]] = Field(default=None, alias="Subrules")
    __properties: ClassVar[List[str]] = ["pkConditionId", "fkRuleId", "RunOrder", "Enabled", "ConditionName", "fkParentConditionId", "Conditions", "Action", "Subrules"]

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
        """Create an instance of RuleConditionHeader from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['Action'] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subrules (list)
        _items = []
        if self.subrules:
            for _item_subrules in self.subrules:
                if _item_subrules:
                    _items.append(_item_subrules.to_dict())
            _dict['Subrules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleConditionHeader from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkConditionId": obj.get("pkConditionId"),
            "fkRuleId": obj.get("fkRuleId"),
            "RunOrder": obj.get("RunOrder"),
            "Enabled": obj.get("Enabled"),
            "ConditionName": obj.get("ConditionName"),
            "fkParentConditionId": obj.get("fkParentConditionId"),
            "Conditions": obj.get("Conditions"),
            "Action": RuleAction.from_dict(obj["Action"]) if obj.get("Action") is not None else None,
            "Subrules": [RuleConditionHeader.from_dict(_item) for _item in obj["Subrules"]] if obj.get("Subrules") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
RuleConditionHeader.model_rebuild(raise_errors=False)

