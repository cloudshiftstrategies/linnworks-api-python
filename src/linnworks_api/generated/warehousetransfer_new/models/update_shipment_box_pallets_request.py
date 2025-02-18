# coding: utf-8

"""
    Warehouse Transfer

    Warehouse Transfer v1

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_box_pallet_model import UpdateShipmentBoxPalletModel
from typing import Optional, Set
from typing_extensions import Self

class UpdateShipmentBoxPalletsRequest(BaseModel):
    """
    UpdateShipmentBoxPalletsRequest
    """ # noqa: E501
    shipment_box_pallets: Optional[List[UpdateShipmentBoxPalletModel]] = Field(default=None, alias="shipmentBoxPallets")
    __properties: ClassVar[List[str]] = ["shipmentBoxPallets"]

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
        """Create an instance of UpdateShipmentBoxPalletsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shipment_box_pallets (list)
        _items = []
        if self.shipment_box_pallets:
            for _item_shipment_box_pallets in self.shipment_box_pallets:
                if _item_shipment_box_pallets:
                    _items.append(_item_shipment_box_pallets.to_dict())
            _dict['shipmentBoxPallets'] = _items
        # set to None if shipment_box_pallets (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_box_pallets is None and "shipment_box_pallets" in self.model_fields_set:
            _dict['shipmentBoxPallets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateShipmentBoxPalletsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentBoxPallets": [UpdateShipmentBoxPalletModel.from_dict(_item) for _item in obj["shipmentBoxPallets"]] if obj.get("shipmentBoxPallets") is not None else None
        })
        return _obj


