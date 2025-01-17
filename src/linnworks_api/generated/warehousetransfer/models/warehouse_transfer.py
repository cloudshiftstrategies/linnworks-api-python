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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.warehousetransfer.models.update_status import UpdateStatus
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_audit import WarehouseTransferAudit
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_bin import WarehouseTransferBin
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_note import WarehouseTransferNote
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_property import WarehouseTransferProperty
from typing import Optional, Set
from typing_extensions import Self

class WarehouseTransfer(BaseModel):
    """
    WarehouseTransfer
    """ # noqa: E501
    pk_transfer_id: Optional[StrictStr] = Field(default=None, alias="PkTransferId")
    from_location_id: Optional[StrictStr] = Field(default=None, alias="FromLocationId")
    to_location_id: Optional[StrictStr] = Field(default=None, alias="ToLocationId")
    from_location: Optional[StrictStr] = Field(default=None, alias="FromLocation")
    to_location: Optional[StrictStr] = Field(default=None, alias="ToLocation")
    status: Optional[StrictStr] = Field(default=None, alias="Status")
    n_status: Optional[StrictInt] = Field(default=None, alias="nStatus")
    reference_number: Optional[StrictStr] = Field(default=None, alias="ReferenceNumber")
    order_date: Optional[datetime] = Field(default=None, alias="OrderDate")
    number_of_items: Optional[StrictInt] = Field(default=None, alias="NumberOfItems")
    number_of_notes: Optional[StrictInt] = Field(default=None, alias="NumberOfNotes")
    fk_original_transfer_id: Optional[StrictStr] = Field(default=None, alias="fkOriginalTransferId")
    original_transfer_reference: Optional[StrictStr] = Field(default=None, alias="OriginalTransferReference")
    is_discrepancy_transfer: Optional[StrictBool] = Field(default=None, alias="IsDiscrepancyTransfer")
    b_logical_delete: Optional[StrictBool] = Field(default=None, alias="BLogicalDelete")
    bins: Optional[List[WarehouseTransferBin]] = Field(default=None, alias="Bins")
    notes: Optional[List[WarehouseTransferNote]] = Field(default=None, alias="Notes")
    audit_trail: Optional[List[WarehouseTransferAudit]] = Field(default=None, alias="AuditTrail")
    transfer_properties: Optional[List[WarehouseTransferProperty]] = Field(default=None, alias="TransferProperties")
    update_status: Optional[UpdateStatus] = Field(default=None, alias="UpdateStatus")
    __properties: ClassVar[List[str]] = ["PkTransferId", "FromLocationId", "ToLocationId", "FromLocation", "ToLocation", "Status", "nStatus", "ReferenceNumber", "OrderDate", "NumberOfItems", "NumberOfNotes", "fkOriginalTransferId", "OriginalTransferReference", "IsDiscrepancyTransfer", "BLogicalDelete", "Bins", "Notes", "AuditTrail", "TransferProperties", "UpdateStatus"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Draft', 'Request', 'Accepted', 'Packing', 'InTransit', 'CheckingIn', 'Delivered']):
            raise ValueError("must be one of enum values ('Draft', 'Request', 'Accepted', 'Packing', 'InTransit', 'CheckingIn', 'Delivered')")
        return value

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
        """Create an instance of WarehouseTransfer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_discrepancy_transfer",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in bins (list)
        _items = []
        if self.bins:
            for _item_bins in self.bins:
                if _item_bins:
                    _items.append(_item_bins.to_dict())
            _dict['Bins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['Notes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in audit_trail (list)
        _items = []
        if self.audit_trail:
            for _item_audit_trail in self.audit_trail:
                if _item_audit_trail:
                    _items.append(_item_audit_trail.to_dict())
            _dict['AuditTrail'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transfer_properties (list)
        _items = []
        if self.transfer_properties:
            for _item_transfer_properties in self.transfer_properties:
                if _item_transfer_properties:
                    _items.append(_item_transfer_properties.to_dict())
            _dict['TransferProperties'] = _items
        # override the default output from pydantic by calling `to_dict()` of update_status
        if self.update_status:
            _dict['UpdateStatus'] = self.update_status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WarehouseTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PkTransferId": obj.get("PkTransferId"),
            "FromLocationId": obj.get("FromLocationId"),
            "ToLocationId": obj.get("ToLocationId"),
            "FromLocation": obj.get("FromLocation"),
            "ToLocation": obj.get("ToLocation"),
            "Status": obj.get("Status"),
            "nStatus": obj.get("nStatus"),
            "ReferenceNumber": obj.get("ReferenceNumber"),
            "OrderDate": obj.get("OrderDate"),
            "NumberOfItems": obj.get("NumberOfItems"),
            "NumberOfNotes": obj.get("NumberOfNotes"),
            "fkOriginalTransferId": obj.get("fkOriginalTransferId"),
            "OriginalTransferReference": obj.get("OriginalTransferReference"),
            "IsDiscrepancyTransfer": obj.get("IsDiscrepancyTransfer"),
            "BLogicalDelete": obj.get("BLogicalDelete"),
            "Bins": [WarehouseTransferBin.from_dict(_item) for _item in obj["Bins"]] if obj.get("Bins") is not None else None,
            "Notes": [WarehouseTransferNote.from_dict(_item) for _item in obj["Notes"]] if obj.get("Notes") is not None else None,
            "AuditTrail": [WarehouseTransferAudit.from_dict(_item) for _item in obj["AuditTrail"]] if obj.get("AuditTrail") is not None else None,
            "TransferProperties": [WarehouseTransferProperty.from_dict(_item) for _item in obj["TransferProperties"]] if obj.get("TransferProperties") is not None else None,
            "UpdateStatus": UpdateStatus.from_dict(obj["UpdateStatus"]) if obj.get("UpdateStatus") is not None else None
        })
        return _obj


