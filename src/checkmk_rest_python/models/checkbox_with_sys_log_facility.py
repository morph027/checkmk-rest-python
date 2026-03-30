from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_sys_log_facility_state import (
    CheckboxWithSysLogFacilityState,
)
from ..models.checkbox_with_sys_log_facility_value import (
    CheckboxWithSysLogFacilityValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxWithSysLogFacility")


@_attrs_define
class CheckboxWithSysLogFacility:
    """
    Attributes:
        state (CheckboxWithSysLogFacilityState | Unset): To enable or disable this field Example: enabled.
        value (CheckboxWithSysLogFacilityValue | Unset):  Example: kern.
    """

    state: CheckboxWithSysLogFacilityState | Unset = UNSET
    value: CheckboxWithSysLogFacilityValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: str | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.value

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
        state: CheckboxWithSysLogFacilityState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithSysLogFacilityState(_state)

        _value = d.pop("value", UNSET)
        value: CheckboxWithSysLogFacilityValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CheckboxWithSysLogFacilityValue(_value)

        checkbox_with_sys_log_facility = cls(
            state=state,
            value=value,
        )

        checkbox_with_sys_log_facility.additional_properties = d
        return checkbox_with_sys_log_facility

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
