from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FlexibleDowntimeMode")


@_attrs_define
class FlexibleDowntimeMode:
    """
    Attributes:
        type_ (Any): The downtime starts if the host or service goes down during the specified start and end time
            window. It will then last for at most the given duration, which can extend past the end time. Default:
            'flexible'. Example: flexible.
        duration_minutes (int): The flexible duration in minutes. Example: 120.
    """

    duration_minutes: int
    type_: Any = "flexible"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        duration_minutes = self.duration_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "duration_minutes": duration_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        duration_minutes = d.pop("duration_minutes")

        flexible_downtime_mode = cls(
            type_=type_,
            duration_minutes=duration_minutes,
        )

        flexible_downtime_mode.additional_properties = d
        return flexible_downtime_mode

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
