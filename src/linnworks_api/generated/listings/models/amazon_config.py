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
from linnworks_api.generated.listings.models.amazon_attribute import AmazonAttribute
from linnworks_api.generated.listings.models.amazon_b_node import AmazonBNode
from linnworks_api.generated.listings.models.amazon_shipping import AmazonShipping
from linnworks_api.generated.listings.models.simple_shipping import SimpleShipping
from typing import Optional, Set
from typing_extensions import Self

class AmazonConfig(BaseModel):
    """
    AmazonConfig
    """ # noqa: E501
    fulfillment_type: Optional[StrictStr] = Field(default=None, alias="FulfillmentType")
    fulfillment_extended_property_name: Optional[StrictStr] = Field(default=None, alias="Fulfillment_ExtendedPropertyName")
    pk_config_id: Optional[StrictStr] = Field(default=None, alias="pkConfigId")
    config_name: Optional[StrictStr] = Field(default=None, alias="ConfigName")
    version: Optional[StrictInt] = Field(default=None, alias="Version")
    site: Optional[StrictStr] = Field(default=None, alias="Site")
    category: Optional[StrictStr] = Field(default=None, alias="Category")
    sub_type: Optional[StrictStr] = Field(default=None, alias="SubType")
    associated_templates: Optional[StrictInt] = Field(default=None, alias="AssociatedTemplates")
    associated_variations: Optional[StrictInt] = Field(default=None, alias="AssociatedVariations")
    picture_attributes: Optional[List[AmazonAttribute]] = Field(default=None, alias="PictureAttributes")
    attributes: Optional[List[AmazonAttribute]] = Field(default=None, alias="Attributes")
    variation_theme_attribute: Optional[AmazonAttribute] = Field(default=None, alias="VariationThemeAttribute")
    parentage_attribute: Optional[AmazonAttribute] = Field(default=None, alias="ParentageAttribute")
    variation_theme: Optional[StrictStr] = Field(default=None, alias="VariationTheme")
    variations: Optional[List[AmazonAttribute]] = Field(default=None, alias="Variations")
    browse_nodes: Optional[List[AmazonBNode]] = Field(default=None, alias="BrowseNodes")
    contains_browse_nodes: Optional[StrictBool] = Field(default=None, alias="ContainsBrowseNodes")
    first_browse_node_extended_property: Optional[StrictStr] = Field(default=None, alias="FirstBrowseNode_ExtendedProperty")
    second_browse_node_extended_property: Optional[StrictStr] = Field(default=None, alias="SecondBrowseNode_ExtendedProperty")
    variation_title_extended_property: Optional[StrictStr] = Field(default=None, alias="VariationTitle_ExtendedProperty")
    is_configurator_edited: Optional[StrictBool] = Field(default=None, alias="IsConfiguratorEdited")
    show_in_inventory: Optional[StrictBool] = Field(default=None, alias="ShowInInventory")
    last_update_time: Optional[StrictInt] = Field(default=None, alias="LastUpdateTime")
    last_update_session_id: Optional[StrictStr] = Field(default=None, alias="LastUpdateSessionId")
    shipping_override_method: Optional[StrictStr] = Field(default=None, alias="ShippingOverrideMethod")
    shipping_option: Optional[SimpleShipping] = Field(default=None, alias="ShippingOption")
    shippings: Optional[List[AmazonShipping]] = Field(default=None, alias="Shippings")
    use_main_item_images: Optional[StrictBool] = Field(default=None, alias="UseMainItemImages")
    ignore_incorrect_variation_children: Optional[StrictBool] = Field(default=None, alias="IgnoreIncorrectVariationChildren")
    __properties: ClassVar[List[str]] = ["FulfillmentType", "Fulfillment_ExtendedPropertyName", "pkConfigId", "ConfigName", "Version", "Site", "Category", "SubType", "AssociatedTemplates", "AssociatedVariations", "PictureAttributes", "Attributes", "VariationThemeAttribute", "ParentageAttribute", "VariationTheme", "Variations", "BrowseNodes", "ContainsBrowseNodes", "FirstBrowseNode_ExtendedProperty", "SecondBrowseNode_ExtendedProperty", "VariationTitle_ExtendedProperty", "IsConfiguratorEdited", "ShowInInventory", "LastUpdateTime", "LastUpdateSessionId", "ShippingOverrideMethod", "ShippingOption", "Shippings", "UseMainItemImages", "IgnoreIncorrectVariationChildren"]

    @field_validator('fulfillment_type')
    def fulfillment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'BOTH', 'MFN', 'FBA']):
            raise ValueError("must be one of enum values ('NONE', 'BOTH', 'MFN', 'FBA')")
        return value

    @field_validator('shipping_override_method')
    def shipping_override_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['None', 'Simple', 'Override']):
            raise ValueError("must be one of enum values ('None', 'Simple', 'Override')")
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
        """Create an instance of AmazonConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in picture_attributes (list)
        _items = []
        if self.picture_attributes:
            for _item_picture_attributes in self.picture_attributes:
                if _item_picture_attributes:
                    _items.append(_item_picture_attributes.to_dict())
            _dict['PictureAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['Attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of variation_theme_attribute
        if self.variation_theme_attribute:
            _dict['VariationThemeAttribute'] = self.variation_theme_attribute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parentage_attribute
        if self.parentage_attribute:
            _dict['ParentageAttribute'] = self.parentage_attribute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in variations (list)
        _items = []
        if self.variations:
            for _item_variations in self.variations:
                if _item_variations:
                    _items.append(_item_variations.to_dict())
            _dict['Variations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in browse_nodes (list)
        _items = []
        if self.browse_nodes:
            for _item_browse_nodes in self.browse_nodes:
                if _item_browse_nodes:
                    _items.append(_item_browse_nodes.to_dict())
            _dict['BrowseNodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of shipping_option
        if self.shipping_option:
            _dict['ShippingOption'] = self.shipping_option.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shippings (list)
        _items = []
        if self.shippings:
            for _item_shippings in self.shippings:
                if _item_shippings:
                    _items.append(_item_shippings.to_dict())
            _dict['Shippings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AmazonConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "FulfillmentType": obj.get("FulfillmentType"),
            "Fulfillment_ExtendedPropertyName": obj.get("Fulfillment_ExtendedPropertyName"),
            "pkConfigId": obj.get("pkConfigId"),
            "ConfigName": obj.get("ConfigName"),
            "Version": obj.get("Version"),
            "Site": obj.get("Site"),
            "Category": obj.get("Category"),
            "SubType": obj.get("SubType"),
            "AssociatedTemplates": obj.get("AssociatedTemplates"),
            "AssociatedVariations": obj.get("AssociatedVariations"),
            "PictureAttributes": [AmazonAttribute.from_dict(_item) for _item in obj["PictureAttributes"]] if obj.get("PictureAttributes") is not None else None,
            "Attributes": [AmazonAttribute.from_dict(_item) for _item in obj["Attributes"]] if obj.get("Attributes") is not None else None,
            "VariationThemeAttribute": AmazonAttribute.from_dict(obj["VariationThemeAttribute"]) if obj.get("VariationThemeAttribute") is not None else None,
            "ParentageAttribute": AmazonAttribute.from_dict(obj["ParentageAttribute"]) if obj.get("ParentageAttribute") is not None else None,
            "VariationTheme": obj.get("VariationTheme"),
            "Variations": [AmazonAttribute.from_dict(_item) for _item in obj["Variations"]] if obj.get("Variations") is not None else None,
            "BrowseNodes": [AmazonBNode.from_dict(_item) for _item in obj["BrowseNodes"]] if obj.get("BrowseNodes") is not None else None,
            "ContainsBrowseNodes": obj.get("ContainsBrowseNodes"),
            "FirstBrowseNode_ExtendedProperty": obj.get("FirstBrowseNode_ExtendedProperty"),
            "SecondBrowseNode_ExtendedProperty": obj.get("SecondBrowseNode_ExtendedProperty"),
            "VariationTitle_ExtendedProperty": obj.get("VariationTitle_ExtendedProperty"),
            "IsConfiguratorEdited": obj.get("IsConfiguratorEdited"),
            "ShowInInventory": obj.get("ShowInInventory"),
            "LastUpdateTime": obj.get("LastUpdateTime"),
            "LastUpdateSessionId": obj.get("LastUpdateSessionId"),
            "ShippingOverrideMethod": obj.get("ShippingOverrideMethod"),
            "ShippingOption": SimpleShipping.from_dict(obj["ShippingOption"]) if obj.get("ShippingOption") is not None else None,
            "Shippings": [AmazonShipping.from_dict(_item) for _item in obj["Shippings"]] if obj.get("Shippings") is not None else None,
            "UseMainItemImages": obj.get("UseMainItemImages"),
            "IgnoreIncorrectVariationChildren": obj.get("IgnoreIncorrectVariationChildren")
        })
        return _obj


