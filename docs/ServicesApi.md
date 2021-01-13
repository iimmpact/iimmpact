# iimmpact.ServicesApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_bill_presentment_get**](ServicesApi.md#v1_bill_presentment_get) | **GET** /v1/bill-presentment | 
[**v1_networkstatus_get**](ServicesApi.md#v1_networkstatus_get) | **GET** /v1/networkstatus | 
[**v1_topup_post**](ServicesApi.md#v1_topup_post) | **POST** /v1/topup | 


# **v1_bill_presentment_get**
> BillPresentmentResponse v1_bill_presentment_get(account, account_name=account_name, product=product)



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
api_instance = iimmpact.ServicesApi(iimmpact.ApiClient(configuration))
account = 'account_example' # str | 
account_name = 'account_name_example' # str |  (optional)
product = 'product_example' # str |  (optional)

try:
    api_response = api_instance.v1_bill_presentment_get(account, account_name=account_name, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->v1_bill_presentment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 
 **account_name** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 

### Return type

[**BillPresentmentResponse**](BillPresentmentResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_networkstatus_get**
> NetworkStatusResponse v1_networkstatus_get(product)



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
api_instance = iimmpact.ServicesApi(iimmpact.ApiClient(configuration))
product = 'product_example' # str | 

try:
    api_response = api_instance.v1_networkstatus_get(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->v1_networkstatus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**|  | 

### Return type

[**NetworkStatusResponse**](NetworkStatusResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_topup_post**
> TopupResponse v1_topup_post(topup_request)



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
api_instance = iimmpact.ServicesApi(iimmpact.ApiClient(configuration))
topup_request = iimmpact.TopupRequest() # TopupRequest | 

try:
    api_response = api_instance.v1_topup_post(topup_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->v1_topup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topup_request** | [**TopupRequest**](TopupRequest.md)|  | 

### Return type

[**TopupResponse**](TopupResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

