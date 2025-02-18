# coding: utf-8

"""
    Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: orders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class SetOrderPackagingRequest(BaseModel):
    """
    Request class for SetOrderPackaging method in Orders controller
    """ # noqa: E501
    fk_packaging_group_id: Optional[StrictStr] = Field(default=None, description="Packaging group Id", alias="fkPackagingGroupId")
    fk_packaging_type_id: Optional[StrictStr] = Field(default=None, description="Packaging Type Id. It has to be one of types available for selected Group Id", alias="fkPackagingTypeId")
    pk_order_id: Optional[StrictStr] = Field(default=None, description="Order Id to set the order packaging data", alias="pkOrderId")
    total_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total weight of order packaging", alias="TotalWeight")
    manual_adjust: Optional[StrictBool] = Field(default=None, description="Indicate if this data is manually adjusted with the rest of fields or is auto calculated", alias="ManualAdjust")
    is_auto_split: Optional[StrictBool] = Field(default=None, description="Indicates whether the order should be auto split. Usually via the 3D packaging methods.", alias="IsAutoSplit")
    total_depth: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total packaging depth", alias="TotalDepth")
    total_height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total Height", alias="TotalHeight")
    total_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total Width", alias="TotalWidth")
    __properties: ClassVar[List[str]] = ["fkPackagingGroupId", "fkPackagingTypeId", "pkOrderId", "TotalWeight", "ManualAdjust", "IsAutoSplit", "TotalDepth", "TotalHeight", "TotalWidth"]

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
        """Create an instance of SetOrderPackagingRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SetOrderPackagingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkPackagingGroupId": obj.get("fkPackagingGroupId"),
            "fkPackagingTypeId": obj.get("fkPackagingTypeId"),
            "pkOrderId": obj.get("pkOrderId"),
            "TotalWeight": obj.get("TotalWeight"),
            "ManualAdjust": obj.get("ManualAdjust"),
            "IsAutoSplit": obj.get("IsAutoSplit"),
            "TotalDepth": obj.get("TotalDepth"),
            "TotalHeight": obj.get("TotalHeight"),
            "TotalWidth": obj.get("TotalWidth")
        })
        return _obj


