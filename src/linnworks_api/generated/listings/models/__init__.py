# coding: utf-8

# flake8: noqa
"""
    Listings API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: listings
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from linnworks_api.generated.listings.models.amazon_attribute import AmazonAttribute
from linnworks_api.generated.listings.models.amazon_b_node import AmazonBNode
from linnworks_api.generated.listings.models.amazon_config import AmazonConfig
from linnworks_api.generated.listings.models.amazon_listing import AmazonListing
from linnworks_api.generated.listings.models.amazon_shipping import AmazonShipping
from linnworks_api.generated.listings.models.amazon_variation import AmazonVariation
from linnworks_api.generated.listings.models.assigned_option import AssignedOption
from linnworks_api.generated.listings.models.assigned_option_set import AssignedOptionSet
from linnworks_api.generated.listings.models.associated_template import AssociatedTemplate
from linnworks_api.generated.listings.models.association_table import AssociationTable
from linnworks_api.generated.listings.models.big_commerce_assigned_products import BigCommerceAssignedProducts
from linnworks_api.generated.listings.models.big_commerce_config_attributes import BigCommerceConfigAttributes
from linnworks_api.generated.listings.models.big_commerce_configurator import BigCommerceConfigurator
from linnworks_api.generated.listings.models.big_commerce_custom_field import BigCommerceCustomField
from linnworks_api.generated.listings.models.big_commerce_image_data import BigCommerceImageData
from linnworks_api.generated.listings.models.big_commerce_listing import BigCommerceListing
from linnworks_api.generated.listings.models.child_image import ChildImage
from linnworks_api.generated.listings.models.child_images_list import ChildImagesList
from linnworks_api.generated.listings.models.child_option import ChildOption
from linnworks_api.generated.listings.models.config_category import ConfigCategory
from linnworks_api.generated.listings.models.config_user_attributes import ConfigUserAttributes
from linnworks_api.generated.listings.models.create_templates_in_bulk_channel_parameters import CreateTemplatesInBulkChannelParameters
from linnworks_api.generated.listings.models.create_templates_in_bulk_parameters import CreateTemplatesInBulkParameters
from linnworks_api.generated.listings.models.e_bay_item import EBayItem
from linnworks_api.generated.listings.models.ebay_attribute import EbayAttribute
from linnworks_api.generated.listings.models.ebay_config import EbayConfig
from linnworks_api.generated.listings.models.ebay_listing import EbayListing
from linnworks_api.generated.listings.models.ebay_listing_audit import EbayListingAudit
from linnworks_api.generated.listings.models.ebay_price_rule import EbayPriceRule
from linnworks_api.generated.listings.models.ebay_prices import EbayPrices
from linnworks_api.generated.listings.models.ebay_seller_profile import EbaySellerProfile
from linnworks_api.generated.listings.models.ebay_shipping_service import EbayShippingService
from linnworks_api.generated.listings.models.ebay_specification import EbaySpecification
from linnworks_api.generated.listings.models.ebay_variation import EbayVariation
from linnworks_api.generated.listings.models.ebay_weight_rule import EbayWeightRule
from linnworks_api.generated.listings.models.end_listings_pending_relist_request import EndListingsPendingRelistRequest
from linnworks_api.generated.listings.models.get_ebay_listing_operations_request import GetEbayListingOperationsRequest
from linnworks_api.generated.listings.models.get_templates_parameters import GetTemplatesParameters
from linnworks_api.generated.listings.models.image_data import ImageData
from linnworks_api.generated.listings.models.key_list import KeyList
from linnworks_api.generated.listings.models.key_value import KeyValue
from linnworks_api.generated.listings.models.key_value_generic_guid_double import KeyValueGenericGuidDouble
from linnworks_api.generated.listings.models.linn_live_key_value import LinnLiveKeyValue
from linnworks_api.generated.listings.models.linnworks_ebay_category import LinnworksEbayCategory
from linnworks_api.generated.listings.models.listing_attributes import ListingAttributes
from linnworks_api.generated.listings.models.listings_cancel_listing_bulk_operation_request import ListingsCancelListingBulkOperationRequest
from linnworks_api.generated.listings.models.listings_create_amazon_configurators_request import ListingsCreateAmazonConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_create_amazon_templates_request import ListingsCreateAmazonTemplatesRequest
from linnworks_api.generated.listings.models.listings_create_bigcommerce_configurators_request import ListingsCreateBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_create_bigcommerce_templates_request import ListingsCreateBigcommerceTemplatesRequest
from linnworks_api.generated.listings.models.listings_create_ebay_templates_request import ListingsCreateEbayTemplatesRequest
from linnworks_api.generated.listings.models.listings_create_magento_configurators_request import ListingsCreateMagentoConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_create_magento_templates_request import ListingsCreateMagentoTemplatesRequest
from linnworks_api.generated.listings.models.listings_create_templates_from_view_in_bulk_request import ListingsCreateTemplatesFromViewInBulkRequest
from linnworks_api.generated.listings.models.listings_createe_bay_configurators_request import ListingsCreateeBayConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_delete_amazon_configurators_request import ListingsDeleteAmazonConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_delete_amazon_templates_request import ListingsDeleteAmazonTemplatesRequest
from linnworks_api.generated.listings.models.listings_delete_bigcommerce_configurators_request import ListingsDeleteBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_delete_bigcommerce_templates_request import ListingsDeleteBigcommerceTemplatesRequest
from linnworks_api.generated.listings.models.listings_delete_ebay_templates_request import ListingsDeleteEbayTemplatesRequest
from linnworks_api.generated.listings.models.listings_delete_magento_configurators_request import ListingsDeleteMagentoConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_delete_magento_templates_request import ListingsDeleteMagentoTemplatesRequest
from linnworks_api.generated.listings.models.listings_deletee_bay_configurators_request import ListingsDeleteeBayConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_end_listings_pending_relist_request import ListingsEndListingsPendingRelistRequest
from linnworks_api.generated.listings.models.listings_get_amazon_templates_request import ListingsGetAmazonTemplatesRequest
from linnworks_api.generated.listings.models.listings_get_big_commerce_templates_request import ListingsGetBigCommerceTemplatesRequest
from linnworks_api.generated.listings.models.listings_get_magento_templates_request import ListingsGetMagentoTemplatesRequest
from linnworks_api.generated.listings.models.listings_gete_bay_templates_request import ListingsGeteBayTemplatesRequest
from linnworks_api.generated.listings.models.listings_process_amazon_listings_request import ListingsProcessAmazonListingsRequest
from linnworks_api.generated.listings.models.listings_process_bigcommerce_listings_request import ListingsProcessBigcommerceListingsRequest
from linnworks_api.generated.listings.models.listings_process_magento_listings_request import ListingsProcessMagentoListingsRequest
from linnworks_api.generated.listings.models.listings_processe_bay_listings_request import ListingsProcesseBayListingsRequest
from linnworks_api.generated.listings.models.listings_set_listing_strike_off_state_request import ListingsSetListingStrikeOffStateRequest
from linnworks_api.generated.listings.models.listings_update_amazon_configurators_request import ListingsUpdateAmazonConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_update_bigcommerce_configurators_request import ListingsUpdateBigcommerceConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_update_magento_configurators_request import ListingsUpdateMagentoConfiguratorsRequest
from linnworks_api.generated.listings.models.listings_updatee_bay_configurators_request import ListingsUpdateeBayConfiguratorsRequest
from linnworks_api.generated.listings.models.magento_assigned_products import MagentoAssignedProducts
from linnworks_api.generated.listings.models.magento_config import MagentoConfig
from linnworks_api.generated.listings.models.magento_config_attributes import MagentoConfigAttributes
from linnworks_api.generated.listings.models.magento_image_data import MagentoImageData
from linnworks_api.generated.listings.models.magento_listing import MagentoListing
from linnworks_api.generated.listings.models.magento_variations_attributes import MagentoVariationsAttributes
from linnworks_api.generated.listings.models.option_value import OptionValue
from linnworks_api.generated.listings.models.option_value_data import OptionValueData
from linnworks_api.generated.listings.models.paged_result_amazon_listing import PagedResultAmazonListing
from linnworks_api.generated.listings.models.paged_result_big_commerce_listing import PagedResultBigCommerceListing
from linnworks_api.generated.listings.models.paged_result_ebay_listing import PagedResultEbayListing
from linnworks_api.generated.listings.models.paged_result_magento_listing import PagedResultMagentoListing
from linnworks_api.generated.listings.models.pickup_location_time import PickupLocationTime
from linnworks_api.generated.listings.models.process_templates_parameters import ProcessTemplatesParameters
from linnworks_api.generated.listings.models.related_product import RelatedProduct
from linnworks_api.generated.listings.models.set_listing_strike_off_state_request import SetListingStrikeOffStateRequest
from linnworks_api.generated.listings.models.shipping import Shipping
from linnworks_api.generated.listings.models.simple_shipping import SimpleShipping
from linnworks_api.generated.listings.models.site_filter import SiteFilter
from linnworks_api.generated.listings.models.tuple_int32_int32 import TupleInt32Int32
from linnworks_api.generated.listings.models.var_attribute import VarAttribute
from linnworks_api.generated.listings.models.variations_attributes_prices import VariationsAttributesPrices
