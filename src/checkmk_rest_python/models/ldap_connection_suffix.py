from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_connection_suffix_state import LDAPConnectionSuffixState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPConnectionSuffix")


@_attrs_define
class LDAPConnectionSuffix:
    """
    Attributes:
        state (LDAPConnectionSuffixState | Unset):  Example: enabled.
        suffix (str | Unset): The LDAP connection suffix can be used to distinguish equal named objects (name
            conflicts), for example user accounts, from different LDAP connections. Example: suffix_example.
    """

    state: LDAPConnectionSuffixState | Unset = UNSET
    suffix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        suffix = self.suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if suffix is not UNSET:
            field_dict["suffix"] = suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPConnectionSuffixState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPConnectionSuffixState(_state)

        suffix = d.pop("suffix", UNSET)

        ldap_connection_suffix = cls(
            state=state,
            suffix=suffix,
        )

        ldap_connection_suffix.additional_properties = d
        return ldap_connection_suffix

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
