# CreditResponse

Schema for the credit usage response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_credits** | **int** |  | 
**used_credits** | **int** |  | 
**remaining_credits** | **int** |  | 
**free_credits** | **int** |  | 
**purchased_credits** | **int** |  | [optional] [default to 0]
**period** | **str** |  | 
**reset_date** | **str** |  | 
**days_until_reset** | **int** |  | 
**plan_tier** | **str** |  | [optional] 

## Example

```python
from at_client.models.credit_response import CreditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditResponse from a JSON string
credit_response_instance = CreditResponse.from_json(json)
# print the JSON string representation of the object
print CreditResponse.to_json()

# convert the object into a dict
credit_response_dict = credit_response_instance.to_dict()
# create an instance of CreditResponse from a dict
credit_response_from_dict = CreditResponse.from_dict(credit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


