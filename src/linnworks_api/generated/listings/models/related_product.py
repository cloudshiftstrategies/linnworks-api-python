# coding: utf-8

"""
    Listings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: listings
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RelatedProduct(BaseModel):
    """
    RelatedProduct
    """ # noqa: E501
    template_id: Optional[StrictStr] = Field(default=None, alias="TemplateId")
    product_id: Optional[StrictInt] = Field(default=None, alias="ProductId")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    link_assigned: Optional[StrictBool] = Field(default=None, alias="LinkAssigned")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    __properties: ClassVar[List[str]] = ["TemplateId", "ProductId", "Name", "LinkAssigned", "Type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UpSells', 'CrossSells', 'Related', 'Grouped']):
            raise ValueError("must be one of enum values ('UpSells', 'CrossSells', 'Related', 'Grouped')")
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
        """Create an instance of RelatedProduct from a JSON string"""
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
        """Create an instance of RelatedProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TemplateId": obj.get("TemplateId"),
            "ProductId": obj.get("ProductId"),
            "Name": obj.get("Name"),
            "LinkAssigned": obj.get("LinkAssigned"),
            "Type": obj.get("Type")
        })
        return _obj


