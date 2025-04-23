# ApiKeyInfo

Schema for API key information (without the actual key)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Unique identifier for the API key | 
**name** | **str** | Name/description for this API key | 
**tier** | [**RateLimitTier**](RateLimitTier.md) | Rate limit tier | 
**status** | [**ApiKeyStatus**](ApiKeyStatus.md) | Status of the API key | 
**created_at** | **datetime** | When the key was created | 
**last_used_at** | **datetime** |  | [optional] 
**rate_limit** | **int** | Requests per minute allowed | 

## Example

```python
from at_client.models.api_key_info import ApiKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyInfo from a JSON string
api_key_info_instance = ApiKeyInfo.from_json(json)
# print the JSON string representation of the object
print ApiKeyInfo.to_json()

# convert the object into a dict
api_key_info_dict = api_key_info_instance.to_dict()
# create an instance of ApiKeyInfo from a dict
api_key_info_from_dict = ApiKeyInfo.from_dict(api_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


