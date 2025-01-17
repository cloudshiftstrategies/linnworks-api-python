# coding: utf-8

# flake8: noqa
"""
    Open Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: openorders
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from linnworks_api.generated.openorders.models.assign_result import AssignResult
from linnworks_api.generated.openorders.models.assign_stock_to_orders_request import AssignStockToOrdersRequest
from linnworks_api.generated.openorders.models.assign_stock_to_orders_response_int32_int32 import AssignStockToOrdersResponseInt32Int32
from linnworks_api.generated.openorders.models.assign_stock_to_orders_response_order_item_batch_extended_guid import AssignStockToOrdersResponseOrderItemBatchExtendedGuid
from linnworks_api.generated.openorders.models.batch_action_result_int32_int32 import BatchActionResultInt32Int32
from linnworks_api.generated.openorders.models.batch_action_result_order_item_batch_extended_guid import BatchActionResultOrderItemBatchExtendedGuid
from linnworks_api.generated.openorders.models.change_order_identifier_request import ChangeOrderIdentifierRequest
from linnworks_api.generated.openorders.models.clear_stock_assignment_request import ClearStockAssignmentRequest
from linnworks_api.generated.openorders.models.customer_address import CustomerAddress
from linnworks_api.generated.openorders.models.delete_identifiers_request import DeleteIdentifiersRequest
from linnworks_api.generated.openorders.models.extended_property import ExtendedProperty
from linnworks_api.generated.openorders.models.generic_order_operation_result import GenericOrderOperationResult
from linnworks_api.generated.openorders.models.generic_paged_result_guid import GenericPagedResultGuid
from linnworks_api.generated.openorders.models.get_available_channels_response import GetAvailableChannelsResponse
from linnworks_api.generated.openorders.models.get_open_orders_details_request import GetOpenOrdersDetailsRequest
from linnworks_api.generated.openorders.models.get_open_orders_details_response import GetOpenOrdersDetailsResponse
from linnworks_api.generated.openorders.models.get_open_orders_request import GetOpenOrdersRequest
from linnworks_api.generated.openorders.models.get_order_identifier_request import GetOrderIdentifierRequest
from linnworks_api.generated.openorders.models.get_order_item_indicator_request import GetOrderItemIndicatorRequest
from linnworks_api.generated.openorders.models.get_order_item_indicator_response import GetOrderItemIndicatorResponse
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_request import GetOrdersLowFidelityRequest
from linnworks_api.generated.openorders.models.get_orders_low_fidelity_response import GetOrdersLowFidelityResponse
from linnworks_api.generated.openorders.models.get_view_stats_request import GetViewStatsRequest
from linnworks_api.generated.openorders.models.identifier import Identifier
from linnworks_api.generated.openorders.models.indicator_request import IndicatorRequest
from linnworks_api.generated.openorders.models.mark_ready_for_collection_request import MarkReadyForCollectionRequest
from linnworks_api.generated.openorders.models.open_order import OpenOrder
from linnworks_api.generated.openorders.models.open_order_item import OpenOrderItem
from linnworks_api.generated.openorders.models.open_order_low_fidelity import OpenOrderLowFidelity
from linnworks_api.generated.openorders.models.order_customer_info import OrderCustomerInfo
from linnworks_api.generated.openorders.models.order_details import OrderDetails
from linnworks_api.generated.openorders.models.order_fulfillment_state import OrderFulfillmentState
from linnworks_api.generated.openorders.models.order_general_info import OrderGeneralInfo
from linnworks_api.generated.openorders.models.order_identifier import OrderIdentifier
from linnworks_api.generated.openorders.models.order_item import OrderItem
from linnworks_api.generated.openorders.models.order_item_base import OrderItemBase
from linnworks_api.generated.openorders.models.order_item_batch import OrderItemBatch
from linnworks_api.generated.openorders.models.order_item_batch_extended import OrderItemBatchExtended
from linnworks_api.generated.openorders.models.order_item_bin_rack import OrderItemBinRack
from linnworks_api.generated.openorders.models.order_item_indicator import OrderItemIndicator
from linnworks_api.generated.openorders.models.order_item_on_order import OrderItemOnOrder
from linnworks_api.generated.openorders.models.order_item_option import OrderItemOption
from linnworks_api.generated.openorders.models.order_note import OrderNote
from linnworks_api.generated.openorders.models.order_shipping_info import OrderShippingInfo
from linnworks_api.generated.openorders.models.order_tax_info import OrderTaxInfo
from linnworks_api.generated.openorders.models.order_totals_info import OrderTotalsInfo
from linnworks_api.generated.openorders.models.order_view_ids import OrderViewIds
from linnworks_api.generated.openorders.models.order_view_stats import OrderViewStats
from linnworks_api.generated.openorders.models.order_view_user_preference import OrderViewUserPreference
from linnworks_api.generated.openorders.models.post_filter_paged_response_open_order import PostFilterPagedResponseOpenOrder
from linnworks_api.generated.openorders.models.product_identifier import ProductIdentifier
from linnworks_api.generated.openorders.models.save_identifiers_request import SaveIdentifiersRequest
from linnworks_api.generated.openorders.models.scheduled_delivery import ScheduledDelivery
from linnworks_api.generated.openorders.models.search_orders_request import SearchOrdersRequest
from linnworks_api.generated.openorders.models.search_orders_response import SearchOrdersResponse
from linnworks_api.generated.openorders.models.service_information import ServiceInformation
from linnworks_api.generated.openorders.models.stock_item_batch import StockItemBatch
from linnworks_api.generated.openorders.models.stock_item_batch_inventory import StockItemBatchInventory
from linnworks_api.generated.openorders.models.stock_item_box_configuration import StockItemBoxConfiguration
from linnworks_api.generated.openorders.models.view_group import ViewGroup
from linnworks_api.generated.openorders.models.view_user import ViewUser
from linnworks_api.generated.openorders.models.view_user_management import ViewUserManagement
