# coding: utf-8

"""
    Open Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: openorders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.openorders.models.order_view_user_preference import OrderViewUserPreference
from linnworks_api.generated.openorders.models.view_user import ViewUser
from linnworks_api.generated.openorders.models.view_user_management import ViewUserManagement
from typing import Optional, Set
from typing_extensions import Self

class OrderViewStats(BaseModel):
    """
    OrderViewStats
    """ # noqa: E501
    view_id: Optional[StrictInt] = Field(default=None, alias="ViewId")
    view_name: Optional[StrictStr] = Field(default=None, alias="ViewName")
    is_system: Optional[StrictBool] = Field(default=None, alias="IsSystem")
    total_orders: Optional[StrictInt] = Field(default=None, alias="TotalOrders")
    location_id: Optional[StrictStr] = Field(default=None, alias="LocationId")
    expiry_date: Optional[datetime] = Field(default=None, alias="ExpiryDate")
    is_calculating: Optional[StrictBool] = Field(default=None, alias="IsCalculating")
    view_exists: Optional[StrictBool] = Field(default=None, alias="ViewExists")
    last_requested: Optional[datetime] = Field(default=None, alias="LastRequested")
    user_management: Optional[ViewUserManagement] = Field(default=None, alias="UserManagement")
    order_view_user_preference: Optional[OrderViewUserPreference] = Field(default=None, alias="OrderViewUserPreference")
    owner: Optional[ViewUser] = Field(default=None, alias="Owner")
    is_cacheable: Optional[StrictBool] = Field(default=None, alias="IsCacheable")
    __properties: ClassVar[List[str]] = ["ViewId", "ViewName", "IsSystem", "TotalOrders", "LocationId", "ExpiryDate", "IsCalculating", "ViewExists", "LastRequested", "UserManagement", "OrderViewUserPreference", "Owner", "IsCacheable"]

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
        """Create an instance of OrderViewStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "expiry_date",
            "is_calculating",
            "view_exists",
            "last_requested",
            "is_cacheable",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user_management
        if self.user_management:
            _dict['UserManagement'] = self.user_management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_view_user_preference
        if self.order_view_user_preference:
            _dict['OrderViewUserPreference'] = self.order_view_user_preference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['Owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderViewStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ViewId": obj.get("ViewId"),
            "ViewName": obj.get("ViewName"),
            "IsSystem": obj.get("IsSystem"),
            "TotalOrders": obj.get("TotalOrders"),
            "LocationId": obj.get("LocationId"),
            "ExpiryDate": obj.get("ExpiryDate"),
            "IsCalculating": obj.get("IsCalculating"),
            "ViewExists": obj.get("ViewExists"),
            "LastRequested": obj.get("LastRequested"),
            "UserManagement": ViewUserManagement.from_dict(obj["UserManagement"]) if obj.get("UserManagement") is not None else None,
            "OrderViewUserPreference": OrderViewUserPreference.from_dict(obj["OrderViewUserPreference"]) if obj.get("OrderViewUserPreference") is not None else None,
            "Owner": ViewUser.from_dict(obj["Owner"]) if obj.get("Owner") is not None else None,
            "IsCacheable": obj.get("IsCacheable")
        })
        return _obj


