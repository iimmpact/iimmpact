# iimmpact.CarInsuranceApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_car_insurance_get**](CarInsuranceApi.md#v1_car_insurance_get) | **GET** /v1/car-insurance | 


# **v1_car_insurance_get**
> CarInsuranceRespone v1_car_insurance_get(vehicle_no, id_no=id_no)



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
api_instance = iimmpact.CarInsuranceApi(iimmpact.ApiClient(configuration))
vehicle_no = 'vehicle_no_example' # str | 
id_no = 'id_no_example' # str |  (optional)

try:
    api_response = api_instance.v1_car_insurance_get(vehicle_no, id_no=id_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarInsuranceApi->v1_car_insurance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_no** | **str**|  | 
 **id_no** | **str**|  | [optional] 

### Return type

[**CarInsuranceRespone**](CarInsuranceRespone.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

