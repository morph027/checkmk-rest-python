from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_contact_group_membership_state import LDAPContactGroupMembershipState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPContactGroupMembership")


@_attrs_define
class LDAPContactGroupMembership:
    """
    Attributes:
        state (LDAPContactGroupMembershipState | Unset):  Example: enabled.
        handle_nested (bool | Unset): When enabled, this plug-in will not only handle direct group memberships, instead
            it will also dig into nested groups and treat the members of those groups as contact group members as well.
            Please bear in mind that this feature might increase the execution time of your LDAP sync.
        sync_from_other_connections (list[str] | Unset): This is a special feature for environments where user accounts
            are located in one LDAP directory and groups objects having them as members are located in other directories.
            You should only enable this feature when you are in this situation and really need it. The current connection is
            always used.
    """

    state: LDAPContactGroupMembershipState | Unset = UNSET
    handle_nested: bool | Unset = UNSET
    sync_from_other_connections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        handle_nested = self.handle_nested

        sync_from_other_connections: list[str] | Unset = UNSET
        if not isinstance(self.sync_from_other_connections, Unset):
            sync_from_other_connections = self.sync_from_other_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if handle_nested is not UNSET:
            field_dict["handle_nested"] = handle_nested
        if sync_from_other_connections is not UNSET:
            field_dict["sync_from_other_connections"] = sync_from_other_connections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPContactGroupMembershipState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPContactGroupMembershipState(_state)

        handle_nested = d.pop("handle_nested", UNSET)

        sync_from_other_connections = cast(
            list[str], d.pop("sync_from_other_connections", UNSET)
        )

        ldap_contact_group_membership = cls(
            state=state,
            handle_nested=handle_nested,
            sync_from_other_connections=sync_from_other_connections,
        )

        ldap_contact_group_membership.additional_properties = d
        return ldap_contact_group_membership

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
