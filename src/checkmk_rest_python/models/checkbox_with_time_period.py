from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_time_period_state import CheckboxWithTimePeriodState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxWithTimePeriod")


@_attrs_define
class CheckboxWithTimePeriod:
    """
    Attributes:
        value (str): Match this rule only during times where the selected time period from the monitoring system is
            active Example: 24X7.
        state (CheckboxWithTimePeriodState | Unset): To enable or disable this field Example: enabled.
    """

    value: str
    state: CheckboxWithTimePeriodState | Unset = UNSET
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
        value = d.pop("value")

        _state = d.pop("state", UNSET)
        state: CheckboxWithTimePeriodState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithTimePeriodState(_state)

        checkbox_with_time_period = cls(
            value=value,
            state=state,
        )

        checkbox_with_time_period.additional_properties = d
        return checkbox_with_time_period

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
