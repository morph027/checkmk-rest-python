from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_sort_order_value_state import CheckboxSortOrderValueState
from ..models.checkbox_sort_order_value_value import CheckboxSortOrderValueValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxSortOrderValue")


@_attrs_define
class CheckboxSortOrderValue:
    """
    Attributes:
        value (CheckboxSortOrderValueValue): With this option you can specify, whether the oldest (default) or the
            newest notification should get shown at the top of the notification mail Example: oldest_first.
        state (CheckboxSortOrderValueState | Unset): To enable or disable this field Example: enabled.
    """

    value: CheckboxSortOrderValueValue
    state: CheckboxSortOrderValueState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = CheckboxSortOrderValueValue(d.pop("value"))

        _state = d.pop("state", UNSET)
        state: CheckboxSortOrderValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxSortOrderValueState(_state)

        checkbox_sort_order_value = cls(
            value=value,
            state=state,
        )

        checkbox_sort_order_value.additional_properties = d
        return checkbox_sort_order_value

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
