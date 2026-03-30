from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_condition_1_operator import LabelCondition1Operator
from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelCondition1")


@_attrs_define
class LabelCondition1:
    """
    Attributes:
        label (str): A label of format "{key}:{value}" Example: os:windows.
        operator (LabelCondition1Operator | Unset): Boolean operator that connects the label to other labels within the
            same label group condition
    """

    label: str
    operator: LabelCondition1Operator | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        _operator = d.pop("operator", UNSET)
        operator: LabelCondition1Operator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = LabelCondition1Operator(_operator)

        label_condition_1 = cls(
            label=label,
            operator=operator,
        )

        label_condition_1.additional_properties = d
        return label_condition_1

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
