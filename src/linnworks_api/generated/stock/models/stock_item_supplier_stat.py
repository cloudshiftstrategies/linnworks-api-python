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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class StockItemSupplierStat(BaseModel):
    """
    StockItemSupplierStat
    """ # noqa: E501
    is_default: Optional[StrictBool] = Field(default=None, alias="IsDefault")
    supplier: Optional[StrictStr] = Field(default=None, alias="Supplier")
    supplier_id: Optional[StrictStr] = Field(default=None, alias="SupplierID")
    code: Optional[StrictStr] = Field(default=None, alias="Code")
    supplier_barcode: Optional[StrictStr] = Field(default=None, alias="SupplierBarcode")
    lead_time: Optional[StrictInt] = Field(default=None, alias="LeadTime")
    purchase_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PurchasePrice")
    min_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="MinPrice")
    max_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="MaxPrice")
    average_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AveragePrice")
    average_lead_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="AverageLeadTime")
    supplier_min_order_qty: Optional[StrictInt] = Field(default=None, alias="SupplierMinOrderQty")
    supplier_pack_size: Optional[StrictInt] = Field(default=None, alias="SupplierPackSize")
    supplier_currency: Optional[StrictStr] = Field(default=None, alias="SupplierCurrency")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    stock_item_int_id: Optional[StrictInt] = Field(default=None, alias="StockItemIntId")
    __properties: ClassVar[List[str]] = ["IsDefault", "Supplier", "SupplierID", "Code", "SupplierBarcode", "LeadTime", "PurchasePrice", "MinPrice", "MaxPrice", "AveragePrice", "AverageLeadTime", "SupplierMinOrderQty", "SupplierPackSize", "SupplierCurrency", "StockItemId", "StockItemIntId"]

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
        """Create an instance of StockItemSupplierStat from a JSON string"""
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
        """Create an instance of StockItemSupplierStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IsDefault": obj.get("IsDefault"),
            "Supplier": obj.get("Supplier"),
            "SupplierID": obj.get("SupplierID"),
            "Code": obj.get("Code"),
            "SupplierBarcode": obj.get("SupplierBarcode"),
            "LeadTime": obj.get("LeadTime"),
            "PurchasePrice": obj.get("PurchasePrice"),
            "MinPrice": obj.get("MinPrice"),
            "MaxPrice": obj.get("MaxPrice"),
            "AveragePrice": obj.get("AveragePrice"),
            "AverageLeadTime": obj.get("AverageLeadTime"),
            "SupplierMinOrderQty": obj.get("SupplierMinOrderQty"),
            "SupplierPackSize": obj.get("SupplierPackSize"),
            "SupplierCurrency": obj.get("SupplierCurrency"),
            "StockItemId": obj.get("StockItemId"),
            "StockItemIntId": obj.get("StockItemIntId")
        })
        return _obj


