from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.label_group_condition_1_operator import LabelGroupCondition1Operator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_condition_1 import LabelCondition1


T = TypeVar("T", bound="LabelGroupCondition1")


@_attrs_define
class LabelGroupCondition1:
    """
    Attributes:
        label_group (list[LabelCondition1]): A list of label conditions that form a label group Example: [{'operator':
            'and', 'label': 'os:linux'}].
        operator (LabelGroupCondition1Operator | Unset): Boolean operator that connects the label group to other label
            groups Default: LabelGroupCondition1Operator.AND.
    """

    label_group: list[LabelCondition1]
    operator: LabelGroupCondition1Operator | Unset = LabelGroupCondition1Operator.AND
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_group = []
        for label_group_item_data in self.label_group:
            label_group_item = label_group_item_data.to_dict()
            label_group.append(label_group_item)

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label_group": label_group,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_condition_1 import LabelCondition1

        d = dict(src_dict)
        label_group = []
        _label_group = d.pop("label_group")
        for label_group_item_data in _label_group:
            label_group_item = LabelCondition1.from_dict(label_group_item_data)

            label_group.append(label_group_item)

        _operator = d.pop("operator", UNSET)
        operator: LabelGroupCondition1Operator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = LabelGroupCondition1Operator(_operator)

        label_group_condition_1 = cls(
            label_group=label_group,
            operator=operator,
        )

        label_group_condition_1.additional_properties = d
        return label_group_condition_1

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
