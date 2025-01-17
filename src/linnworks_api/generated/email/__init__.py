# coding: utf-8

# flake8: noqa

"""
    Email API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: email
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from linnworks_api.generated.email.api.email_api import EmailApi

# import ApiClient
from linnworks_api.generated.email.api_response import ApiResponse
from linnworks_api.generated.email.api_client import ApiClient
from linnworks_api.generated.email.configuration import Configuration
from linnworks_api.generated.email.exceptions import OpenApiException
from linnworks_api.generated.email.exceptions import ApiTypeError
from linnworks_api.generated.email.exceptions import ApiValueError
from linnworks_api.generated.email.exceptions import ApiKeyError
from linnworks_api.generated.email.exceptions import ApiAttributeError
from linnworks_api.generated.email.exceptions import ApiException

# import models into sdk package
from linnworks_api.generated.email.models.email_generate_adhoc_email_request import EmailGenerateAdhocEmailRequest
from linnworks_api.generated.email.models.email_generate_free_text_email_request import EmailGenerateFreeTextEmailRequest
from linnworks_api.generated.email.models.email_stub_custom_tag import EmailStubCustomTag
from linnworks_api.generated.email.models.email_template import EmailTemplate
from linnworks_api.generated.email.models.email_template_header import EmailTemplateHeader
from linnworks_api.generated.email.models.email_template_type import EmailTemplateType
from linnworks_api.generated.email.models.generate_adhoc_email_request import GenerateAdhocEmailRequest
from linnworks_api.generated.email.models.generate_adhoc_email_response import GenerateAdhocEmailResponse
from linnworks_api.generated.email.models.generate_free_text_email_request import GenerateFreeTextEmailRequest
from linnworks_api.generated.email.models.generate_free_text_email_response import GenerateFreeTextEmailResponse
from linnworks_api.generated.email.models.template_tag import TemplateTag
