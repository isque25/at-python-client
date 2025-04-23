# AppModelsCoreErrorResponse

Standard error response model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Error message | 
**code** | **str** |  | [optional] 
**errors** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from at_client.models.app_models_core_error_response import AppModelsCoreErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppModelsCoreErrorResponse from a JSON string
app_models_core_error_response_instance = AppModelsCoreErrorResponse.from_json(json)
# print the JSON string representation of the object
print AppModelsCoreErrorResponse.to_json()

# convert the object into a dict
app_models_core_error_response_dict = app_models_core_error_response_instance.to_dict()
# create an instance of AppModelsCoreErrorResponse from a dict
app_models_core_error_response_from_dict = AppModelsCoreErrorResponse.from_dict(app_models_core_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


