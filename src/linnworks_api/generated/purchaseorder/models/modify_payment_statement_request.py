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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.purchaseorder.models.add_payment_statement_item import AddPaymentStatementItem
from linnworks_api.generated.purchaseorder.models.update_payment_statement_item import UpdatePaymentStatementItem
from typing import Optional, Set
from typing_extensions import Self

class ModifyPaymentStatementRequest(BaseModel):
    """
    ModifyPaymentStatementRequest
    """ # noqa: E501
    items_to_add: Optional[List[AddPaymentStatementItem]] = Field(default=None, description="list of payment statements to add. Each item has Id which will be returned to you to match the item you are adding to array on your side", alias="itemsToAdd")
    items_to_update: Optional[List[UpdatePaymentStatementItem]] = Field(default=None, description="List of payment statements to update. Each line is identified by", alias="itemsToUpdate")
    items_to_delete: Optional[List[StrictInt]] = Field(default=None, description="List of payment statements to delete, provide list of PurchasePaymentStatementId's", alias="itemsToDelete")
    purchase_id: Optional[StrictStr] = Field(default=None, description="Purchase order id", alias="PurchaseId")
    __properties: ClassVar[List[str]] = ["itemsToAdd", "itemsToUpdate", "itemsToDelete", "PurchaseId"]

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
        """Create an instance of ModifyPaymentStatementRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items_to_add (list)
        _items = []
        if self.items_to_add:
            for _item_items_to_add in self.items_to_add:
                if _item_items_to_add:
                    _items.append(_item_items_to_add.to_dict())
            _dict['itemsToAdd'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items_to_update (list)
        _items = []
        if self.items_to_update:
            for _item_items_to_update in self.items_to_update:
                if _item_items_to_update:
                    _items.append(_item_items_to_update.to_dict())
            _dict['itemsToUpdate'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModifyPaymentStatementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemsToAdd": [AddPaymentStatementItem.from_dict(_item) for _item in obj["itemsToAdd"]] if obj.get("itemsToAdd") is not None else None,
            "itemsToUpdate": [UpdatePaymentStatementItem.from_dict(_item) for _item in obj["itemsToUpdate"]] if obj.get("itemsToUpdate") is not None else None,
            "itemsToDelete": obj.get("itemsToDelete"),
            "PurchaseId": obj.get("PurchaseId")
        })
        return _obj


