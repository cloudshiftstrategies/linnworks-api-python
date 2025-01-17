# coding: utf-8

"""
    Warehouse Transfer

    Warehouse Transfer v2

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_model import ShipmentItemModel
from linnworks_api.generated.warehousetransfer_v2.models.shipment_status import ShipmentStatus
from typing import Optional, Set
from typing_extensions import Self

class ShipmentModel(BaseModel):
    """
    ShipmentModel
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    shipping_plan_id: Optional[StrictInt] = Field(default=None, alias="shippingPlanId")
    amazon_shipment_id: Optional[StrictStr] = Field(default=None, alias="amazonShipmentId")
    warehouse_address: Optional[StrictStr] = Field(default=None, alias="warehouseAddress")
    status: Optional[ShipmentStatus] = None
    update_date: Optional[datetime] = Field(default=None, alias="updateDate")
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    items: Optional[List[ShipmentItemModel]] = None
    contact_name: Optional[StrictStr] = Field(default=None, alias="contactName")
    contact_email: Optional[StrictStr] = Field(default=None, alias="contactEmail")
    contact_phone_number: Optional[StrictStr] = Field(default=None, alias="contactPhoneNumber")
    ready_to_ship_window: Optional[datetime] = Field(default=None, alias="readyToShipWindow")
    __properties: ClassVar[List[str]] = ["id", "name", "shippingPlanId", "amazonShipmentId", "warehouseAddress", "status", "updateDate", "createDate", "items", "contactName", "contactEmail", "contactPhoneNumber", "readyToShipWindow"]

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
        """Create an instance of ShipmentModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if amazon_shipment_id (nullable) is None
        # and model_fields_set contains the field
        if self.amazon_shipment_id is None and "amazon_shipment_id" in self.model_fields_set:
            _dict['amazonShipmentId'] = None

        # set to None if warehouse_address (nullable) is None
        # and model_fields_set contains the field
        if self.warehouse_address is None and "warehouse_address" in self.model_fields_set:
            _dict['warehouseAddress'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if contact_name (nullable) is None
        # and model_fields_set contains the field
        if self.contact_name is None and "contact_name" in self.model_fields_set:
            _dict['contactName'] = None

        # set to None if contact_email (nullable) is None
        # and model_fields_set contains the field
        if self.contact_email is None and "contact_email" in self.model_fields_set:
            _dict['contactEmail'] = None

        # set to None if contact_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.contact_phone_number is None and "contact_phone_number" in self.model_fields_set:
            _dict['contactPhoneNumber'] = None

        # set to None if ready_to_ship_window (nullable) is None
        # and model_fields_set contains the field
        if self.ready_to_ship_window is None and "ready_to_ship_window" in self.model_fields_set:
            _dict['readyToShipWindow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipmentModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "shippingPlanId": obj.get("shippingPlanId"),
            "amazonShipmentId": obj.get("amazonShipmentId"),
            "warehouseAddress": obj.get("warehouseAddress"),
            "status": obj.get("status"),
            "updateDate": obj.get("updateDate"),
            "createDate": obj.get("createDate"),
            "items": [ShipmentItemModel.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "contactName": obj.get("contactName"),
            "contactEmail": obj.get("contactEmail"),
            "contactPhoneNumber": obj.get("contactPhoneNumber"),
            "readyToShipWindow": obj.get("readyToShipWindow")
        })
        return _obj


