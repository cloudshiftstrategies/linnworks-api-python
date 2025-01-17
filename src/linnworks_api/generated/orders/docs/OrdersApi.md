# linnworks_api.generated.orders.OrdersApi

All URIs are relative to *https://eu-ext.linnworks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_coupon**](OrdersApi.md#add_coupon) | **POST** /api/Orders/AddCoupon | AddCoupon
[**add_extended_properties**](OrdersApi.md#add_extended_properties) | **POST** /api/Orders/AddExtendedProperties | AddExtendedProperties
[**add_order_item**](OrdersApi.md#add_order_item) | **POST** /api/Orders/AddOrderItem | AddOrderItem
[**add_order_service**](OrdersApi.md#add_order_service) | **POST** /api/Orders/AddOrderService | AddOrderService
[**assign_order_item_batches**](OrdersApi.md#assign_order_item_batches) | **POST** /api/Orders/AssignOrderItemBatches | AssignOrderItemBatches
[**assign_stock_to_order**](OrdersApi.md#assign_stock_to_order) | **POST** /api/Orders/AssignStockToOrder | AssignStockToOrder
[**assign_to_folder**](OrdersApi.md#assign_to_folder) | **POST** /api/Orders/AssignToFolder | AssignToFolder
[**cancel_order**](OrdersApi.md#cancel_order) | **POST** /api/Orders/CancelOrder | CancelOrder
[**change_order_tag**](OrdersApi.md#change_order_tag) | **POST** /api/Orders/ChangeOrderTag | ChangeOrderTag
[**change_shipping_method**](OrdersApi.md#change_shipping_method) | **POST** /api/Orders/ChangeShippingMethod | ChangeShippingMethod
[**change_status**](OrdersApi.md#change_status) | **POST** /api/Orders/ChangeStatus | ChangeStatus
[**clear_invoice_printed**](OrdersApi.md#clear_invoice_printed) | **POST** /api/Orders/ClearInvoicePrinted | ClearInvoicePrinted
[**clear_pick_list_printed**](OrdersApi.md#clear_pick_list_printed) | **POST** /api/Orders/ClearPickListPrinted | ClearPickListPrinted
[**clear_shipping_label_info**](OrdersApi.md#clear_shipping_label_info) | **POST** /api/Orders/ClearShippingLabelInfo | ClearShippingLabelInfo
[**complete_order**](OrdersApi.md#complete_order) | **POST** /api/Orders/CompleteOrder | CompleteOrder
[**create_new_item_and_link**](OrdersApi.md#create_new_item_and_link) | **POST** /api/Orders/CreateNewItemAndLink | CreateNewItemAndLink
[**create_new_order**](OrdersApi.md#create_new_order) | **POST** /api/Orders/CreateNewOrder | CreateNewOrder
[**create_orders**](OrdersApi.md#create_orders) | **POST** /api/Orders/CreateOrders | CreateOrders
[**create_serialised_values_for_order_items**](OrdersApi.md#create_serialised_values_for_order_items) | **POST** /api/Orders/CreateSerialisedValuesForOrderItems | CreateSerialisedValuesForOrderItems
[**customer_look_up**](OrdersApi.md#customer_look_up) | **GET** /api/Orders/CustomerLookUp | CustomerLookUp
[**delete_order**](OrdersApi.md#delete_order) | **POST** /api/Orders/DeleteOrder | DeleteOrder
[**get_all_available_order_item_batchs_by_order_id**](OrdersApi.md#get_all_available_order_item_batchs_by_order_id) | **POST** /api/Orders/GetAllAvailableOrderItemBatchsByOrderId | GetAllAvailableOrderItemBatchsByOrderId
[**get_all_open_orders**](OrdersApi.md#get_all_open_orders) | **POST** /api/Orders/GetAllOpenOrders | GetAllOpenOrders
[**get_all_open_orders_between_index**](OrdersApi.md#get_all_open_orders_between_index) | **POST** /api/Orders/GetAllOpenOrdersBetweenIndex | GetAllOpenOrdersBetweenIndex
[**get_assigned_order_item_batches**](OrdersApi.md#get_assigned_order_item_batches) | **POST** /api/Orders/GetAssignedOrderItemBatches | GetAssignedOrderItemBatches
[**get_available_folders**](OrdersApi.md#get_available_folders) | **GET** /api/Orders/GetAvailableFolders | GetAvailableFolders
[**get_batch_pilots**](OrdersApi.md#get_batch_pilots) | **GET** /api/Orders/GetBatchPilots | GetBatchPilots
[**get_countries**](OrdersApi.md#get_countries) | **GET** /api/Orders/GetCountries | GetCountries
[**get_default_payment_method_id_for_new_order**](OrdersApi.md#get_default_payment_method_id_for_new_order) | **GET** /api/Orders/GetDefaultPaymentMethodIdForNewOrder | GetDefaultPaymentMethodIdForNewOrder
[**get_draft_orders**](OrdersApi.md#get_draft_orders) | **GET** /api/Orders/GetDraftOrders | GetDraftOrders
[**get_extended_properties**](OrdersApi.md#get_extended_properties) | **GET** /api/Orders/GetExtendedProperties | GetExtendedProperties
[**get_extended_property_names**](OrdersApi.md#get_extended_property_names) | **GET** /api/Orders/GetExtendedPropertyNames | GetExtendedPropertyNames
[**get_extended_property_types**](OrdersApi.md#get_extended_property_types) | **GET** /api/Orders/GetExtendedPropertyTypes | GetExtendedPropertyTypes
[**get_linked_items**](OrdersApi.md#get_linked_items) | **GET** /api/Orders/GetLinkedItems | GetLinkedItems
[**get_open_order_id_by_order_or_reference_id**](OrdersApi.md#get_open_order_id_by_order_or_reference_id) | **POST** /api/Orders/GetOpenOrderIdByOrderOrReferenceId | GetOpenOrderIdByOrderOrReferenceId
[**get_open_order_items_suppliers**](OrdersApi.md#get_open_order_items_suppliers) | **GET** /api/Orders/GetOpenOrderItemsSuppliers | GetOpenOrderItemsSuppliers
[**get_open_orders**](OrdersApi.md#get_open_orders) | **POST** /api/Orders/GetOpenOrders | GetOpenOrders
[**get_open_orders_by_item_barcode**](OrdersApi.md#get_open_orders_by_item_barcode) | **POST** /api/Orders/GetOpenOrdersByItemBarcode | GetOpenOrdersByItemBarcode
[**get_order**](OrdersApi.md#get_order) | **POST** /api/Orders/GetOrder | GetOrder
[**get_order_audit_trail**](OrdersApi.md#get_order_audit_trail) | **GET** /api/Orders/GetOrderAuditTrail | GetOrderAuditTrail
[**get_order_audit_trails_by_ids**](OrdersApi.md#get_order_audit_trails_by_ids) | **POST** /api/Orders/GetOrderAuditTrailsByIds | GetOrderAuditTrailsByIds
[**get_order_by_id**](OrdersApi.md#get_order_by_id) | **GET** /api/Orders/GetOrderById | GetOrderById
[**get_order_details_by_num_order_id**](OrdersApi.md#get_order_details_by_num_order_id) | **GET** /api/Orders/GetOrderDetailsByNumOrderId | GetOrderDetailsByNumOrderId
[**get_order_details_by_reference_id**](OrdersApi.md#get_order_details_by_reference_id) | **GET** /api/Orders/GetOrderDetailsByReferenceId | GetOrderDetailsByReferenceId
[**get_order_item_batches_by_order_ids**](OrdersApi.md#get_order_item_batches_by_order_ids) | **POST** /api/Orders/GetOrderItemBatchesByOrderIds | GetOrderItemBatchesByOrderIds
[**get_order_item_batchs_by_order_id**](OrdersApi.md#get_order_item_batchs_by_order_id) | **POST** /api/Orders/GetOrderItemBatchsByOrderId | GetOrderItemBatchsByOrderId
[**get_order_item_composition**](OrdersApi.md#get_order_item_composition) | **GET** /api/Orders/GetOrderItemComposition | GetOrderItemComposition
[**get_order_item_row_serial_values_by_order_ids**](OrdersApi.md#get_order_item_row_serial_values_by_order_ids) | **POST** /api/Orders/GetOrderItemRowSerialValuesByOrderIds | GetOrderItemRowSerialValuesByOrderIds
[**get_order_items**](OrdersApi.md#get_order_items) | **GET** /api/Orders/GetOrderItems | GetOrderItems
[**get_order_note_types**](OrdersApi.md#get_order_note_types) | **GET** /api/Orders/GetOrderNoteTypes | GetOrderNoteTypes
[**get_order_notes**](OrdersApi.md#get_order_notes) | **GET** /api/Orders/GetOrderNotes | GetOrderNotes
[**get_order_packaging_calculation**](OrdersApi.md#get_order_packaging_calculation) | **POST** /api/Orders/GetOrderPackagingCalculation | GetOrderPackagingCalculation
[**get_order_packaging_split**](OrdersApi.md#get_order_packaging_split) | **GET** /api/Orders/GetOrderPackagingSplit | GetOrderPackagingSplit
[**get_order_relations**](OrdersApi.md#get_order_relations) | **GET** /api/Orders/GetOrderRelations | GetOrderRelations
[**get_order_view**](OrdersApi.md#get_order_view) | **GET** /api/Orders/GetOrderView | GetOrderView
[**get_order_views**](OrdersApi.md#get_order_views) | **GET** /api/Orders/GetOrderViews | GetOrderViews
[**get_order_xml**](OrdersApi.md#get_order_xml) | **GET** /api/Orders/GetOrderXml | GetOrderXml
[**get_order_xml_js_tree**](OrdersApi.md#get_order_xml_js_tree) | **GET** /api/Orders/GetOrderXmlJSTree | GetOrderXmlJSTree
[**get_orders**](OrdersApi.md#get_orders) | **POST** /api/Orders/GetOrders | GetOrders
[**get_orders_by_id**](OrdersApi.md#get_orders_by_id) | **POST** /api/Orders/GetOrdersById | GetOrdersById
[**get_orders_notes**](OrdersApi.md#get_orders_notes) | **POST** /api/Orders/GetOrdersNotes | GetOrdersNotes
[**get_orders_relations**](OrdersApi.md#get_orders_relations) | **POST** /api/Orders/GetOrdersRelations | GetOrdersRelations
[**get_packaging_groups**](OrdersApi.md#get_packaging_groups) | **GET** /api/Orders/GetPackagingGroups | GetPackagingGroups
[**get_payment_methods**](OrdersApi.md#get_payment_methods) | **GET** /api/Orders/GetPaymentMethods | GetPaymentMethods
[**get_shipping_methods**](OrdersApi.md#get_shipping_methods) | **GET** /api/Orders/GetShippingMethods | GetShippingMethods
[**get_user_location_id**](OrdersApi.md#get_user_location_id) | **GET** /api/Orders/GetUserLocationId | GetUserLocationId
[**lock_order**](OrdersApi.md#lock_order) | **POST** /api/Orders/LockOrder | LockOrder
[**merge_orders**](OrdersApi.md#merge_orders) | **POST** /api/Orders/MergeOrders | MergeOrders
[**move_to_location**](OrdersApi.md#move_to_location) | **POST** /api/Orders/MoveToLocation | MoveToLocation
[**process_fulfilment_centre_order**](OrdersApi.md#process_fulfilment_centre_order) | **POST** /api/Orders/ProcessFulfilmentCentreOrder | ProcessFulfilmentCentreOrder
[**process_order**](OrdersApi.md#process_order) | **POST** /api/Orders/ProcessOrder | ProcessOrder
[**process_order_by_order_or_reference_id**](OrdersApi.md#process_order_by_order_or_reference_id) | **POST** /api/Orders/ProcessOrderByOrderOrReferenceId | ProcessOrderByOrderOrReferenceId
[**process_order_required_batch_scans**](OrdersApi.md#process_order_required_batch_scans) | **POST** /api/Orders/ProcessOrder_RequiredBatchScans | ProcessOrder_RequiredBatchScans
[**process_orders_in_batch**](OrdersApi.md#process_orders_in_batch) | **POST** /api/Orders/ProcessOrdersInBatch | ProcessOrdersInBatch
[**recalculate_single_order_packaging**](OrdersApi.md#recalculate_single_order_packaging) | **POST** /api/Orders/RecalculateSingleOrderPackaging | RecalculateSingleOrderPackaging
[**remove_order_item**](OrdersApi.md#remove_order_item) | **POST** /api/Orders/RemoveOrderItem | RemoveOrderItem
[**run_rules_engine**](OrdersApi.md#run_rules_engine) | **POST** /api/Orders/RunRulesEngine | RunRulesEngine
[**save_order_view**](OrdersApi.md#save_order_view) | **POST** /api/Orders/SaveOrderView | SaveOrderView
[**set_additional_info**](OrdersApi.md#set_additional_info) | **POST** /api/Orders/SetAdditionalInfo | SetAdditionalInfo
[**set_available_folders**](OrdersApi.md#set_available_folders) | **POST** /api/Orders/SetAvailableFolders | SetAvailableFolders
[**set_default_payment_method_id_for_new_order**](OrdersApi.md#set_default_payment_method_id_for_new_order) | **POST** /api/Orders/SetDefaultPaymentMethodIdForNewOrder | SetDefaultPaymentMethodIdForNewOrder
[**set_extended_properties**](OrdersApi.md#set_extended_properties) | **POST** /api/Orders/SetExtendedProperties | SetExtendedProperties
[**set_invoices_printed**](OrdersApi.md#set_invoices_printed) | **POST** /api/Orders/SetInvoicesPrinted | SetInvoicesPrinted
[**set_labels_printed**](OrdersApi.md#set_labels_printed) | **POST** /api/Orders/SetLabelsPrinted | SetLabelsPrinted
[**set_order_customer_info**](OrdersApi.md#set_order_customer_info) | **POST** /api/Orders/SetOrderCustomerInfo | SetOrderCustomerInfo
[**set_order_general_info**](OrdersApi.md#set_order_general_info) | **POST** /api/Orders/SetOrderGeneralInfo | SetOrderGeneralInfo
[**set_order_notes**](OrdersApi.md#set_order_notes) | **POST** /api/Orders/SetOrderNotes | SetOrderNotes
[**set_order_packaging**](OrdersApi.md#set_order_packaging) | **POST** /api/Orders/SetOrderPackaging | SetOrderPackaging
[**set_order_packaging_split**](OrdersApi.md#set_order_packaging_split) | **POST** /api/Orders/SetOrderPackagingSplit | SetOrderPackagingSplit
[**set_order_shipping_info**](OrdersApi.md#set_order_shipping_info) | **POST** /api/Orders/SetOrderShippingInfo | SetOrderShippingInfo
[**set_order_split_packaging_manual_overwrite**](OrdersApi.md#set_order_split_packaging_manual_overwrite) | **POST** /api/Orders/SetOrderSplitPackagingManualOverwrite | SetOrderSplitPackagingManualOverwrite
[**set_order_totals_info**](OrdersApi.md#set_order_totals_info) | **POST** /api/Orders/SetOrderTotalsInfo | SetOrderTotalsInfo
[**set_payment_methods**](OrdersApi.md#set_payment_methods) | **POST** /api/Orders/SetPaymentMethods | SetPaymentMethods
[**set_pick_list_printed**](OrdersApi.md#set_pick_list_printed) | **POST** /api/Orders/SetPickListPrinted | SetPickListPrinted
[**split_order**](OrdersApi.md#split_order) | **POST** /api/Orders/SplitOrder | SplitOrder
[**unassign_to_folder**](OrdersApi.md#unassign_to_folder) | **POST** /api/Orders/UnassignToFolder | UnassignToFolder
[**update_additional_info**](OrdersApi.md#update_additional_info) | **POST** /api/Orders/UpdateAdditionalInfo | UpdateAdditionalInfo
[**update_billing_address**](OrdersApi.md#update_billing_address) | **POST** /api/Orders/UpdateBillingAddress | UpdateBillingAddress
[**update_link_item**](OrdersApi.md#update_link_item) | **POST** /api/Orders/UpdateLinkItem | UpdateLinkItem
[**update_order_item**](OrdersApi.md#update_order_item) | **POST** /api/Orders/UpdateOrderItem | UpdateOrderItem
[**validate_coupon**](OrdersApi.md#validate_coupon) | **POST** /api/Orders/ValidateCoupon | ValidateCoupon


# **add_coupon**
> UpdateOrderItemResult add_coupon(orders_add_coupon_request)

AddCoupon

Add a coupon to a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_add_coupon_request import OrdersAddCouponRequest
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_add_coupon_request = linnworks_api.generated.orders.OrdersAddCouponRequest() # OrdersAddCouponRequest | 

    try:
        # AddCoupon
        api_response = api_instance.add_coupon(orders_add_coupon_request)
        print("The response of OrdersApi->add_coupon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_coupon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_add_coupon_request** | [**OrdersAddCouponRequest**](OrdersAddCouponRequest.md)|  | 

### Return type

[**UpdateOrderItemResult**](UpdateOrderItemResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_extended_properties**
> AddExtendedPropertiesResponse add_extended_properties(orders_add_extended_properties_request)

AddExtendedProperties

Adds extended properties to a Linnworks orders.  This will NOT update properties that match on property name / value <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.add_extended_properties_response import AddExtendedPropertiesResponse
from linnworks_api.generated.orders.models.orders_add_extended_properties_request import OrdersAddExtendedPropertiesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_add_extended_properties_request = linnworks_api.generated.orders.OrdersAddExtendedPropertiesRequest() # OrdersAddExtendedPropertiesRequest | 

    try:
        # AddExtendedProperties
        api_response = api_instance.add_extended_properties(orders_add_extended_properties_request)
        print("The response of OrdersApi->add_extended_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_extended_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_add_extended_properties_request** | [**OrdersAddExtendedPropertiesRequest**](OrdersAddExtendedPropertiesRequest.md)|  | 

### Return type

[**AddExtendedPropertiesResponse**](AddExtendedPropertiesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_item**
> UpdateOrderItemResult add_order_item(orders_add_order_item_request)

AddOrderItem

Add an item to a specific order.  Line pricing is optional with the default values being  - PricePerUnit: Stock item retail price  - DiscountPercentage: 0  - TaxRatePercentage: Stock item tax rate.  - TaxInclusive: true <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_add_order_item_request import OrdersAddOrderItemRequest
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_add_order_item_request = linnworks_api.generated.orders.OrdersAddOrderItemRequest() # OrdersAddOrderItemRequest | 

    try:
        # AddOrderItem
        api_response = api_instance.add_order_item(orders_add_order_item_request)
        print("The response of OrdersApi->add_order_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_order_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_add_order_item_request** | [**OrdersAddOrderItemRequest**](OrdersAddOrderItemRequest.md)|  | 

### Return type

[**UpdateOrderItemResult**](UpdateOrderItemResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_order_service**
> UpdateOrderItemResult add_order_service(request=request)

AddOrderService

Add a service to an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_add_order_service_request import OrdersAddOrderServiceRequest
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.OrdersAddOrderServiceRequest() # OrdersAddOrderServiceRequest |  (optional)

    try:
        # AddOrderService
        api_response = api_instance.add_order_service(request=request)
        print("The response of OrdersApi->add_order_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_order_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**OrdersAddOrderServiceRequest**](OrdersAddOrderServiceRequest.md)|  | [optional] 

### Return type

[**UpdateOrderItemResult**](UpdateOrderItemResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_order_item_batches**
> assign_order_item_batches(orders_assign_order_item_batches_request)

AssignOrderItemBatches

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_assign_order_item_batches_request import OrdersAssignOrderItemBatchesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_assign_order_item_batches_request = linnworks_api.generated.orders.OrdersAssignOrderItemBatchesRequest() # OrdersAssignOrderItemBatchesRequest | 

    try:
        # AssignOrderItemBatches
        api_instance.assign_order_item_batches(orders_assign_order_item_batches_request)
    except Exception as e:
        print("Exception when calling OrdersApi->assign_order_item_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_assign_order_item_batches_request** | [**OrdersAssignOrderItemBatchesRequest**](OrdersAssignOrderItemBatchesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_stock_to_order**
> List[OrderItemBatch] assign_stock_to_order(orders_assign_stock_to_order_request)

AssignStockToOrder

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_item_batch import OrderItemBatch
from linnworks_api.generated.orders.models.orders_assign_stock_to_order_request import OrdersAssignStockToOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_assign_stock_to_order_request = linnworks_api.generated.orders.OrdersAssignStockToOrderRequest() # OrdersAssignStockToOrderRequest | 

    try:
        # AssignStockToOrder
        api_response = api_instance.assign_stock_to_order(orders_assign_stock_to_order_request)
        print("The response of OrdersApi->assign_stock_to_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->assign_stock_to_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_assign_stock_to_order_request** | [**OrdersAssignStockToOrderRequest**](OrdersAssignStockToOrderRequest.md)|  | 

### Return type

[**List[OrderItemBatch]**](OrderItemBatch.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_to_folder**
> List[str] assign_to_folder(orders_assign_to_folder_request)

AssignToFolder

Assign a list of orders to a specific folder. This operation can not be executed on locked or parked orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_assign_to_folder_request import OrdersAssignToFolderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_assign_to_folder_request = linnworks_api.generated.orders.OrdersAssignToFolderRequest() # OrdersAssignToFolderRequest | 

    try:
        # AssignToFolder
        api_response = api_instance.assign_to_folder(orders_assign_to_folder_request)
        print("The response of OrdersApi->assign_to_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->assign_to_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_assign_to_folder_request** | [**OrdersAssignToFolderRequest**](OrdersAssignToFolderRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> str cancel_order(orders_cancel_order_request)

CancelOrder

Cancel a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_cancel_order_request import OrdersCancelOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_cancel_order_request = linnworks_api.generated.orders.OrdersCancelOrderRequest() # OrdersCancelOrderRequest | 

    try:
        # CancelOrder
        api_response = api_instance.cancel_order(orders_cancel_order_request)
        print("The response of OrdersApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_cancel_order_request** | [**OrdersCancelOrderRequest**](OrdersCancelOrderRequest.md)|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_order_tag**
> List[str] change_order_tag(orders_change_order_tag_request)

ChangeOrderTag

Change the tag for the specific order list. Tags can be 1-6 for custom tags, or 7 to initialize a 'parked' status on the order. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_change_order_tag_request import OrdersChangeOrderTagRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_change_order_tag_request = linnworks_api.generated.orders.OrdersChangeOrderTagRequest() # OrdersChangeOrderTagRequest | 

    try:
        # ChangeOrderTag
        api_response = api_instance.change_order_tag(orders_change_order_tag_request)
        print("The response of OrdersApi->change_order_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->change_order_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_change_order_tag_request** | [**OrdersChangeOrderTagRequest**](OrdersChangeOrderTagRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_shipping_method**
> List[str] change_shipping_method(orders_change_shipping_method_request)

ChangeShippingMethod

Change the shipping method to a list of orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_change_shipping_method_request import OrdersChangeShippingMethodRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_change_shipping_method_request = linnworks_api.generated.orders.OrdersChangeShippingMethodRequest() # OrdersChangeShippingMethodRequest | 

    try:
        # ChangeShippingMethod
        api_response = api_instance.change_shipping_method(orders_change_shipping_method_request)
        print("The response of OrdersApi->change_shipping_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->change_shipping_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_change_shipping_method_request** | [**OrdersChangeShippingMethodRequest**](OrdersChangeShippingMethodRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_status**
> List[str] change_status(orders_change_status_request)

ChangeStatus

Change the status to a list of orders  0 = 'UNPAID'  1 = 'PAID'  2 = 'RETURN'  3 = 'PENDING'  4 = 'RESEND' <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_change_status_request import OrdersChangeStatusRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_change_status_request = linnworks_api.generated.orders.OrdersChangeStatusRequest() # OrdersChangeStatusRequest | 

    try:
        # ChangeStatus
        api_response = api_instance.change_status(orders_change_status_request)
        print("The response of OrdersApi->change_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->change_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_change_status_request** | [**OrdersChangeStatusRequest**](OrdersChangeStatusRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_invoice_printed**
> List[str] clear_invoice_printed(orders_clear_invoice_printed_request)

ClearInvoicePrinted

Clear invoice printed flag for a list of orders. This operation can not be executed on locked or parked orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_clear_invoice_printed_request import OrdersClearInvoicePrintedRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_clear_invoice_printed_request = linnworks_api.generated.orders.OrdersClearInvoicePrintedRequest() # OrdersClearInvoicePrintedRequest | 

    try:
        # ClearInvoicePrinted
        api_response = api_instance.clear_invoice_printed(orders_clear_invoice_printed_request)
        print("The response of OrdersApi->clear_invoice_printed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->clear_invoice_printed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_clear_invoice_printed_request** | [**OrdersClearInvoicePrintedRequest**](OrdersClearInvoicePrintedRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_pick_list_printed**
> List[str] clear_pick_list_printed(orders_clear_pick_list_printed_request)

ClearPickListPrinted

Clear invoice printed flag for a list of orders. This operation can not be executed on locked or parked orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_clear_pick_list_printed_request import OrdersClearPickListPrintedRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_clear_pick_list_printed_request = linnworks_api.generated.orders.OrdersClearPickListPrintedRequest() # OrdersClearPickListPrintedRequest | 

    try:
        # ClearPickListPrinted
        api_response = api_instance.clear_pick_list_printed(orders_clear_pick_list_printed_request)
        print("The response of OrdersApi->clear_pick_list_printed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->clear_pick_list_printed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_clear_pick_list_printed_request** | [**OrdersClearPickListPrintedRequest**](OrdersClearPickListPrintedRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_shipping_label_info**
> List[KeyValuePairGuidString] clear_shipping_label_info(orders_clear_shipping_label_info_request)

ClearShippingLabelInfo

Clear the shipping label info to a list of orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.key_value_pair_guid_string import KeyValuePairGuidString
from linnworks_api.generated.orders.models.orders_clear_shipping_label_info_request import OrdersClearShippingLabelInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_clear_shipping_label_info_request = linnworks_api.generated.orders.OrdersClearShippingLabelInfoRequest() # OrdersClearShippingLabelInfoRequest | 

    try:
        # ClearShippingLabelInfo
        api_response = api_instance.clear_shipping_label_info(orders_clear_shipping_label_info_request)
        print("The response of OrdersApi->clear_shipping_label_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->clear_shipping_label_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_clear_shipping_label_info_request** | [**OrdersClearShippingLabelInfoRequest**](OrdersClearShippingLabelInfoRequest.md)|  | 

### Return type

[**List[KeyValuePairGuidString]**](KeyValuePairGuidString.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_order**
> str complete_order(orders_complete_order_request)

CompleteOrder

Complete a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_complete_order_request import OrdersCompleteOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_complete_order_request = linnworks_api.generated.orders.OrdersCompleteOrderRequest() # OrdersCompleteOrderRequest | 

    try:
        # CompleteOrder
        api_response = api_instance.complete_order(orders_complete_order_request)
        print("The response of OrdersApi->complete_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->complete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_complete_order_request** | [**OrdersCompleteOrderRequest**](OrdersCompleteOrderRequest.md)|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_item_and_link**
> str create_new_item_and_link(orders_create_new_item_and_link_request)

CreateNewItemAndLink

Create a new item and link it to a specific stock item <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_create_new_item_and_link_request import OrdersCreateNewItemAndLinkRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_create_new_item_and_link_request = linnworks_api.generated.orders.OrdersCreateNewItemAndLinkRequest() # OrdersCreateNewItemAndLinkRequest | 

    try:
        # CreateNewItemAndLink
        api_response = api_instance.create_new_item_and_link(orders_create_new_item_and_link_request)
        print("The response of OrdersApi->create_new_item_and_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_new_item_and_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_create_new_item_and_link_request** | [**OrdersCreateNewItemAndLinkRequest**](OrdersCreateNewItemAndLinkRequest.md)|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_order**
> OpenOrder create_new_order(orders_create_new_order_request)

CreateNewOrder

Create an empty draft order. (Please see CreateOrders call) <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.CreateOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.open_order import OpenOrder
from linnworks_api.generated.orders.models.orders_create_new_order_request import OrdersCreateNewOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_create_new_order_request = linnworks_api.generated.orders.OrdersCreateNewOrderRequest() # OrdersCreateNewOrderRequest | 

    try:
        # CreateNewOrder
        api_response = api_instance.create_new_order(orders_create_new_order_request)
        print("The response of OrdersApi->create_new_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_create_new_order_request** | [**OrdersCreateNewOrderRequest**](OrdersCreateNewOrderRequest.md)|  | 

### Return type

[**OpenOrder**](OpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_orders**
> List[str] create_orders(orders_create_orders_request)

CreateOrders

Creates new orders, once an order is paid it will be skipped on save. Returns list of pkOrderId's that were saved. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_create_orders_request import OrdersCreateOrdersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_create_orders_request = linnworks_api.generated.orders.OrdersCreateOrdersRequest() # OrdersCreateOrdersRequest | 

    try:
        # CreateOrders
        api_response = api_instance.create_orders(orders_create_orders_request)
        print("The response of OrdersApi->create_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_create_orders_request** | [**OrdersCreateOrdersRequest**](OrdersCreateOrdersRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_serialised_values_for_order_items**
> create_serialised_values_for_order_items(request=request)

CreateSerialisedValuesForOrderItems

Create serial data for the given orderItemRowIds <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.create_serialised_values_for_order_items_request import CreateSerialisedValuesForOrderItemsRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.CreateSerialisedValuesForOrderItemsRequest() # CreateSerialisedValuesForOrderItemsRequest | Request with list of OrderItemSerialModel as property. Each entry represents an OrderItemRowId and a list of collections of serial data. Seperated by correlation (quantity for this row)               Note there can be one collection of serial data for each physical item being shipped - e.g. an order item with quantity of 2 can have 2 collections of serial data (optional)

    try:
        # CreateSerialisedValuesForOrderItems
        api_instance.create_serialised_values_for_order_items(request=request)
    except Exception as e:
        print("Exception when calling OrdersApi->create_serialised_values_for_order_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSerialisedValuesForOrderItemsRequest**](CreateSerialisedValuesForOrderItemsRequest.md)| Request with list of OrderItemSerialModel as property. Each entry represents an OrderItemRowId and a list of collections of serial data. Seperated by correlation (quantity for this row)               Note there can be one collection of serial data for each physical item being shipped - e.g. an order item with quantity of 2 can have 2 collections of serial data | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_look_up**
> List[CustomerAddress] customer_look_up(var_field=var_field, txt=txt)

CustomerLookUp

Get a list of possible addresses based on a search <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.customer_address import CustomerAddress
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    var_field = 'var_field_example' # str | Field to search by (optional)
    txt = 'txt_example' # str | Text to find (optional)

    try:
        # CustomerLookUp
        api_response = api_instance.customer_look_up(var_field=var_field, txt=txt)
        print("The response of OrdersApi->customer_look_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->customer_look_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_field** | **str**| Field to search by | [optional] 
 **txt** | **str**| Text to find | [optional] 

### Return type

[**List[CustomerAddress]**](CustomerAddress.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> delete_order(orders_delete_order_request)

DeleteOrder

Delete a specific order <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.DeleteOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_delete_order_request import OrdersDeleteOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_delete_order_request = linnworks_api.generated.orders.OrdersDeleteOrderRequest() # OrdersDeleteOrderRequest | 

    try:
        # DeleteOrder
        api_instance.delete_order(orders_delete_order_request)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_delete_order_request** | [**OrdersDeleteOrderRequest**](OrdersDeleteOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_available_order_item_batchs_by_order_id**
> List[StockItemBatch] get_all_available_order_item_batchs_by_order_id(orders_get_all_available_order_item_batchs_by_order_id_request)

GetAllAvailableOrderItemBatchsByOrderId

Get a list of available batchs for each order item for the specified order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_get_all_available_order_item_batchs_by_order_id_request import OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest
from linnworks_api.generated.orders.models.stock_item_batch import StockItemBatch
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_all_available_order_item_batchs_by_order_id_request = linnworks_api.generated.orders.OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest() # OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest | 

    try:
        # GetAllAvailableOrderItemBatchsByOrderId
        api_response = api_instance.get_all_available_order_item_batchs_by_order_id(orders_get_all_available_order_item_batchs_by_order_id_request)
        print("The response of OrdersApi->get_all_available_order_item_batchs_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_all_available_order_item_batchs_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_all_available_order_item_batchs_by_order_id_request** | [**OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest**](OrdersGetAllAvailableOrderItemBatchsByOrderIdRequest.md)|  | 

### Return type

[**List[StockItemBatch]**](StockItemBatch.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_open_orders**
> List[str] get_all_open_orders(orders_get_all_open_orders_request)

GetAllOpenOrders

Get the list of Id's of all open orders (without pagination) <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_get_all_open_orders_request import OrdersGetAllOpenOrdersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_all_open_orders_request = linnworks_api.generated.orders.OrdersGetAllOpenOrdersRequest() # OrdersGetAllOpenOrdersRequest | 

    try:
        # GetAllOpenOrders
        api_response = api_instance.get_all_open_orders(orders_get_all_open_orders_request)
        print("The response of OrdersApi->get_all_open_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_all_open_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_all_open_orders_request** | [**OrdersGetAllOpenOrdersRequest**](OrdersGetAllOpenOrdersRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_open_orders_between_index**
> List[str] get_all_open_orders_between_index(orders_get_all_open_orders_between_index_request)

GetAllOpenOrdersBetweenIndex

Get the list of open order id's between two index with the current filters and sorting <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_get_all_open_orders_between_index_request import OrdersGetAllOpenOrdersBetweenIndexRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_all_open_orders_between_index_request = linnworks_api.generated.orders.OrdersGetAllOpenOrdersBetweenIndexRequest() # OrdersGetAllOpenOrdersBetweenIndexRequest | 

    try:
        # GetAllOpenOrdersBetweenIndex
        api_response = api_instance.get_all_open_orders_between_index(orders_get_all_open_orders_between_index_request)
        print("The response of OrdersApi->get_all_open_orders_between_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_all_open_orders_between_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_all_open_orders_between_index_request** | [**OrdersGetAllOpenOrdersBetweenIndexRequest**](OrdersGetAllOpenOrdersBetweenIndexRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_order_item_batches**
> List[OrderItemBatch] get_assigned_order_item_batches(orders_get_assigned_order_item_batches_request)

GetAssignedOrderItemBatches

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_item_batch import OrderItemBatch
from linnworks_api.generated.orders.models.orders_get_assigned_order_item_batches_request import OrdersGetAssignedOrderItemBatchesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_assigned_order_item_batches_request = linnworks_api.generated.orders.OrdersGetAssignedOrderItemBatchesRequest() # OrdersGetAssignedOrderItemBatchesRequest | 

    try:
        # GetAssignedOrderItemBatches
        api_response = api_instance.get_assigned_order_item_batches(orders_get_assigned_order_item_batches_request)
        print("The response of OrdersApi->get_assigned_order_item_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_assigned_order_item_batches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_assigned_order_item_batches_request** | [**OrdersGetAssignedOrderItemBatchesRequest**](OrdersGetAssignedOrderItemBatchesRequest.md)|  | 

### Return type

[**List[OrderItemBatch]**](OrderItemBatch.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_folders**
> List[OrderFolder] get_available_folders()

GetAvailableFolders

Get list of available folders that orders can be assigned to <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_folder import OrderFolder
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetAvailableFolders
        api_response = api_instance.get_available_folders()
        print("The response of OrdersApi->get_available_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_available_folders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderFolder]**](OrderFolder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_pilots**
> List[KeyValuePairGuidString] get_batch_pilots()

GetBatchPilots

Get the list of available batch pilots <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.key_value_pair_guid_string import KeyValuePairGuidString
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetBatchPilots
        api_response = api_instance.get_batch_pilots()
        print("The response of OrdersApi->get_batch_pilots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_batch_pilots: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[KeyValuePairGuidString]**](KeyValuePairGuidString.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> List[OrderCountry] get_countries()

GetCountries

Get list of available countries <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_country import OrderCountry
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetCountries
        api_response = api_instance.get_countries()
        print("The response of OrdersApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderCountry]**](OrderCountry.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_payment_method_id_for_new_order**
> str get_default_payment_method_id_for_new_order()

GetDefaultPaymentMethodIdForNewOrder

Get the default payment method for new direct orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetDefaultPaymentMethodIdForNewOrder
        api_response = api_instance.get_default_payment_method_id_for_new_order()
        print("The response of OrdersApi->get_default_payment_method_id_for_new_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_default_payment_method_id_for_new_order: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_orders**
> List[str] get_draft_orders()

GetDraftOrders

Get list of draft orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetDraftOrders
        api_response = api_instance.get_draft_orders()
        print("The response of OrdersApi->get_draft_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_draft_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_properties**
> List[ExtendedProperty] get_extended_properties(order_id=order_id)

GetExtendedProperties

Get the extended properties for a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.extended_property import ExtendedProperty
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetExtendedProperties
        api_response = api_instance.get_extended_properties(order_id=order_id)
        print("The response of OrdersApi->get_extended_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_extended_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[ExtendedProperty]**](ExtendedProperty.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_property_names**
> List[str] get_extended_property_names()

GetExtendedPropertyNames

Get the available types of extended properties <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetExtendedPropertyNames
        api_response = api_instance.get_extended_property_names()
        print("The response of OrdersApi->get_extended_property_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_extended_property_names: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_property_types**
> List[str] get_extended_property_types()

GetExtendedPropertyTypes

Get the available types of extended properties <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetExtendedPropertyTypes
        api_response = api_instance.get_extended_property_types()
        print("The response of OrdersApi->get_extended_property_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_extended_property_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_items**
> List[LinkedItem] get_linked_items(item_id=item_id)

GetLinkedItems

Get linked items to another one <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.linked_item import LinkedItem
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    item_id = 'item_id_example' # str | Item id (pkStockItemId) (optional)

    try:
        # GetLinkedItems
        api_response = api_instance.get_linked_items(item_id=item_id)
        print("The response of OrdersApi->get_linked_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_linked_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Item id (pkStockItemId) | [optional] 

### Return type

[**List[LinkedItem]**](LinkedItem.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_order_id_by_order_or_reference_id**
> str get_open_order_id_by_order_or_reference_id(orders_get_open_order_id_by_order_or_reference_id_request)

GetOpenOrderIdByOrderOrReferenceId

Get an order by reference number or order number <b>Permissions Required: </b> GlobalPermissions.OrderBookNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_get_open_order_id_by_order_or_reference_id_request import OrdersGetOpenOrderIdByOrderOrReferenceIdRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_open_order_id_by_order_or_reference_id_request = linnworks_api.generated.orders.OrdersGetOpenOrderIdByOrderOrReferenceIdRequest() # OrdersGetOpenOrderIdByOrderOrReferenceIdRequest | 

    try:
        # GetOpenOrderIdByOrderOrReferenceId
        api_response = api_instance.get_open_order_id_by_order_or_reference_id(orders_get_open_order_id_by_order_or_reference_id_request)
        print("The response of OrdersApi->get_open_order_id_by_order_or_reference_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_open_order_id_by_order_or_reference_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_open_order_id_by_order_or_reference_id_request** | [**OrdersGetOpenOrderIdByOrderOrReferenceIdRequest**](OrdersGetOpenOrderIdByOrderOrReferenceIdRequest.md)|  | 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_order_items_suppliers**
> List[KeyValuePairGuidGuid] get_open_order_items_suppliers(order_id=order_id)

GetOpenOrderItemsSuppliers

Get items suppliers list for a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.key_value_pair_guid_guid import KeyValuePairGuidGuid
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOpenOrderItemsSuppliers
        api_response = api_instance.get_open_order_items_suppliers(order_id=order_id)
        print("The response of OrdersApi->get_open_order_items_suppliers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_open_order_items_suppliers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[KeyValuePairGuidGuid]**](KeyValuePairGuidGuid.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_orders**
> GenericPagedResultOpenOrder get_open_orders(orders_get_open_orders_request)

GetOpenOrders

Get a paged list of open orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.generic_paged_result_open_order import GenericPagedResultOpenOrder
from linnworks_api.generated.orders.models.orders_get_open_orders_request import OrdersGetOpenOrdersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_open_orders_request = linnworks_api.generated.orders.OrdersGetOpenOrdersRequest() # OrdersGetOpenOrdersRequest | 

    try:
        # GetOpenOrders
        api_response = api_instance.get_open_orders(orders_get_open_orders_request)
        print("The response of OrdersApi->get_open_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_open_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_open_orders_request** | [**OrdersGetOpenOrdersRequest**](OrdersGetOpenOrdersRequest.md)|  | 

### Return type

[**GenericPagedResultOpenOrder**](GenericPagedResultOpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_orders_by_item_barcode**
> KeyValuePairListOrderSummaryString get_open_orders_by_item_barcode(orders_get_open_orders_by_item_barcode_request)

GetOpenOrdersByItemBarcode

Get orders by order item barcode <b>Permissions Required: </b> GlobalPermissions.OrderBookNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.key_value_pair_list_order_summary_string import KeyValuePairListOrderSummaryString
from linnworks_api.generated.orders.models.orders_get_open_orders_by_item_barcode_request import OrdersGetOpenOrdersByItemBarcodeRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_open_orders_by_item_barcode_request = linnworks_api.generated.orders.OrdersGetOpenOrdersByItemBarcodeRequest() # OrdersGetOpenOrdersByItemBarcodeRequest | 

    try:
        # GetOpenOrdersByItemBarcode
        api_response = api_instance.get_open_orders_by_item_barcode(orders_get_open_orders_by_item_barcode_request)
        print("The response of OrdersApi->get_open_orders_by_item_barcode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_open_orders_by_item_barcode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_open_orders_by_item_barcode_request** | [**OrdersGetOpenOrdersByItemBarcodeRequest**](OrdersGetOpenOrdersByItemBarcodeRequest.md)|  | 

### Return type

[**KeyValuePairListOrderSummaryString**](KeyValuePairListOrderSummaryString.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OpenOrder get_order(orders_get_order_request)

GetOrder

Get a specific open order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.open_order import OpenOrder
from linnworks_api.generated.orders.models.orders_get_order_request import OrdersGetOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_order_request = linnworks_api.generated.orders.OrdersGetOrderRequest() # OrdersGetOrderRequest | 

    try:
        # GetOrder
        api_response = api_instance.get_order(orders_get_order_request)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_order_request** | [**OrdersGetOrderRequest**](OrdersGetOrderRequest.md)|  | 

### Return type

[**OpenOrder**](OpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_audit_trail**
> List[OrderAuditTrail] get_order_audit_trail(order_id=order_id)

GetOrderAuditTrail

Get order audit trail <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_audit_trail import OrderAuditTrail
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOrderAuditTrail
        api_response = api_instance.get_order_audit_trail(order_id=order_id)
        print("The response of OrdersApi->get_order_audit_trail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_audit_trail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[OrderAuditTrail]**](OrderAuditTrail.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_audit_trails_by_ids**
> GetOrderAuditTrailsByIdsResponse get_order_audit_trails_by_ids(request=request)

GetOrderAuditTrailsByIds

Returns a list of audit trails for the provided order ids <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.get_order_audit_trails_by_ids_request import GetOrderAuditTrailsByIdsRequest
from linnworks_api.generated.orders.models.get_order_audit_trails_by_ids_response import GetOrderAuditTrailsByIdsResponse
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.GetOrderAuditTrailsByIdsRequest() # GetOrderAuditTrailsByIdsRequest |  (optional)

    try:
        # GetOrderAuditTrailsByIds
        api_response = api_instance.get_order_audit_trails_by_ids(request=request)
        print("The response of OrdersApi->get_order_audit_trails_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_audit_trails_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderAuditTrailsByIdsRequest**](GetOrderAuditTrailsByIdsRequest.md)|  | [optional] 

### Return type

[**GetOrderAuditTrailsByIdsResponse**](GetOrderAuditTrailsByIdsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> OrderDetails get_order_by_id(pk_order_id=pk_order_id)

GetOrderById

Retrieves the order detail for a unique system order id identifier (pkOrderId)  For working with open orders recommended to use OpenOrders/GetOpenOrdersDetails <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_details import OrderDetails
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    pk_order_id = 'pk_order_id_example' # str | pkOrderId (optional)

    try:
        # GetOrderById
        api_response = api_instance.get_order_by_id(pk_order_id=pk_order_id)
        print("The response of OrdersApi->get_order_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_order_id** | **str**| pkOrderId | [optional] 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_details_by_num_order_id**
> OrderDetails get_order_details_by_num_order_id(order_id=order_id)

GetOrderDetailsByNumOrderId

Retrieves the order detail for a given order numeric id. If not found  empty class is returned.    For working with open orders recommended to use OpenOrders/GetOpenOrdersDetails <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_details import OrderDetails
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 56 # int | Order Id (numeric) (optional)

    try:
        # GetOrderDetailsByNumOrderId
        api_response = api_instance.get_order_details_by_num_order_id(order_id=order_id)
        print("The response of OrdersApi->get_order_details_by_num_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_details_by_num_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order Id (numeric) | [optional] 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_details_by_reference_id**
> List[OrderDetails] get_order_details_by_reference_id(reference_id=reference_id)

GetOrderDetailsByReferenceId

Retrieves a list of order details for a given order reference number, returns maximum of 50 orders.  For eBay orders, if Sellling Manager Pro sales number is available the order can be retrived by this number <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_details import OrderDetails
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    reference_id = 'reference_id_example' # str | Order reference id, or SecondaryReferenceNumber (optional)

    try:
        # GetOrderDetailsByReferenceId
        api_response = api_instance.get_order_details_by_reference_id(reference_id=reference_id)
        print("The response of OrdersApi->get_order_details_by_reference_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_details_by_reference_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_id** | **str**| Order reference id, or SecondaryReferenceNumber | [optional] 

### Return type

[**List[OrderDetails]**](OrderDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_batches_by_order_ids**
> GetOrderItemBatchesByOrderIdsResponse get_order_item_batches_by_order_ids(request=request)

GetOrderItemBatchesByOrderIds

Get a list of order item batch information for the specified orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.get_order_item_batches_by_order_ids_request import GetOrderItemBatchesByOrderIdsRequest
from linnworks_api.generated.orders.models.get_order_item_batches_by_order_ids_response import GetOrderItemBatchesByOrderIdsResponse
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.GetOrderItemBatchesByOrderIdsRequest() # GetOrderItemBatchesByOrderIdsRequest | Made up of list of pkOrderIds (optional)

    try:
        # GetOrderItemBatchesByOrderIds
        api_response = api_instance.get_order_item_batches_by_order_ids(request=request)
        print("The response of OrdersApi->get_order_item_batches_by_order_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_item_batches_by_order_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderItemBatchesByOrderIdsRequest**](GetOrderItemBatchesByOrderIdsRequest.md)| Made up of list of pkOrderIds | [optional] 

### Return type

[**GetOrderItemBatchesByOrderIdsResponse**](GetOrderItemBatchesByOrderIdsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_batchs_by_order_id**
> List[OrderItemBatch] get_order_item_batchs_by_order_id(parameters=parameters)

GetOrderItemBatchsByOrderId

Get a list of order item batch information for the specified order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_item_batch import OrderItemBatch
from linnworks_api.generated.orders.models.order_item_batch_info import OrderItemBatchInfo
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    parameters = linnworks_api.generated.orders.OrderItemBatchInfo() # OrderItemBatchInfo | Made up of pkOrderId (optional)

    try:
        # GetOrderItemBatchsByOrderId
        api_response = api_instance.get_order_item_batchs_by_order_id(parameters=parameters)
        print("The response of OrdersApi->get_order_item_batchs_by_order_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_item_batchs_by_order_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameters** | [**OrderItemBatchInfo**](OrderItemBatchInfo.md)| Made up of pkOrderId | [optional] 

### Return type

[**List[OrderItemBatch]**](OrderItemBatch.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_composition**
> OrderItem get_order_item_composition(order_id=order_id, stock_item_id=stock_item_id, fulfilment_center=fulfilment_center)

GetOrderItemComposition

Get the detail (composition) of a specific order item <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_item import OrderItem
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)
    stock_item_id = 'stock_item_id_example' # str | Stock item id (optional)
    fulfilment_center = 'fulfilment_center_example' # str | Location to get the order item composition for (optional)

    try:
        # GetOrderItemComposition
        api_response = api_instance.get_order_item_composition(order_id=order_id, stock_item_id=stock_item_id, fulfilment_center=fulfilment_center)
        print("The response of OrdersApi->get_order_item_composition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_item_composition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 
 **stock_item_id** | **str**| Stock item id | [optional] 
 **fulfilment_center** | **str**| Location to get the order item composition for | [optional] 

### Return type

[**OrderItem**](OrderItem.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_row_serial_values_by_order_ids**
> GetSerialisedValuesForOrdersResponse get_order_item_row_serial_values_by_order_ids(request=request)

GetOrderItemRowSerialValuesByOrderIds

Get order item row serial information by requested order ids. Maximum requested orderIds is 25. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.get_order_item_row_serial_values_by_order_ids_request import GetOrderItemRowSerialValuesByOrderIdsRequest
from linnworks_api.generated.orders.models.get_serialised_values_for_orders_response import GetSerialisedValuesForOrdersResponse
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.GetOrderItemRowSerialValuesByOrderIdsRequest() # GetOrderItemRowSerialValuesByOrderIdsRequest | Request with collection of order ids as properties (optional)

    try:
        # GetOrderItemRowSerialValuesByOrderIds
        api_response = api_instance.get_order_item_row_serial_values_by_order_ids(request=request)
        print("The response of OrdersApi->get_order_item_row_serial_values_by_order_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_item_row_serial_values_by_order_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderItemRowSerialValuesByOrderIdsRequest**](GetOrderItemRowSerialValuesByOrderIdsRequest.md)| Request with collection of order ids as properties | [optional] 

### Return type

[**GetSerialisedValuesForOrdersResponse**](GetSerialisedValuesForOrdersResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_items**
> List[OrderItem] get_order_items(order_id=order_id, fulfilment_center=fulfilment_center)

GetOrderItems

Get order items <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_item import OrderItem
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)
    fulfilment_center = 'fulfilment_center_example' # str | Current fulfilment center (optional)

    try:
        # GetOrderItems
        api_response = api_instance.get_order_items(order_id=order_id, fulfilment_center=fulfilment_center)
        print("The response of OrdersApi->get_order_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 
 **fulfilment_center** | **str**| Current fulfilment center | [optional] 

### Return type

[**List[OrderItem]**](OrderItem.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_note_types**
> List[OrderNoteType] get_order_note_types()

GetOrderNoteTypes

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_note_type import OrderNoteType
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetOrderNoteTypes
        api_response = api_instance.get_order_note_types()
        print("The response of OrdersApi->get_order_note_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_note_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrderNoteType]**](OrderNoteType.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_notes**
> List[OrderNote] get_order_notes(order_id=order_id)

GetOrderNotes

Get the order notes <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_note import OrderNote
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOrderNotes
        api_response = api_instance.get_order_notes(order_id=order_id)
        print("The response of OrdersApi->get_order_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[OrderNote]**](OrderNote.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_packaging_calculation**
> List[CalcOrderHeader] get_order_packaging_calculation(request=request)

GetOrderPackagingCalculation

Retrieves order packaging, weight and dimension information with split packaging. The method can perform ad hoc recalculation and saving of any changes. <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.calc_order_header import CalcOrderHeader
from linnworks_api.generated.orders.models.get_order_packaging_calculation_request import GetOrderPackagingCalculationRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    request = linnworks_api.generated.orders.GetOrderPackagingCalculationRequest() # GetOrderPackagingCalculationRequest | Orders to get packaging calculations for (optional)

    try:
        # GetOrderPackagingCalculation
        api_response = api_instance.get_order_packaging_calculation(request=request)
        print("The response of OrdersApi->get_order_packaging_calculation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_packaging_calculation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GetOrderPackagingCalculationRequest**](GetOrderPackagingCalculationRequest.md)| Orders to get packaging calculations for | [optional] 

### Return type

[**List[CalcOrderHeader]**](CalcOrderHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_packaging_split**
> List[OrderPackagingSplit] get_order_packaging_split(order_id=order_id, open_orders_only=open_orders_only)

GetOrderPackagingSplit

Get a possible order split by packaging <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_packaging_split import OrderPackagingSplit
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)
    open_orders_only = True # bool | Whether to search open orders only, or all orders (optional)

    try:
        # GetOrderPackagingSplit
        api_response = api_instance.get_order_packaging_split(order_id=order_id, open_orders_only=open_orders_only)
        print("The response of OrdersApi->get_order_packaging_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_packaging_split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 
 **open_orders_only** | **bool**| Whether to search open orders only, or all orders | [optional] 

### Return type

[**List[OrderPackagingSplit]**](OrderPackagingSplit.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_relations**
> List[OrderRelation] get_order_relations(order_id=order_id)

GetOrderRelations

Get order relations <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_relation import OrderRelation
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOrderRelations
        api_response = api_instance.get_order_relations(order_id=order_id)
        print("The response of OrdersApi->get_order_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[OrderRelation]**](OrderRelation.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_view**
> UserOrderView get_order_view(pk_view_id=pk_view_id, mark_as_latest_viewed=mark_as_latest_viewed)

GetOrderView

Get a specific open order view <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.user_order_view import UserOrderView
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    pk_view_id = 56 # int | View id (optional)
    mark_as_latest_viewed = True # bool | Mark it in the database as latest viewer (optional)

    try:
        # GetOrderView
        api_response = api_instance.get_order_view(pk_view_id=pk_view_id, mark_as_latest_viewed=mark_as_latest_viewed)
        print("The response of OrdersApi->get_order_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pk_view_id** | **int**| View id | [optional] 
 **mark_as_latest_viewed** | **bool**| Mark it in the database as latest viewer | [optional] 

### Return type

[**UserOrderView**](UserOrderView.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_views**
> List[UserOrderView] get_order_views()

GetOrderViews

Get open order views <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.user_order_view import UserOrderView
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetOrderViews
        api_response = api_instance.get_order_views()
        print("The response of OrdersApi->get_order_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_views: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserOrderView]**](UserOrderView.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_xml**
> List[OrderXML] get_order_xml(order_id=order_id)

GetOrderXml

Get order XML received from channel <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_xml import OrderXML
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOrderXml
        api_response = api_instance.get_order_xml(order_id=order_id)
        print("The response of OrdersApi->get_order_xml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_xml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

[**List[OrderXML]**](OrderXML.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_xml_js_tree**
> str get_order_xml_js_tree(order_id=order_id)

GetOrderXmlJSTree

Get order XML received from channel <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    order_id = 'order_id_example' # str | Order id (optional)

    try:
        # GetOrderXmlJSTree
        api_response = api_instance.get_order_xml_js_tree(order_id=order_id)
        print("The response of OrdersApi->get_order_xml_js_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order_xml_js_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order id | [optional] 

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> List[OpenOrder] get_orders(orders_get_orders_request)

GetOrders

Get list of open orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.open_order import OpenOrder
from linnworks_api.generated.orders.models.orders_get_orders_request import OrdersGetOrdersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_orders_request = linnworks_api.generated.orders.OrdersGetOrdersRequest() # OrdersGetOrdersRequest | 

    try:
        # GetOrders
        api_response = api_instance.get_orders(orders_get_orders_request)
        print("The response of OrdersApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_orders_request** | [**OrdersGetOrdersRequest**](OrdersGetOrdersRequest.md)|  | 

### Return type

[**List[OpenOrder]**](OpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_by_id**
> List[OrderDetails] get_orders_by_id(orders_get_orders_by_id_request)

GetOrdersById

Retrieves the order detail list for a list of order id identifiers (pkOrderId)  For working with open orders recommended to use OpenOrders/GetOpenOrdersDetails <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_details import OrderDetails
from linnworks_api.generated.orders.models.orders_get_orders_by_id_request import OrdersGetOrdersByIdRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_orders_by_id_request = linnworks_api.generated.orders.OrdersGetOrdersByIdRequest() # OrdersGetOrdersByIdRequest | 

    try:
        # GetOrdersById
        api_response = api_instance.get_orders_by_id(orders_get_orders_by_id_request)
        print("The response of OrdersApi->get_orders_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_orders_by_id_request** | [**OrdersGetOrdersByIdRequest**](OrdersGetOrdersByIdRequest.md)|  | 

### Return type

[**List[OrderDetails]**](OrderDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_notes**
> Dict[str, List[OrderNote]] get_orders_notes(orders_get_orders_notes_request)

GetOrdersNotes

 <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_note import OrderNote
from linnworks_api.generated.orders.models.orders_get_orders_notes_request import OrdersGetOrdersNotesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_orders_notes_request = linnworks_api.generated.orders.OrdersGetOrdersNotesRequest() # OrdersGetOrdersNotesRequest | 

    try:
        # GetOrdersNotes
        api_response = api_instance.get_orders_notes(orders_get_orders_notes_request)
        print("The response of OrdersApi->get_orders_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_orders_notes_request** | [**OrdersGetOrdersNotesRequest**](OrdersGetOrdersNotesRequest.md)|  | 

### Return type

**Dict[str, List[OrderNote]]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_relations**
> Dict[str, List[OrderRelation]] get_orders_relations(orders_get_orders_relations_request)

GetOrdersRelations

Get order relations for a list of orders. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_relation import OrderRelation
from linnworks_api.generated.orders.models.orders_get_orders_relations_request import OrdersGetOrdersRelationsRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_get_orders_relations_request = linnworks_api.generated.orders.OrdersGetOrdersRelationsRequest() # OrdersGetOrdersRelationsRequest | 

    try:
        # GetOrdersRelations
        api_response = api_instance.get_orders_relations(orders_get_orders_relations_request)
        print("The response of OrdersApi->get_orders_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_get_orders_relations_request** | [**OrdersGetOrdersRelationsRequest**](OrdersGetOrdersRelationsRequest.md)|  | 

### Return type

**Dict[str, List[OrderRelation]]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packaging_groups**
> List[PackageGroup] get_packaging_groups()

GetPackagingGroups

Get available packaging groups <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.package_group import PackageGroup
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetPackagingGroups
        api_response = api_instance.get_packaging_groups()
        print("The response of OrdersApi->get_packaging_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_packaging_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PackageGroup]**](PackageGroup.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods**
> List[PaymentMethod] get_payment_methods()

GetPaymentMethods

Get the available payment methods <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.payment_method import PaymentMethod
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetPaymentMethods
        api_response = api_instance.get_payment_methods()
        print("The response of OrdersApi->get_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_payment_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PaymentMethod]**](PaymentMethod.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_methods**
> List[ShippingMethod] get_shipping_methods()

GetShippingMethods

Get available shipping methods <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.shipping_method import ShippingMethod
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetShippingMethods
        api_response = api_instance.get_shipping_methods()
        print("The response of OrdersApi->get_shipping_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_shipping_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ShippingMethod]**](ShippingMethod.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_location_id**
> str get_user_location_id()

GetUserLocationId

Get the user location from settings <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)

    try:
        # GetUserLocationId
        api_response = api_instance.get_user_location_id()
        print("The response of OrdersApi->get_user_location_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_user_location_id: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_order**
> lock_order(orders_lock_order_request)

LockOrder

Lock a list of orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_lock_order_request import OrdersLockOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_lock_order_request = linnworks_api.generated.orders.OrdersLockOrderRequest() # OrdersLockOrderRequest | 

    try:
        # LockOrder
        api_instance.lock_order(orders_lock_order_request)
    except Exception as e:
        print("Exception when calling OrdersApi->lock_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_lock_order_request** | [**OrdersLockOrderRequest**](OrdersLockOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_orders**
> OpenOrder merge_orders(orders_merge_orders_request)

MergeOrders

Merge a list of orders into a new one <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrders.MergeOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.open_order import OpenOrder
from linnworks_api.generated.orders.models.orders_merge_orders_request import OrdersMergeOrdersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_merge_orders_request = linnworks_api.generated.orders.OrdersMergeOrdersRequest() # OrdersMergeOrdersRequest | 

    try:
        # MergeOrders
        api_response = api_instance.merge_orders(orders_merge_orders_request)
        print("The response of OrdersApi->merge_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->merge_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_merge_orders_request** | [**OrdersMergeOrdersRequest**](OrdersMergeOrdersRequest.md)|  | 

### Return type

[**OpenOrder**](OpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_to_location**
> MoveToLocationResult move_to_location(orders_move_to_location_request)

MoveToLocation

Move a list of orders to a specific location <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.move_to_location_result import MoveToLocationResult
from linnworks_api.generated.orders.models.orders_move_to_location_request import OrdersMoveToLocationRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_move_to_location_request = linnworks_api.generated.orders.OrdersMoveToLocationRequest() # OrdersMoveToLocationRequest | 

    try:
        # MoveToLocation
        api_response = api_instance.move_to_location(orders_move_to_location_request)
        print("The response of OrdersApi->move_to_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->move_to_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_move_to_location_request** | [**OrdersMoveToLocationRequest**](OrdersMoveToLocationRequest.md)|  | 

### Return type

[**MoveToLocationResult**](MoveToLocationResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_fulfilment_centre_order**
> ProcessOrderResult process_fulfilment_centre_order(orders_process_fulfilment_centre_order_request)

ProcessFulfilmentCentreOrder

Process Orders associated with a Fulfilment Centre <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_process_fulfilment_centre_order_request import OrdersProcessFulfilmentCentreOrderRequest
from linnworks_api.generated.orders.models.process_order_result import ProcessOrderResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_process_fulfilment_centre_order_request = linnworks_api.generated.orders.OrdersProcessFulfilmentCentreOrderRequest() # OrdersProcessFulfilmentCentreOrderRequest | 

    try:
        # ProcessFulfilmentCentreOrder
        api_response = api_instance.process_fulfilment_centre_order(orders_process_fulfilment_centre_order_request)
        print("The response of OrdersApi->process_fulfilment_centre_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->process_fulfilment_centre_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_process_fulfilment_centre_order_request** | [**OrdersProcessFulfilmentCentreOrderRequest**](OrdersProcessFulfilmentCentreOrderRequest.md)|  | 

### Return type

[**ProcessOrderResult**](ProcessOrderResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_order**
> ProcessOrderResult process_order(orders_process_order_request)

ProcessOrder

Process a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_process_order_request import OrdersProcessOrderRequest
from linnworks_api.generated.orders.models.process_order_result import ProcessOrderResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_process_order_request = linnworks_api.generated.orders.OrdersProcessOrderRequest() # OrdersProcessOrderRequest | 

    try:
        # ProcessOrder
        api_response = api_instance.process_order(orders_process_order_request)
        print("The response of OrdersApi->process_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->process_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_process_order_request** | [**OrdersProcessOrderRequest**](OrdersProcessOrderRequest.md)|  | 

### Return type

[**ProcessOrderResult**](ProcessOrderResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_order_by_order_or_reference_id**
> ProcessOrderByOrderIdOrReferenceResponse process_order_by_order_or_reference_id(orders_process_order_by_order_or_reference_id_request)

ProcessOrderByOrderOrReferenceId

 <b>Permissions Required: </b> GlobalPermissions.OrderBook.DespatchConsoleNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_process_order_by_order_or_reference_id_request import OrdersProcessOrderByOrderOrReferenceIdRequest
from linnworks_api.generated.orders.models.process_order_by_order_id_or_reference_response import ProcessOrderByOrderIdOrReferenceResponse
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_process_order_by_order_or_reference_id_request = linnworks_api.generated.orders.OrdersProcessOrderByOrderOrReferenceIdRequest() # OrdersProcessOrderByOrderOrReferenceIdRequest | 

    try:
        # ProcessOrderByOrderOrReferenceId
        api_response = api_instance.process_order_by_order_or_reference_id(orders_process_order_by_order_or_reference_id_request)
        print("The response of OrdersApi->process_order_by_order_or_reference_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->process_order_by_order_or_reference_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_process_order_by_order_or_reference_id_request** | [**OrdersProcessOrderByOrderOrReferenceIdRequest**](OrdersProcessOrderByOrderOrReferenceIdRequest.md)|  | 

### Return type

[**ProcessOrderByOrderIdOrReferenceResponse**](ProcessOrderByOrderIdOrReferenceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_order_required_batch_scans**
> process_order_required_batch_scans(orders_process_order_required_batch_scans_request)

ProcessOrder_RequiredBatchScans

Update the order with the batch numbers scanned during process order (i.e. those items with dbo.StockItem.BatchNumberScanRequired set)  batches must be provided for all items in the order which require batch number scanning (including composite children)  Overwrites any existing batch assignment for the required items <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_process_order_required_batch_scans_request import OrdersProcessOrderRequiredBatchScansRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_process_order_required_batch_scans_request = linnworks_api.generated.orders.OrdersProcessOrderRequiredBatchScansRequest() # OrdersProcessOrderRequiredBatchScansRequest | 

    try:
        # ProcessOrder_RequiredBatchScans
        api_instance.process_order_required_batch_scans(orders_process_order_required_batch_scans_request)
    except Exception as e:
        print("Exception when calling OrdersApi->process_order_required_batch_scans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_process_order_required_batch_scans_request** | [**OrdersProcessOrderRequiredBatchScansRequest**](OrdersProcessOrderRequiredBatchScansRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_orders_in_batch**
> List[ProcessOrderResult] process_orders_in_batch(orders_process_orders_in_batch_request)

ProcessOrdersInBatch

Process a list of orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_process_orders_in_batch_request import OrdersProcessOrdersInBatchRequest
from linnworks_api.generated.orders.models.process_order_result import ProcessOrderResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_process_orders_in_batch_request = linnworks_api.generated.orders.OrdersProcessOrdersInBatchRequest() # OrdersProcessOrdersInBatchRequest | 

    try:
        # ProcessOrdersInBatch
        api_response = api_instance.process_orders_in_batch(orders_process_orders_in_batch_request)
        print("The response of OrdersApi->process_orders_in_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->process_orders_in_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_process_orders_in_batch_request** | [**OrdersProcessOrdersInBatchRequest**](OrdersProcessOrdersInBatchRequest.md)|  | 

### Return type

[**List[ProcessOrderResult]**](ProcessOrderResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_single_order_packaging**
> CalcOrderHeader recalculate_single_order_packaging(orders_recalculate_single_order_packaging_request)

RecalculateSingleOrderPackaging

Designed to recalculate order packaging totals based on the object provided <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.calc_order_header import CalcOrderHeader
from linnworks_api.generated.orders.models.orders_recalculate_single_order_packaging_request import OrdersRecalculateSingleOrderPackagingRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_recalculate_single_order_packaging_request = linnworks_api.generated.orders.OrdersRecalculateSingleOrderPackagingRequest() # OrdersRecalculateSingleOrderPackagingRequest | 

    try:
        # RecalculateSingleOrderPackaging
        api_response = api_instance.recalculate_single_order_packaging(orders_recalculate_single_order_packaging_request)
        print("The response of OrdersApi->recalculate_single_order_packaging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->recalculate_single_order_packaging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_recalculate_single_order_packaging_request** | [**OrdersRecalculateSingleOrderPackagingRequest**](OrdersRecalculateSingleOrderPackagingRequest.md)|  | 

### Return type

[**CalcOrderHeader**](CalcOrderHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_order_item**
> UpdateOrderItemResult remove_order_item(orders_remove_order_item_request)

RemoveOrderItem

Remove item from an order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_remove_order_item_request import OrdersRemoveOrderItemRequest
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_remove_order_item_request = linnworks_api.generated.orders.OrdersRemoveOrderItemRequest() # OrdersRemoveOrderItemRequest | 

    try:
        # RemoveOrderItem
        api_response = api_instance.remove_order_item(orders_remove_order_item_request)
        print("The response of OrdersApi->remove_order_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->remove_order_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_remove_order_item_request** | [**OrdersRemoveOrderItemRequest**](OrdersRemoveOrderItemRequest.md)|  | 

### Return type

[**UpdateOrderItemResult**](UpdateOrderItemResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_rules_engine**
> List[str] run_rules_engine(orders_run_rules_engine_request)

RunRulesEngine

Run Rules Engine on Open Orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_run_rules_engine_request import OrdersRunRulesEngineRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_run_rules_engine_request = linnworks_api.generated.orders.OrdersRunRulesEngineRequest() # OrdersRunRulesEngineRequest | 

    try:
        # RunRulesEngine
        api_response = api_instance.run_rules_engine(orders_run_rules_engine_request)
        print("The response of OrdersApi->run_rules_engine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->run_rules_engine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_run_rules_engine_request** | [**OrdersRunRulesEngineRequest**](OrdersRunRulesEngineRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_order_view**
> save_order_view(orders_save_order_view_request)

SaveOrderView

Update a open order view <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_save_order_view_request import OrdersSaveOrderViewRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_save_order_view_request = linnworks_api.generated.orders.OrdersSaveOrderViewRequest() # OrdersSaveOrderViewRequest | 

    try:
        # SaveOrderView
        api_instance.save_order_view(orders_save_order_view_request)
    except Exception as e:
        print("Exception when calling OrdersApi->save_order_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_save_order_view_request** | [**OrdersSaveOrderViewRequest**](OrdersSaveOrderViewRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_additional_info**
> set_additional_info(orders_set_additional_info_request)

SetAdditionalInfo

Overwrites the existing order item additional info <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_additional_info_request import OrdersSetAdditionalInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_additional_info_request = linnworks_api.generated.orders.OrdersSetAdditionalInfoRequest() # OrdersSetAdditionalInfoRequest | 

    try:
        # SetAdditionalInfo
        api_instance.set_additional_info(orders_set_additional_info_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_additional_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_additional_info_request** | [**OrdersSetAdditionalInfoRequest**](OrdersSetAdditionalInfoRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_available_folders**
> List[OrderFolder] set_available_folders(orders_set_available_folders_request)

SetAvailableFolders

Set the list of available folders that orders can be assigned to <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_folder import OrderFolder
from linnworks_api.generated.orders.models.orders_set_available_folders_request import OrdersSetAvailableFoldersRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_available_folders_request = linnworks_api.generated.orders.OrdersSetAvailableFoldersRequest() # OrdersSetAvailableFoldersRequest | 

    try:
        # SetAvailableFolders
        api_response = api_instance.set_available_folders(orders_set_available_folders_request)
        print("The response of OrdersApi->set_available_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_available_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_available_folders_request** | [**OrdersSetAvailableFoldersRequest**](OrdersSetAvailableFoldersRequest.md)|  | 

### Return type

[**List[OrderFolder]**](OrderFolder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_payment_method_id_for_new_order**
> set_default_payment_method_id_for_new_order(orders_set_default_payment_method_id_for_new_order_request)

SetDefaultPaymentMethodIdForNewOrder

Set the default payment method for new direct orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_default_payment_method_id_for_new_order_request import OrdersSetDefaultPaymentMethodIdForNewOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_default_payment_method_id_for_new_order_request = linnworks_api.generated.orders.OrdersSetDefaultPaymentMethodIdForNewOrderRequest() # OrdersSetDefaultPaymentMethodIdForNewOrderRequest | 

    try:
        # SetDefaultPaymentMethodIdForNewOrder
        api_instance.set_default_payment_method_id_for_new_order(orders_set_default_payment_method_id_for_new_order_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_default_payment_method_id_for_new_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_default_payment_method_id_for_new_order_request** | [**OrdersSetDefaultPaymentMethodIdForNewOrderRequest**](OrdersSetDefaultPaymentMethodIdForNewOrderRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_extended_properties**
> List[ExtendedProperty] set_extended_properties(orders_set_extended_properties_request)

SetExtendedProperties

Set the extended properties for a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.extended_property import ExtendedProperty
from linnworks_api.generated.orders.models.orders_set_extended_properties_request import OrdersSetExtendedPropertiesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_extended_properties_request = linnworks_api.generated.orders.OrdersSetExtendedPropertiesRequest() # OrdersSetExtendedPropertiesRequest | 

    try:
        # SetExtendedProperties
        api_response = api_instance.set_extended_properties(orders_set_extended_properties_request)
        print("The response of OrdersApi->set_extended_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_extended_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_extended_properties_request** | [**OrdersSetExtendedPropertiesRequest**](OrdersSetExtendedPropertiesRequest.md)|  | 

### Return type

[**List[ExtendedProperty]**](ExtendedProperty.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_invoices_printed**
> List[str] set_invoices_printed(orders_set_invoices_printed_request)

SetInvoicesPrinted

Mark a list of orders as invoice printed. This operation can not be executed on locked or parked orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_invoices_printed_request import OrdersSetInvoicesPrintedRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_invoices_printed_request = linnworks_api.generated.orders.OrdersSetInvoicesPrintedRequest() # OrdersSetInvoicesPrintedRequest | 

    try:
        # SetInvoicesPrinted
        api_response = api_instance.set_invoices_printed(orders_set_invoices_printed_request)
        print("The response of OrdersApi->set_invoices_printed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_invoices_printed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_invoices_printed_request** | [**OrdersSetInvoicesPrintedRequest**](OrdersSetInvoicesPrintedRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_labels_printed**
> List[str] set_labels_printed(orders_set_labels_printed_request)

SetLabelsPrinted

Mark a list of orders as label printed <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_labels_printed_request import OrdersSetLabelsPrintedRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_labels_printed_request = linnworks_api.generated.orders.OrdersSetLabelsPrintedRequest() # OrdersSetLabelsPrintedRequest | 

    try:
        # SetLabelsPrinted
        api_response = api_instance.set_labels_printed(orders_set_labels_printed_request)
        print("The response of OrdersApi->set_labels_printed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_labels_printed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_labels_printed_request** | [**OrdersSetLabelsPrintedRequest**](OrdersSetLabelsPrintedRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_customer_info**
> OrderTotalsInfo set_order_customer_info(orders_set_order_customer_info_request)

SetOrderCustomerInfo

Update the customer info of a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.order_totals_info import OrderTotalsInfo
from linnworks_api.generated.orders.models.orders_set_order_customer_info_request import OrdersSetOrderCustomerInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_customer_info_request = linnworks_api.generated.orders.OrdersSetOrderCustomerInfoRequest() # OrdersSetOrderCustomerInfoRequest | 

    try:
        # SetOrderCustomerInfo
        api_response = api_instance.set_order_customer_info(orders_set_order_customer_info_request)
        print("The response of OrdersApi->set_order_customer_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_customer_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_customer_info_request** | [**OrdersSetOrderCustomerInfoRequest**](OrdersSetOrderCustomerInfoRequest.md)|  | 

### Return type

[**OrderTotalsInfo**](OrderTotalsInfo.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_general_info**
> set_order_general_info(orders_set_order_general_info_request)

SetOrderGeneralInfo

Update the general info of a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_order_general_info_request import OrdersSetOrderGeneralInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_general_info_request = linnworks_api.generated.orders.OrdersSetOrderGeneralInfoRequest() # OrdersSetOrderGeneralInfoRequest | 

    try:
        # SetOrderGeneralInfo
        api_instance.set_order_general_info(orders_set_order_general_info_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_general_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_general_info_request** | [**OrdersSetOrderGeneralInfoRequest**](OrdersSetOrderGeneralInfoRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_notes**
> set_order_notes(orders_set_order_notes_request)

SetOrderNotes

Set the order notes for a specific order  SetOrderNotes overwrites the existing order notes with those in the list provided.   Any existing notes should be retrieved using GetOrderNotes and added to this list, so that they are not lost/overwritten. <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_order_notes_request import OrdersSetOrderNotesRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_notes_request = linnworks_api.generated.orders.OrdersSetOrderNotesRequest() # OrdersSetOrderNotesRequest | 

    try:
        # SetOrderNotes
        api_instance.set_order_notes(orders_set_order_notes_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_notes_request** | [**OrdersSetOrderNotesRequest**](OrdersSetOrderNotesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_packaging**
> CalcOrderHeader set_order_packaging(orders_set_order_packaging_request)

SetOrderPackaging

Designed to save order packaging when it has already been calculated but not saved or is a manual edit. <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.calc_order_header import CalcOrderHeader
from linnworks_api.generated.orders.models.orders_set_order_packaging_request import OrdersSetOrderPackagingRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_packaging_request = linnworks_api.generated.orders.OrdersSetOrderPackagingRequest() # OrdersSetOrderPackagingRequest | 

    try:
        # SetOrderPackaging
        api_response = api_instance.set_order_packaging(orders_set_order_packaging_request)
        print("The response of OrdersApi->set_order_packaging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_packaging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_packaging_request** | [**OrdersSetOrderPackagingRequest**](OrdersSetOrderPackagingRequest.md)|  | 

### Return type

[**CalcOrderHeader**](CalcOrderHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_packaging_split**
> UpdateTotalsResult set_order_packaging_split(orders_set_order_packaging_split_request)

SetOrderPackagingSplit

Split an order by packaging <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_order_packaging_split_request import OrdersSetOrderPackagingSplitRequest
from linnworks_api.generated.orders.models.update_totals_result import UpdateTotalsResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_packaging_split_request = linnworks_api.generated.orders.OrdersSetOrderPackagingSplitRequest() # OrdersSetOrderPackagingSplitRequest | 

    try:
        # SetOrderPackagingSplit
        api_response = api_instance.set_order_packaging_split(orders_set_order_packaging_split_request)
        print("The response of OrdersApi->set_order_packaging_split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_packaging_split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_packaging_split_request** | [**OrdersSetOrderPackagingSplitRequest**](OrdersSetOrderPackagingSplitRequest.md)|  | 

### Return type

[**UpdateTotalsResult**](UpdateTotalsResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_shipping_info**
> UpdateTotalsResult set_order_shipping_info(orders_set_order_shipping_info_request)

SetOrderShippingInfo

Update the shipping info of a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_order_shipping_info_request import OrdersSetOrderShippingInfoRequest
from linnworks_api.generated.orders.models.update_totals_result import UpdateTotalsResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_shipping_info_request = linnworks_api.generated.orders.OrdersSetOrderShippingInfoRequest() # OrdersSetOrderShippingInfoRequest | 

    try:
        # SetOrderShippingInfo
        api_response = api_instance.set_order_shipping_info(orders_set_order_shipping_info_request)
        print("The response of OrdersApi->set_order_shipping_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_shipping_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_shipping_info_request** | [**OrdersSetOrderShippingInfoRequest**](OrdersSetOrderShippingInfoRequest.md)|  | 

### Return type

[**UpdateTotalsResult**](UpdateTotalsResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_split_packaging_manual_overwrite**
> CalcOrderHeader set_order_split_packaging_manual_overwrite(orders_set_order_split_packaging_manual_overwrite_request)

SetOrderSplitPackagingManualOverwrite

Designed to save order split packaging after a manual override <b>Permissions Required: </b> GlobalPermissions.OrderBook.ViewOrderDetailsNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.calc_order_header import CalcOrderHeader
from linnworks_api.generated.orders.models.orders_set_order_split_packaging_manual_overwrite_request import OrdersSetOrderSplitPackagingManualOverwriteRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_split_packaging_manual_overwrite_request = linnworks_api.generated.orders.OrdersSetOrderSplitPackagingManualOverwriteRequest() # OrdersSetOrderSplitPackagingManualOverwriteRequest | 

    try:
        # SetOrderSplitPackagingManualOverwrite
        api_response = api_instance.set_order_split_packaging_manual_overwrite(orders_set_order_split_packaging_manual_overwrite_request)
        print("The response of OrdersApi->set_order_split_packaging_manual_overwrite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_split_packaging_manual_overwrite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_split_packaging_manual_overwrite_request** | [**OrdersSetOrderSplitPackagingManualOverwriteRequest**](OrdersSetOrderSplitPackagingManualOverwriteRequest.md)|  | 

### Return type

[**CalcOrderHeader**](CalcOrderHeader.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_totals_info**
> set_order_totals_info(orders_set_order_totals_info_request)

SetOrderTotalsInfo

Update totals info of a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_order_totals_info_request import OrdersSetOrderTotalsInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_order_totals_info_request = linnworks_api.generated.orders.OrdersSetOrderTotalsInfoRequest() # OrdersSetOrderTotalsInfoRequest | 

    try:
        # SetOrderTotalsInfo
        api_instance.set_order_totals_info(orders_set_order_totals_info_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_order_totals_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_order_totals_info_request** | [**OrdersSetOrderTotalsInfoRequest**](OrdersSetOrderTotalsInfoRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment_methods**
> List[PaymentMethod] set_payment_methods(orders_set_payment_methods_request)

SetPaymentMethods

Set the available payment methods <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_payment_methods_request import OrdersSetPaymentMethodsRequest
from linnworks_api.generated.orders.models.payment_method import PaymentMethod
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_payment_methods_request = linnworks_api.generated.orders.OrdersSetPaymentMethodsRequest() # OrdersSetPaymentMethodsRequest | 

    try:
        # SetPaymentMethods
        api_response = api_instance.set_payment_methods(orders_set_payment_methods_request)
        print("The response of OrdersApi->set_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->set_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_payment_methods_request** | [**OrdersSetPaymentMethodsRequest**](OrdersSetPaymentMethodsRequest.md)|  | 

### Return type

[**List[PaymentMethod]**](PaymentMethod.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pick_list_printed**
> set_pick_list_printed(orders_set_pick_list_printed_request)

SetPickListPrinted

Sets the print flag for the given orders. This operation can not be executed on locked or parked orders <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_set_pick_list_printed_request import OrdersSetPickListPrintedRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_set_pick_list_printed_request = linnworks_api.generated.orders.OrdersSetPickListPrintedRequest() # OrdersSetPickListPrintedRequest | 

    try:
        # SetPickListPrinted
        api_instance.set_pick_list_printed(orders_set_pick_list_printed_request)
    except Exception as e:
        print("Exception when calling OrdersApi->set_pick_list_printed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_set_pick_list_printed_request** | [**OrdersSetPickListPrintedRequest**](OrdersSetPickListPrintedRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_order**
> List[OpenOrder] split_order(orders_split_order_request)

SplitOrder

Split a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.open_order import OpenOrder
from linnworks_api.generated.orders.models.orders_split_order_request import OrdersSplitOrderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_split_order_request = linnworks_api.generated.orders.OrdersSplitOrderRequest() # OrdersSplitOrderRequest | 

    try:
        # SplitOrder
        api_response = api_instance.split_order(orders_split_order_request)
        print("The response of OrdersApi->split_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->split_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_split_order_request** | [**OrdersSplitOrderRequest**](OrdersSplitOrderRequest.md)|  | 

### Return type

[**List[OpenOrder]**](OpenOrder.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_to_folder**
> List[str] unassign_to_folder(orders_unassign_to_folder_request)

UnassignToFolder

Unassign a list of orders to a specific folder. This operation can not be executed on locked or parked orders <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_unassign_to_folder_request import OrdersUnassignToFolderRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_unassign_to_folder_request = linnworks_api.generated.orders.OrdersUnassignToFolderRequest() # OrdersUnassignToFolderRequest | 

    try:
        # UnassignToFolder
        api_response = api_instance.unassign_to_folder(orders_unassign_to_folder_request)
        print("The response of OrdersApi->unassign_to_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->unassign_to_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_unassign_to_folder_request** | [**OrdersUnassignToFolderRequest**](OrdersUnassignToFolderRequest.md)|  | 

### Return type

**List[str]**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_additional_info**
> update_additional_info(orders_update_additional_info_request)

UpdateAdditionalInfo

Updates additional info of a specific item <b>Permissions Required: </b> GlobalPermissions.OrderBook.OpenOrdersNode <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>250</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_update_additional_info_request import OrdersUpdateAdditionalInfoRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_update_additional_info_request = linnworks_api.generated.orders.OrdersUpdateAdditionalInfoRequest() # OrdersUpdateAdditionalInfoRequest | 

    try:
        # UpdateAdditionalInfo
        api_instance.update_additional_info(orders_update_additional_info_request)
    except Exception as e:
        print("Exception when calling OrdersApi->update_additional_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_update_additional_info_request** | [**OrdersUpdateAdditionalInfoRequest**](OrdersUpdateAdditionalInfoRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_address**
> update_billing_address(orders_update_billing_address_request)

UpdateBillingAddress

Update the billing address of a specific order <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_update_billing_address_request import OrdersUpdateBillingAddressRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_update_billing_address_request = linnworks_api.generated.orders.OrdersUpdateBillingAddressRequest() # OrdersUpdateBillingAddressRequest | 

    try:
        # UpdateBillingAddress
        api_instance.update_billing_address(orders_update_billing_address_request)
    except Exception as e:
        print("Exception when calling OrdersApi->update_billing_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_update_billing_address_request** | [**OrdersUpdateBillingAddressRequest**](OrdersUpdateBillingAddressRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link_item**
> update_link_item(orders_update_link_item_request)

UpdateLinkItem

Update linked item <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_update_link_item_request import OrdersUpdateLinkItemRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_update_link_item_request = linnworks_api.generated.orders.OrdersUpdateLinkItemRequest() # OrdersUpdateLinkItemRequest | 

    try:
        # UpdateLinkItem
        api_instance.update_link_item(orders_update_link_item_request)
    except Exception as e:
        print("Exception when calling OrdersApi->update_link_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_update_link_item_request** | [**OrdersUpdateLinkItemRequest**](OrdersUpdateLinkItemRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_item**
> UpdateOrderItemResult update_order_item(orders_update_order_item_request)

UpdateOrderItem

Update an order item <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.orders_update_order_item_request import OrdersUpdateOrderItemRequest
from linnworks_api.generated.orders.models.update_order_item_result import UpdateOrderItemResult
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_update_order_item_request = linnworks_api.generated.orders.OrdersUpdateOrderItemRequest() # OrdersUpdateOrderItemRequest | 

    try:
        # UpdateOrderItem
        api_response = api_instance.update_order_item(orders_update_order_item_request)
        print("The response of OrdersApi->update_order_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_order_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_update_order_item_request** | [**OrdersUpdateOrderItemRequest**](OrdersUpdateOrderItemRequest.md)|  | 

### Return type

[**UpdateOrderItemResult**](UpdateOrderItemResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_coupon**
> CouponValidationResult validate_coupon(orders_validate_coupon_request)

ValidateCoupon

Validate a coupon <b>Rate limit: </b><span style=\"background-color:#0272d9;color:white;padding:4px 8px;text-align:center;border-radius:5px; font-size: small;\"><b>150</b></span> / minute

### Example

* Api Key Authentication (token):

```python
import linnworks_api.generated.orders
from linnworks_api.generated.orders.models.coupon_validation_result import CouponValidationResult
from linnworks_api.generated.orders.models.orders_validate_coupon_request import OrdersValidateCouponRequest
from linnworks_api.generated.orders.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://eu-ext.linnworks.net
# See configuration.py for a list of all supported configuration parameters.
configuration = linnworks_api.generated.orders.Configuration(
    host = "https://eu-ext.linnworks.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with linnworks_api.generated.orders.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linnworks_api.generated.orders.OrdersApi(api_client)
    orders_validate_coupon_request = linnworks_api.generated.orders.OrdersValidateCouponRequest() # OrdersValidateCouponRequest | 

    try:
        # ValidateCoupon
        api_response = api_instance.validate_coupon(orders_validate_coupon_request)
        print("The response of OrdersApi->validate_coupon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->validate_coupon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orders_validate_coupon_request** | [**OrdersValidateCouponRequest**](OrdersValidateCouponRequest.md)|  | 

### Return type

[**CouponValidationResult**](CouponValidationResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

