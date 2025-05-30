# coding: utf-8

"""
    \"Agent Toolkit: LLM-Friendly Tools and Search APIs\"

    API for LLM-friendly web search and content retrieval

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class AppSchemasSearchErrorResponse(BaseModel):
    """
    Schema for error responses  # noqa: E501
    """
    detail: StrictStr = Field(default=..., description="Error detail message")
    __properties = ["detail"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AppSchemasSearchErrorResponse:
        """Create an instance of AppSchemasSearchErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AppSchemasSearchErrorResponse:
        """Create an instance of AppSchemasSearchErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AppSchemasSearchErrorResponse.parse_obj(obj)

        _obj = AppSchemasSearchErrorResponse.parse_obj({
            "detail": obj.get("detail")
        })
        return _obj


