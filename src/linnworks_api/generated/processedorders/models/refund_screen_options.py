# coding: utf-8

"""
    Processed Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: processedorders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RefundScreenOptions(BaseModel):
    """
    RefundScreenOptions
    """ # noqa: E501
    free_text_option: Optional[StrictStr] = Field(default=None, alias="FreeTextOption")
    can_refund_shipping: Optional[StrictBool] = Field(default=None, alias="CanRefundShipping")
    order_has_service_items: Optional[StrictBool] = Field(default=None, alias="OrderHasServiceItems")
    is_shipping_refund_automated: Optional[StrictBool] = Field(default=None, alias="IsShippingRefundAutomated")
    is_service_refund_automated: Optional[StrictBool] = Field(default=None, alias="IsServiceRefundAutomated")
    supports_automated_refunds: Optional[StrictBool] = Field(default=None, alias="SupportsAutomatedRefunds")
    __properties: ClassVar[List[str]] = ["FreeTextOption", "CanRefundShipping", "OrderHasServiceItems", "IsShippingRefundAutomated", "IsServiceRefundAutomated", "SupportsAutomatedRefunds"]

    @field_validator('free_text_option')
    def free_text_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OK', 'ChannelRefundFunctionalityNotImplemented', 'ChannelRefundsDisabled', 'NotAllowed']):
            raise ValueError("must be one of enum values ('OK', 'ChannelRefundFunctionalityNotImplemented', 'ChannelRefundsDisabled', 'NotAllowed')")
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
        """Create an instance of RefundScreenOptions from a JSON string"""
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
        """Create an instance of RefundScreenOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FreeTextOption": obj.get("FreeTextOption"),
            "CanRefundShipping": obj.get("CanRefundShipping"),
            "OrderHasServiceItems": obj.get("OrderHasServiceItems"),
            "IsShippingRefundAutomated": obj.get("IsShippingRefundAutomated"),
            "IsServiceRefundAutomated": obj.get("IsServiceRefundAutomated"),
            "SupportsAutomatedRefunds": obj.get("SupportsAutomatedRefunds")
        })
        return _obj


