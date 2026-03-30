from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_groups_to_attributes_state import LDAPGroupsToAttributesState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_groups_to_sync_disable_notifications import (
        LDAPGroupsToSyncDisableNotifications,
    )


T = TypeVar("T", bound="LDAPGroupsToAttributes")


@_attrs_define
class LDAPGroupsToAttributes:
    """
    Attributes:
        state (LDAPGroupsToAttributesState | Unset):  Example: enabled.
        handle_nested (bool | Unset): Once you enable this option, this plug-in will not only handle direct group
            memberships, instead it will also dig into nested groups and treat the members of those groups as contact group
            members as well. Please bear in mind that this feature might increase the execution time of your LDAP sync.
            (Active Directory only at the moment)
        sync_from_other_connections (list[str] | Unset): This is a special feature for environments where user accounts
            are located in one LDAP directory and groups objects having them as members are located in other directories.
            You should only enable this feature when you are in this situation and really need it. The current connection is
            always used.
        groups_to_sync (list[LDAPGroupsToSyncDisableNotifications] | Unset): Specify the groups to control the value of
            a given user attribute. If a user is not a member of a group, the attribute will be left at its default value.
            When a single attribute is set by multiple groups and a user is a member of multiple of these groups, the later
            plug-in in the list will override the others. Example: [{'group_cn': 'group_cn_example', 'attribute_to_set':
            'mega_menu_icons', 'value': 'mega_menu_icons'}].
    """

    state: LDAPGroupsToAttributesState | Unset = UNSET
    handle_nested: bool | Unset = UNSET
    sync_from_other_connections: list[str] | Unset = UNSET
    groups_to_sync: list[LDAPGroupsToSyncDisableNotifications] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        handle_nested = self.handle_nested

        sync_from_other_connections: list[str] | Unset = UNSET
        if not isinstance(self.sync_from_other_connections, Unset):
            sync_from_other_connections = self.sync_from_other_connections

        groups_to_sync: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups_to_sync, Unset):
            groups_to_sync = []
            for groups_to_sync_item_data in self.groups_to_sync:
                groups_to_sync_item = groups_to_sync_item_data.to_dict()
                groups_to_sync.append(groups_to_sync_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if handle_nested is not UNSET:
            field_dict["handle_nested"] = handle_nested
        if sync_from_other_connections is not UNSET:
            field_dict["sync_from_other_connections"] = sync_from_other_connections
        if groups_to_sync is not UNSET:
            field_dict["groups_to_sync"] = groups_to_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_groups_to_sync_disable_notifications import (
            LDAPGroupsToSyncDisableNotifications,
        )

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPGroupsToAttributesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPGroupsToAttributesState(_state)

        handle_nested = d.pop("handle_nested", UNSET)

        sync_from_other_connections = cast(
            list[str], d.pop("sync_from_other_connections", UNSET)
        )

        _groups_to_sync = d.pop("groups_to_sync", UNSET)
        groups_to_sync: list[LDAPGroupsToSyncDisableNotifications] | Unset = UNSET
        if _groups_to_sync is not UNSET:
            groups_to_sync = []
            for groups_to_sync_item_data in _groups_to_sync:
                groups_to_sync_item = LDAPGroupsToSyncDisableNotifications.from_dict(
                    groups_to_sync_item_data
                )

                groups_to_sync.append(groups_to_sync_item)

        ldap_groups_to_attributes = cls(
            state=state,
            handle_nested=handle_nested,
            sync_from_other_connections=sync_from_other_connections,
            groups_to_sync=groups_to_sync,
        )

        ldap_groups_to_attributes.additional_properties = d
        return ldap_groups_to_attributes

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
