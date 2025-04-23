# ExtractResult

Schema for a successful extraction result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL from which content was extracted. | 
**raw_content** | **str** | The full content extracted from the page. | 
**images** | **List[str]** |  | [optional] 
**links** | **List[str]** |  | [optional] 
**cache_hit** | **bool** | Indicates if this result was served from cache. | [optional] [default to False]

## Example

```python
from at_client.models.extract_result import ExtractResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractResult from a JSON string
extract_result_instance = ExtractResult.from_json(json)
# print the JSON string representation of the object
print ExtractResult.to_json()

# convert the object into a dict
extract_result_dict = extract_result_instance.to_dict()
# create an instance of ExtractResult from a dict
extract_result_from_dict = ExtractResult.from_dict(extract_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


