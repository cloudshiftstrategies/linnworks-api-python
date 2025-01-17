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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.warehousetransfer_v2.models.unit_of_measurement import UnitOfMeasurement
from linnworks_api.generated.warehousetransfer_v2.models.unit_of_weight import UnitOfWeight
from typing import Optional, Set
from typing_extensions import Self

class ShipmentBoxModel(BaseModel):
    """
    ShipmentBoxModel
    """ # noqa: E501
    shipment_box_id: Optional[StrictInt] = Field(default=None, alias="shipmentBoxId")
    shipment_id: Optional[StrictInt] = Field(default=None, alias="shipmentId")
    packing_group_id: Optional[StrictInt] = Field(default=None, alias="packingGroupId")
    name: Optional[StrictStr] = None
    height: Optional[Union[StrictFloat, StrictInt]] = None
    length: Optional[Union[StrictFloat, StrictInt]] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    shipment_measurement_unit: Optional[UnitOfMeasurement] = Field(default=None, alias="shipmentMeasurementUnit")
    weight: Optional[Union[StrictFloat, StrictInt]] = None
    shipment_weight_unit: Optional[UnitOfWeight] = Field(default=None, alias="shipmentWeightUnit")
    quantity: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["shipmentBoxId", "shipmentId", "packingGroupId", "name", "height", "length", "width", "shipmentMeasurementUnit", "weight", "shipmentWeightUnit", "quantity"]

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
        """Create an instance of ShipmentBoxModel from a JSON string"""
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
        # set to None if shipment_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_id is None and "shipment_id" in self.model_fields_set:
            _dict['shipmentId'] = None

        # set to None if packing_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.packing_group_id is None and "packing_group_id" in self.model_fields_set:
            _dict['packingGroupId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipmentBoxModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentBoxId": obj.get("shipmentBoxId"),
            "shipmentId": obj.get("shipmentId"),
            "packingGroupId": obj.get("packingGroupId"),
            "name": obj.get("name"),
            "height": obj.get("height"),
            "length": obj.get("length"),
            "width": obj.get("width"),
            "shipmentMeasurementUnit": obj.get("shipmentMeasurementUnit"),
            "weight": obj.get("weight"),
            "shipmentWeightUnit": obj.get("shipmentWeightUnit"),
            "quantity": obj.get("quantity")
        })
        return _obj


