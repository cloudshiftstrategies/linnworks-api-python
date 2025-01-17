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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.orders.models.order_item_bin_rack import OrderItemBinRack
from linnworks_api.generated.orders.models.order_item_on_order import OrderItemOnOrder
from linnworks_api.generated.orders.models.order_item_option import OrderItemOption
from linnworks_api.generated.orders.models.stock_item_box_configuration import StockItemBoxConfiguration
from typing import Optional, Set
from typing_extensions import Self

class OrderItem(BaseModel):
    """
    OrderItem
    """ # noqa: E501
    item_id: Optional[StrictStr] = Field(default=None, alias="ItemId")
    item_number: Optional[StrictStr] = Field(default=None, alias="ItemNumber")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    item_source: Optional[StrictStr] = Field(default=None, alias="ItemSource")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    quantity: Optional[StrictInt] = Field(default=None, alias="Quantity")
    category_name: Optional[StrictStr] = Field(default=None, alias="CategoryName")
    composite_availablity: Optional[StrictInt] = Field(default=None, alias="CompositeAvailablity")
    stock_levels_specified: Optional[StrictBool] = Field(default=None, alias="StockLevelsSpecified")
    on_order: Optional[StrictInt] = Field(default=None, alias="OnOrder")
    on_purchase_order: Optional[OrderItemOnOrder] = Field(default=None, alias="OnPurchaseOrder")
    in_order_book: Optional[StrictInt] = Field(default=None, alias="InOrderBook")
    level: Optional[StrictInt] = Field(default=None, alias="Level")
    minimum_level: Optional[StrictInt] = Field(default=None, alias="MinimumLevel")
    available_stock: Optional[StrictInt] = Field(default=None, alias="AvailableStock")
    price_per_unit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PricePerUnit")
    unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnitCost")
    despatch_stock_unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="DespatchStockUnitCost")
    discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Discount")
    tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Tax")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="TaxRate")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Cost")
    cost_inc_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="CostIncTax")
    composite_sub_items: Optional[List[OrderItem]] = Field(default=None, alias="CompositeSubItems")
    is_service: Optional[StrictBool] = Field(default=None, alias="IsService")
    sales_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="SalesTax")
    tax_cost_inclusive: Optional[StrictBool] = Field(default=None, alias="TaxCostInclusive")
    part_shipped: Optional[StrictBool] = Field(default=None, alias="PartShipped")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Weight")
    barcode_number: Optional[StrictStr] = Field(default=None, alias="BarcodeNumber")
    market: Optional[StrictInt] = Field(default=None, alias="Market")
    channel_sku: Optional[StrictStr] = Field(default=None, alias="ChannelSKU")
    channel_title: Optional[StrictStr] = Field(default=None, alias="ChannelTitle")
    discount_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="DiscountValue")
    has_image: Optional[StrictBool] = Field(default=None, alias="HasImage")
    image_id: Optional[StrictStr] = Field(default=None, alias="ImageId")
    additional_info: Optional[List[OrderItemOption]] = Field(default=None, alias="AdditionalInfo")
    stock_level_indicator: Optional[StrictInt] = Field(default=None, alias="StockLevelIndicator")
    shipping_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ShippingCost")
    part_shipped_qty: Optional[StrictInt] = Field(default=None, alias="PartShippedQty")
    item_name: Optional[StrictStr] = Field(default=None, alias="ItemName")
    batch_number_scan_required: Optional[StrictBool] = Field(default=None, alias="BatchNumberScanRequired")
    serial_number_scan_required: Optional[StrictBool] = Field(default=None, alias="SerialNumberScanRequired")
    bin_rack: Optional[StrictStr] = Field(default=None, alias="BinRack")
    bin_racks: Optional[List[OrderItemBinRack]] = Field(default=None, alias="BinRacks")
    inventory_tracking_type: Optional[StrictInt] = Field(default=None, alias="InventoryTrackingType")
    is_batched_stock_item: Optional[StrictBool] = Field(default=None, alias="isBatchedStockItem")
    is_warehouse_managed: Optional[StrictBool] = Field(default=None, alias="IsWarehouseManaged")
    is_unlinked: Optional[StrictBool] = Field(default=None, alias="IsUnlinked")
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="StockItemIntId")
    boxes: Optional[List[StockItemBoxConfiguration]] = Field(default=None, alias="Boxes")
    added_date: Optional[datetime] = Field(default=None, alias="AddedDate")
    row_id: Optional[StrictStr] = Field(default=None, alias="RowId")
    order_id: Optional[StrictStr] = Field(default=None, alias="OrderId")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    __properties: ClassVar[List[str]] = ["ItemId", "ItemNumber", "SKU", "ItemSource", "Title", "Quantity", "CategoryName", "CompositeAvailablity", "StockLevelsSpecified", "OnOrder", "OnPurchaseOrder", "InOrderBook", "Level", "MinimumLevel", "AvailableStock", "PricePerUnit", "UnitCost", "DespatchStockUnitCost", "Discount", "Tax", "TaxRate", "Cost", "CostIncTax", "CompositeSubItems", "IsService", "SalesTax", "TaxCostInclusive", "PartShipped", "Weight", "BarcodeNumber", "Market", "ChannelSKU", "ChannelTitle", "DiscountValue", "HasImage", "ImageId", "AdditionalInfo", "StockLevelIndicator", "ShippingCost", "PartShippedQty", "ItemName", "BatchNumberScanRequired", "SerialNumberScanRequired", "BinRack", "BinRacks", "InventoryTrackingType", "isBatchedStockItem", "IsWarehouseManaged", "IsUnlinked", "StockItemIntId", "Boxes", "AddedDate", "RowId", "OrderId", "StockItemId"]

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
        """Create an instance of OrderItem from a JSON string"""
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
            "tax",
            "discount_value",
            "has_image",
            "is_batched_stock_item",
            "is_unlinked",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of on_purchase_order
        if self.on_purchase_order:
            _dict['OnPurchaseOrder'] = self.on_purchase_order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in composite_sub_items (list)
        _items = []
        if self.composite_sub_items:
            for _item_composite_sub_items in self.composite_sub_items:
                if _item_composite_sub_items:
                    _items.append(_item_composite_sub_items.to_dict())
            _dict['CompositeSubItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_info (list)
        _items = []
        if self.additional_info:
            for _item_additional_info in self.additional_info:
                if _item_additional_info:
                    _items.append(_item_additional_info.to_dict())
            _dict['AdditionalInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bin_racks (list)
        _items = []
        if self.bin_racks:
            for _item_bin_racks in self.bin_racks:
                if _item_bin_racks:
                    _items.append(_item_bin_racks.to_dict())
            _dict['BinRacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in boxes (list)
        _items = []
        if self.boxes:
            for _item_boxes in self.boxes:
                if _item_boxes:
                    _items.append(_item_boxes.to_dict())
            _dict['Boxes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ItemId": obj.get("ItemId"),
            "ItemNumber": obj.get("ItemNumber"),
            "SKU": obj.get("SKU"),
            "ItemSource": obj.get("ItemSource"),
            "Title": obj.get("Title"),
            "Quantity": obj.get("Quantity"),
            "CategoryName": obj.get("CategoryName"),
            "CompositeAvailablity": obj.get("CompositeAvailablity"),
            "StockLevelsSpecified": obj.get("StockLevelsSpecified"),
            "OnOrder": obj.get("OnOrder"),
            "OnPurchaseOrder": OrderItemOnOrder.from_dict(obj["OnPurchaseOrder"]) if obj.get("OnPurchaseOrder") is not None else None,
            "InOrderBook": obj.get("InOrderBook"),
            "Level": obj.get("Level"),
            "MinimumLevel": obj.get("MinimumLevel"),
            "AvailableStock": obj.get("AvailableStock"),
            "PricePerUnit": obj.get("PricePerUnit"),
            "UnitCost": obj.get("UnitCost"),
            "DespatchStockUnitCost": obj.get("DespatchStockUnitCost"),
            "Discount": obj.get("Discount"),
            "Tax": obj.get("Tax"),
            "TaxRate": obj.get("TaxRate"),
            "Cost": obj.get("Cost"),
            "CostIncTax": obj.get("CostIncTax"),
            "CompositeSubItems": [OrderItem.from_dict(_item) for _item in obj["CompositeSubItems"]] if obj.get("CompositeSubItems") is not None else None,
            "IsService": obj.get("IsService"),
            "SalesTax": obj.get("SalesTax"),
            "TaxCostInclusive": obj.get("TaxCostInclusive"),
            "PartShipped": obj.get("PartShipped"),
            "Weight": obj.get("Weight"),
            "BarcodeNumber": obj.get("BarcodeNumber"),
            "Market": obj.get("Market"),
            "ChannelSKU": obj.get("ChannelSKU"),
            "ChannelTitle": obj.get("ChannelTitle"),
            "DiscountValue": obj.get("DiscountValue"),
            "HasImage": obj.get("HasImage"),
            "ImageId": obj.get("ImageId"),
            "AdditionalInfo": [OrderItemOption.from_dict(_item) for _item in obj["AdditionalInfo"]] if obj.get("AdditionalInfo") is not None else None,
            "StockLevelIndicator": obj.get("StockLevelIndicator"),
            "ShippingCost": obj.get("ShippingCost"),
            "PartShippedQty": obj.get("PartShippedQty"),
            "ItemName": obj.get("ItemName"),
            "BatchNumberScanRequired": obj.get("BatchNumberScanRequired"),
            "SerialNumberScanRequired": obj.get("SerialNumberScanRequired"),
            "BinRack": obj.get("BinRack"),
            "BinRacks": [OrderItemBinRack.from_dict(_item) for _item in obj["BinRacks"]] if obj.get("BinRacks") is not None else None,
            "InventoryTrackingType": obj.get("InventoryTrackingType"),
            "isBatchedStockItem": obj.get("isBatchedStockItem"),
            "IsWarehouseManaged": obj.get("IsWarehouseManaged"),
            "IsUnlinked": obj.get("IsUnlinked"),
            "StockItemIntId": obj.get("StockItemIntId"),
            "Boxes": [StockItemBoxConfiguration.from_dict(_item) for _item in obj["Boxes"]] if obj.get("Boxes") is not None else None,
            "AddedDate": obj.get("AddedDate"),
            "RowId": obj.get("RowId"),
            "OrderId": obj.get("OrderId"),
            "StockItemId": obj.get("StockItemId")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
OrderItem.model_rebuild(raise_errors=False)

