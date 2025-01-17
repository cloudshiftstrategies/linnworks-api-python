# coding: utf-8

"""
    Open Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: openorders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderItemOnOrder(BaseModel):
    """
    OrderItemOnOrder
    """ # noqa: E501
    pk_purchase_item_id: Optional[StrictStr] = Field(default=None, alias="pkPurchaseItemId")
    rowid: Optional[StrictStr] = Field(default=None, alias="Rowid")
    pk_purchase_id: Optional[StrictStr] = Field(default=None, alias="pkPurchaseId")
    external_invoice_number: Optional[StrictStr] = Field(default=None, alias="ExternalInvoiceNumber")
    fk_supplier_id: Optional[StrictStr] = Field(default=None, alias="fkSupplierId")
    date_of_delivery: Optional[datetime] = Field(default=None, alias="DateOfDelivery")
    quoted_delivery_date: Optional[datetime] = Field(default=None, alias="QuotedDeliveryDate")
    supplier_name: Optional[StrictStr] = Field(default=None, alias="SupplierName")
    fk_location_id: Optional[StrictStr] = Field(default=None, alias="fkLocationId")
    __properties: ClassVar[List[str]] = ["pkPurchaseItemId", "Rowid", "pkPurchaseId", "ExternalInvoiceNumber", "fkSupplierId", "DateOfDelivery", "QuotedDeliveryDate", "SupplierName", "fkLocationId"]

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
        """Create an instance of OrderItemOnOrder from a JSON string"""
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
        """Create an instance of OrderItemOnOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkPurchaseItemId": obj.get("pkPurchaseItemId"),
            "Rowid": obj.get("Rowid"),
            "pkPurchaseId": obj.get("pkPurchaseId"),
            "ExternalInvoiceNumber": obj.get("ExternalInvoiceNumber"),
            "fkSupplierId": obj.get("fkSupplierId"),
            "DateOfDelivery": obj.get("DateOfDelivery"),
            "QuotedDeliveryDate": obj.get("QuotedDeliveryDate"),
            "SupplierName": obj.get("SupplierName"),
            "fkLocationId": obj.get("fkLocationId")
        })
        return _obj


