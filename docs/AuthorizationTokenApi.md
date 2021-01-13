# iimmpact.AuthorizationTokenApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_token_post**](AuthorizationTokenApi.md#v1_token_post) | **POST** /v1/token | 
[**v1_token_refresh_post**](AuthorizationTokenApi.md#v1_token_refresh_post) | **POST** /v1/token/refresh | 


# **v1_token_post**
> TokenResponse v1_token_post(token_request)



### Example
```python
from __future__ import print_function
import time
import iimmpact
from iimmpact.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iimmpact.AuthorizationTokenApi()
token_request = iimmpact.TokenRequest() # TokenRequest | 

try:
    api_response = api_instance.v1_token_post(token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationTokenApi->v1_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_token_refresh_post**
> TokenResponse v1_token_refresh_post(refresh_token_request)



### Example
```python
from __future__ import print_function
import time
import iimmpact
from iimmpact.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iimmpact.AuthorizationTokenApi()
refresh_token_request = iimmpact.RefreshTokenRequest() # RefreshTokenRequest | 

try:
    api_response = api_instance.v1_token_refresh_post(refresh_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationTokenApi->v1_token_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

