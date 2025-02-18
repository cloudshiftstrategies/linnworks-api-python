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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.returnsrefunds.models.new_refund_line import NewRefundLine
from typing import Optional, Set
from typing_extensions import Self

class CreateRefundRequest(BaseModel):
    """
    CreateRefundRequest
    """ # noqa: E501
    channel_initiated: Optional[StrictBool] = Field(default=None, description="Determines whether the refund was initiated on the channel, or within Linnworks", alias="ChannelInitiated")
    order_id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the order this refund is associated with", alias="OrderId")
    refund_lines: Optional[List[NewRefundLine]] = Field(default=None, description="A collection of line-level refunds detailing the refund as a whole", alias="RefundLines")
    __properties: ClassVar[List[str]] = ["ChannelInitiated", "OrderId", "RefundLines"]

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
        """Create an instance of CreateRefundRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in refund_lines (list)
        _items = []
        if self.refund_lines:
            for _item_refund_lines in self.refund_lines:
                if _item_refund_lines:
                    _items.append(_item_refund_lines.to_dict())
            _dict['RefundLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRefundRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChannelInitiated": obj.get("ChannelInitiated"),
            "OrderId": obj.get("OrderId"),
            "RefundLines": [NewRefundLine.from_dict(_item) for _item in obj["RefundLines"]] if obj.get("RefundLines") is not None else None
        })
        return _obj


