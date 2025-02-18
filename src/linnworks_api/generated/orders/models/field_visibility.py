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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FieldVisibility(BaseModel):
    """
    FieldVisibility
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    visible: Optional[StrictBool] = Field(default=None, alias="Visible")
    can_filter: Optional[StrictBool] = Field(default=None, alias="CanFilter")
    can_sort: Optional[StrictBool] = Field(default=None, alias="CanSort")
    field_type: Optional[StrictStr] = Field(default=None, alias="FieldType")
    code: Optional[StrictStr] = Field(default=None, alias="Code")
    sub_fields: Optional[List[FieldVisibility]] = Field(default=None, alias="SubFields")
    is_filter_only: Optional[StrictBool] = Field(default=None, alias="IsFilterOnly")
    hot_button_icon: Optional[StrictStr] = Field(default=None, alias="HotButtonIcon")
    hot_button_key: Optional[StrictStr] = Field(default=None, alias="HotButtonKey")
    __properties: ClassVar[List[str]] = ["Name", "Visible", "CanFilter", "CanSort", "FieldType", "Code", "SubFields", "IsFilterOnly", "HotButtonIcon", "HotButtonKey"]

    @field_validator('field_type')
    def field_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Decimal', 'Text', 'List', 'Date', 'Boolean', 'None', 'Button', 'HtmlList', 'Integer']):
            raise ValueError("must be one of enum values ('Decimal', 'Text', 'List', 'Date', 'Boolean', 'None', 'Button', 'HtmlList', 'Integer')")
        return value

    @field_validator('code')
    def code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'GENERAL_INFO', 'GENERAL_INFO_ORDER_ID', 'GENERAL_INFO_REFERENCE_NUMBER', 'GENERAL_INFO_CHANNEL_REFERENCE_NUMBER', 'GENERAL_INFO_EXTERNAL_REFERENCE_NUMBER', 'GENERAL_INFO_DATE', 'GENERAL_INFO_SOURCE', 'GENERAL_INFO_SUBSOURCE', 'GENERAL_INFO_LABEL_PRINTED', 'GENERAL_INFO_INVOICE_PRINTED', 'GENERAL_INFO_PICK_LIST_PRINTED', 'GENERAL_INFO_IS_RULE_RUN', 'GENERAL_INFO_NOTES', 'GENERAL_INFO_LOCKED', 'GENERAL_INFO_PARKED', 'GENERAL_INFO_PART_SHIPPED', 'GENERAL_INFO_TAG', 'GENERAL_INFO_IDENTIFIER', 'GENERAL_INFO_STATUS', 'GENERAL_INFO_DESPATCHBYDATE', 'GENERAL_INFO_ITEMS_COUNT', 'GENERAL_INFO_SHIPPING_LABEL_ERROR', 'GENERAL_INFO_HAS_SHIPPING_LABEL_ERROR', 'SHIPPING_INFORMATION', 'SHIPPING_INFORMATION_VENDOR', 'SHIPPING_INFORMATION_SERVICE', 'SHIPPING_INFORMATION_WEIGHT', 'SHIPPING_INFORMATION_PACKAGING_GROUP', 'SHIPPING_INFORMATION_PACKAGING_TYPE', 'SHIPPING_INFORMATION_COST', 'SHIPPING_INFORMATION_TRACKING_NUMBER', 'SHIPPING_INFORMATION_SERVICE_ID', 'SHIPPING_SCHEDULED_DELIVERY_START', 'SHIPPING_SCHEDULED_DELIVERY_END', 'CUSTOMER', 'CUSTOMER_ADDRESS_ADDRESS', 'CUSTOMER_ADDRESS_FULL_NAME', 'CUSTOMER_ADDRESS_COMPANY', 'CUSTOMER_ADDRESS_POSTCODE', 'CUSTOMER_ADDRESS_COUNTY', 'CUSTOMER_ADDRESS_COUNTRY', 'CUSTOMER_ADDRESS_COUNTRY_ZONE', 'CUSTOMER_ADDRESS_ADDRESS1', 'CUSTOMER_ADDRESS_ADDRESS2', 'CUSTOMER_ADDRESS_ADDRESS3', 'CUSTOMER_ADDRESS_TOWN', 'CUSTOMER_EMAIL', 'CUSTOMER_CHANNEL_BUYER_NAME', 'CUSTOMER_PHONE', 'CUSTOMER_BILLING_ADDRESS', 'CUSTOMER_BILLING_ADDRESS_NAME', 'CUSTOMER_BILLING_ADDRESS_COMPANY', 'CUSTOMER_BILLING_ADDRESS_ADDRESS1', 'CUSTOMER_BILLING_ADDRESS_ADDRESS2', 'CUSTOMER_BILLING_ADDRESS_ADDRESS3', 'CUSTOMER_BILLING_ADDRESS_TOWN', 'CUSTOMER_BILLING_ADDRESS_REGION', 'CUSTOMER_BILLING_ADDRESS_POSTCODE', 'CUSTOMER_BILLING_ADDRESS_COUNTRY', 'CUSTOMER_BILLING_EMAIL', 'CUSTOMER_BILLING_PHONE', 'TOTALS', 'TOTALS_SUBTOTAL', 'TOTALS_SHIPPING', 'TOTALS_TAX', 'TOTALS_TOTAL', 'TOTALS_DISCOUNT', 'TOTALS_CURRENCY', 'TOTALS_PAYMENT_METHOD', 'TOTALS_COUNTRY_TAX_RATE', 'ORDER_TOTAL', 'ORDER_TOTAL_TOTAL', 'ORDER_TOTAL_CURRENCY', 'ORDER_TAX', 'ORDER_TAX_TOTAL', 'ORDER_TAX_CURRENCY', 'FOLDER', 'FOLDERS', 'JOB', 'ITEMS', 'ITEMS_IMAGE', 'ITEMS_SKU', 'ITEMS_ORIGINAL_SKU', 'ITEMS_TITLE', 'ITEMS_ORIGINAL_TITLE', 'ITEMS_ITEM_NUMBER', 'ITEMS_IS_SERVICE', 'ITEMS_QUANTITY', 'ITEMS_SOURCE', 'ITEMS_LINE', 'ITEMS_COST_INC_TAX', 'ITEMS_COST', 'ITEMS_SALES_TAX', 'ITEMS_TAX_RATE', 'ITEMS_CURRENCY', 'ITEMS_CATEGORY', 'ITEMS_BINRACK', 'ITEMS_TAX_COST_INCLUSIVE', 'ITEMS_DISCOUNT', 'ITEMS_SUM_QUANTITY', 'ITEMS_WEIGHT', 'ITEMS_UNIT_COST', 'ITEMS_PRICE_PER_UNIT', 'ITEMS_BATCHED', 'ITEMS_INVENTORY_TRACKING_TYPE', 'ITEMS_BARCODE_NUMBER', 'STOCK_LEVEL', 'CAN_FULFIL', 'HOT_BUTTONS', 'HOT_BUTTON', 'ADDITIONAL', 'LOCATION_ID', 'ITEMS_STOCKITEM_ID', 'ITEMS_COMPOSITE_PARENT_ID', 'GENERAL_INFO_STOCK_ALLOCATION', 'GENERAL_INFO_NOTE', 'GENERAL_INFO_NOTE_COUNT', 'GENERAL_INFO_PICKWAVE_IDS', 'FULFILLMENT', 'FULFILLMENT_STATE', 'FULFILLMENT_ADDITIONAL', 'GENERAL_INFO_INVOICE_PRINT_ERROR', 'GENERAL_INFO_PICK_LIST_PRINT_ERROR']):
            raise ValueError("must be one of enum values ('NONE', 'GENERAL_INFO', 'GENERAL_INFO_ORDER_ID', 'GENERAL_INFO_REFERENCE_NUMBER', 'GENERAL_INFO_CHANNEL_REFERENCE_NUMBER', 'GENERAL_INFO_EXTERNAL_REFERENCE_NUMBER', 'GENERAL_INFO_DATE', 'GENERAL_INFO_SOURCE', 'GENERAL_INFO_SUBSOURCE', 'GENERAL_INFO_LABEL_PRINTED', 'GENERAL_INFO_INVOICE_PRINTED', 'GENERAL_INFO_PICK_LIST_PRINTED', 'GENERAL_INFO_IS_RULE_RUN', 'GENERAL_INFO_NOTES', 'GENERAL_INFO_LOCKED', 'GENERAL_INFO_PARKED', 'GENERAL_INFO_PART_SHIPPED', 'GENERAL_INFO_TAG', 'GENERAL_INFO_IDENTIFIER', 'GENERAL_INFO_STATUS', 'GENERAL_INFO_DESPATCHBYDATE', 'GENERAL_INFO_ITEMS_COUNT', 'GENERAL_INFO_SHIPPING_LABEL_ERROR', 'GENERAL_INFO_HAS_SHIPPING_LABEL_ERROR', 'SHIPPING_INFORMATION', 'SHIPPING_INFORMATION_VENDOR', 'SHIPPING_INFORMATION_SERVICE', 'SHIPPING_INFORMATION_WEIGHT', 'SHIPPING_INFORMATION_PACKAGING_GROUP', 'SHIPPING_INFORMATION_PACKAGING_TYPE', 'SHIPPING_INFORMATION_COST', 'SHIPPING_INFORMATION_TRACKING_NUMBER', 'SHIPPING_INFORMATION_SERVICE_ID', 'SHIPPING_SCHEDULED_DELIVERY_START', 'SHIPPING_SCHEDULED_DELIVERY_END', 'CUSTOMER', 'CUSTOMER_ADDRESS_ADDRESS', 'CUSTOMER_ADDRESS_FULL_NAME', 'CUSTOMER_ADDRESS_COMPANY', 'CUSTOMER_ADDRESS_POSTCODE', 'CUSTOMER_ADDRESS_COUNTY', 'CUSTOMER_ADDRESS_COUNTRY', 'CUSTOMER_ADDRESS_COUNTRY_ZONE', 'CUSTOMER_ADDRESS_ADDRESS1', 'CUSTOMER_ADDRESS_ADDRESS2', 'CUSTOMER_ADDRESS_ADDRESS3', 'CUSTOMER_ADDRESS_TOWN', 'CUSTOMER_EMAIL', 'CUSTOMER_CHANNEL_BUYER_NAME', 'CUSTOMER_PHONE', 'CUSTOMER_BILLING_ADDRESS', 'CUSTOMER_BILLING_ADDRESS_NAME', 'CUSTOMER_BILLING_ADDRESS_COMPANY', 'CUSTOMER_BILLING_ADDRESS_ADDRESS1', 'CUSTOMER_BILLING_ADDRESS_ADDRESS2', 'CUSTOMER_BILLING_ADDRESS_ADDRESS3', 'CUSTOMER_BILLING_ADDRESS_TOWN', 'CUSTOMER_BILLING_ADDRESS_REGION', 'CUSTOMER_BILLING_ADDRESS_POSTCODE', 'CUSTOMER_BILLING_ADDRESS_COUNTRY', 'CUSTOMER_BILLING_EMAIL', 'CUSTOMER_BILLING_PHONE', 'TOTALS', 'TOTALS_SUBTOTAL', 'TOTALS_SHIPPING', 'TOTALS_TAX', 'TOTALS_TOTAL', 'TOTALS_DISCOUNT', 'TOTALS_CURRENCY', 'TOTALS_PAYMENT_METHOD', 'TOTALS_COUNTRY_TAX_RATE', 'ORDER_TOTAL', 'ORDER_TOTAL_TOTAL', 'ORDER_TOTAL_CURRENCY', 'ORDER_TAX', 'ORDER_TAX_TOTAL', 'ORDER_TAX_CURRENCY', 'FOLDER', 'FOLDERS', 'JOB', 'ITEMS', 'ITEMS_IMAGE', 'ITEMS_SKU', 'ITEMS_ORIGINAL_SKU', 'ITEMS_TITLE', 'ITEMS_ORIGINAL_TITLE', 'ITEMS_ITEM_NUMBER', 'ITEMS_IS_SERVICE', 'ITEMS_QUANTITY', 'ITEMS_SOURCE', 'ITEMS_LINE', 'ITEMS_COST_INC_TAX', 'ITEMS_COST', 'ITEMS_SALES_TAX', 'ITEMS_TAX_RATE', 'ITEMS_CURRENCY', 'ITEMS_CATEGORY', 'ITEMS_BINRACK', 'ITEMS_TAX_COST_INCLUSIVE', 'ITEMS_DISCOUNT', 'ITEMS_SUM_QUANTITY', 'ITEMS_WEIGHT', 'ITEMS_UNIT_COST', 'ITEMS_PRICE_PER_UNIT', 'ITEMS_BATCHED', 'ITEMS_INVENTORY_TRACKING_TYPE', 'ITEMS_BARCODE_NUMBER', 'STOCK_LEVEL', 'CAN_FULFIL', 'HOT_BUTTONS', 'HOT_BUTTON', 'ADDITIONAL', 'LOCATION_ID', 'ITEMS_STOCKITEM_ID', 'ITEMS_COMPOSITE_PARENT_ID', 'GENERAL_INFO_STOCK_ALLOCATION', 'GENERAL_INFO_NOTE', 'GENERAL_INFO_NOTE_COUNT', 'GENERAL_INFO_PICKWAVE_IDS', 'FULFILLMENT', 'FULFILLMENT_STATE', 'FULFILLMENT_ADDITIONAL', 'GENERAL_INFO_INVOICE_PRINT_ERROR', 'GENERAL_INFO_PICK_LIST_PRINT_ERROR')")
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
        """Create an instance of FieldVisibility from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sub_fields (list)
        _items = []
        if self.sub_fields:
            for _item_sub_fields in self.sub_fields:
                if _item_sub_fields:
                    _items.append(_item_sub_fields.to_dict())
            _dict['SubFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FieldVisibility from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Name": obj.get("Name"),
            "Visible": obj.get("Visible"),
            "CanFilter": obj.get("CanFilter"),
            "CanSort": obj.get("CanSort"),
            "FieldType": obj.get("FieldType"),
            "Code": obj.get("Code"),
            "SubFields": [FieldVisibility.from_dict(_item) for _item in obj["SubFields"]] if obj.get("SubFields") is not None else None,
            "IsFilterOnly": obj.get("IsFilterOnly"),
            "HotButtonIcon": obj.get("HotButtonIcon"),
            "HotButtonKey": obj.get("HotButtonKey")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
FieldVisibility.model_rebuild(raise_errors=False)

