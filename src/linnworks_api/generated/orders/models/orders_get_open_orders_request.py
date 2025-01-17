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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.orders.models.field_sorting import FieldSorting
from linnworks_api.generated.orders.models.fields_filter import FieldsFilter
from typing import Optional, Set
from typing_extensions import Self

class OrdersGetOpenOrdersRequest(BaseModel):
    """
    OrdersGetOpenOrdersRequest
    """ # noqa: E501
    entries_per_page: Optional[StrictInt] = Field(default=None, description="Entries per page", alias="entriesPerPage")
    page_number: Optional[StrictInt] = Field(default=None, description="Page number", alias="pageNumber")
    filters: Optional[FieldsFilter] = None
    sorting: Optional[List[FieldSorting]] = Field(default=None, description="Sorting to apply")
    fulfilment_center: Optional[StrictStr] = Field(default=None, description="Location to get the orders for", alias="fulfilmentCenter")
    additional_filter: Optional[StrictStr] = Field(default=None, description="Additional filter", alias="additionalFilter")
    __properties: ClassVar[List[str]] = ["entriesPerPage", "pageNumber", "filters", "sorting", "fulfilmentCenter", "additionalFilter"]

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
        """Create an instance of OrdersGetOpenOrdersRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sorting (list)
        _items = []
        if self.sorting:
            for _item_sorting in self.sorting:
                if _item_sorting:
                    _items.append(_item_sorting.to_dict())
            _dict['sorting'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrdersGetOpenOrdersRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entriesPerPage": obj.get("entriesPerPage"),
            "pageNumber": obj.get("pageNumber"),
            "filters": FieldsFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "sorting": [FieldSorting.from_dict(_item) for _item in obj["sorting"]] if obj.get("sorting") is not None else None,
            "fulfilmentCenter": obj.get("fulfilmentCenter"),
            "additionalFilter": obj.get("additionalFilter")
        })
        return _obj


