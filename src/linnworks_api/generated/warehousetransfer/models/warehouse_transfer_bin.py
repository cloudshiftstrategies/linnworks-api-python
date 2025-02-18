# coding: utf-8

"""
    Warehouse Transfer (Legacy) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: warehousetransfer
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_bin_note import WarehouseTransferBinNote
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_item import WarehouseTransferItem
from typing import Optional, Set
from typing_extensions import Self

class WarehouseTransferBin(BaseModel):
    """
    WarehouseTransferBin
    """ # noqa: E501
    pk_bin_id: Optional[StrictStr] = Field(default=None, alias="PkBinId")
    bin_name: Optional[StrictStr] = Field(default=None, alias="BinName")
    bin_reference: Optional[StrictStr] = Field(default=None, alias="BinReference")
    bin_barcode: Optional[StrictStr] = Field(default=None, alias="BinBarcode")
    bin_notes: Optional[List[WarehouseTransferBinNote]] = Field(default=None, alias="BinNotes")
    bin_items: Optional[List[WarehouseTransferItem]] = Field(default=None, alias="BinItems")
    __properties: ClassVar[List[str]] = ["PkBinId", "BinName", "BinReference", "BinBarcode", "BinNotes", "BinItems"]

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
        """Create an instance of WarehouseTransferBin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bin_notes (list)
        _items = []
        if self.bin_notes:
            for _item_bin_notes in self.bin_notes:
                if _item_bin_notes:
                    _items.append(_item_bin_notes.to_dict())
            _dict['BinNotes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bin_items (list)
        _items = []
        if self.bin_items:
            for _item_bin_items in self.bin_items:
                if _item_bin_items:
                    _items.append(_item_bin_items.to_dict())
            _dict['BinItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WarehouseTransferBin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PkBinId": obj.get("PkBinId"),
            "BinName": obj.get("BinName"),
            "BinReference": obj.get("BinReference"),
            "BinBarcode": obj.get("BinBarcode"),
            "BinNotes": [WarehouseTransferBinNote.from_dict(_item) for _item in obj["BinNotes"]] if obj.get("BinNotes") is not None else None,
            "BinItems": [WarehouseTransferItem.from_dict(_item) for _item in obj["BinItems"]] if obj.get("BinItems") is not None else None
        })
        return _obj


