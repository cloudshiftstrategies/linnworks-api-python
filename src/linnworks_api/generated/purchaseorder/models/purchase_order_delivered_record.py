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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PurchaseOrderDeliveredRecord(BaseModel):
    """
    PurchaseOrderDeliveredRecord
    """ # noqa: E501
    fk_delivery_id: Optional[StrictInt] = Field(default=None, alias="fkDeliveryId")
    pk_delivery_record_id: Optional[StrictInt] = Field(default=None, alias="pkDeliveryRecordId")
    fk_purchase_item_id: Optional[StrictStr] = Field(default=None, alias="fkPurchaseItemId")
    fk_stock_location_id: Optional[StrictStr] = Field(default=None, alias="fkStockLocationId")
    unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="UnitCost")
    delivered_quantity: Optional[StrictInt] = Field(default=None, alias="DeliveredQuantity")
    created_date_time: Optional[datetime] = Field(default=None, alias="CreatedDateTime")
    modified_date_time: Optional[datetime] = Field(default=None, alias="ModifiedDateTime")
    fk_batch_inventory_id: Optional[StrictInt] = Field(default=None, alias="fkBatchInventoryId")
    __properties: ClassVar[List[str]] = ["fkDeliveryId", "pkDeliveryRecordId", "fkPurchaseItemId", "fkStockLocationId", "UnitCost", "DeliveredQuantity", "CreatedDateTime", "ModifiedDateTime", "fkBatchInventoryId"]

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
        """Create an instance of PurchaseOrderDeliveredRecord from a JSON string"""
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
        """Create an instance of PurchaseOrderDeliveredRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fkDeliveryId": obj.get("fkDeliveryId"),
            "pkDeliveryRecordId": obj.get("pkDeliveryRecordId"),
            "fkPurchaseItemId": obj.get("fkPurchaseItemId"),
            "fkStockLocationId": obj.get("fkStockLocationId"),
            "UnitCost": obj.get("UnitCost"),
            "DeliveredQuantity": obj.get("DeliveredQuantity"),
            "CreatedDateTime": obj.get("CreatedDateTime"),
            "ModifiedDateTime": obj.get("ModifiedDateTime"),
            "fkBatchInventoryId": obj.get("fkBatchInventoryId")
        })
        return _obj


