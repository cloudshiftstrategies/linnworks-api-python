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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.orders.models.order_item import OrderItem
from linnworks_api.generated.orders.models.order_summary import OrderSummary
from linnworks_api.generated.orders.models.stock_item_batch import StockItemBatch
from typing import Optional, Set
from typing_extensions import Self

class ProcessOrderByOrderIdOrReferenceResponse(BaseModel):
    """
    A response class used when processing an order by order id or reference
    """ # noqa: E501
    processed_state: Optional[StrictStr] = Field(default=None, description="The processed state", alias="ProcessedState")
    message: Optional[StrictStr] = Field(default=None, description="A message - Provided if there have been errors", alias="Message")
    response: Optional[Dict[str, Any]] = Field(default=None, description="A response object used if further action is required", alias="Response")
    order_id: Optional[StrictStr] = Field(default=None, description="The ID of the order - Guid empty if not found", alias="OrderId")
    order_summary: Optional[OrderSummary] = Field(default=None, alias="OrderSummary")
    items: Optional[List[OrderItem]] = Field(default=None, description="The items that need to be scanned - If any", alias="Items")
    batch_information: Optional[List[StockItemBatch]] = Field(default=None, description="The batched items", alias="BatchInformation")
    __properties: ClassVar[List[str]] = ["ProcessedState", "Message", "Response", "OrderId", "OrderSummary", "Items", "BatchInformation"]

    @field_validator('processed_state')
    def processed_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PROCESSED', 'NOT_FOUND', 'SCAN_REQUIRED', 'NOT_PROCESSED', 'NOTE_ACKNOWLEDGEMENT_REQUIRED', 'NOT_IN_WORKFLOW']):
            raise ValueError("must be one of enum values ('PROCESSED', 'NOT_FOUND', 'SCAN_REQUIRED', 'NOT_PROCESSED', 'NOTE_ACKNOWLEDGEMENT_REQUIRED', 'NOT_IN_WORKFLOW')")
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
        """Create an instance of ProcessOrderByOrderIdOrReferenceResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order_summary
        if self.order_summary:
            _dict['OrderSummary'] = self.order_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['Items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in batch_information (list)
        _items = []
        if self.batch_information:
            for _item_batch_information in self.batch_information:
                if _item_batch_information:
                    _items.append(_item_batch_information.to_dict())
            _dict['BatchInformation'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProcessOrderByOrderIdOrReferenceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ProcessedState": obj.get("ProcessedState"),
            "Message": obj.get("Message"),
            "Response": obj.get("Response"),
            "OrderId": obj.get("OrderId"),
            "OrderSummary": OrderSummary.from_dict(obj["OrderSummary"]) if obj.get("OrderSummary") is not None else None,
            "Items": [OrderItem.from_dict(_item) for _item in obj["Items"]] if obj.get("Items") is not None else None,
            "BatchInformation": [StockItemBatch.from_dict(_item) for _item in obj["BatchInformation"]] if obj.get("BatchInformation") is not None else None
        })
        return _obj


