# SearchResult

Schema for a single search result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the search result | 
**snippet** | **str** | A clean summary or snippet from the search result | 
**url** | **str** | The URL of the search result | 
**published_date** | **date** |  | [optional] 
**modified_date** | **date** |  | [optional] 
**crawl_date** | **date** |  | [optional] 
**domain** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**enhanced_with_selenium** | **bool** |  | [optional] 

## Example

```python
from at_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print SearchResult.to_json()

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_from_dict = SearchResult.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


