from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_sys_log_facility_to_use_value_state import (
    CheckboxSysLogFacilityToUseValueState,
)
from ..models.checkbox_sys_log_facility_to_use_value_value import (
    CheckboxSysLogFacilityToUseValueValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxSysLogFacilityToUseValue")


@_attrs_define
class CheckboxSysLogFacilityToUseValue:
    """
    Attributes:
        state (CheckboxSysLogFacilityToUseValueState | Unset): To enable or disable this field Example: enabled.
        value (CheckboxSysLogFacilityToUseValueValue | Unset):
    """

    state: CheckboxSysLogFacilityToUseValueState | Unset = UNSET
    value: CheckboxSysLogFacilityToUseValueValue | Unset = UNSET
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
        state: CheckboxSysLogFacilityToUseValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxSysLogFacilityToUseValueState(_state)

        _value = d.pop("value", UNSET)
        value: CheckboxSysLogFacilityToUseValueValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CheckboxSysLogFacilityToUseValueValue(_value)

        checkbox_sys_log_facility_to_use_value = cls(
            state=state,
            value=value,
        )

        checkbox_sys_log_facility_to_use_value.additional_properties = d
        return checkbox_sys_log_facility_to_use_value

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
