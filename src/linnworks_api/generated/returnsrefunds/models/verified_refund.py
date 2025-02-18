# coding: utf-8

"""
    Returns and Refunds API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: returnsrefunds
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.returnsrefunds.models.post_sale_status import PostSaleStatus
from linnworks_api.generated.returnsrefunds.models.refund_error import RefundError
from linnworks_api.generated.returnsrefunds.models.verified_refund_item import VerifiedRefundItem
from typing import Optional, Set
from typing_extensions import Self

class VerifiedRefund(BaseModel):
    """
    VerifiedRefund
    """ # noqa: E501
    refund_row_id: Optional[StrictStr] = Field(default=None, alias="RefundRowId")
    refund_header_id: Optional[StrictInt] = Field(default=None, alias="RefundHeaderId")
    status: Optional[PostSaleStatus] = Field(default=None, alias="Status")
    refunded_unit: Optional[StrictStr] = Field(default=None, alias="RefundedUnit")
    is_shipping_refund: Optional[StrictBool] = Field(default=None, alias="IsShippingRefund")
    is_additional_refund: Optional[StrictBool] = Field(default=None, alias="IsAdditionalRefund")
    is_cancellation: Optional[StrictBool] = Field(default=None, alias="IsCancellation")
    refunded_item: Optional[VerifiedRefundItem] = Field(default=None, alias="RefundedItem")
    validation_error: Optional[StrictStr] = Field(default=None, alias="ValidationError")
    error: Optional[StrictStr] = Field(default=None, alias="Error")
    errors: Optional[List[RefundError]] = Field(default=None, alias="Errors")
    actioned: Optional[StrictBool] = Field(default=None, alias="Actioned")
    actioned_date: Optional[datetime] = Field(default=None, alias="ActionedDate")
    channel_initiated: Optional[StrictBool] = Field(default=None, alias="ChannelInitiated")
    internal: Optional[StrictBool] = Field(default=None, alias="Internal")
    deleted: Optional[StrictBool] = Field(default=None, alias="Deleted")
    external_reference: Optional[StrictStr] = Field(default=None, alias="ExternalReference")
    is_free_text: Optional[StrictBool] = Field(default=None, alias="IsFreeText")
    free_text_or_note: Optional[StrictStr] = Field(default=None, alias="FreeTextOrNote")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Amount")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    reason_tag: Optional[StrictStr] = Field(default=None, alias="ReasonTag")
    sub_reason_tag: Optional[StrictStr] = Field(default=None, alias="SubReasonTag")
    insufficient_refund_tag: Optional[StrictStr] = Field(default=None, alias="InsufficientRefundTag")
    insufficient_refund_note: Optional[StrictStr] = Field(default=None, alias="InsufficientRefundNote")
    reason_category: Optional[StrictStr] = Field(default=None, alias="ReasonCategory")
    __properties: ClassVar[List[str]] = ["RefundRowId", "RefundHeaderId", "Status", "RefundedUnit", "IsShippingRefund", "IsAdditionalRefund", "IsCancellation", "RefundedItem", "ValidationError", "Error", "Errors", "Actioned", "ActionedDate", "ChannelInitiated", "Internal", "Deleted", "ExternalReference", "IsFreeText", "FreeTextOrNote", "Amount", "Quantity", "ReasonTag", "SubReasonTag", "InsufficientRefundTag", "InsufficientRefundNote", "ReasonCategory"]

    @field_validator('refunded_unit')
    def refunded_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Item', 'Shipping', 'Service', 'Additional']):
            raise ValueError("must be one of enum values ('Item', 'Shipping', 'Service', 'Additional')")
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
        """Create an instance of VerifiedRefund from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "is_shipping_refund",
            "is_additional_refund",
            "is_cancellation",
            "is_free_text",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['Status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refunded_item
        if self.refunded_item:
            _dict['RefundedItem'] = self.refunded_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['Errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerifiedRefund from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RefundRowId": obj.get("RefundRowId"),
            "RefundHeaderId": obj.get("RefundHeaderId"),
            "Status": PostSaleStatus.from_dict(obj["Status"]) if obj.get("Status") is not None else None,
            "RefundedUnit": obj.get("RefundedUnit"),
            "IsShippingRefund": obj.get("IsShippingRefund"),
            "IsAdditionalRefund": obj.get("IsAdditionalRefund"),
            "IsCancellation": obj.get("IsCancellation"),
            "RefundedItem": VerifiedRefundItem.from_dict(obj["RefundedItem"]) if obj.get("RefundedItem") is not None else None,
            "ValidationError": obj.get("ValidationError"),
            "Error": obj.get("Error"),
            "Errors": [RefundError.from_dict(_item) for _item in obj["Errors"]] if obj.get("Errors") is not None else None,
            "Actioned": obj.get("Actioned"),
            "ActionedDate": obj.get("ActionedDate"),
            "ChannelInitiated": obj.get("ChannelInitiated"),
            "Internal": obj.get("Internal"),
            "Deleted": obj.get("Deleted"),
            "ExternalReference": obj.get("ExternalReference"),
            "IsFreeText": obj.get("IsFreeText"),
            "FreeTextOrNote": obj.get("FreeTextOrNote"),
            "Amount": obj.get("Amount"),
            "Quantity": obj.get("Quantity"),
            "ReasonTag": obj.get("ReasonTag"),
            "SubReasonTag": obj.get("SubReasonTag"),
            "InsufficientRefundTag": obj.get("InsufficientRefundTag"),
            "InsufficientRefundNote": obj.get("InsufficientRefundNote"),
            "ReasonCategory": obj.get("ReasonCategory")
        })
        return _obj


