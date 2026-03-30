from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_console_alert_attributes_base_match_type import (
    EventConsoleAlertAttributesBaseMatchType,
)

T = TypeVar("T", bound="EventConsoleAlertAttributesBase")


@_attrs_define
class EventConsoleAlertAttributesBase:
    """
    Attributes:
        match_type (EventConsoleAlertAttributesBaseMatchType):  Example: match_only_event_console_events.
    """

    match_type: EventConsoleAlertAttributesBaseMatchType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_type = self.match_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match_type": match_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_type = EventConsoleAlertAttributesBaseMatchType(d.pop("match_type"))

        event_console_alert_attributes_base = cls(
            match_type=match_type,
        )

        event_console_alert_attributes_base.additional_properties = d
        return event_console_alert_attributes_base

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
