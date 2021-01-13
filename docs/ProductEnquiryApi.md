# iimmpact.ProductEnquiryApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_products_get**](ProductEnquiryApi.md#v1_products_get) | **GET** /v1/products | 


# **v1_products_get**
> InlineResponse2002 v1_products_get(category=category)



### Example
```python
from __future__ import print_function
import time
import iimmpact
from iimmpact.rest import ApiException
from pprint import pprint

# Configure API key authorization: SSO
configuration = iimmpact.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = iimmpact.ProductEnquiryApi(iimmpact.ApiClient(configuration))
category = 'category_example' # str |  (optional)

try:
    api_response = api_instance.v1_products_get(category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductEnquiryApi->v1_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

