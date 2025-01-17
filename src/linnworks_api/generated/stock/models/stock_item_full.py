# coding: utf-8

"""
    Stock API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: stock
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
from linnworks_api.generated.stock.models.stock_item_description import StockItemDescription
from linnworks_api.generated.stock.models.stock_item_extended_property import StockItemExtendedProperty
from linnworks_api.generated.stock.models.stock_item_image import StockItemImage
from linnworks_api.generated.stock.models.stock_item_level import StockItemLevel
from linnworks_api.generated.stock.models.stock_item_price import StockItemPrice
from linnworks_api.generated.stock.models.stock_item_supplier_stat import StockItemSupplierStat
from linnworks_api.generated.stock.models.stock_item_title import StockItemTitle
from typing import Optional, Set
from typing_extensions import Self

class StockItemFull(BaseModel):
    """
    StockItemFull
    """ # noqa: E501
    suppliers: Optional[List[StockItemSupplierStat]] = Field(default=None, alias="Suppliers")
    stock_levels: Optional[List[StockItemLevel]] = Field(default=None, alias="StockLevels")
    item_channel_descriptions: Optional[List[StockItemDescription]] = Field(default=None, alias="ItemChannelDescriptions")
    item_extended_properties: Optional[List[StockItemExtendedProperty]] = Field(default=None, alias="ItemExtendedProperties")
    item_channel_titles: Optional[List[StockItemTitle]] = Field(default=None, alias="ItemChannelTitles")
    item_channel_prices: Optional[List[StockItemPrice]] = Field(default=None, alias="ItemChannelPrices")
    images: Optional[List[StockItemImage]] = Field(default=None, alias="Images")
    item_number: Optional[StrictStr] = Field(default=None, alias="ItemNumber")
    item_title: Optional[StrictStr] = Field(default=None, alias="ItemTitle")
    barcode_number: Optional[StrictStr] = Field(default=None, alias="BarcodeNumber")
    meta_data: Optional[StrictStr] = Field(default=None, alias="MetaData")
    is_variation_parent: Optional[StrictBool] = Field(default=None, alias="IsVariationParent")
    is_batched_stock_type: Optional[StrictBool] = Field(default=None, alias="isBatchedStockType")
    purchase_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PurchasePrice")
    retail_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="RetailPrice")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="TaxRate")
    postal_service_id: Optional[StrictStr] = Field(default=None, alias="PostalServiceId")
    postal_service_name: Optional[StrictStr] = Field(default=None, alias="PostalServiceName")
    category_id: Optional[StrictStr] = Field(default=None, alias="CategoryId")
    category_name: Optional[StrictStr] = Field(default=None, alias="CategoryName")
    package_group_id: Optional[StrictStr] = Field(default=None, alias="PackageGroupId")
    package_group_name: Optional[StrictStr] = Field(default=None, alias="PackageGroupName")
    height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Height")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Width")
    depth: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Depth")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Weight")
    creation_date: Optional[datetime] = Field(default=None, alias="CreationDate")
    inventory_tracking_type: Optional[StrictInt] = Field(default=None, alias="InventoryTrackingType")
    batch_number_scan_required: Optional[StrictBool] = Field(default=None, alias="BatchNumberScanRequired")
    serial_number_scan_required: Optional[StrictBool] = Field(default=None, alias="SerialNumberScanRequired")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="StockItemIntId")
    __properties: ClassVar[List[str]] = ["Suppliers", "StockLevels", "ItemChannelDescriptions", "ItemExtendedProperties", "ItemChannelTitles", "ItemChannelPrices", "Images", "ItemNumber", "ItemTitle", "BarcodeNumber", "MetaData", "IsVariationParent", "isBatchedStockType", "PurchasePrice", "RetailPrice", "TaxRate", "PostalServiceId", "PostalServiceName", "CategoryId", "CategoryName", "PackageGroupId", "PackageGroupName", "Height", "Width", "Depth", "Weight", "CreationDate", "InventoryTrackingType", "BatchNumberScanRequired", "SerialNumberScanRequired", "StockItemId", "StockItemIntId"]

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
        """Create an instance of StockItemFull from a JSON string"""
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
            "item_channel_descriptions",
            "item_extended_properties",
            "item_channel_titles",
            "item_channel_prices",
            "is_batched_stock_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in suppliers (list)
        _items = []
        if self.suppliers:
            for _item_suppliers in self.suppliers:
                if _item_suppliers:
                    _items.append(_item_suppliers.to_dict())
            _dict['Suppliers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in stock_levels (list)
        _items = []
        if self.stock_levels:
            for _item_stock_levels in self.stock_levels:
                if _item_stock_levels:
                    _items.append(_item_stock_levels.to_dict())
            _dict['StockLevels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in item_channel_descriptions (list)
        _items = []
        if self.item_channel_descriptions:
            for _item_item_channel_descriptions in self.item_channel_descriptions:
                if _item_item_channel_descriptions:
                    _items.append(_item_item_channel_descriptions.to_dict())
            _dict['ItemChannelDescriptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in item_extended_properties (list)
        _items = []
        if self.item_extended_properties:
            for _item_item_extended_properties in self.item_extended_properties:
                if _item_item_extended_properties:
                    _items.append(_item_item_extended_properties.to_dict())
            _dict['ItemExtendedProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in item_channel_titles (list)
        _items = []
        if self.item_channel_titles:
            for _item_item_channel_titles in self.item_channel_titles:
                if _item_item_channel_titles:
                    _items.append(_item_item_channel_titles.to_dict())
            _dict['ItemChannelTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in item_channel_prices (list)
        _items = []
        if self.item_channel_prices:
            for _item_item_channel_prices in self.item_channel_prices:
                if _item_item_channel_prices:
                    _items.append(_item_item_channel_prices.to_dict())
            _dict['ItemChannelPrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['Images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StockItemFull from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Suppliers": [StockItemSupplierStat.from_dict(_item) for _item in obj["Suppliers"]] if obj.get("Suppliers") is not None else None,
            "StockLevels": [StockItemLevel.from_dict(_item) for _item in obj["StockLevels"]] if obj.get("StockLevels") is not None else None,
            "ItemChannelDescriptions": [StockItemDescription.from_dict(_item) for _item in obj["ItemChannelDescriptions"]] if obj.get("ItemChannelDescriptions") is not None else None,
            "ItemExtendedProperties": [StockItemExtendedProperty.from_dict(_item) for _item in obj["ItemExtendedProperties"]] if obj.get("ItemExtendedProperties") is not None else None,
            "ItemChannelTitles": [StockItemTitle.from_dict(_item) for _item in obj["ItemChannelTitles"]] if obj.get("ItemChannelTitles") is not None else None,
            "ItemChannelPrices": [StockItemPrice.from_dict(_item) for _item in obj["ItemChannelPrices"]] if obj.get("ItemChannelPrices") is not None else None,
            "Images": [StockItemImage.from_dict(_item) for _item in obj["Images"]] if obj.get("Images") is not None else None,
            "ItemNumber": obj.get("ItemNumber"),
            "ItemTitle": obj.get("ItemTitle"),
            "BarcodeNumber": obj.get("BarcodeNumber"),
            "MetaData": obj.get("MetaData"),
            "IsVariationParent": obj.get("IsVariationParent"),
            "isBatchedStockType": obj.get("isBatchedStockType"),
            "PurchasePrice": obj.get("PurchasePrice"),
            "RetailPrice": obj.get("RetailPrice"),
            "TaxRate": obj.get("TaxRate"),
            "PostalServiceId": obj.get("PostalServiceId"),
            "PostalServiceName": obj.get("PostalServiceName"),
            "CategoryId": obj.get("CategoryId"),
            "CategoryName": obj.get("CategoryName"),
            "PackageGroupId": obj.get("PackageGroupId"),
            "PackageGroupName": obj.get("PackageGroupName"),
            "Height": obj.get("Height"),
            "Width": obj.get("Width"),
            "Depth": obj.get("Depth"),
            "Weight": obj.get("Weight"),
            "CreationDate": obj.get("CreationDate"),
            "InventoryTrackingType": obj.get("InventoryTrackingType"),
            "BatchNumberScanRequired": obj.get("BatchNumberScanRequired"),
            "SerialNumberScanRequired": obj.get("SerialNumberScanRequired"),
            "StockItemId": obj.get("StockItemId"),
            "StockItemIntId": obj.get("StockItemIntId")
        })
        return _obj


