from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_response_timeout_state import LDAPResponseTimeoutState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPResponseTimeout")


@_attrs_define
class LDAPResponseTimeout:
    """
    Attributes:
        state (LDAPResponseTimeoutState | Unset):  Example: enabled.
        seconds (int | Unset): Timeout for the initial connection to the LDAP server in seconds. Example: 5.
    """

    state: LDAPResponseTimeoutState | Unset = UNSET
    seconds: int | Unset = UNSET
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
        state: LDAPResponseTimeoutState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPResponseTimeoutState(_state)

        seconds = d.pop("seconds", UNSET)

        ldap_response_timeout = cls(
            state=state,
            seconds=seconds,
        )

        ldap_response_timeout.additional_properties = d
        return ldap_response_timeout

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
