from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_sync_interval import LDAPSyncInterval


T = TypeVar("T", bound="LDAPOther")


@_attrs_define
class LDAPOther:
    """
    Attributes:
        sync_interval (LDAPSyncInterval | Unset):
    """

    sync_interval: LDAPSyncInterval | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync_interval, Unset):
            sync_interval = self.sync_interval.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_interval is not UNSET:
            field_dict["sync_interval"] = sync_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_sync_interval import LDAPSyncInterval

        d = dict(src_dict)
        _sync_interval = d.pop("sync_interval", UNSET)
        sync_interval: LDAPSyncInterval | Unset
        if isinstance(_sync_interval, Unset):
            sync_interval = UNSET
        else:
            sync_interval = LDAPSyncInterval.from_dict(_sync_interval)

        ldap_other = cls(
            sync_interval=sync_interval,
        )

        ldap_other.additional_properties = d
        return ldap_other

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
