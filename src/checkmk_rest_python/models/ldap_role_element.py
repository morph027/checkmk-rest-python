from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_role_element_state import LDAPRoleElementState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPRoleElement")


@_attrs_define
class LDAPRoleElement:
    """
    Attributes:
        state (LDAPRoleElementState | Unset):  Example: enabled.
        group_dn (str | Unset): This group must be defined within the scope of the LDAP Group Settings Example: cmk-
            users.
        search_in (str | Unset): An existing ldap connection. Example: LDAP_1.
    """

    state: LDAPRoleElementState | Unset = UNSET
    group_dn: str | Unset = UNSET
    search_in: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        group_dn = self.group_dn

        search_in = self.search_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if group_dn is not UNSET:
            field_dict["group_dn"] = group_dn
        if search_in is not UNSET:
            field_dict["search_in"] = search_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPRoleElementState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPRoleElementState(_state)

        group_dn = d.pop("group_dn", UNSET)

        search_in = d.pop("search_in", UNSET)

        ldap_role_element = cls(
            state=state,
            group_dn=group_dn,
            search_in=search_in,
        )

        ldap_role_element.additional_properties = d
        return ldap_role_element

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
