from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldaptcp_port_state import LDAPTCPPortState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPTCPPort")


@_attrs_define
class LDAPTCPPort:
    """
    Attributes:
        state (LDAPTCPPortState | Unset):  Example: enabled.
        port (int | Unset):  Example: 389.
    """

    state: LDAPTCPPortState | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPTCPPortState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPTCPPortState(_state)

        port = d.pop("port", UNSET)

        ldaptcp_port = cls(
            state=state,
            port=port,
        )

        ldaptcp_port.additional_properties = d
        return ldaptcp_port

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
