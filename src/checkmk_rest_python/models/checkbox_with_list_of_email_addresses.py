from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_list_of_email_addresses_state import (
    CheckboxWithListOfEmailAddressesState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxWithListOfEmailAddresses")


@_attrs_define
class CheckboxWithListOfEmailAddresses:
    """
    Attributes:
        value (list[str]): You may paste a text from your clipboard which contains several parts separated by ';'
            characters into the last input field. The text will then be split by these separators and the single parts are
            added into dedicated input fields Example: ['email1@tribe.com', 'email2@tribe.com'].
        state (CheckboxWithListOfEmailAddressesState | Unset): To enable or disable this field Example: enabled.
    """

    value: list[str]
    state: CheckboxWithListOfEmailAddressesState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

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
        value = cast(list[str], d.pop("value"))

        _state = d.pop("state", UNSET)
        state: CheckboxWithListOfEmailAddressesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithListOfEmailAddressesState(_state)

        checkbox_with_list_of_email_addresses = cls(
            value=value,
            state=state,
        )

        checkbox_with_list_of_email_addresses.additional_properties = d
        return checkbox_with_list_of_email_addresses

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
