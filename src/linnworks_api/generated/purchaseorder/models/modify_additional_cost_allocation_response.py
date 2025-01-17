# coding: utf-8

"""
    Purchase Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: purchaseorder
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.purchaseorder.models.modified_additional_cost_allocation_item import ModifiedAdditionalCostAllocationItem
from typing import Optional, Set
from typing_extensions import Self

class ModifyAdditionalCostAllocationResponse(BaseModel):
    """
    ModifyAdditionalCostAllocationResponse
    """ # noqa: E501
    modified_items: Optional[List[ModifiedAdditionalCostAllocationItem]] = Field(default=None, description="list of modified items with Ids matched to CostAllocationId", alias="ModifiedItems")
    __properties: ClassVar[List[str]] = ["ModifiedItems"]

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
        """Create an instance of ModifyAdditionalCostAllocationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in modified_items (list)
        _items = []
        if self.modified_items:
            for _item_modified_items in self.modified_items:
                if _item_modified_items:
                    _items.append(_item_modified_items.to_dict())
            _dict['ModifiedItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModifyAdditionalCostAllocationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ModifiedItems": [ModifiedAdditionalCostAllocationItem.from_dict(_item) for _item in obj["ModifiedItems"]] if obj.get("ModifiedItems") is not None else None
        })
        return _obj


