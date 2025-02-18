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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer_v2.models.amazon_config_error_response import AmazonConfigErrorResponse
from linnworks_api.generated.warehousetransfer_v2.models.shipment_card_model import ShipmentCardModel
from typing import Optional, Set
from typing_extensions import Self

class GetShipmentCardsResponse(BaseModel):
    """
    GetShipmentCardsResponse
    """ # noqa: E501
    cards: Optional[List[ShipmentCardModel]] = None
    last_update_date: Optional[datetime] = Field(default=None, alias="lastUpdateDate")
    amazon_config_errors: Optional[List[AmazonConfigErrorResponse]] = Field(default=None, alias="amazonConfigErrors")
    __properties: ClassVar[List[str]] = ["cards", "lastUpdateDate", "amazonConfigErrors"]

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
        """Create an instance of GetShipmentCardsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cards (list)
        _items = []
        if self.cards:
            for _item_cards in self.cards:
                if _item_cards:
                    _items.append(_item_cards.to_dict())
            _dict['cards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in amazon_config_errors (list)
        _items = []
        if self.amazon_config_errors:
            for _item_amazon_config_errors in self.amazon_config_errors:
                if _item_amazon_config_errors:
                    _items.append(_item_amazon_config_errors.to_dict())
            _dict['amazonConfigErrors'] = _items
        # set to None if cards (nullable) is None
        # and model_fields_set contains the field
        if self.cards is None and "cards" in self.model_fields_set:
            _dict['cards'] = None

        # set to None if amazon_config_errors (nullable) is None
        # and model_fields_set contains the field
        if self.amazon_config_errors is None and "amazon_config_errors" in self.model_fields_set:
            _dict['amazonConfigErrors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetShipmentCardsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cards": [ShipmentCardModel.from_dict(_item) for _item in obj["cards"]] if obj.get("cards") is not None else None,
            "lastUpdateDate": obj.get("lastUpdateDate"),
            "amazonConfigErrors": [AmazonConfigErrorResponse.from_dict(_item) for _item in obj["amazonConfigErrors"]] if obj.get("amazonConfigErrors") is not None else None
        })
        return _obj


