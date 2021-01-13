# iimmpact.TransactionHistoryApi

All URIs are relative to *https://api.iimmpact.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_balance_statement_get**](TransactionHistoryApi.md#v1_balance_statement_get) | **GET** /v1/balance-statement | 
[**v1_transactions_get**](TransactionHistoryApi.md#v1_transactions_get) | **GET** /v1/transactions | 


# **v1_balance_statement_get**
> BalanceStatementResponse v1_balance_statement_get(_date, limit=limit, remarks=remarks, sort=sort, type=type, direction=direction, page=page, amount=amount)



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
api_instance = iimmpact.TransactionHistoryApi(iimmpact.ApiClient(configuration))
_date = '_date_example' # str | 
limit = 'limit_example' # str |  (optional)
remarks = 'remarks_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)
type = 'type_example' # str |  (optional)
direction = 'direction_example' # str |  (optional)
page = 'page_example' # str |  (optional)
amount = 'amount_example' # str |  (optional)

try:
    api_response = api_instance.v1_balance_statement_get(_date, limit=limit, remarks=remarks, sort=sort, type=type, direction=direction, page=page, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionHistoryApi->v1_balance_statement_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**|  | 
 **limit** | **str**|  | [optional] 
 **remarks** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **str**|  | [optional] 
 **amount** | **str**|  | [optional] 

### Return type

[**BalanceStatementResponse**](BalanceStatementResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transactions_get**
> TransactionsResponse v1_transactions_get(_date, refid=refid, limit=limit, sort=sort, offset=offset, direction=direction, status=status, account=account, accept_encoding=accept_encoding, sn=sn, product=product)



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
api_instance = iimmpact.TransactionHistoryApi(iimmpact.ApiClient(configuration))
_date = '_date_example' # str | 
refid = 'refid_example' # str |  (optional)
limit = 'limit_example' # str |  (optional)
sort = 'sort_example' # str |  (optional)
offset = 'offset_example' # str |  (optional)
direction = 'direction_example' # str |  (optional)
status = 'status_example' # str |  (optional)
account = 'account_example' # str |  (optional)
accept_encoding = 'accept_encoding_example' # str |  (optional)
sn = 'sn_example' # str |  (optional)
product = 'product_example' # str |  (optional)

try:
    api_response = api_instance.v1_transactions_get(_date, refid=refid, limit=limit, sort=sort, offset=offset, direction=direction, status=status, account=account, accept_encoding=accept_encoding, sn=sn, product=product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionHistoryApi->v1_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**|  | 
 **refid** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **account** | **str**|  | [optional] 
 **accept_encoding** | **str**|  | [optional] 
 **sn** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[SSO](../README.md#SSO)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

