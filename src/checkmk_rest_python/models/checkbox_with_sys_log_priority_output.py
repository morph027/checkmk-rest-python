from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_sys_log_priority_output_state import (
    CheckboxWithSysLogPriorityOutputState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sys_log_to_from_priorities_output import SysLogToFromPrioritiesOutput


T = TypeVar("T", bound="CheckboxWithSysLogPriorityOutput")


@_attrs_define
class CheckboxWithSysLogPriorityOutput:
    """
    Attributes:
        state (CheckboxWithSysLogPriorityOutputState | Unset): To enable or disable this field Example: enabled.
        value (SysLogToFromPrioritiesOutput | Unset):
    """

    state: CheckboxWithSysLogPriorityOutputState | Unset = UNSET
    value: SysLogToFromPrioritiesOutput | Unset = UNSET
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
        from ..models.sys_log_to_from_priorities_output import (
            SysLogToFromPrioritiesOutput,
        )

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckboxWithSysLogPriorityOutputState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithSysLogPriorityOutputState(_state)

        _value = d.pop("value", UNSET)
        value: SysLogToFromPrioritiesOutput | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = SysLogToFromPrioritiesOutput.from_dict(_value)

        checkbox_with_sys_log_priority_output = cls(
            state=state,
            value=value,
        )

        checkbox_with_sys_log_priority_output.additional_properties = d
        return checkbox_with_sys_log_priority_output

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
