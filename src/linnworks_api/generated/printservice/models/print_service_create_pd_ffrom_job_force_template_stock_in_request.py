# coding: utf-8

"""
    Print Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: printservice
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from linnworks_api.generated.printservice.models.client_context import ClientContext
from linnworks_api.generated.printservice.models.key_value_string_string import KeyValueStringString
from linnworks_api.generated.printservice.models.printing_key import PrintingKey
from typing import Optional, Set
from typing_extensions import Self

class PrintServiceCreatePDFfromJobForceTemplateStockInRequest(BaseModel):
    """
    PrintServiceCreatePDFfromJobForceTemplateStockInRequest
    """ # noqa: E501
    template_type: Optional[StrictStr] = Field(default=None, description="The template type", alias="templateType")
    printing_keys: Optional[List[PrintingKey]] = Field(default=None, description="A list of IDs to print (e.g. Order IDs or Warehouse Transfer IDs)", alias="PrintingKeys")
    template_id: Optional[StrictInt] = Field(default=None, description="The ID of the template to use", alias="templateID")
    parameters: Optional[List[KeyValueStringString]] = None
    printer_name: Optional[StrictStr] = Field(default=None, description="printer name of the virtual printer to use. If null then the sepecified in the template", alias="printerName")
    print_zone_code: Optional[StrictStr] = Field(default=None, description="Print zone code, if present, will override the printer used if the template has a set printer for that zone", alias="printZoneCode")
    page_start_number: Optional[StrictInt] = Field(default=None, description="The starting page of the document to generate from (optional, default to 0)", alias="pageStartNumber")
    operation_id: Optional[StrictStr] = Field(default=None, description="The ID of the current operation, used in logging for tracing (optional, default to null)", alias="operationId")
    context: Optional[ClientContext] = None
    __properties: ClassVar[List[str]] = ["templateType", "PrintingKeys", "templateID", "parameters", "printerName", "printZoneCode", "pageStartNumber", "operationId", "context"]

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
        """Create an instance of PrintServiceCreatePDFfromJobForceTemplateStockInRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in printing_keys (list)
        _items = []
        if self.printing_keys:
            for _item_printing_keys in self.printing_keys:
                if _item_printing_keys:
                    _items.append(_item_printing_keys.to_dict())
            _dict['PrintingKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item_parameters in self.parameters:
                if _item_parameters:
                    _items.append(_item_parameters.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintServiceCreatePDFfromJobForceTemplateStockInRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templateType": obj.get("templateType"),
            "PrintingKeys": [PrintingKey.from_dict(_item) for _item in obj["PrintingKeys"]] if obj.get("PrintingKeys") is not None else None,
            "templateID": obj.get("templateID"),
            "parameters": [KeyValueStringString.from_dict(_item) for _item in obj["parameters"]] if obj.get("parameters") is not None else None,
            "printerName": obj.get("printerName"),
            "printZoneCode": obj.get("printZoneCode"),
            "pageStartNumber": obj.get("pageStartNumber"),
            "operationId": obj.get("operationId"),
            "context": ClientContext.from_dict(obj["context"]) if obj.get("context") is not None else None
        })
        return _obj


