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
from linnworks_api.generated.purchaseorder.models.change_purchase_order_status_parameter import ChangePurchaseOrderStatusParameter
from typing import Optional, Set
from typing_extensions import Self

class PurchaseOrderChangePurchaseOrderStatusRequest(BaseModel):
    """
    PurchaseOrderChangePurchaseOrderStatusRequest
    """ # noqa: E501
    change_status_parameter: Optional[ChangePurchaseOrderStatusParameter] = Field(default=None, alias="changeStatusParameter")
    __properties: ClassVar[List[str]] = ["changeStatusParameter"]

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
        """Create an instance of PurchaseOrderChangePurchaseOrderStatusRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of change_status_parameter
        if self.change_status_parameter:
            _dict['changeStatusParameter'] = self.change_status_parameter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseOrderChangePurchaseOrderStatusRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changeStatusParameter": ChangePurchaseOrderStatusParameter.from_dict(obj["changeStatusParameter"]) if obj.get("changeStatusParameter") is not None else None
        })
        return _obj


