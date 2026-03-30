from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPSyncInterval")


@_attrs_define
class LDAPSyncInterval:
    """
    Attributes:
        days (int | Unset):
        hours (int | Unset):
        minutes (int | Unset):
    """

    days: int | Unset = UNSET
    hours: int | Unset = UNSET
    minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        hours = self.hours

        minutes = self.minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days", UNSET)

        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        ldap_sync_interval = cls(
            days=days,
            hours=hours,
            minutes=minutes,
        )

        ldap_sync_interval.additional_properties = d
        return ldap_sync_interval

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
