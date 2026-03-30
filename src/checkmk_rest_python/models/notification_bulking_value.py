from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_bulking_value_state import NotificationBulkingValueState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.always_bulk import AlwaysBulk
    from ..models.time_period import TimePeriod


T = TypeVar("T", bound="NotificationBulkingValue")


@_attrs_define
class NotificationBulkingValue:
    """
    Attributes:
        state (NotificationBulkingValueState | Unset): To enable or disable this field Example: enabled.
        value (AlwaysBulk | TimePeriod | Unset):
    """

    state: NotificationBulkingValueState | Unset = UNSET
    value: AlwaysBulk | TimePeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.always_bulk import AlwaysBulk

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: dict[str, Any] | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, AlwaysBulk):
            value = self.value.to_dict()
        else:
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
        from ..models.always_bulk import AlwaysBulk
        from ..models.time_period import TimePeriod

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: NotificationBulkingValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NotificationBulkingValueState(_state)

        def _parse_value(data: object) -> AlwaysBulk | TimePeriod | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_notification_bulking_when_to_bulk_selector_type_0 = (
                    AlwaysBulk.from_dict(data)
                )

                return (
                    componentsschemas_notification_bulking_when_to_bulk_selector_type_0
                )
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_notification_bulking_when_to_bulk_selector_type_1 = (
                TimePeriod.from_dict(data)
            )

            return componentsschemas_notification_bulking_when_to_bulk_selector_type_1

        value = _parse_value(d.pop("value", UNSET))

        notification_bulking_value = cls(
            state=state,
            value=value,
        )

        notification_bulking_value.additional_properties = d
        return notification_bulking_value

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
