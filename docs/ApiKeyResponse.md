# ApiKeyResponse

Schema for API key response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Unique identifier for the API key | 
**api_key** | **str** | The actual API key (shown only once) | 
**name** | **str** | Name/description for this API key | 
**tier** | [**RateLimitTier**](RateLimitTier.md) | Rate limit tier | 
**created_at** | **datetime** | When the key was created | 
**rate_limit** | **int** | Requests per minute allowed | 

## Example

```python
from at_client.models.api_key_response import ApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponse from a JSON string
api_key_response_instance = ApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print ApiKeyResponse.to_json()

# convert the object into a dict
api_key_response_dict = api_key_response_instance.to_dict()
# create an instance of ApiKeyResponse from a dict
api_key_response_from_dict = ApiKeyResponse.from_dict(api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


