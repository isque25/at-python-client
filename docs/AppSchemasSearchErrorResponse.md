# AppSchemasSearchErrorResponse

Schema for error responses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Error detail message | 

## Example

```python
from at_client.models.app_schemas_search_error_response import AppSchemasSearchErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSchemasSearchErrorResponse from a JSON string
app_schemas_search_error_response_instance = AppSchemasSearchErrorResponse.from_json(json)
# print the JSON string representation of the object
print AppSchemasSearchErrorResponse.to_json()

# convert the object into a dict
app_schemas_search_error_response_dict = app_schemas_search_error_response_instance.to_dict()
# create an instance of AppSchemasSearchErrorResponse from a dict
app_schemas_search_error_response_from_dict = AppSchemasSearchErrorResponse.from_dict(app_schemas_search_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


