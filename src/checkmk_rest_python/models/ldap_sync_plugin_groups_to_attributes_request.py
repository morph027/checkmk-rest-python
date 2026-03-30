from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_sync_plugin_group_all_others_request import (
        LDAPSyncPluginGroupAllOthersRequest,
    )
    from ..models.ldap_sync_plugin_group_disable_notifications_request import (
        LDAPSyncPluginGroupDisableNotificationsRequest,
    )


T = TypeVar("T", bound="LDAPSyncPluginGroupsToAttributesRequest")


@_attrs_define
class LDAPSyncPluginGroupsToAttributesRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        handle_nested (bool | Unset): Once you enable this option, this plug-in will not only handle direct group
            memberships, instead it will also dig into nested groups and treat the members of those groups as contact group
            members as well. Please bear in mind that this feature might increase the execution time of your LDAP sync.
            Default: False. Example: True.
        sync_from_other_connections (list[str] | Unset): The LDAP attribute whose contents shall be synced into this
            custom attribute. Example: ['LDAP_1', 'LDAP_2'].
        groups_to_sync (list[LDAPSyncPluginGroupAllOthersRequest | LDAPSyncPluginGroupDisableNotificationsRequest] |
            Unset):
    """

    state: Any = "enabled"
    handle_nested: bool | Unset = False
    sync_from_other_connections: list[str] | Unset = UNSET
    groups_to_sync: (
        list[
            LDAPSyncPluginGroupAllOthersRequest
            | LDAPSyncPluginGroupDisableNotificationsRequest
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ldap_sync_plugin_group_disable_notifications_request import (
            LDAPSyncPluginGroupDisableNotificationsRequest,
        )

        state = self.state

        handle_nested = self.handle_nested

        sync_from_other_connections: list[str] | Unset = UNSET
        if not isinstance(self.sync_from_other_connections, Unset):
            sync_from_other_connections = self.sync_from_other_connections

        groups_to_sync: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups_to_sync, Unset):
            groups_to_sync = []
            for groups_to_sync_item_data in self.groups_to_sync:
                groups_to_sync_item: dict[str, Any]
                if isinstance(
                    groups_to_sync_item_data,
                    LDAPSyncPluginGroupDisableNotificationsRequest,
                ):
                    groups_to_sync_item = groups_to_sync_item_data.to_dict()
                else:
                    groups_to_sync_item = groups_to_sync_item_data.to_dict()

                groups_to_sync.append(groups_to_sync_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if handle_nested is not UNSET:
            field_dict["handle_nested"] = handle_nested
        if sync_from_other_connections is not UNSET:
            field_dict["sync_from_other_connections"] = sync_from_other_connections
        if groups_to_sync is not UNSET:
            field_dict["groups_to_sync"] = groups_to_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_sync_plugin_group_all_others_request import (
            LDAPSyncPluginGroupAllOthersRequest,
        )
        from ..models.ldap_sync_plugin_group_disable_notifications_request import (
            LDAPSyncPluginGroupDisableNotificationsRequest,
        )

        d = dict(src_dict)
        state = d.pop("state")

        handle_nested = d.pop("handle_nested", UNSET)

        sync_from_other_connections = cast(
            list[str], d.pop("sync_from_other_connections", UNSET)
        )

        _groups_to_sync = d.pop("groups_to_sync", UNSET)
        groups_to_sync: (
            list[
                LDAPSyncPluginGroupAllOthersRequest
                | LDAPSyncPluginGroupDisableNotificationsRequest
            ]
            | Unset
        ) = UNSET
        if _groups_to_sync is not UNSET:
            groups_to_sync = []
            for groups_to_sync_item_data in _groups_to_sync:

                def _parse_groups_to_sync_item(
                    data: object,
                ) -> (
                    LDAPSyncPluginGroupAllOthersRequest
                    | LDAPSyncPluginGroupDisableNotificationsRequest
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_ldap_sync_plugin_groups_to_sync_selector_type_0 = LDAPSyncPluginGroupDisableNotificationsRequest.from_dict(
                            data
                        )

                        return componentsschemas_ldap_sync_plugin_groups_to_sync_selector_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ldap_sync_plugin_groups_to_sync_selector_type_1 = LDAPSyncPluginGroupAllOthersRequest.from_dict(
                        data
                    )

                    return componentsschemas_ldap_sync_plugin_groups_to_sync_selector_type_1

                groups_to_sync_item = _parse_groups_to_sync_item(
                    groups_to_sync_item_data
                )

                groups_to_sync.append(groups_to_sync_item)

        ldap_sync_plugin_groups_to_attributes_request = cls(
            state=state,
            handle_nested=handle_nested,
            sync_from_other_connections=sync_from_other_connections,
            groups_to_sync=groups_to_sync,
        )

        ldap_sync_plugin_groups_to_attributes_request.additional_properties = d
        return ldap_sync_plugin_groups_to_attributes_request

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
