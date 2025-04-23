# SearchResponse

Schema for the search response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query that was processed | 
**results** | [**List[SearchResult]**](SearchResult.md) | List of search results | 
**summary** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**result_count** | **int** | Number of results returned | [optional] [default to 0]
**applied_filters** | **Dict[str, object]** |  | [optional] 
**selenium_enhancement** | **bool** |  | [optional] 
**enhanced_results_count** | **int** |  | [optional] 

## Example

```python
from at_client.models.search_response import SearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponse from a JSON string
search_response_instance = SearchResponse.from_json(json)
# print the JSON string representation of the object
print SearchResponse.to_json()

# convert the object into a dict
search_response_dict = search_response_instance.to_dict()
# create an instance of SearchResponse from a dict
search_response_from_dict = SearchResponse.from_dict(search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


