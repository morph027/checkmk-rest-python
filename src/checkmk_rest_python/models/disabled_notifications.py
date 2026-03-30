from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disable_notification_custom_time_range import (
        DisableNotificationCustomTimeRange,
    )


T = TypeVar("T", bound="DisabledNotifications")


@_attrs_define
class DisabledNotifications:
    """
    Attributes:
        disable (bool | Unset): Option if all notifications should be temporarily disabled
        timerange (DisableNotificationCustomTimeRange | Unset):
    """

    disable: bool | Unset = UNSET
    timerange: DisableNotificationCustomTimeRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable = self.disable

        timerange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timerange, Unset):
            timerange = self.timerange.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable is not UNSET:
            field_dict["disable"] = disable
        if timerange is not UNSET:
            field_dict["timerange"] = timerange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disable_notification_custom_time_range import (
            DisableNotificationCustomTimeRange,
        )

        d = dict(src_dict)
        disable = d.pop("disable", UNSET)

        _timerange = d.pop("timerange", UNSET)
        timerange: DisableNotificationCustomTimeRange | Unset
        if isinstance(_timerange, Unset):
            timerange = UNSET
        else:
            timerange = DisableNotificationCustomTimeRange.from_dict(_timerange)

        disabled_notifications = cls(
            disable=disable,
            timerange=timerange,
        )

        disabled_notifications.additional_properties = d
        return disabled_notifications

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
