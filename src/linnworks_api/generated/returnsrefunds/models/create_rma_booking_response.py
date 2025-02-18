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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.returnsrefunds.models.verified_rma_item import VerifiedRMAItem
from typing import Optional, Set
from typing_extensions import Self

class CreateRMABookingResponse(BaseModel):
    """
    CreateRMABookingResponse
    """ # noqa: E501
    rma_header_id: Optional[StrictInt] = Field(default=None, description="An identifier for the RMA request header being worked with. Newly created RMA headers will have this field populated as part of the \"Create\" request", alias="RMAHeaderId")
    items: Optional[List[VerifiedRMAItem]] = Field(default=None, description="A collection of verified and validated items that have been added to this RMA request", alias="Items")
    errors: Optional[List[StrictStr]] = Field(default=None, description="Any global validation errors are included in this collection, along with a concatenation of any errors found in an individual item", alias="Errors")
    info: Optional[List[StrictStr]] = Field(default=None, description="Any global validation information is included in this collection, along with a concatenation of any information found in an individual item", alias="Info")
    __properties: ClassVar[List[str]] = ["RMAHeaderId", "Items", "Errors", "Info"]

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
        """Create an instance of CreateRMABookingResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['Items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRMABookingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RMAHeaderId": obj.get("RMAHeaderId"),
            "Items": [VerifiedRMAItem.from_dict(_item) for _item in obj["Items"]] if obj.get("Items") is not None else None,
            "Errors": obj.get("Errors"),
            "Info": obj.get("Info")
        })
        return _obj


