# coding: utf-8

"""
    Inventory API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: inventory
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.inventory.models.custom_attribute_data import CustomAttributeData
from linnworks_api.generated.inventory.models.parameter_info import ParameterInfo
from typing import Optional, Set
from typing_extensions import Self

class MethodInfo(BaseModel):
    """
    MethodInfo
    """ # noqa: E501
    member_type: Optional[StrictStr] = Field(default=None, alias="MemberType")
    return_type: Optional[StrictStr] = Field(default=None, alias="ReturnType")
    return_parameter: Optional[ParameterInfo] = Field(default=None, alias="ReturnParameter")
    return_type_custom_attributes: Optional[Dict[str, Any]] = Field(default=None, alias="ReturnTypeCustomAttributes")
    method_implementation_flags: Optional[StrictStr] = Field(default=None, alias="MethodImplementationFlags")
    method_handle: Optional[Dict[str, Any]] = Field(default=None, alias="MethodHandle")
    attributes: Optional[StrictStr] = Field(default=None, alias="Attributes")
    calling_convention: Optional[StrictStr] = Field(default=None, alias="CallingConvention")
    is_generic_method_definition: Optional[StrictBool] = Field(default=None, alias="IsGenericMethodDefinition")
    contains_generic_parameters: Optional[StrictBool] = Field(default=None, alias="ContainsGenericParameters")
    is_generic_method: Optional[StrictBool] = Field(default=None, alias="IsGenericMethod")
    is_security_critical: Optional[StrictBool] = Field(default=None, alias="IsSecurityCritical")
    is_security_safe_critical: Optional[StrictBool] = Field(default=None, alias="IsSecuritySafeCritical")
    is_security_transparent: Optional[StrictBool] = Field(default=None, alias="IsSecurityTransparent")
    is_public: Optional[StrictBool] = Field(default=None, alias="IsPublic")
    is_private: Optional[StrictBool] = Field(default=None, alias="IsPrivate")
    is_family: Optional[StrictBool] = Field(default=None, alias="IsFamily")
    is_assembly: Optional[StrictBool] = Field(default=None, alias="IsAssembly")
    is_family_and_assembly: Optional[StrictBool] = Field(default=None, alias="IsFamilyAndAssembly")
    is_family_or_assembly: Optional[StrictBool] = Field(default=None, alias="IsFamilyOrAssembly")
    is_static: Optional[StrictBool] = Field(default=None, alias="IsStatic")
    is_final: Optional[StrictBool] = Field(default=None, alias="IsFinal")
    is_virtual: Optional[StrictBool] = Field(default=None, alias="IsVirtual")
    is_hide_by_sig: Optional[StrictBool] = Field(default=None, alias="IsHideBySig")
    is_abstract: Optional[StrictBool] = Field(default=None, alias="IsAbstract")
    is_special_name: Optional[StrictBool] = Field(default=None, alias="IsSpecialName")
    is_constructor: Optional[StrictBool] = Field(default=None, alias="IsConstructor")
    name: Optional[StrictStr] = Field(default=None, alias="Name")
    declaring_type: Optional[StrictStr] = Field(default=None, alias="DeclaringType")
    reflected_type: Optional[StrictStr] = Field(default=None, alias="ReflectedType")
    custom_attributes: Optional[List[CustomAttributeData]] = Field(default=None, alias="CustomAttributes")
    metadata_token: Optional[StrictInt] = Field(default=None, alias="MetadataToken")
    module: Optional[Dict[str, Any]] = Field(default=None, alias="Module")
    __properties: ClassVar[List[str]] = ["MemberType", "ReturnType", "ReturnParameter", "ReturnTypeCustomAttributes", "MethodImplementationFlags", "MethodHandle", "Attributes", "CallingConvention", "IsGenericMethodDefinition", "ContainsGenericParameters", "IsGenericMethod", "IsSecurityCritical", "IsSecuritySafeCritical", "IsSecurityTransparent", "IsPublic", "IsPrivate", "IsFamily", "IsAssembly", "IsFamilyAndAssembly", "IsFamilyOrAssembly", "IsStatic", "IsFinal", "IsVirtual", "IsHideBySig", "IsAbstract", "IsSpecialName", "IsConstructor", "Name", "DeclaringType", "ReflectedType", "CustomAttributes", "MetadataToken", "Module"]

    @field_validator('member_type')
    def member_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Constructor', 'Event', 'Field', 'Method', 'Property', 'TypeInfo', 'Custom', 'NestedType', 'All']):
            raise ValueError("must be one of enum values ('Constructor', 'Event', 'Field', 'Method', 'Property', 'TypeInfo', 'Custom', 'NestedType', 'All')")
        return value

    @field_validator('method_implementation_flags')
    def method_implementation_flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CodeTypeMask', 'IL', 'Native', 'OPTIL', 'Runtime', 'ManagedMask', 'Unmanaged', 'Managed', 'ForwardRef', 'PreserveSig', 'InternalCall', 'Synchronized', 'NoInlining', 'AggressiveInlining', 'NoOptimization', 'SecurityMitigations', 'MaxMethodImplVal']):
            raise ValueError("must be one of enum values ('CodeTypeMask', 'IL', 'Native', 'OPTIL', 'Runtime', 'ManagedMask', 'Unmanaged', 'Managed', 'ForwardRef', 'PreserveSig', 'InternalCall', 'Synchronized', 'NoInlining', 'AggressiveInlining', 'NoOptimization', 'SecurityMitigations', 'MaxMethodImplVal')")
        return value

    @field_validator('attributes')
    def attributes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MemberAccessMask', 'PrivateScope', 'Private', 'FamANDAssem', 'Assembly', 'Family', 'FamORAssem', 'Public', 'Static', 'Final', 'Virtual', 'HideBySig', 'CheckAccessOnOverride', 'VtableLayoutMask', 'ReuseSlot', 'NewSlot', 'Abstract', 'SpecialName', 'PinvokeImpl', 'UnmanagedExport', 'RTSpecialName', 'ReservedMask', 'HasSecurity', 'RequireSecObject']):
            raise ValueError("must be one of enum values ('MemberAccessMask', 'PrivateScope', 'Private', 'FamANDAssem', 'Assembly', 'Family', 'FamORAssem', 'Public', 'Static', 'Final', 'Virtual', 'HideBySig', 'CheckAccessOnOverride', 'VtableLayoutMask', 'ReuseSlot', 'NewSlot', 'Abstract', 'SpecialName', 'PinvokeImpl', 'UnmanagedExport', 'RTSpecialName', 'ReservedMask', 'HasSecurity', 'RequireSecObject')")
        return value

    @field_validator('calling_convention')
    def calling_convention_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Standard', 'VarArgs', 'Any', 'HasThis', 'ExplicitThis']):
            raise ValueError("must be one of enum values ('Standard', 'VarArgs', 'Any', 'HasThis', 'ExplicitThis')")
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
        """Create an instance of MethodInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "member_type",
            "return_type",
            "method_implementation_flags",
            "method_handle",
            "attributes",
            "calling_convention",
            "is_generic_method_definition",
            "contains_generic_parameters",
            "is_generic_method",
            "is_security_critical",
            "is_security_safe_critical",
            "is_security_transparent",
            "is_public",
            "is_private",
            "is_family",
            "is_assembly",
            "is_family_and_assembly",
            "is_family_or_assembly",
            "is_static",
            "is_final",
            "is_virtual",
            "is_hide_by_sig",
            "is_abstract",
            "is_special_name",
            "is_constructor",
            "name",
            "declaring_type",
            "reflected_type",
            "custom_attributes",
            "metadata_token",
            "module",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of return_parameter
        if self.return_parameter:
            _dict['ReturnParameter'] = self.return_parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_attributes (list)
        _items = []
        if self.custom_attributes:
            for _item_custom_attributes in self.custom_attributes:
                if _item_custom_attributes:
                    _items.append(_item_custom_attributes.to_dict())
            _dict['CustomAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MethodInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MemberType": obj.get("MemberType"),
            "ReturnType": obj.get("ReturnType"),
            "ReturnParameter": ParameterInfo.from_dict(obj["ReturnParameter"]) if obj.get("ReturnParameter") is not None else None,
            "ReturnTypeCustomAttributes": obj.get("ReturnTypeCustomAttributes"),
            "MethodImplementationFlags": obj.get("MethodImplementationFlags"),
            "MethodHandle": obj.get("MethodHandle"),
            "Attributes": obj.get("Attributes"),
            "CallingConvention": obj.get("CallingConvention"),
            "IsGenericMethodDefinition": obj.get("IsGenericMethodDefinition"),
            "ContainsGenericParameters": obj.get("ContainsGenericParameters"),
            "IsGenericMethod": obj.get("IsGenericMethod"),
            "IsSecurityCritical": obj.get("IsSecurityCritical"),
            "IsSecuritySafeCritical": obj.get("IsSecuritySafeCritical"),
            "IsSecurityTransparent": obj.get("IsSecurityTransparent"),
            "IsPublic": obj.get("IsPublic"),
            "IsPrivate": obj.get("IsPrivate"),
            "IsFamily": obj.get("IsFamily"),
            "IsAssembly": obj.get("IsAssembly"),
            "IsFamilyAndAssembly": obj.get("IsFamilyAndAssembly"),
            "IsFamilyOrAssembly": obj.get("IsFamilyOrAssembly"),
            "IsStatic": obj.get("IsStatic"),
            "IsFinal": obj.get("IsFinal"),
            "IsVirtual": obj.get("IsVirtual"),
            "IsHideBySig": obj.get("IsHideBySig"),
            "IsAbstract": obj.get("IsAbstract"),
            "IsSpecialName": obj.get("IsSpecialName"),
            "IsConstructor": obj.get("IsConstructor"),
            "Name": obj.get("Name"),
            "DeclaringType": obj.get("DeclaringType"),
            "ReflectedType": obj.get("ReflectedType"),
            "CustomAttributes": [CustomAttributeData.from_dict(_item) for _item in obj["CustomAttributes"]] if obj.get("CustomAttributes") is not None else None,
            "MetadataToken": obj.get("MetadataToken"),
            "Module": obj.get("Module")
        })
        return _obj


