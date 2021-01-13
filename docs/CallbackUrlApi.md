# iimmpact.CallbackUrlApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_callback_url_get**](CallbackUrlApi.md#v1_callback_url_get) | **GET** /v1/callback-url | 
[**v1_callback_url_post**](CallbackUrlApi.md#v1_callback_url_post) | **POST** /v1/callback-url | 


# **v1_callback_url_get**
> CallbackUrlResponse v1_callback_url_get()



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
api_instance = iimmpact.CallbackUrlApi(iimmpact.ApiClient(configuration))

try:
    api_response = api_instance.v1_callback_url_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallbackUrlApi->v1_callback_url_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CallbackUrlResponse**](CallbackUrlResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_callback_url_post**
> CallbackUrlResponse v1_callback_url_post(url)



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
api_instance = iimmpact.CallbackUrlApi(iimmpact.ApiClient(configuration))
url = 'url_example' # str | 

try:
    api_response = api_instance.v1_callback_url_post(url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallbackUrlApi->v1_callback_url_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

### Return type

[**CallbackUrlResponse**](CallbackUrlResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

