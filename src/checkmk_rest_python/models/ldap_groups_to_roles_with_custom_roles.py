from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_groups_to_roles_with_custom_roles_state import (
    LDAPGroupsToRolesWithCustomRolesState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_role_element import LDAPRoleElement


T = TypeVar("T", bound="LDAPGroupsToRolesWithCustomRoles")


@_attrs_define
class LDAPGroupsToRolesWithCustomRoles:
    """
    Attributes:
        state (LDAPGroupsToRolesWithCustomRolesState | Unset):  Example: enabled.
        handle_nested (bool | Unset): Once you enable this option, this plug-in will not only handle direct group
            memberships, instead it will also dig into nested groups and treat the members of those groups as contact group
            members as well. Please bear in mind that this feature might increase the execution time of your LDAP sync
        admin (list[LDAPRoleElement] | Unset):
        agent_registration (list[LDAPRoleElement] | Unset):
        guest (list[LDAPRoleElement] | Unset):
        user (list[LDAPRoleElement] | Unset):
        no_permissions (list[LDAPRoleElement] | Unset):
    """

    state: LDAPGroupsToRolesWithCustomRolesState | Unset = UNSET
    handle_nested: bool | Unset = UNSET
    admin: list[LDAPRoleElement] | Unset = UNSET
    agent_registration: list[LDAPRoleElement] | Unset = UNSET
    guest: list[LDAPRoleElement] | Unset = UNSET
    user: list[LDAPRoleElement] | Unset = UNSET
    no_permissions: list[LDAPRoleElement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        handle_nested = self.handle_nested

        admin: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.admin, Unset):
            admin = []
            for admin_item_data in self.admin:
                admin_item = admin_item_data.to_dict()
                admin.append(admin_item)

        agent_registration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agent_registration, Unset):
            agent_registration = []
            for agent_registration_item_data in self.agent_registration:
                agent_registration_item = agent_registration_item_data.to_dict()
                agent_registration.append(agent_registration_item)

        guest: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.guest, Unset):
            guest = []
            for guest_item_data in self.guest:
                guest_item = guest_item_data.to_dict()
                guest.append(guest_item)

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)

        no_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no_permissions, Unset):
            no_permissions = []
            for no_permissions_item_data in self.no_permissions:
                no_permissions_item = no_permissions_item_data.to_dict()
                no_permissions.append(no_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if handle_nested is not UNSET:
            field_dict["handle_nested"] = handle_nested
        if admin is not UNSET:
            field_dict["admin"] = admin
        if agent_registration is not UNSET:
            field_dict["agent_registration"] = agent_registration
        if guest is not UNSET:
            field_dict["guest"] = guest
        if user is not UNSET:
            field_dict["user"] = user
        if no_permissions is not UNSET:
            field_dict["no_permissions"] = no_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_role_element import LDAPRoleElement

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPGroupsToRolesWithCustomRolesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPGroupsToRolesWithCustomRolesState(_state)

        handle_nested = d.pop("handle_nested", UNSET)

        _admin = d.pop("admin", UNSET)
        admin: list[LDAPRoleElement] | Unset = UNSET
        if _admin is not UNSET:
            admin = []
            for admin_item_data in _admin:
                admin_item = LDAPRoleElement.from_dict(admin_item_data)

                admin.append(admin_item)

        _agent_registration = d.pop("agent_registration", UNSET)
        agent_registration: list[LDAPRoleElement] | Unset = UNSET
        if _agent_registration is not UNSET:
            agent_registration = []
            for agent_registration_item_data in _agent_registration:
                agent_registration_item = LDAPRoleElement.from_dict(
                    agent_registration_item_data
                )

                agent_registration.append(agent_registration_item)

        _guest = d.pop("guest", UNSET)
        guest: list[LDAPRoleElement] | Unset = UNSET
        if _guest is not UNSET:
            guest = []
            for guest_item_data in _guest:
                guest_item = LDAPRoleElement.from_dict(guest_item_data)

                guest.append(guest_item)

        _user = d.pop("user", UNSET)
        user: list[LDAPRoleElement] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for user_item_data in _user:
                user_item = LDAPRoleElement.from_dict(user_item_data)

                user.append(user_item)

        _no_permissions = d.pop("no_permissions", UNSET)
        no_permissions: list[LDAPRoleElement] | Unset = UNSET
        if _no_permissions is not UNSET:
            no_permissions = []
            for no_permissions_item_data in _no_permissions:
                no_permissions_item = LDAPRoleElement.from_dict(
                    no_permissions_item_data
                )

                no_permissions.append(no_permissions_item)

        ldap_groups_to_roles_with_custom_roles = cls(
            state=state,
            handle_nested=handle_nested,
            admin=admin,
            agent_registration=agent_registration,
            guest=guest,
            user=user,
            no_permissions=no_permissions,
        )

        ldap_groups_to_roles_with_custom_roles.additional_properties = d
        return ldap_groups_to_roles_with_custom_roles

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
