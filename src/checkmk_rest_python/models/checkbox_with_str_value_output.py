from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_str_value_output_state import (
    CheckboxWithStrValueOutputState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxWithStrValueOutput")


@_attrs_define
class CheckboxWithStrValueOutput:
    """
    Attributes:
        state (CheckboxWithStrValueOutputState | Unset): To enable or disable this field Example: enabled.
        value (str | Unset):
    """

    state: CheckboxWithStrValueOutputState | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckboxWithStrValueOutputState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithStrValueOutputState(_state)

        value = d.pop("value", UNSET)

        checkbox_with_str_value_output = cls(
            state=state,
            value=value,
        )

        checkbox_with_str_value_output.additional_properties = d
        return checkbox_with_str_value_output

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
