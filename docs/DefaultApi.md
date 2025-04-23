# at_client.DefaultApi

All URIs are relative to *https://api.agenttoolkit.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_google_options_api_v1_auth_google_options**](DefaultApi.md#auth_google_options_api_v1_auth_google_options) | **OPTIONS** /api/v1/auth/google | Auth Google Options
[**auth_logout_options_api_v1_auth_logout_options**](DefaultApi.md#auth_logout_options_api_v1_auth_logout_options) | **OPTIONS** /api/v1/auth/logout | Auth Logout Options
[**auth_me_options_api_v1_auth_me_options**](DefaultApi.md#auth_me_options_api_v1_auth_me_options) | **OPTIONS** /api/v1/auth/me | Auth Me Options
[**create_api_key_endpoint_api_v1_api_keys_post**](DefaultApi.md#create_api_key_endpoint_api_v1_api_keys_post) | **POST** /api/v1/api-keys | Create Api Key Endpoint
[**extract_content_api_v1_extract_post**](DefaultApi.md#extract_content_api_v1_extract_post) | **POST** /api/v1/extract | Extract Content
[**extract_content_get_api_v1_extract_get**](DefaultApi.md#extract_content_get_api_v1_extract_get) | **GET** /api/v1/extract | Extract Content Get
[**get_current_user_info_api_v1_auth_me_get**](DefaultApi.md#get_current_user_info_api_v1_auth_me_get) | **GET** /api/v1/auth/me | Get Current User Info
[**get_providers_api_v1_providers_get**](DefaultApi.md#get_providers_api_v1_providers_get) | **GET** /api/v1/providers | Get Providers
[**google_auth_api_v1_auth_google_post**](DefaultApi.md#google_auth_api_v1_auth_google_post) | **POST** /api/v1/auth/google | Google Auth
[**list_api_keys_api_v1_api_keys_get**](DefaultApi.md#list_api_keys_api_v1_api_keys_get) | **GET** /api/v1/api-keys | List Api Keys
[**logout_api_v1_auth_logout_post**](DefaultApi.md#logout_api_v1_auth_logout_post) | **POST** /api/v1/auth/logout | Logout
[**providers_options_api_v1_providers_options**](DefaultApi.md#providers_options_api_v1_providers_options) | **OPTIONS** /api/v1/providers | Providers Options
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**search_api_v1_search_get**](DefaultApi.md#search_api_v1_search_get) | **GET** /api/v1/search | Search
[**update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put**](DefaultApi.md#update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put) | **PUT** /api/v1/api-keys/{key_id}/status | Update Api Key Status Endpoint


# **auth_google_options_api_v1_auth_google_options**
> object auth_google_options_api_v1_auth_google_options()

Auth Google Options

Handle preflight OPTIONS request for Google auth endpoint

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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Auth Google Options
        api_response = api_instance.auth_google_options_api_v1_auth_google_options()
        print("The response of DefaultApi->auth_google_options_api_v1_auth_google_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_google_options_api_v1_auth_google_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **auth_logout_options_api_v1_auth_logout_options**
> object auth_logout_options_api_v1_auth_logout_options()

Auth Logout Options

Handle preflight OPTIONS request for auth/logout endpoint

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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Auth Logout Options
        api_response = api_instance.auth_logout_options_api_v1_auth_logout_options()
        print("The response of DefaultApi->auth_logout_options_api_v1_auth_logout_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_logout_options_api_v1_auth_logout_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **auth_me_options_api_v1_auth_me_options**
> object auth_me_options_api_v1_auth_me_options()

Auth Me Options

Handle preflight OPTIONS request for auth/me endpoint

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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Auth Me Options
        api_response = api_instance.auth_me_options_api_v1_auth_me_options()
        print("The response of DefaultApi->auth_me_options_api_v1_auth_me_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->auth_me_options_api_v1_auth_me_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **create_api_key_endpoint_api_v1_api_keys_post**
> ApiKeyResponse create_api_key_endpoint_api_v1_api_keys_post(api_key_create, auth_token=auth_token)

Create Api Key Endpoint

Create a new API key for the authenticated user

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import at_client
from at_client.models.api_key_create import ApiKeyCreate
from at_client.models.api_key_response import ApiKeyResponse
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
    api_instance = at_client.DefaultApi(api_client)
    api_key_create = at_client.ApiKeyCreate() # ApiKeyCreate | 
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # Create Api Key Endpoint
        api_response = api_instance.create_api_key_endpoint_api_v1_api_keys_post(api_key_create, auth_token=auth_token)
        print("The response of DefaultApi->create_api_key_endpoint_api_v1_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_api_key_endpoint_api_v1_api_keys_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create** | [**ApiKeyCreate**](ApiKeyCreate.md)|  | 
 **auth_token** | **str**|  | [optional] 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_content_api_v1_extract_post**
> ExtractResponse extract_content_api_v1_extract_post(extract_request)

Extract Content

Extract content from one or more URLs using Selenium.

Args:
    request: ExtractRequest object with URLs and extraction options
    
Returns:
    ExtractResponse with extraction results and metadata

### Example

```python
import time
import os
import at_client
from at_client.models.extract_request import ExtractRequest
from at_client.models.extract_response import ExtractResponse
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
    api_instance = at_client.DefaultApi(api_client)
    extract_request = at_client.ExtractRequest() # ExtractRequest | 

    try:
        # Extract Content
        api_response = api_instance.extract_content_api_v1_extract_post(extract_request)
        print("The response of DefaultApi->extract_content_api_v1_extract_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->extract_content_api_v1_extract_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_request** | [**ExtractRequest**](ExtractRequest.md)|  | 

### Return type

[**ExtractResponse**](ExtractResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_content_get_api_v1_extract_get**
> ExtractResponse extract_content_get_api_v1_extract_get(url, include_images=include_images, include_links=include_links, extract_depth=extract_depth)

Extract Content Get

Extract content from a URL using Selenium (GET method).

Args:
    url: URL to extract content from
    include_images: Whether to include images in the result
    include_links: Whether to include internal links in the result
    extract_depth: Depth of extraction ("basic" or "advanced")

Returns:
    ExtractResponse with extraction results and metadata

### Example

```python
import time
import os
import at_client
from at_client.models.extract_response import ExtractResponse
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
    api_instance = at_client.DefaultApi(api_client)
    url = 'url_example' # str | URL to extract content from
    include_images = False # bool | Include images in the response (optional) (default to False)
    include_links = False # bool | Include internal links found on the page in the response (optional) (default to False)
    extract_depth = 'basic' # str | Depth of extraction ('basic' or 'advanced') (optional) (default to 'basic')

    try:
        # Extract Content Get
        api_response = api_instance.extract_content_get_api_v1_extract_get(url, include_images=include_images, include_links=include_links, extract_depth=extract_depth)
        print("The response of DefaultApi->extract_content_get_api_v1_extract_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->extract_content_get_api_v1_extract_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL to extract content from | 
 **include_images** | **bool**| Include images in the response | [optional] [default to False]
 **include_links** | **bool**| Include internal links found on the page in the response | [optional] [default to False]
 **extract_depth** | **str**| Depth of extraction (&#39;basic&#39; or &#39;advanced&#39;) | [optional] [default to &#39;basic&#39;]

### Return type

[**ExtractResponse**](ExtractResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info_api_v1_auth_me_get**
> Dict[str, object] get_current_user_info_api_v1_auth_me_get(auth_token=auth_token)

Get Current User Info

Get current user information from cookie authentication

### Example

* OAuth Authentication (OAuth2PasswordBearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with at_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = at_client.DefaultApi(api_client)
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # Get Current User Info
        api_response = api_instance.get_current_user_info_api_v1_auth_me_get(auth_token=auth_token)
        print("The response of DefaultApi->get_current_user_info_api_v1_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_current_user_info_api_v1_auth_me_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_providers_api_v1_providers_get**
> List[Dict[str, object]] get_providers_api_v1_providers_get(auth_token=auth_token)

Get Providers

Return a list of available search providers and their capabilities.

This endpoint returns information about all search providers supported
by the API, including their capabilities, requirements, and other metadata.

Returns:
    List of provider objects with details about each provider

### Example

* OAuth Authentication (OAuth2PasswordBearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with at_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = at_client.DefaultApi(api_client)
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # Get Providers
        api_response = api_instance.get_providers_api_v1_providers_get(auth_token=auth_token)
        print("The response of DefaultApi->get_providers_api_v1_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_providers_api_v1_providers_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | [optional] 

### Return type

**List[Dict[str, object]]**

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

# **google_auth_api_v1_auth_google_post**
> object google_auth_api_v1_auth_google_post(request_body)

Google Auth

Authenticate a user with Google OAuth token and set HTTP-only cookie

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
    api_instance = at_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Google Auth
        api_response = api_instance.google_auth_api_v1_auth_google_post(request_body)
        print("The response of DefaultApi->google_auth_api_v1_auth_google_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->google_auth_api_v1_auth_google_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys_api_v1_api_keys_get**
> List[ApiKeyInfo] list_api_keys_api_v1_api_keys_get(auth_token=auth_token)

List Api Keys

List all API keys for the authenticated user

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import at_client
from at_client.models.api_key_info import ApiKeyInfo
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
    api_instance = at_client.DefaultApi(api_client)
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # List Api Keys
        api_response = api_instance.list_api_keys_api_v1_api_keys_get(auth_token=auth_token)
        print("The response of DefaultApi->list_api_keys_api_v1_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_api_keys_api_v1_api_keys_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_token** | **str**|  | [optional] 

### Return type

[**List[ApiKeyInfo]**](ApiKeyInfo.md)

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

# **logout_api_v1_auth_logout_post**
> object logout_api_v1_auth_logout_post()

Logout

Log out a user by clearing the auth cookie

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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Logout
        api_response = api_instance.logout_api_v1_auth_logout_post()
        print("The response of DefaultApi->logout_api_v1_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->logout_api_v1_auth_logout_post: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **providers_options_api_v1_providers_options**
> object providers_options_api_v1_providers_options()

Providers Options

Handle preflight OPTIONS request for providers endpoint

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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Providers Options
        api_response = api_instance.providers_options_api_v1_providers_options()
        print("The response of DefaultApi->providers_options_api_v1_providers_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->providers_options_api_v1_providers_options: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **root_get**
> object root_get()

Root



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
    api_instance = at_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **search_api_v1_search_get**
> SearchResponse search_api_v1_search_get(query, language=language, country=country, max_results=max_results, summarize=summarize, provider=provider, topic=topic, use_selenium=use_selenium, published_start_date=published_start_date, published_end_date=published_end_date, crawl_start_date=crawl_start_date, crawl_end_date=crawl_end_date, include_domains=include_domains, exclude_domains=exclude_domains, include_terms=include_terms, exclude_terms=exclude_terms)

Search

Search endpoint that returns formatted results from external search provider.

Args:
    query: The search query string
    language: Optional ISO language code (e.g., 'en', 'fr')
    country: Optional country code (e.g., 'us', 'gb')
    max_results: Maximum number of results to return (1-10)
    summarize: Whether to generate a summary of results using LLM
    provider: Search provider to use (google, bing, duckduckgo)
    topic: Search topic category
    use_selenium: Whether to enhance DuckDuckGo results with Selenium
    published_start_date: Filter results published after this date
    published_end_date: Filter results published before this date
    crawl_start_date: Filter results crawled after this date
    crawl_end_date: Filter results crawled before this date
    include_domains: Filter results to only include these domains
    exclude_domains: Filter results to exclude these domains
    include_terms: Filter results to only include these terms
    exclude_terms: Filter results to exclude these terms
    
Returns:
    JSON response with formatted search results

### Example

```python
import time
import os
import at_client
from at_client.models.search_response import SearchResponse
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
    api_instance = at_client.DefaultApi(api_client)
    query = 'query_example' # str | Search query string
    language = 'language_example' # str | ISO language code (e.g., 'en', 'fr') (optional)
    country = 'country_example' # str | Country code (e.g., 'us', 'gb') (optional)
    max_results = 10 # int | Maximum number of results to return (optional) (default to 10)
    summarize = False # bool | Whether to generate a summary of results using LLM (optional) (default to False)
    provider = 'provider_example' # str | Search provider to use (optional)
    topic = 'general' # str | Search topic category (optional) (default to 'general')
    use_selenium = True # bool | Whether to enhance DuckDuckGo results with Selenium (only applies to DuckDuckGo provider) (optional) (default to True)
    published_start_date = '2013-10-20' # date | Start date for published content (YYYY-MM-DD) (optional)
    published_end_date = '2013-10-20' # date | End date for published content (YYYY-MM-DD) (optional)
    crawl_start_date = '2013-10-20' # date | Start date for crawled content (YYYY-MM-DD) (optional)
    crawl_end_date = '2013-10-20' # date | End date for crawled content (YYYY-MM-DD) (optional)
    include_domains = ['include_domains_example'] # List[str] | Domains to include in search results (optional)
    exclude_domains = ['exclude_domains_example'] # List[str] | Domains to exclude from search results (optional)
    include_terms = ['include_terms_example'] # List[str] | Terms that must be included in search results (optional)
    exclude_terms = ['exclude_terms_example'] # List[str] | Terms that must be excluded from search results (optional)

    try:
        # Search
        api_response = api_instance.search_api_v1_search_get(query, language=language, country=country, max_results=max_results, summarize=summarize, provider=provider, topic=topic, use_selenium=use_selenium, published_start_date=published_start_date, published_end_date=published_end_date, crawl_start_date=crawl_start_date, crawl_end_date=crawl_end_date, include_domains=include_domains, exclude_domains=exclude_domains, include_terms=include_terms, exclude_terms=exclude_terms)
        print("The response of DefaultApi->search_api_v1_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_api_v1_search_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query string | 
 **language** | **str**| ISO language code (e.g., &#39;en&#39;, &#39;fr&#39;) | [optional] 
 **country** | **str**| Country code (e.g., &#39;us&#39;, &#39;gb&#39;) | [optional] 
 **max_results** | **int**| Maximum number of results to return | [optional] [default to 10]
 **summarize** | **bool**| Whether to generate a summary of results using LLM | [optional] [default to False]
 **provider** | **str**| Search provider to use | [optional] 
 **topic** | **str**| Search topic category | [optional] [default to &#39;general&#39;]
 **use_selenium** | **bool**| Whether to enhance DuckDuckGo results with Selenium (only applies to DuckDuckGo provider) | [optional] [default to True]
 **published_start_date** | **date**| Start date for published content (YYYY-MM-DD) | [optional] 
 **published_end_date** | **date**| End date for published content (YYYY-MM-DD) | [optional] 
 **crawl_start_date** | **date**| Start date for crawled content (YYYY-MM-DD) | [optional] 
 **crawl_end_date** | **date**| End date for crawled content (YYYY-MM-DD) | [optional] 
 **include_domains** | [**List[str]**](str.md)| Domains to include in search results | [optional] 
 **exclude_domains** | [**List[str]**](str.md)| Domains to exclude from search results | [optional] 
 **include_terms** | [**List[str]**](str.md)| Terms that must be included in search results | [optional] 
 **exclude_terms** | [**List[str]**](str.md)| Terms that must be excluded from search results | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put**
> object update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put(key_id, status, auth_token=auth_token)

Update Api Key Status Endpoint

Update the status of an API key (activate, disable, revoke)

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import at_client
from at_client.models.api_key_status import ApiKeyStatus
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
    api_instance = at_client.DefaultApi(api_client)
    key_id = 'key_id_example' # str | 
    status = at_client.ApiKeyStatus() # ApiKeyStatus | 
    auth_token = 'auth_token_example' # str |  (optional)

    try:
        # Update Api Key Status Endpoint
        api_response = api_instance.update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put(key_id, status, auth_token=auth_token)
        print("The response of DefaultApi->update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_api_key_status_endpoint_api_v1_api_keys_key_id_status_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **status** | [**ApiKeyStatus**](.md)|  | 
 **auth_token** | **str**|  | [optional] 

### Return type

**object**

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

