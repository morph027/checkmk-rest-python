from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_restrict_notification_numbers_output_state import (
    CheckboxRestrictNotificationNumbersOutputState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.from_to_notification_numbers_output import (
        FromToNotificationNumbersOutput,
    )


T = TypeVar("T", bound="CheckboxRestrictNotificationNumbersOutput")


@_attrs_define
class CheckboxRestrictNotificationNumbersOutput:
    """
    Attributes:
        state (CheckboxRestrictNotificationNumbersOutputState | Unset): To enable or disable this field Example:
            enabled.
        value (FromToNotificationNumbersOutput | Unset):
    """

    state: CheckboxRestrictNotificationNumbersOutputState | Unset = UNSET
    value: FromToNotificationNumbersOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

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
        from ..models.from_to_notification_numbers_output import (
            FromToNotificationNumbersOutput,
        )

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckboxRestrictNotificationNumbersOutputState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxRestrictNotificationNumbersOutputState(_state)

        _value = d.pop("value", UNSET)
        value: FromToNotificationNumbersOutput | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = FromToNotificationNumbersOutput.from_dict(_value)

        checkbox_restrict_notification_numbers_output = cls(
            state=state,
            value=value,
        )

        checkbox_restrict_notification_numbers_output.additional_properties = d
        return checkbox_restrict_notification_numbers_output

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
