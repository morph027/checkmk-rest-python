from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_console_alerts_response_match_type import (
    EventConsoleAlertsResponseMatchType,
)
from ..models.event_console_alerts_response_state import EventConsoleAlertsResponseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_console_alert_attrs_response import (
        EventConsoleAlertAttrsResponse,
    )


T = TypeVar("T", bound="EventConsoleAlertsResponse")


@_attrs_define
class EventConsoleAlertsResponse:
    """
    Attributes:
        state (EventConsoleAlertsResponseState | Unset): To enable or disable this field Example: enabled.
        match_type (EventConsoleAlertsResponseMatchType | Unset):  Example: match_only_event_console_events.
        values (EventConsoleAlertAttrsResponse | Unset):
    """

    state: EventConsoleAlertsResponseState | Unset = UNSET
    match_type: EventConsoleAlertsResponseMatchType | Unset = UNSET
    values: EventConsoleAlertAttrsResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        match_type: str | Unset = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type.value

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_console_alert_attrs_response import (
            EventConsoleAlertAttrsResponse,
        )

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: EventConsoleAlertsResponseState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EventConsoleAlertsResponseState(_state)

        _match_type = d.pop("match_type", UNSET)
        match_type: EventConsoleAlertsResponseMatchType | Unset
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = EventConsoleAlertsResponseMatchType(_match_type)

        _values = d.pop("values", UNSET)
        values: EventConsoleAlertAttrsResponse | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = EventConsoleAlertAttrsResponse.from_dict(_values)

        event_console_alerts_response = cls(
            state=state,
            match_type=match_type,
            values=values,
        )

        event_console_alerts_response.additional_properties = d
        return event_console_alerts_response

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
