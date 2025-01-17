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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer_v2.models.incentive_model import IncentiveModel
from linnworks_api.generated.warehousetransfer_v2.models.option_status import OptionStatus
from linnworks_api.generated.warehousetransfer_v2.models.packing_group_model import PackingGroupModel
from linnworks_api.generated.warehousetransfer_v2.models.shipping_configuration_model import ShippingConfigurationModel
from typing import Optional, Set
from typing_extensions import Self

class PackingOptionModel(BaseModel):
    """
    PackingOptionModel
    """ # noqa: E501
    packing_option_id: Optional[StrictStr] = Field(default=None, alias="packingOptionId")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")
    status: Optional[OptionStatus] = None
    packing_groups: Optional[List[PackingGroupModel]] = Field(default=None, alias="packingGroups")
    fees: Optional[List[IncentiveModel]] = None
    discounts: Optional[List[IncentiveModel]] = None
    shipping_configurations: Optional[List[ShippingConfigurationModel]] = Field(default=None, alias="shippingConfigurations")
    __properties: ClassVar[List[str]] = ["packingOptionId", "expirationDate", "status", "packingGroups", "fees", "discounts", "shippingConfigurations"]

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
        """Create an instance of PackingOptionModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in packing_groups (list)
        _items = []
        if self.packing_groups:
            for _item_packing_groups in self.packing_groups:
                if _item_packing_groups:
                    _items.append(_item_packing_groups.to_dict())
            _dict['packingGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fees (list)
        _items = []
        if self.fees:
            for _item_fees in self.fees:
                if _item_fees:
                    _items.append(_item_fees.to_dict())
            _dict['fees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in discounts (list)
        _items = []
        if self.discounts:
            for _item_discounts in self.discounts:
                if _item_discounts:
                    _items.append(_item_discounts.to_dict())
            _dict['discounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_configurations (list)
        _items = []
        if self.shipping_configurations:
            for _item_shipping_configurations in self.shipping_configurations:
                if _item_shipping_configurations:
                    _items.append(_item_shipping_configurations.to_dict())
            _dict['shippingConfigurations'] = _items
        # set to None if packing_option_id (nullable) is None
        # and model_fields_set contains the field
        if self.packing_option_id is None and "packing_option_id" in self.model_fields_set:
            _dict['packingOptionId'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expirationDate'] = None

        # set to None if packing_groups (nullable) is None
        # and model_fields_set contains the field
        if self.packing_groups is None and "packing_groups" in self.model_fields_set:
            _dict['packingGroups'] = None

        # set to None if fees (nullable) is None
        # and model_fields_set contains the field
        if self.fees is None and "fees" in self.model_fields_set:
            _dict['fees'] = None

        # set to None if discounts (nullable) is None
        # and model_fields_set contains the field
        if self.discounts is None and "discounts" in self.model_fields_set:
            _dict['discounts'] = None

        # set to None if shipping_configurations (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_configurations is None and "shipping_configurations" in self.model_fields_set:
            _dict['shippingConfigurations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PackingOptionModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "packingOptionId": obj.get("packingOptionId"),
            "expirationDate": obj.get("expirationDate"),
            "status": obj.get("status"),
            "packingGroups": [PackingGroupModel.from_dict(_item) for _item in obj["packingGroups"]] if obj.get("packingGroups") is not None else None,
            "fees": [IncentiveModel.from_dict(_item) for _item in obj["fees"]] if obj.get("fees") is not None else None,
            "discounts": [IncentiveModel.from_dict(_item) for _item in obj["discounts"]] if obj.get("discounts") is not None else None,
            "shippingConfigurations": [ShippingConfigurationModel.from_dict(_item) for _item in obj["shippingConfigurations"]] if obj.get("shippingConfigurations") is not None else None
        })
        return _obj


