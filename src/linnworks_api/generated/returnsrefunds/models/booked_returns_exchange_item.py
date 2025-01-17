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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.returnsrefunds.models.stock_item_batch_inventory import StockItemBatchInventory
from typing import Optional, Set
from typing_extensions import Self

class BookedReturnsExchangeItem(BaseModel):
    """
    BookedReturnsExchangeItem
    """ # noqa: E501
    fk_order_item_row_id: Optional[StrictStr] = Field(default=None, alias="fkOrderItemRowId")
    order_item_batch_id: Optional[StrictInt] = Field(default=None, alias="OrderItemBatchId")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="BatchInventoryId")
    batch_number: Optional[StrictStr] = Field(default=None, alias="BatchNumber")
    row_type: Optional[StrictStr] = Field(default=None, alias="RowType")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    item_title: Optional[StrictStr] = Field(default=None, alias="ItemTitle")
    return_qty: Optional[StrictInt] = Field(default=None, alias="ReturnQty")
    max_return_qty: Optional[StrictInt] = Field(default=None, alias="MaxReturnQty")
    new_qty: Optional[StrictInt] = Field(default=None, alias="NewQty")
    new_sku: Optional[StrictStr] = Field(default=None, alias="NewSKU")
    new_title: Optional[StrictStr] = Field(default=None, alias="NewTitle")
    fk_new_stock_item_id: Optional[StrictStr] = Field(default=None, alias="fkNewStockItemId")
    category: Optional[StrictStr] = Field(default=None, alias="Category")
    reason: Optional[StrictStr] = Field(default=None, alias="Reason")
    fk_return_location_id: Optional[StrictStr] = Field(default=None, alias="fkReturnLocationId")
    return_location: Optional[StrictStr] = Field(default=None, alias="ReturnLocation")
    pending_refund_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PendingRefundAmount")
    scrapped: Optional[StrictBool] = Field(default=None, alias="Scrapped")
    scrap_qty: Optional[StrictInt] = Field(default=None, alias="ScrapQty")
    parent_order_item_row_id: Optional[StrictStr] = Field(default=None, alias="ParentOrderItemRowId")
    additional_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AdditionalCost")
    c_currency: Optional[StrictStr] = Field(default=None, alias="cCurrency")
    pk_return_id: Optional[StrictInt] = Field(default=None, alias="pkReturnId")
    channel_reason: Optional[StrictStr] = Field(default=None, alias="ChannelReason")
    channel_reason_sec: Optional[StrictStr] = Field(default=None, alias="ChannelReasonSec")
    return_date: Optional[datetime] = Field(default=None, alias="ReturnDate")
    despatch_unit_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="DespatchUnitValue")
    batch_inventory: Optional[StockItemBatchInventory] = Field(default=None, alias="BatchInventory")
    __properties: ClassVar[List[str]] = ["fkOrderItemRowId", "OrderItemBatchId", "StockItemId", "BatchInventoryId", "BatchNumber", "RowType", "SKU", "ItemTitle", "ReturnQty", "MaxReturnQty", "NewQty", "NewSKU", "NewTitle", "fkNewStockItemId", "Category", "Reason", "fkReturnLocationId", "ReturnLocation", "PendingRefundAmount", "Scrapped", "ScrapQty", "ParentOrderItemRowId", "AdditionalCost", "cCurrency", "pkReturnId", "ChannelReason", "ChannelReasonSec", "ReturnDate", "DespatchUnitValue", "BatchInventory"]

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
        """Create an instance of BookedReturnsExchangeItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of batch_inventory
        if self.batch_inventory:
            _dict['BatchInventory'] = self.batch_inventory.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BookedReturnsExchangeItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkOrderItemRowId": obj.get("fkOrderItemRowId"),
            "OrderItemBatchId": obj.get("OrderItemBatchId"),
            "StockItemId": obj.get("StockItemId"),
            "BatchInventoryId": obj.get("BatchInventoryId"),
            "BatchNumber": obj.get("BatchNumber"),
            "RowType": obj.get("RowType"),
            "SKU": obj.get("SKU"),
            "ItemTitle": obj.get("ItemTitle"),
            "ReturnQty": obj.get("ReturnQty"),
            "MaxReturnQty": obj.get("MaxReturnQty"),
            "NewQty": obj.get("NewQty"),
            "NewSKU": obj.get("NewSKU"),
            "NewTitle": obj.get("NewTitle"),
            "fkNewStockItemId": obj.get("fkNewStockItemId"),
            "Category": obj.get("Category"),
            "Reason": obj.get("Reason"),
            "fkReturnLocationId": obj.get("fkReturnLocationId"),
            "ReturnLocation": obj.get("ReturnLocation"),
            "PendingRefundAmount": obj.get("PendingRefundAmount"),
            "Scrapped": obj.get("Scrapped"),
            "ScrapQty": obj.get("ScrapQty"),
            "ParentOrderItemRowId": obj.get("ParentOrderItemRowId"),
            "AdditionalCost": obj.get("AdditionalCost"),
            "cCurrency": obj.get("cCurrency"),
            "pkReturnId": obj.get("pkReturnId"),
            "ChannelReason": obj.get("ChannelReason"),
            "ChannelReasonSec": obj.get("ChannelReasonSec"),
            "ReturnDate": obj.get("ReturnDate"),
            "DespatchUnitValue": obj.get("DespatchUnitValue"),
            "BatchInventory": StockItemBatchInventory.from_dict(obj["BatchInventory"]) if obj.get("BatchInventory") is not None else None
        })
        return _obj


