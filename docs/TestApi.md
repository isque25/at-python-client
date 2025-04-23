# at_client.TestApi

All URIs are relative to *https://api.agenttoolkit.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_rate_limit_api_v1_test_rate_limit_get**](TestApi.md#test_rate_limit_api_v1_test_rate_limit_get) | **GET** /api/v1/test/rate-limit | Test Rate Limit
[**test_rate_limit_api_v1_test_rate_limit_get_0**](TestApi.md#test_rate_limit_api_v1_test_rate_limit_get_0) | **GET** /api/v1/test/rate-limit | Test Rate Limit


# **test_rate_limit_api_v1_test_rate_limit_get**
> Dict[str, object] test_rate_limit_api_v1_test_rate_limit_get()

Test Rate Limit

Test endpoint to demonstrate rate limiting behavior.

This endpoint will return a simple response but will be subject to the
global rate limit. Use it to test if rate limiting is working correctly.

### Example

```python
import time
import os
import at_client
from at_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agenttoolkit.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = at_client.Configuration(
    host = "https://api.agenttoolkit.ai"
)


# Enter a context with an instance of the API client
with at_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = at_client.TestApi(api_client)

    try:
        # Test Rate Limit
        api_response = api_instance.test_rate_limit_api_v1_test_rate_limit_get()
        print("The response of TestApi->test_rate_limit_api_v1_test_rate_limit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_rate_limit_api_v1_test_rate_limit_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rate_limit_api_v1_test_rate_limit_get_0**
> Dict[str, object] test_rate_limit_api_v1_test_rate_limit_get_0()

Test Rate Limit

Test endpoint to demonstrate rate limiting behavior.

This endpoint will return a simple response but will be subject to the
global rate limit. Use it to test if rate limiting is working correctly.

### Example

```python
import time
import os
import at_client
from at_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.agenttoolkit.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = at_client.Configuration(
    host = "https://api.agenttoolkit.ai"
)


# Enter a context with an instance of the API client
with at_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = at_client.TestApi(api_client)

    try:
        # Test Rate Limit
        api_response = api_instance.test_rate_limit_api_v1_test_rate_limit_get_0()
        print("The response of TestApi->test_rate_limit_api_v1_test_rate_limit_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestApi->test_rate_limit_api_v1_test_rate_limit_get_0: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

