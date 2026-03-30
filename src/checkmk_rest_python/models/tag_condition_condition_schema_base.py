from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_condition_condition_schema_base_operator import (
    TagConditionConditionSchemaBaseOperator,
)

T = TypeVar("T", bound="TagConditionConditionSchemaBase")


@_attrs_define
class TagConditionConditionSchemaBase:
    """
    Attributes:
        key (str): The name of the tag.
        operator (TagConditionConditionSchemaBaseOperator): If the matched tag should be one of the given values, or
            not.
        value (list[str]): A list of values for the tag.
    """

    key: str
    operator: TagConditionConditionSchemaBaseOperator
    value: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        operator = self.operator.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        operator = TagConditionConditionSchemaBaseOperator(d.pop("operator"))

        value = cast(list[str], d.pop("value"))

        tag_condition_condition_schema_base = cls(
            key=key,
            operator=operator,
            value=value,
        )

        tag_condition_condition_schema_base.additional_properties = d
        return tag_condition_condition_schema_base

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
