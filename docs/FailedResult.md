# FailedResult

Schema for a failed extraction result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL that failed to be processed. | 
**error** | **str** | Error message describing why the URL couldn&#39;t be processed. | 

## Example

```python
from at_client.models.failed_result import FailedResult

# TODO update the JSON string below
json = "{}"
# create an instance of FailedResult from a JSON string
failed_result_instance = FailedResult.from_json(json)
# print the JSON string representation of the object
print FailedResult.to_json()

# convert the object into a dict
failed_result_dict = failed_result_instance.to_dict()
# create an instance of FailedResult from a dict
failed_result_from_dict = FailedResult.from_dict(failed_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


