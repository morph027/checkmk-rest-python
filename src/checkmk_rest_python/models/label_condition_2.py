from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_condition_2_operator import LabelCondition2Operator

T = TypeVar("T", bound="LabelCondition2")


@_attrs_define
class LabelCondition2:
    """
    Attributes:
        key (str): The key of the label. e.g. 'os' in 'os:windows'
        operator (LabelCondition2Operator): How the label should be matched.
        value (str): The value of the label. e.g. 'windows' in 'os:windows'
    """

    key: str
    operator: LabelCondition2Operator
    value: str
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

        operator = LabelCondition2Operator(d.pop("operator"))

        value = d.pop("value")

        label_condition_2 = cls(
            key=key,
            operator=operator,
            value=value,
        )

        label_condition_2.additional_properties = d
        return label_condition_2

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
