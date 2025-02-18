# coding: utf-8

"""
    Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: orders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from linnworks_api.generated.orders.models.face import Face
from typing import Optional, Set
from typing_extensions import Self

class PackedItem(BaseModel):
    """
    PackedItem
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, alias="ID")
    pk_stock_item_id: Optional[StrictStr] = Field(default=None, alias="PkStockItemId")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Width")
    height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Height")
    depth: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Depth")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Weight")
    x: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="X")
    y: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Y")
    z: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="Z")
    layer: Optional[StrictInt] = Field(default=None, alias="Layer")
    faces: Optional[List[Face]] = Field(default=None, alias="Faces")
    __properties: ClassVar[List[str]] = ["ID", "PkStockItemId", "SKU", "Width", "Height", "Depth", "Weight", "X", "Y", "Z", "Layer", "Faces"]

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
        """Create an instance of PackedItem from a JSON string"""
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
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in faces (list)
        _items = []
        if self.faces:
            for _item_faces in self.faces:
                if _item_faces:
                    _items.append(_item_faces.to_dict())
            _dict['Faces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PackedItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ID": obj.get("ID"),
            "PkStockItemId": obj.get("PkStockItemId"),
            "SKU": obj.get("SKU"),
            "Width": obj.get("Width"),
            "Height": obj.get("Height"),
            "Depth": obj.get("Depth"),
            "Weight": obj.get("Weight"),
            "X": obj.get("X"),
            "Y": obj.get("Y"),
            "Z": obj.get("Z"),
            "Layer": obj.get("Layer"),
            "Faces": [Face.from_dict(_item) for _item in obj["Faces"]] if obj.get("Faces") is not None else None
        })
        return _obj


