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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.warehousetransfer_v2.models.amazon_prep_instruction_item import AmazonPrepInstructionItem
from linnworks_api.generated.warehousetransfer_v2.models.sku_prep_barcode_instruction import SkuPrepBarcodeInstruction
from linnworks_api.generated.warehousetransfer_v2.models.sku_prep_guidance import SkuPrepGuidance
from typing import Optional, Set
from typing_extensions import Self

class UpdateShipmentItemPrepInstructionRequestItem(BaseModel):
    """
    UpdateShipmentItemPrepInstructionRequestItem
    """ # noqa: E501
    shipment_item_id: Optional[StrictInt] = Field(default=None, alias="shipmentItemId")
    barcode_instruction: Optional[SkuPrepBarcodeInstruction] = Field(default=None, alias="barcodeInstruction")
    prep_guidance: Optional[SkuPrepGuidance] = Field(default=None, alias="prepGuidance")
    prep_instruction_list: Optional[List[AmazonPrepInstructionItem]] = Field(default=None, alias="prepInstructionList")
    fee_amount_per_unit: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, alias="feeAmountPerUnit")
    total_fee_amount: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, alias="totalFeeAmount")
    __properties: ClassVar[List[str]] = ["shipmentItemId", "barcodeInstruction", "prepGuidance", "prepInstructionList", "feeAmountPerUnit", "totalFeeAmount"]

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
        """Create an instance of UpdateShipmentItemPrepInstructionRequestItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in prep_instruction_list (list)
        _items = []
        if self.prep_instruction_list:
            for _item_prep_instruction_list in self.prep_instruction_list:
                if _item_prep_instruction_list:
                    _items.append(_item_prep_instruction_list.to_dict())
            _dict['prepInstructionList'] = _items
        # set to None if prep_instruction_list (nullable) is None
        # and model_fields_set contains the field
        if self.prep_instruction_list is None and "prep_instruction_list" in self.model_fields_set:
            _dict['prepInstructionList'] = None

        # set to None if fee_amount_per_unit (nullable) is None
        # and model_fields_set contains the field
        if self.fee_amount_per_unit is None and "fee_amount_per_unit" in self.model_fields_set:
            _dict['feeAmountPerUnit'] = None

        # set to None if total_fee_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_fee_amount is None and "total_fee_amount" in self.model_fields_set:
            _dict['totalFeeAmount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateShipmentItemPrepInstructionRequestItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipmentItemId": obj.get("shipmentItemId"),
            "barcodeInstruction": obj.get("barcodeInstruction"),
            "prepGuidance": obj.get("prepGuidance"),
            "prepInstructionList": [AmazonPrepInstructionItem.from_dict(_item) for _item in obj["prepInstructionList"]] if obj.get("prepInstructionList") is not None else None,
            "feeAmountPerUnit": obj.get("feeAmountPerUnit"),
            "totalFeeAmount": obj.get("totalFeeAmount")
        })
        return _obj


