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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.listings.models.ebay_attribute import EbayAttribute
from linnworks_api.generated.listings.models.ebay_prices import EbayPrices
from linnworks_api.generated.listings.models.ebay_variation import EbayVariation
from linnworks_api.generated.listings.models.image_data import ImageData
from linnworks_api.generated.listings.models.key_list import KeyList
from linnworks_api.generated.listings.models.key_value import KeyValue
from linnworks_api.generated.listings.models.linnworks_ebay_category import LinnworksEbayCategory
from typing import Optional, Set
from typing_extensions import Self

class EbayListing(BaseModel):
    """
    EbayListing
    """ # noqa: E501
    is_created_with_mapping_tool: Optional[StrictBool] = Field(default=None, alias="IsCreatedWithMappingTool")
    template_id: Optional[StrictStr] = Field(default=None, alias="TemplateId")
    inventory_item_id: Optional[StrictStr] = Field(default=None, alias="InventoryItemId")
    variation_group_name: Optional[StrictStr] = Field(default=None, alias="VariationGroupName")
    config_id: Optional[StrictStr] = Field(default=None, alias="ConfigId")
    config_name: Optional[StrictStr] = Field(default=None, alias="ConfigName")
    listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="ListingIds")
    sku: Optional[StrictStr] = Field(default=None, alias="SKU")
    account_id: Optional[StrictStr] = Field(default=None, alias="AccountId")
    barcode: Optional[StrictStr] = Field(default=None, alias="Barcode")
    barcode_error_message: Optional[StrictStr] = Field(default=None, alias="BarcodeErrorMessage")
    multiple_identifiers: Optional[List[KeyValue]] = Field(default=None, alias="MultipleIdentifiers")
    price: Optional[EbayPrices] = Field(default=None, alias="Price")
    available_quantity: Optional[StrictInt] = Field(default=None, alias="AvailableQuantity")
    title: Optional[StrictStr] = Field(default=None, alias="Title")
    sub_title: Optional[StrictStr] = Field(default=None, alias="SubTitle")
    description: Optional[StrictStr] = Field(default=None, alias="Description")
    e_pid: Optional[StrictStr] = Field(default=None, alias="ePID")
    is_catalog_match: Optional[StrictBool] = Field(default=None, alias="IsCatalogMatch")
    is_product_required: Optional[StrictBool] = Field(default=None, alias="IsProductRequired")
    attributes: Optional[List[EbayAttribute]] = Field(default=None, alias="Attributes")
    pictures: Optional[List[ImageData]] = Field(default=None, alias="Pictures")
    categories: Optional[List[LinnworksEbayCategory]] = Field(default=None, alias="Categories")
    store_categories: Optional[List[LinnworksEbayCategory]] = Field(default=None, alias="StoreCategories")
    dont_use_variation_pictures: Optional[StrictBool] = Field(default=None, alias="DontUseVariationPictures")
    variation_picture_specific: Optional[StrictStr] = Field(default=None, alias="VariationPictureSpecific")
    variations: Optional[List[EbayVariation]] = Field(default=None, alias="Variations")
    variations_positions: Optional[List[KeyList]] = Field(default=None, alias="VariationsPositions")
    old_variations: Optional[List[EbayVariation]] = Field(default=None, alias="OldVariations")
    old_variation_specifics: Optional[List[KeyList]] = Field(default=None, alias="OldVariationSpecifics")
    is_product_confirmation_required: Optional[StrictBool] = Field(default=None, alias="IsProductConfirmationRequired")
    status: Optional[StrictStr] = Field(default=None, alias="Status")
    error_message: Optional[StrictStr] = Field(default=None, alias="ErrorMessage")
    adjustments: Optional[StrictInt] = Field(default=None, alias="Adjustments")
    title_source: Optional[StrictStr] = Field(default=None, alias="TitleSource")
    is_pending_relist: Optional[StrictBool] = Field(default=None, alias="IsPendingRelist")
    start_time: Optional[datetime] = Field(default=None, alias="StartTime")
    is_read_only: Optional[StrictBool] = Field(default=None, alias="IsReadOnly")
    is_virtual_template: Optional[StrictBool] = Field(default=None, alias="IsVirtualTemplate")
    site: Optional[StrictStr] = Field(default=None, alias="Site")
    currency: Optional[StrictStr] = Field(default=None, alias="Currency")
    use_suggested_category: Optional[StrictBool] = Field(default=None, alias="UseSuggestedCategory")
    allow_category_change: Optional[StrictBool] = Field(default=None, alias="AllowCategoryChange")
    lot_size: Optional[StrictInt] = Field(default=None, alias="LotSize")
    is_recommendation: Optional[StrictBool] = Field(default=None, alias="IsRecommendation")
    recommendation_message: Optional[StrictStr] = Field(default=None, alias="RecommendationMessage")
    use_new_api: Optional[StrictBool] = Field(default=None, alias="UseNewApi")
    __properties: ClassVar[List[str]] = ["IsCreatedWithMappingTool", "TemplateId", "InventoryItemId", "VariationGroupName", "ConfigId", "ConfigName", "ListingIds", "SKU", "AccountId", "Barcode", "BarcodeErrorMessage", "MultipleIdentifiers", "Price", "AvailableQuantity", "Title", "SubTitle", "Description", "ePID", "IsCatalogMatch", "IsProductRequired", "Attributes", "Pictures", "Categories", "StoreCategories", "DontUseVariationPictures", "VariationPictureSpecific", "Variations", "VariationsPositions", "OldVariations", "OldVariationSpecifics", "IsProductConfirmationRequired", "Status", "ErrorMessage", "Adjustments", "TitleSource", "IsPendingRelist", "StartTime", "IsReadOnly", "IsVirtualTemplate", "Site", "Currency", "UseSuggestedCategory", "AllowCategoryChange", "LotSize", "IsRecommendation", "RecommendationMessage", "UseNewApi"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NOT_LISTED', 'OK', 'CREATING', 'UPDATING', 'DELETING', 'LISTING', 'ENDING', 'MANUALLY_ENDED', 'MIGRATING']):
            raise ValueError("must be one of enum values ('NOT_LISTED', 'OK', 'CREATING', 'UPDATING', 'DELETING', 'LISTING', 'ENDING', 'MANUALLY_ENDED', 'MIGRATING')")
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
        """Create an instance of EbayListing from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['Price'] = self.price.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['Categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in store_categories (list)
        _items = []
        if self.store_categories:
            for _item_store_categories in self.store_categories:
                if _item_store_categories:
                    _items.append(_item_store_categories.to_dict())
            _dict['StoreCategories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item_variations in self.variations:
                if _item_variations:
                    _items.append(_item_variations.to_dict())
            _dict['Variations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variations_positions (list)
        _items = []
        if self.variations_positions:
            for _item_variations_positions in self.variations_positions:
                if _item_variations_positions:
                    _items.append(_item_variations_positions.to_dict())
            _dict['VariationsPositions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in old_variations (list)
        _items = []
        if self.old_variations:
            for _item_old_variations in self.old_variations:
                if _item_old_variations:
                    _items.append(_item_old_variations.to_dict())
            _dict['OldVariations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in old_variation_specifics (list)
        _items = []
        if self.old_variation_specifics:
            for _item_old_variation_specifics in self.old_variation_specifics:
                if _item_old_variation_specifics:
                    _items.append(_item_old_variation_specifics.to_dict())
            _dict['OldVariationSpecifics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EbayListing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "IsCreatedWithMappingTool": obj.get("IsCreatedWithMappingTool"),
            "TemplateId": obj.get("TemplateId"),
            "InventoryItemId": obj.get("InventoryItemId"),
            "VariationGroupName": obj.get("VariationGroupName"),
            "ConfigId": obj.get("ConfigId"),
            "ConfigName": obj.get("ConfigName"),
            "ListingIds": obj.get("ListingIds"),
            "SKU": obj.get("SKU"),
            "AccountId": obj.get("AccountId"),
            "Barcode": obj.get("Barcode"),
            "BarcodeErrorMessage": obj.get("BarcodeErrorMessage"),
            "MultipleIdentifiers": [KeyValue.from_dict(_item) for _item in obj["MultipleIdentifiers"]] if obj.get("MultipleIdentifiers") is not None else None,
            "Price": EbayPrices.from_dict(obj["Price"]) if obj.get("Price") is not None else None,
            "AvailableQuantity": obj.get("AvailableQuantity"),
            "Title": obj.get("Title"),
            "SubTitle": obj.get("SubTitle"),
            "Description": obj.get("Description"),
            "ePID": obj.get("ePID"),
            "IsCatalogMatch": obj.get("IsCatalogMatch"),
            "IsProductRequired": obj.get("IsProductRequired"),
            "Attributes": [EbayAttribute.from_dict(_item) for _item in obj["Attributes"]] if obj.get("Attributes") is not None else None,
            "Pictures": [ImageData.from_dict(_item) for _item in obj["Pictures"]] if obj.get("Pictures") is not None else None,
            "Categories": [LinnworksEbayCategory.from_dict(_item) for _item in obj["Categories"]] if obj.get("Categories") is not None else None,
            "StoreCategories": [LinnworksEbayCategory.from_dict(_item) for _item in obj["StoreCategories"]] if obj.get("StoreCategories") is not None else None,
            "DontUseVariationPictures": obj.get("DontUseVariationPictures"),
            "VariationPictureSpecific": obj.get("VariationPictureSpecific"),
            "Variations": [EbayVariation.from_dict(_item) for _item in obj["Variations"]] if obj.get("Variations") is not None else None,
            "VariationsPositions": [KeyList.from_dict(_item) for _item in obj["VariationsPositions"]] if obj.get("VariationsPositions") is not None else None,
            "OldVariations": [EbayVariation.from_dict(_item) for _item in obj["OldVariations"]] if obj.get("OldVariations") is not None else None,
            "OldVariationSpecifics": [KeyList.from_dict(_item) for _item in obj["OldVariationSpecifics"]] if obj.get("OldVariationSpecifics") is not None else None,
            "IsProductConfirmationRequired": obj.get("IsProductConfirmationRequired"),
            "Status": obj.get("Status"),
            "ErrorMessage": obj.get("ErrorMessage"),
            "Adjustments": obj.get("Adjustments"),
            "TitleSource": obj.get("TitleSource"),
            "IsPendingRelist": obj.get("IsPendingRelist"),
            "StartTime": obj.get("StartTime"),
            "IsReadOnly": obj.get("IsReadOnly"),
            "IsVirtualTemplate": obj.get("IsVirtualTemplate"),
            "Site": obj.get("Site"),
            "Currency": obj.get("Currency"),
            "UseSuggestedCategory": obj.get("UseSuggestedCategory"),
            "AllowCategoryChange": obj.get("AllowCategoryChange"),
            "LotSize": obj.get("LotSize"),
            "IsRecommendation": obj.get("IsRecommendation"),
            "RecommendationMessage": obj.get("RecommendationMessage"),
            "UseNewApi": obj.get("UseNewApi")
        })
        return _obj


