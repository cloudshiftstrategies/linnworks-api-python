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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from linnworks_api.generated.warehousetransfer_v2.models.item_batches import ItemBatches
from typing import Optional, Set
from typing_extensions import Self

class AddFbaItemBatchRequestInput(BaseModel):
    """
    AddFbaItemBatchRequestInput
    """ # noqa: E501
    batches: List[ItemBatches]
    from_location: StrictStr = Field(alias="fromLocation")
    shipment_item_id: StrictInt = Field(alias="shipmentItemId")
    __properties: ClassVar[List[str]] = ["batches", "fromLocation", "shipmentItemId"]

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
        """Create an instance of AddFbaItemBatchRequestInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in batches (list)
        _items = []
        if self.batches:
            for _item_batches in self.batches:
                if _item_batches:
                    _items.append(_item_batches.to_dict())
            _dict['batches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddFbaItemBatchRequestInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batches": [ItemBatches.from_dict(_item) for _item in obj["batches"]] if obj.get("batches") is not None else None,
            "fromLocation": obj.get("fromLocation"),
            "shipmentItemId": obj.get("shipmentItemId")
        })
        return _obj


