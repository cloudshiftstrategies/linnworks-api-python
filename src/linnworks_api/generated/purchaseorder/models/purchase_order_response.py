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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.purchaseorder.models.purchase_order_additional_cost import PurchaseOrderAdditionalCost
from linnworks_api.generated.purchaseorder.models.purchase_order_delivered_record import PurchaseOrderDeliveredRecord
from linnworks_api.generated.purchaseorder.models.purchase_order_header import PurchaseOrderHeader
from linnworks_api.generated.purchaseorder.models.purchase_order_item import PurchaseOrderItem
from linnworks_api.generated.purchaseorder.models.purchase_order_payment_statement import PurchaseOrderPaymentStatement
from typing import Optional, Set
from typing_extensions import Self

class PurchaseOrderResponse(BaseModel):
    """
    PurchaseOrderResponse
    """ # noqa: E501
    note_count: Optional[StrictInt] = Field(default=None, alias="NoteCount")
    purchase_order_header: Optional[PurchaseOrderHeader] = Field(default=None, alias="PurchaseOrderHeader")
    purchase_order_item: Optional[List[PurchaseOrderItem]] = Field(default=None, alias="PurchaseOrderItem")
    additional_costs: Optional[List[PurchaseOrderAdditionalCost]] = Field(default=None, alias="AdditionalCosts")
    payment_statements: Optional[List[PurchaseOrderPaymentStatement]] = Field(default=None, alias="PaymentStatements")
    delivered_records: Optional[List[PurchaseOrderDeliveredRecord]] = Field(default=None, alias="DeliveredRecords")
    __properties: ClassVar[List[str]] = ["NoteCount", "PurchaseOrderHeader", "PurchaseOrderItem", "AdditionalCosts", "PaymentStatements", "DeliveredRecords"]

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
        """Create an instance of PurchaseOrderResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of purchase_order_header
        if self.purchase_order_header:
            _dict['PurchaseOrderHeader'] = self.purchase_order_header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in purchase_order_item (list)
        _items = []
        if self.purchase_order_item:
            for _item_purchase_order_item in self.purchase_order_item:
                if _item_purchase_order_item:
                    _items.append(_item_purchase_order_item.to_dict())
            _dict['PurchaseOrderItem'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_costs (list)
        _items = []
        if self.additional_costs:
            for _item_additional_costs in self.additional_costs:
                if _item_additional_costs:
                    _items.append(_item_additional_costs.to_dict())
            _dict['AdditionalCosts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payment_statements (list)
        _items = []
        if self.payment_statements:
            for _item_payment_statements in self.payment_statements:
                if _item_payment_statements:
                    _items.append(_item_payment_statements.to_dict())
            _dict['PaymentStatements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in delivered_records (list)
        _items = []
        if self.delivered_records:
            for _item_delivered_records in self.delivered_records:
                if _item_delivered_records:
                    _items.append(_item_delivered_records.to_dict())
            _dict['DeliveredRecords'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseOrderResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "NoteCount": obj.get("NoteCount"),
            "PurchaseOrderHeader": PurchaseOrderHeader.from_dict(obj["PurchaseOrderHeader"]) if obj.get("PurchaseOrderHeader") is not None else None,
            "PurchaseOrderItem": [PurchaseOrderItem.from_dict(_item) for _item in obj["PurchaseOrderItem"]] if obj.get("PurchaseOrderItem") is not None else None,
            "AdditionalCosts": [PurchaseOrderAdditionalCost.from_dict(_item) for _item in obj["AdditionalCosts"]] if obj.get("AdditionalCosts") is not None else None,
            "PaymentStatements": [PurchaseOrderPaymentStatement.from_dict(_item) for _item in obj["PaymentStatements"]] if obj.get("PaymentStatements") is not None else None,
            "DeliveredRecords": [PurchaseOrderDeliveredRecord.from_dict(_item) for _item in obj["DeliveredRecords"]] if obj.get("DeliveredRecords") is not None else None
        })
        return _obj


