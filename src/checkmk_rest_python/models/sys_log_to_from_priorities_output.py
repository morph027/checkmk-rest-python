from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sys_log_to_from_priorities_output_from_priority import (
    SysLogToFromPrioritiesOutputFromPriority,
)
from ..models.sys_log_to_from_priorities_output_to_priority import (
    SysLogToFromPrioritiesOutputToPriority,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SysLogToFromPrioritiesOutput")


@_attrs_define
class SysLogToFromPrioritiesOutput:
    """
    Attributes:
        from_priority (SysLogToFromPrioritiesOutputFromPriority | Unset):  Example: warning.
        to_priority (SysLogToFromPrioritiesOutputToPriority | Unset):  Example: warning.
    """

    from_priority: SysLogToFromPrioritiesOutputFromPriority | Unset = UNSET
    to_priority: SysLogToFromPrioritiesOutputToPriority | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_priority: str | Unset = UNSET
        if not isinstance(self.from_priority, Unset):
            from_priority = self.from_priority.value

        to_priority: str | Unset = UNSET
        if not isinstance(self.to_priority, Unset):
            to_priority = self.to_priority.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_priority is not UNSET:
            field_dict["from_priority"] = from_priority
        if to_priority is not UNSET:
            field_dict["to_priority"] = to_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_priority = d.pop("from_priority", UNSET)
        from_priority: SysLogToFromPrioritiesOutputFromPriority | Unset
        if isinstance(_from_priority, Unset):
            from_priority = UNSET
        else:
            from_priority = SysLogToFromPrioritiesOutputFromPriority(_from_priority)

        _to_priority = d.pop("to_priority", UNSET)
        to_priority: SysLogToFromPrioritiesOutputToPriority | Unset
        if isinstance(_to_priority, Unset):
            to_priority = UNSET
        else:
            to_priority = SysLogToFromPrioritiesOutputToPriority(_to_priority)

        sys_log_to_from_priorities_output = cls(
            from_priority=from_priority,
            to_priority=to_priority,
        )

        sys_log_to_from_priorities_output.additional_properties = d
        return sys_log_to_from_priorities_output

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
