from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_event_console_alerts_state import CheckboxEventConsoleAlertsState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_console_alert_attributes import EventConsoleAlertAttributes
    from ..models.event_console_alert_attributes_base import (
        EventConsoleAlertAttributesBase,
    )


T = TypeVar("T", bound="CheckboxEventConsoleAlerts")


@_attrs_define
class CheckboxEventConsoleAlerts:
    """
    Attributes:
        value (EventConsoleAlertAttributes | EventConsoleAlertAttributesBase):
        state (CheckboxEventConsoleAlertsState | Unset): To enable or disable this field Example: enabled.
    """

    value: EventConsoleAlertAttributes | EventConsoleAlertAttributesBase
    state: CheckboxEventConsoleAlertsState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_console_alert_attributes import EventConsoleAlertAttributes

        value: dict[str, Any]
        if isinstance(self.value, EventConsoleAlertAttributes):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

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
        from ..models.event_console_alert_attributes import EventConsoleAlertAttributes
        from ..models.event_console_alert_attributes_base import (
            EventConsoleAlertAttributesBase,
        )

        d = dict(src_dict)

        def _parse_value(
            data: object,
        ) -> EventConsoleAlertAttributes | EventConsoleAlertAttributesBase:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_type_selector_type_0 = (
                    EventConsoleAlertAttributes.from_dict(data)
                )

                return componentsschemas_match_type_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_type_selector_type_1 = (
                EventConsoleAlertAttributesBase.from_dict(data)
            )

            return componentsschemas_match_type_selector_type_1

        value = _parse_value(d.pop("value"))

        _state = d.pop("state", UNSET)
        state: CheckboxEventConsoleAlertsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxEventConsoleAlertsState(_state)

        checkbox_event_console_alerts = cls(
            value=value,
            state=state,
        )

        checkbox_event_console_alerts.additional_properties = d
        return checkbox_event_console_alerts

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
