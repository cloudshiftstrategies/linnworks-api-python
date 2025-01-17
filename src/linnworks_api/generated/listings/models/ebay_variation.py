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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.listings.models.ebay_attribute import EbayAttribute
from linnworks_api.generated.listings.models.ebay_prices import EbayPrices
from linnworks_api.generated.listings.models.image_data import ImageData
from linnworks_api.generated.listings.models.key_value import KeyValue
from typing import Optional, Set
from typing_extensions import Self

class EbayVariation(BaseModel):
    """
    EbayVariation
    """ # noqa: E501
    collision_number: Optional[StrictInt] = Field(default=None, alias="CollisionNumber")
    is_linked: Optional[StrictBool] = Field(default=None, alias="IsLinked")
    stock_item_id: Optional[StrictStr] = Field(default=None, alias="StockItemId")
    barcode: Optional[StrictStr] = Field(default=None, alias="Barcode")
    multiple_identifiers: Optional[List[KeyValue]] = Field(default=None, alias="MultipleIdentifiers")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    e_pid: Optional[StrictStr] = Field(default=None, alias="ePID")
    is_catalog_match: Optional[StrictBool] = Field(default=None, alias="IsCatalogMatch")
    attributes: Optional[List[EbayAttribute]] = Field(default=None, alias="Attributes")
    error_mesage: Optional[StrictStr] = Field(default=None, alias="ErrorMesage")
    pictures: Optional[List[ImageData]] = Field(default=None, alias="Pictures")
    price: Optional[EbayPrices] = Field(default=None, alias="Price")
    lot_size: Optional[StrictInt] = Field(default=None, alias="LotSize")
    __properties: ClassVar[List[str]] = ["CollisionNumber", "IsLinked", "StockItemId", "Barcode", "MultipleIdentifiers", "Title", "SKU", "ePID", "IsCatalogMatch", "Attributes", "ErrorMesage", "Pictures", "Price", "LotSize"]

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
        """Create an instance of EbayVariation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in multiple_identifiers (list)
        _items = []
        if self.multiple_identifiers:
            for _item_multiple_identifiers in self.multiple_identifiers:
                if _item_multiple_identifiers:
                    _items.append(_item_multiple_identifiers.to_dict())
            _dict['MultipleIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['Attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pictures (list)
        _items = []
        if self.pictures:
            for _item_pictures in self.pictures:
                if _item_pictures:
                    _items.append(_item_pictures.to_dict())
            _dict['Pictures'] = _items
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['Price'] = self.price.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EbayVariation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CollisionNumber": obj.get("CollisionNumber"),
            "IsLinked": obj.get("IsLinked"),
            "StockItemId": obj.get("StockItemId"),
            "Barcode": obj.get("Barcode"),
            "MultipleIdentifiers": [KeyValue.from_dict(_item) for _item in obj["MultipleIdentifiers"]] if obj.get("MultipleIdentifiers") is not None else None,
            "Title": obj.get("Title"),
            "SKU": obj.get("SKU"),
            "ePID": obj.get("ePID"),
            "IsCatalogMatch": obj.get("IsCatalogMatch"),
            "Attributes": [EbayAttribute.from_dict(_item) for _item in obj["Attributes"]] if obj.get("Attributes") is not None else None,
            "ErrorMesage": obj.get("ErrorMesage"),
            "Pictures": [ImageData.from_dict(_item) for _item in obj["Pictures"]] if obj.get("Pictures") is not None else None,
            "Price": EbayPrices.from_dict(obj["Price"]) if obj.get("Price") is not None else None,
            "LotSize": obj.get("LotSize")
        })
        return _obj


