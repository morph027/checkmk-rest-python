from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThrottlePeriodicNotificationsOutput")


@_attrs_define
class ThrottlePeriodicNotificationsOutput:
    """
    Attributes:
        beginning_from (int | Unset): Beginning notification number Example: 10.
        send_every_nth_notification (int | Unset): The rate then you will receive the notification 1 through 10 and then
            15, 20, 25... and so on Example: 5.
    """

    beginning_from: int | Unset = UNSET
    send_every_nth_notification: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beginning_from = self.beginning_from

        send_every_nth_notification = self.send_every_nth_notification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beginning_from is not UNSET:
            field_dict["beginning_from"] = beginning_from
        if send_every_nth_notification is not UNSET:
            field_dict["send_every_nth_notification"] = send_every_nth_notification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        beginning_from = d.pop("beginning_from", UNSET)

        send_every_nth_notification = d.pop("send_every_nth_notification", UNSET)

        throttle_periodic_notifications_output = cls(
            beginning_from=beginning_from,
            send_every_nth_notification=send_every_nth_notification,
        )

        throttle_periodic_notifications_output.additional_properties = d
        return throttle_periodic_notifications_output

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
