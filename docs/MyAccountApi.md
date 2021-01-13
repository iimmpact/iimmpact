# iimmpact.MyAccountApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_auth_change_password_post**](MyAccountApi.md#v1_auth_change_password_post) | **POST** /v1/auth/change-password | 
[**v1_auth_new_password_challenge_post**](MyAccountApi.md#v1_auth_new_password_challenge_post) | **POST** /v1/auth/new-password-challenge | 
[**v1_balance_get**](MyAccountApi.md#v1_balance_get) | **GET** /v1/balance | 


# **v1_auth_change_password_post**
> InlineResponse2001 v1_auth_change_password_post(new_password_request)



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
api_instance = iimmpact.MyAccountApi(iimmpact.ApiClient(configuration))
new_password_request = iimmpact.ChangePasswordRequest() # ChangePasswordRequest | 

try:
    api_response = api_instance.v1_auth_change_password_post(new_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->v1_auth_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_new_password_challenge_post**
> NewPasswordResponses v1_auth_new_password_challenge_post(new_password_request)



### Example
```python
from __future__ import print_function
import time
import iimmpact
from iimmpact.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iimmpact.MyAccountApi()
new_password_request = iimmpact.NewPasswordRequest() # NewPasswordRequest | 

try:
    api_response = api_instance.v1_auth_new_password_challenge_post(new_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->v1_auth_new_password_challenge_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_password_request** | [**NewPasswordRequest**](NewPasswordRequest.md)|  | 

### Return type

[**NewPasswordResponses**](NewPasswordResponses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_balance_get**
> InlineResponse200 v1_balance_get()



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
api_instance = iimmpact.MyAccountApi(iimmpact.ApiClient(configuration))

try:
    api_response = api_instance.v1_balance_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->v1_balance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

