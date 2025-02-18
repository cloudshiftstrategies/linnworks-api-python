# coding: utf-8

"""
    Purchase Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: purchaseorder
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AddPaymentStatementItem(BaseModel):
    """
    Add payment statement item Id
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Each item in the request can have unique Id supplied (uniqueidentifier) this Id will be returned to you in the response so you can match request item with the response", alias="Id")
    reference: Optional[StrictStr] = Field(default=None, description="Payment statement reference", alias="Reference")
    conversion_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Conversion rate from system currency, i.e. system currency rate to additional cost currency. For example if your system currency is GBP and payment statementis in USD the converted value is USD / Rate, example calculation, Rate 1.27, Additional cost total is 100, converted value = 100 USD / 1.27 = 78.98 GBP", alias="ConversionRate")
    currency: Optional[StrictStr] = Field(default=None, description="Currency code", alias="Currency")
    fk_purchase_additional_cost_item_id: Optional[StrictInt] = Field(default=None, description="Relation to additional cost line. If no value is set then the payment statement relates to PO supplier", alias="fkPurchaseAdditionalCostItemId")
    line_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Cost of the purchase order the payment contributes to", alias="LineCost")
    payment_date: Optional[datetime] = Field(default=None, description="Date when payment statement was marked as paid", alias="PaymentDate")
    creation_date: Optional[datetime] = Field(default=None, description="Date when the payment statement was added", alias="CreationDate")
    __properties: ClassVar[List[str]] = ["Id", "Reference", "ConversionRate", "Currency", "fkPurchaseAdditionalCostItemId", "LineCost", "PaymentDate", "CreationDate"]

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
        """Create an instance of AddPaymentStatementItem from a JSON string"""
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
        """Create an instance of AddPaymentStatementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Reference": obj.get("Reference"),
            "ConversionRate": obj.get("ConversionRate"),
            "Currency": obj.get("Currency"),
            "fkPurchaseAdditionalCostItemId": obj.get("fkPurchaseAdditionalCostItemId"),
            "LineCost": obj.get("LineCost"),
            "PaymentDate": obj.get("PaymentDate"),
            "CreationDate": obj.get("CreationDate")
        })
        return _obj


