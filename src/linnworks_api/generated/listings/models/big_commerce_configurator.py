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
from linnworks_api.generated.listings.models.big_commerce_config_attributes import BigCommerceConfigAttributes
from linnworks_api.generated.listings.models.config_category import ConfigCategory
from linnworks_api.generated.listings.models.config_user_attributes import ConfigUserAttributes
from linnworks_api.generated.listings.models.var_attribute import VarAttribute
from typing import Optional, Set
from typing_extensions import Self

class BigCommerceConfigurator(BaseModel):
    """
    BigCommerceConfigurator
    """ # noqa: E501
    attributes: Optional[List[BigCommerceConfigAttributes]] = Field(default=None, alias="Attributes")
    option_set_name: Optional[StrictStr] = Field(default=None, alias="OptionSetName")
    var_attributes: Optional[List[VarAttribute]] = Field(default=None, alias="VarAttributes")
    user_attributes: Optional[List[ConfigUserAttributes]] = Field(default=None, alias="UserAttributes")
    pk_configid: Optional[StrictStr] = Field(default=None, alias="pkConfigid")
    categories: Optional[List[ConfigCategory]] = Field(default=None, alias="Categories")
    site: Optional[StrictStr] = Field(default=None, alias="Site")
    config_name: Optional[StrictStr] = Field(default=None, alias="ConfigName")
    category_extended_property: Optional[StrictStr] = Field(default=None, alias="CategoryExtendedProperty")
    manage_stock: Optional[StrictBool] = Field(default=None, alias="ManageStock")
    show_in_inventory: Optional[StrictBool] = Field(default=None, alias="ShowInInventory")
    is_changed: Optional[StrictBool] = Field(default=None, alias="IsChanged")
    last_update_time: Optional[StrictInt] = Field(default=None, alias="LastUpdateTime")
    last_update_session_id: Optional[StrictStr] = Field(default=None, alias="LastUpdateSessionId")
    associated_single: Optional[StrictInt] = Field(default=None, alias="AssociatedSingle")
    associated_variation: Optional[StrictInt] = Field(default=None, alias="AssociatedVariation")
    total_attributes: Optional[StrictInt] = Field(default=None, alias="TotalAttributes")
    total_var_attributes: Optional[StrictInt] = Field(default=None, alias="TotalVarAttributes")
    var_title_ext_property: Optional[StrictStr] = Field(default=None, alias="VarTitleExtProperty")
    use_main_item_images: Optional[StrictBool] = Field(default=None, alias="UseMainItemImages")
    glt_configurator_id: Optional[StrictInt] = Field(default=None, alias="GltConfiguratorId")
    __properties: ClassVar[List[str]] = ["Attributes", "OptionSetName", "VarAttributes", "UserAttributes", "pkConfigid", "Categories", "Site", "ConfigName", "CategoryExtendedProperty", "ManageStock", "ShowInInventory", "IsChanged", "LastUpdateTime", "LastUpdateSessionId", "AssociatedSingle", "AssociatedVariation", "TotalAttributes", "TotalVarAttributes", "VarTitleExtProperty", "UseMainItemImages", "GltConfiguratorId"]

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
        """Create an instance of BigCommerceConfigurator from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['Attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in var_attributes (list)
        _items = []
        if self.var_attributes:
            for _item_var_attributes in self.var_attributes:
                if _item_var_attributes:
                    _items.append(_item_var_attributes.to_dict())
            _dict['VarAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in user_attributes (list)
        _items = []
        if self.user_attributes:
            for _item_user_attributes in self.user_attributes:
                if _item_user_attributes:
                    _items.append(_item_user_attributes.to_dict())
            _dict['UserAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['Categories'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BigCommerceConfigurator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Attributes": [BigCommerceConfigAttributes.from_dict(_item) for _item in obj["Attributes"]] if obj.get("Attributes") is not None else None,
            "OptionSetName": obj.get("OptionSetName"),
            "VarAttributes": [VarAttribute.from_dict(_item) for _item in obj["VarAttributes"]] if obj.get("VarAttributes") is not None else None,
            "UserAttributes": [ConfigUserAttributes.from_dict(_item) for _item in obj["UserAttributes"]] if obj.get("UserAttributes") is not None else None,
            "pkConfigid": obj.get("pkConfigid"),
            "Categories": [ConfigCategory.from_dict(_item) for _item in obj["Categories"]] if obj.get("Categories") is not None else None,
            "Site": obj.get("Site"),
            "ConfigName": obj.get("ConfigName"),
            "CategoryExtendedProperty": obj.get("CategoryExtendedProperty"),
            "ManageStock": obj.get("ManageStock"),
            "ShowInInventory": obj.get("ShowInInventory"),
            "IsChanged": obj.get("IsChanged"),
            "LastUpdateTime": obj.get("LastUpdateTime"),
            "LastUpdateSessionId": obj.get("LastUpdateSessionId"),
            "AssociatedSingle": obj.get("AssociatedSingle"),
            "AssociatedVariation": obj.get("AssociatedVariation"),
            "TotalAttributes": obj.get("TotalAttributes"),
            "TotalVarAttributes": obj.get("TotalVarAttributes"),
            "VarTitleExtProperty": obj.get("VarTitleExtProperty"),
            "UseMainItemImages": obj.get("UseMainItemImages"),
            "GltConfiguratorId": obj.get("GltConfiguratorId")
        })
        return _obj


