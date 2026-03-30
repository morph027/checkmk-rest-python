from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sys_log_to_from_priorities_from_priority import (
    SysLogToFromPrioritiesFromPriority,
)
from ..models.sys_log_to_from_priorities_to_priority import (
    SysLogToFromPrioritiesToPriority,
)

T = TypeVar("T", bound="SysLogToFromPriorities")


@_attrs_define
class SysLogToFromPriorities:
    """
    Attributes:
        from_priority (SysLogToFromPrioritiesFromPriority):  Example: warning.
        to_priority (SysLogToFromPrioritiesToPriority):  Example: warning.
    """

    from_priority: SysLogToFromPrioritiesFromPriority
    to_priority: SysLogToFromPrioritiesToPriority
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_priority = self.from_priority.value

        to_priority = self.to_priority.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_priority": from_priority,
                "to_priority": to_priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_priority = SysLogToFromPrioritiesFromPriority(d.pop("from_priority"))

        to_priority = SysLogToFromPrioritiesToPriority(d.pop("to_priority"))

        sys_log_to_from_priorities = cls(
            from_priority=from_priority,
            to_priority=to_priority,
        )

        sys_log_to_from_priorities.additional_properties = d
        return sys_log_to_from_priorities

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
