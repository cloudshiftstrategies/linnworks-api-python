# coding: utf-8

"""
    Returns and Refunds API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: returnsrefunds
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderNote(BaseModel):
    """
    OrderNote
    """ # noqa: E501
    order_note_id: Optional[StrictStr] = Field(default=None, alias="OrderNoteId")
    order_id: Optional[StrictStr] = Field(default=None, alias="OrderId")
    note_date: Optional[datetime] = Field(default=None, alias="NoteDate")
    internal: Optional[StrictBool] = Field(default=None, alias="Internal")
    note: Optional[StrictStr] = Field(default=None, alias="Note")
    created_by: Optional[StrictStr] = Field(default=None, alias="CreatedBy")
    note_type_id: Optional[StrictInt] = Field(default=None, alias="NoteTypeId")
    __properties: ClassVar[List[str]] = ["OrderNoteId", "OrderId", "NoteDate", "Internal", "Note", "CreatedBy", "NoteTypeId"]

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
        """Create an instance of OrderNote from a JSON string"""
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
        """Create an instance of OrderNote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "OrderNoteId": obj.get("OrderNoteId"),
            "OrderId": obj.get("OrderId"),
            "NoteDate": obj.get("NoteDate"),
            "Internal": obj.get("Internal"),
            "Note": obj.get("Note"),
            "CreatedBy": obj.get("CreatedBy"),
            "NoteTypeId": obj.get("NoteTypeId")
        })
        return _obj


