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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class UpdatePurchaseOrderItem(BaseModel):
    """
    Purchase order item to update
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="unique row id, to uniquely identify submitted item. This Id will be returned in the response so you can match request to response items", alias="Id")
    purchase_item_id: Optional[StrictStr] = Field(default=None, alias="PurchaseItemId")
    stock_item_id: Optional[StrictStr] = Field(default=None, description="pkStockItemId. Use Get Stock Item API call to get the id of a product by SKU or Title", alias="StockItemId")
    qty: Optional[StrictInt] = Field(default=None, description="Quantity of items in the purchase order line", alias="Qty")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Line Total cost of all the purchase order item inclusive of tax (unitcost * qty) + tax", alias="Cost")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Product tax rate", alias="TaxRate")
    pack_quantity: Optional[StrictInt] = Field(default=None, description="Number of items in a single pack. This is for reference purposes only. Not used for any calculations.", alias="PackQuantity")
    pack_size: Optional[StrictInt] = Field(default=None, description="Number of packs ordered. This is for reference purposes only. Not used for any calculations.", alias="PackSize")
    __properties: ClassVar[List[str]] = ["Id", "PurchaseItemId", "StockItemId", "Qty", "Cost", "TaxRate", "PackQuantity", "PackSize"]

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
        """Create an instance of UpdatePurchaseOrderItem from a JSON string"""
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
        """Create an instance of UpdatePurchaseOrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "PurchaseItemId": obj.get("PurchaseItemId"),
            "StockItemId": obj.get("StockItemId"),
            "Qty": obj.get("Qty"),
            "Cost": obj.get("Cost"),
            "TaxRate": obj.get("TaxRate"),
            "PackQuantity": obj.get("PackQuantity"),
            "PackSize": obj.get("PackSize")
        })
        return _obj


