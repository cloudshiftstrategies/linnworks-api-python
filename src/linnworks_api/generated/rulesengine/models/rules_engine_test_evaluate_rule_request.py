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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.rulesengine.models.testpad_value import TestpadValue
from typing import Optional, Set
from typing_extensions import Self

class RulesEngineTestEvaluateRuleRequest(BaseModel):
    """
    RulesEngineTestEvaluateRuleRequest
    """ # noqa: E501
    test_values: Optional[List[TestpadValue]] = Field(default=None, description="Test values", alias="testValues")
    pk_rule_id: Optional[StrictInt] = Field(default=None, description="The rule to test against", alias="pkRuleId")
    __properties: ClassVar[List[str]] = ["testValues", "pkRuleId"]

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
        """Create an instance of RulesEngineTestEvaluateRuleRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in test_values (list)
        _items = []
        if self.test_values:
            for _item_test_values in self.test_values:
                if _item_test_values:
                    _items.append(_item_test_values.to_dict())
            _dict['testValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RulesEngineTestEvaluateRuleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "testValues": [TestpadValue.from_dict(_item) for _item in obj["testValues"]] if obj.get("testValues") is not None else None,
            "pkRuleId": obj.get("pkRuleId")
        })
        return _obj


