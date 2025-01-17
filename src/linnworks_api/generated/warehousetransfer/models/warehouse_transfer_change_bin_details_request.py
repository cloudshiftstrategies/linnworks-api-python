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
from typing import Optional, Set
from typing_extensions import Self

class WarehouseTransferChangeBinDetailsRequest(BaseModel):
    """
    WarehouseTransferChangeBinDetailsRequest
    """ # noqa: E501
    pk_transfer_id: Optional[StrictStr] = Field(default=None, description="The id of the transfer the bin belongs to.", alias="pkTransferId")
    pk_bin_id: Optional[StrictStr] = Field(default=None, description="The id of the bin.", alias="pkBinId")
    bin_name: Optional[StrictStr] = Field(default=None, description="The new name for the bin (pass an empty string if no change is required).", alias="BinName")
    bin_reference: Optional[StrictStr] = Field(default=None, description="The new reference for the bin (pass an empty string if no change is required).", alias="BinReference")
    bin_barcode: Optional[StrictStr] = Field(default=None, description="The new barcode for the bin  (pass an empty string if no change is required).", alias="BinBarcode")
    __properties: ClassVar[List[str]] = ["pkTransferId", "pkBinId", "BinName", "BinReference", "BinBarcode"]

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
        """Create an instance of WarehouseTransferChangeBinDetailsRequest from a JSON string"""
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
        """Create an instance of WarehouseTransferChangeBinDetailsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pkTransferId": obj.get("pkTransferId"),
            "pkBinId": obj.get("pkBinId"),
            "BinName": obj.get("BinName"),
            "BinReference": obj.get("BinReference"),
            "BinBarcode": obj.get("BinBarcode")
        })
        return _obj


