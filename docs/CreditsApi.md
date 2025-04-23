# at_client.CreditsApi

All URIs are relative to *https://api.agenttoolkit.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credits_api_v1_credits_get**](CreditsApi.md#get_credits_api_v1_credits_get) | **GET** /api/v1/credits | Get Credits


# **get_credits_api_v1_credits_get**
> CreditResponse get_credits_api_v1_credits_get(auth_token=auth_token)

Get Credits

Get current credit usage and limits for the authenticated user.

Returns:
    CreditResponse with total, used, and remaining credits

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import at_client
from at_client.models.credit_response import CreditResponse
from at_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agenttoolkit.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = at_client.Configuration(
    host = "https://api.agenttoolkit.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with at_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = at_client.CreditsApi(api_client)
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # Get Credits
        api_response = api_instance.get_credits_api_v1_credits_get(auth_token=auth_token)
        print("The response of CreditsApi->get_credits_api_v1_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_credits_api_v1_credits_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | [optional] 

### Return type

[**CreditResponse**](CreditResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

