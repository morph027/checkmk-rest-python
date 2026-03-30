from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_connect_timeout_state import LDAPConnectTimeoutState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPConnectTimeout")


@_attrs_define
class LDAPConnectTimeout:
    """
    Attributes:
        state (LDAPConnectTimeoutState | Unset):  Example: enabled.
        seconds (float | Unset): Timeout for the initial connection to the LDAP server in seconds. Example: 2.0.
    """

    state: LDAPConnectTimeoutState | Unset = UNSET
    seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if seconds is not UNSET:
            field_dict["seconds"] = seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPConnectTimeoutState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPConnectTimeoutState(_state)

        seconds = d.pop("seconds", UNSET)

        ldap_connect_timeout = cls(
            state=state,
            seconds=seconds,
        )

        ldap_connect_timeout.additional_properties = d
        return ldap_connect_timeout

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
