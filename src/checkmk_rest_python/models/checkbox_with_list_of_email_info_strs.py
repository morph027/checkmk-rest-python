from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_list_of_email_info_strs_state import (
    CheckboxWithListOfEmailInfoStrsState,
)
from ..models.checkbox_with_list_of_email_info_strs_value_item import (
    CheckboxWithListOfEmailInfoStrsValueItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxWithListOfEmailInfoStrs")


@_attrs_define
class CheckboxWithListOfEmailInfoStrs:
    """
    Attributes:
        value (list[CheckboxWithListOfEmailInfoStrsValueItem]): Information to be displayed in the email body. Example:
            ['abstime', 'graph'].
        state (CheckboxWithListOfEmailInfoStrsState | Unset): To enable or disable this field Example: enabled.
    """

    value: list[CheckboxWithListOfEmailInfoStrsValueItem]
    state: CheckboxWithListOfEmailInfoStrsState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = []
        for value_item_data in self.value:
            value_item = value_item_data.value
            value.append(value_item)

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
        value = []
        _value = d.pop("value")
        for value_item_data in _value:
            value_item = CheckboxWithListOfEmailInfoStrsValueItem(value_item_data)

            value.append(value_item)

        _state = d.pop("state", UNSET)
        state: CheckboxWithListOfEmailInfoStrsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithListOfEmailInfoStrsState(_state)

        checkbox_with_list_of_email_info_strs = cls(
            value=value,
            state=state,
        )

        checkbox_with_list_of_email_info_strs.additional_properties = d
        return checkbox_with_list_of_email_info_strs

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
