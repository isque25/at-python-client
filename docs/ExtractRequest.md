# ExtractRequest

Schema for extract request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | List of URLs to extract content from. | 
**include_images** | **bool** | Include images in the response. | [optional] [default to False]
**include_links** | **bool** | Include internal links found on the page in the response. | [optional] [default to False]
**extract_depth** | **str** | Depth of extraction. &#39;advanced&#39; retrieves more data including tables and embedded content. | [optional] [default to 'basic']

## Example

```python
from at_client.models.extract_request import ExtractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractRequest from a JSON string
extract_request_instance = ExtractRequest.from_json(json)
# print the JSON string representation of the object
print ExtractRequest.to_json()

# convert the object into a dict
extract_request_dict = extract_request_instance.to_dict()
# create an instance of ExtractRequest from a dict
extract_request_from_dict = ExtractRequest.from_dict(extract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


