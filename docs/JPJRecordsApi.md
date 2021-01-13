# iimmpact.JPJRecordsApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jpj_driving_license_get**](JPJRecordsApi.md#v1_jpj_driving_license_get) | **GET** /v1/jpj/driving-license | 
[**v1_jpj_driving_test_results_get**](JPJRecordsApi.md#v1_jpj_driving_test_results_get) | **GET** /v1/jpj/driving-test-results | 
[**v1_jpj_motor_vehicle_expiry_get**](JPJRecordsApi.md#v1_jpj_motor_vehicle_expiry_get) | **GET** /v1/jpj/motor-vehicle-expiry | 
[**v1_jpj_summons_get**](JPJRecordsApi.md#v1_jpj_summons_get) | **GET** /v1/jpj/summons | 


# **v1_jpj_driving_license_get**
> DrivingLicenseRespone v1_jpj_driving_license_get(id_no, id_type, captcha=captcha)



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
api_instance = iimmpact.JPJRecordsApi(iimmpact.ApiClient(configuration))
id_no = 'id_no_example' # str | 
id_type = 'id_type_example' # str | 
captcha = 'captcha_example' # str |  (optional)

try:
    api_response = api_instance.v1_jpj_driving_license_get(id_no, id_type, captcha=captcha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JPJRecordsApi->v1_jpj_driving_license_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_no** | **str**|  | 
 **id_type** | **str**|  | 
 **captcha** | **str**|  | [optional] 

### Return type

[**DrivingLicenseRespone**](DrivingLicenseRespone.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jpj_driving_test_results_get**
> DrivingTestRespone v1_jpj_driving_test_results_get(id_no, id_type, captcha=captcha)



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
api_instance = iimmpact.JPJRecordsApi(iimmpact.ApiClient(configuration))
id_no = 'id_no_example' # str | 
id_type = 'id_type_example' # str | 
captcha = 'captcha_example' # str |  (optional)

try:
    api_response = api_instance.v1_jpj_driving_test_results_get(id_no, id_type, captcha=captcha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JPJRecordsApi->v1_jpj_driving_test_results_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_no** | **str**|  | 
 **id_type** | **str**|  | 
 **captcha** | **str**|  | [optional] 

### Return type

[**DrivingTestRespone**](DrivingTestRespone.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jpj_motor_vehicle_expiry_get**
> VehicleExpiryResponse v1_jpj_motor_vehicle_expiry_get(id_no, id_type, vehicle_no, captcha=captcha)



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
api_instance = iimmpact.JPJRecordsApi(iimmpact.ApiClient(configuration))
id_no = 'id_no_example' # str | 
id_type = 'id_type_example' # str | 
vehicle_no = 'vehicle_no_example' # str | 
captcha = 'captcha_example' # str |  (optional)

try:
    api_response = api_instance.v1_jpj_motor_vehicle_expiry_get(id_no, id_type, vehicle_no, captcha=captcha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JPJRecordsApi->v1_jpj_motor_vehicle_expiry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_no** | **str**|  | 
 **id_type** | **str**|  | 
 **vehicle_no** | **str**|  | 
 **captcha** | **str**|  | [optional] 

### Return type

[**VehicleExpiryResponse**](VehicleExpiryResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jpj_summons_get**
> JPJSummonsResponse v1_jpj_summons_get(id_no, id_type, captcha=captcha)



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
api_instance = iimmpact.JPJRecordsApi(iimmpact.ApiClient(configuration))
id_no = 'id_no_example' # str | 
id_type = 'id_type_example' # str | 
captcha = 'captcha_example' # str |  (optional)

try:
    api_response = api_instance.v1_jpj_summons_get(id_no, id_type, captcha=captcha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JPJRecordsApi->v1_jpj_summons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_no** | **str**|  | 
 **id_type** | **str**|  | 
 **captcha** | **str**|  | [optional] 

### Return type

[**JPJSummonsResponse**](JPJSummonsResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

