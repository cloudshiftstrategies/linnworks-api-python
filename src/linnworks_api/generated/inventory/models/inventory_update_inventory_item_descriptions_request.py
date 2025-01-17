# coding: utf-8

"""
    Inventory API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: inventory
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.inventory.models.stock_item_description import StockItemDescription
from typing import Optional, Set
from typing_extensions import Self

class InventoryUpdateInventoryItemDescriptionsRequest(BaseModel):
    """
    InventoryUpdateInventoryItemDescriptionsRequest
    """ # noqa: E501
    inventory_item_descriptions: Optional[List[StockItemDescription]] = Field(default=None, description="list of stockitem Descriptions", alias="inventoryItemDescriptions")
    __properties: ClassVar[List[str]] = ["inventoryItemDescriptions"]

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
        """Create an instance of InventoryUpdateInventoryItemDescriptionsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inventory_item_descriptions (list)
        _items = []
        if self.inventory_item_descriptions:
            for _item_inventory_item_descriptions in self.inventory_item_descriptions:
                if _item_inventory_item_descriptions:
                    _items.append(_item_inventory_item_descriptions.to_dict())
            _dict['inventoryItemDescriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InventoryUpdateInventoryItemDescriptionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inventoryItemDescriptions": [StockItemDescription.from_dict(_item) for _item in obj["inventoryItemDescriptions"]] if obj.get("inventoryItemDescriptions") is not None else None
        })
        return _obj


