from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_version_state import LDAPVersionState
from ..models.ldap_version_version import LDAPVersionVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPVersion")


@_attrs_define
class LDAPVersion:
    """
    Attributes:
        state (LDAPVersionState | Unset):  Example: enabled.
        version (LDAPVersionVersion | Unset): The selected LDAP version the LDAP server is serving. Most modern servers
            use LDAP version 3. Example: 3.
    """

    state: LDAPVersionState | Unset = UNSET
    version: LDAPVersionVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        version: int | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPVersionState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPVersionState(_state)

        _version = d.pop("version", UNSET)
        version: LDAPVersionVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = LDAPVersionVersion(_version)

        ldap_version = cls(
            state=state,
            version=version,
        )

        ldap_version.additional_properties = d
        return ldap_version

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
