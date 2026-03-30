from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subject_for_host_notifications_checkbox_state import (
    SubjectForHostNotificationsCheckboxState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectForHostNotificationsCheckbox")


@_attrs_define
class SubjectForHostNotificationsCheckbox:
    """
    Attributes:
        state (SubjectForHostNotificationsCheckboxState | Unset): To enable or disable this field Example: enabled.
        value (str | Unset): Here you are allowed to use all macros that are defined in the notification context.
            Example: Check_MK: $HOSTNAME$ - $EVENT_TXT$.
    """

    state: SubjectForHostNotificationsCheckboxState | Unset = UNSET
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
        state: SubjectForHostNotificationsCheckboxState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = SubjectForHostNotificationsCheckboxState(_state)

        value = d.pop("value", UNSET)

        subject_for_host_notifications_checkbox = cls(
            state=state,
            value=value,
        )

        subject_for_host_notifications_checkbox.additional_properties = d
        return subject_for_host_notifications_checkbox

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
