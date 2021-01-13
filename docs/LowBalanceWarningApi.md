# iimmpact.LowBalanceWarningApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_low_balance_threshold_get**](LowBalanceWarningApi.md#v1_low_balance_threshold_get) | **GET** /v1/low-balance-threshold | 
[**v1_low_balance_threshold_post**](LowBalanceWarningApi.md#v1_low_balance_threshold_post) | **POST** /v1/low-balance-threshold | 


# **v1_low_balance_threshold_get**
> LowBalanceWarningResponse v1_low_balance_threshold_get()



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
api_instance = iimmpact.LowBalanceWarningApi(iimmpact.ApiClient(configuration))

try:
    api_response = api_instance.v1_low_balance_threshold_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LowBalanceWarningApi->v1_low_balance_threshold_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LowBalanceWarningResponse**](LowBalanceWarningResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_low_balance_threshold_post**
> LowBalanceWarningResponse v1_low_balance_threshold_post(amount)



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
api_instance = iimmpact.LowBalanceWarningApi(iimmpact.ApiClient(configuration))
amount = 'amount_example' # str | 

try:
    api_response = api_instance.v1_low_balance_threshold_post(amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LowBalanceWarningApi->v1_low_balance_threshold_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | 

### Return type

[**LowBalanceWarningResponse**](LowBalanceWarningResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

