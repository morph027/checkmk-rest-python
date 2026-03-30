from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_console_alert_attributes_match_type import (
    EventConsoleAlertAttributesMatchType,
)

if TYPE_CHECKING:
    from ..models.event_console_alert_attrs_create import EventConsoleAlertAttrsCreate


T = TypeVar("T", bound="EventConsoleAlertAttributes")


@_attrs_define
class EventConsoleAlertAttributes:
    """
    Attributes:
        match_type (EventConsoleAlertAttributesMatchType):  Example: match_only_event_console_events.
        values (EventConsoleAlertAttrsCreate):
    """

    match_type: EventConsoleAlertAttributesMatchType
    values: EventConsoleAlertAttrsCreate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_type = self.match_type.value

        values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match_type": match_type,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_console_alert_attrs_create import (
            EventConsoleAlertAttrsCreate,
        )

        d = dict(src_dict)
        match_type = EventConsoleAlertAttributesMatchType(d.pop("match_type"))

        values = EventConsoleAlertAttrsCreate.from_dict(d.pop("values"))

        event_console_alert_attributes = cls(
            match_type=match_type,
            values=values,
        )

        event_console_alert_attributes.additional_properties = d
        return event_console_alert_attributes

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
