from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_over_priority_emergency_level import PushOverPriorityEmergencyLevel

T = TypeVar("T", bound="PushOverPriorityEmergency")


@_attrs_define
class PushOverPriorityEmergency:
    """
    Attributes:
        level (PushOverPriorityEmergencyLevel): The pushover priority level Example: emergency.
        retry (int): The retry interval in seconds Example: 60.
        expire (int): The expiration time in seconds Example: 3600.
        receipt (str): The receipt of the message Example: The receipt can be used to periodically poll receipts API to
            get the status of the notification. See <a href="https://pushover.net/api#receipt" target="_blank">Pushover
            receipts and callbacks</a> for more information..
    """

    level: PushOverPriorityEmergencyLevel
    retry: int
    expire: int
    receipt: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level.value

        retry = self.retry

        expire = self.expire

        receipt = self.receipt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "retry": retry,
                "expire": expire,
                "receipt": receipt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level = PushOverPriorityEmergencyLevel(d.pop("level"))

        retry = d.pop("retry")

        expire = d.pop("expire")

        receipt = d.pop("receipt")

        push_over_priority_emergency = cls(
            level=level,
            retry=retry,
            expire=expire,
            receipt=receipt,
        )

        push_over_priority_emergency.additional_properties = d
        return push_over_priority_emergency

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
