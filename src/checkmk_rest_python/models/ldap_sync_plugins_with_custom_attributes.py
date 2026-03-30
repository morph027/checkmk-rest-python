from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_contact_group_membership import LDAPContactGroupMembership
    from ..models.ldap_groups_to_attributes import LDAPGroupsToAttributes
    from ..models.ldap_groups_to_roles_with_custom_roles import (
        LDAPGroupsToRolesWithCustomRoles,
    )
    from ..models.ldap_sync_plugin_alias import LDAPSyncPluginAlias
    from ..models.ldap_sync_plugin_auth_exp import LDAPSyncPluginAuthExp
    from ..models.ldap_sync_plugin_disable_notifications import (
        LDAPSyncPluginDisableNotifications,
    )
    from ..models.ldap_sync_plugin_email_address import LDAPSyncPluginEmailAddress
    from ..models.ldap_sync_plugin_menu_icons import LDAPSyncPluginMenuIcons
    from ..models.ldap_sync_plugin_nav_bar_icons import LDAPSyncPluginNavBarIcons
    from ..models.ldap_sync_plugin_pager import LDAPSyncPluginPager
    from ..models.ldap_sync_plugin_show_mode import LDAPSyncPluginShowMode
    from ..models.ldap_sync_plugin_side_bar_position import (
        LDAPSyncPluginSideBarPosition,
    )
    from ..models.ldap_sync_plugin_start_url import LDAPSyncPluginStartURL
    from ..models.ldap_sync_plugin_temp_unit import LDAPSyncPluginTempUnit
    from ..models.ldap_sync_plugin_ui_theme import LDAPSyncPluginUITheme
    from ..models.ldap_sync_plugin_visibility_of_hosts_or_services import (
        LDAPSyncPluginVisibilityOfHostsOrServices,
    )


T = TypeVar("T", bound="LDAPSyncPluginsWithCustomAttributes")


@_attrs_define
class LDAPSyncPluginsWithCustomAttributes:
    """
    Attributes:
        alias (LDAPSyncPluginAlias | Unset):
        authentication_expiration (LDAPSyncPluginAuthExp | Unset):
        disable_notifications (LDAPSyncPluginDisableNotifications | Unset):
        email_address (LDAPSyncPluginEmailAddress | Unset):
        mega_menu_icons (LDAPSyncPluginMenuIcons | Unset):
        navigation_bar_icons (LDAPSyncPluginNavBarIcons | Unset):
        pager (LDAPSyncPluginPager | Unset):
        show_mode (LDAPSyncPluginShowMode | Unset):
        ui_sidebar_position (LDAPSyncPluginSideBarPosition | Unset):
        start_url (LDAPSyncPluginStartURL | Unset):
        temperature_unit (LDAPSyncPluginTempUnit | Unset):
        ui_theme (LDAPSyncPluginUITheme | Unset):
        visibility_of_hosts_or_services (LDAPSyncPluginVisibilityOfHostsOrServices | Unset):
        contact_group_membership (LDAPContactGroupMembership | Unset):
        groups_to_custom_user_attributes (LDAPGroupsToAttributes | Unset):
        groups_to_roles (LDAPGroupsToRolesWithCustomRoles | Unset):
    """

    alias: LDAPSyncPluginAlias | Unset = UNSET
    authentication_expiration: LDAPSyncPluginAuthExp | Unset = UNSET
    disable_notifications: LDAPSyncPluginDisableNotifications | Unset = UNSET
    email_address: LDAPSyncPluginEmailAddress | Unset = UNSET
    mega_menu_icons: LDAPSyncPluginMenuIcons | Unset = UNSET
    navigation_bar_icons: LDAPSyncPluginNavBarIcons | Unset = UNSET
    pager: LDAPSyncPluginPager | Unset = UNSET
    show_mode: LDAPSyncPluginShowMode | Unset = UNSET
    ui_sidebar_position: LDAPSyncPluginSideBarPosition | Unset = UNSET
    start_url: LDAPSyncPluginStartURL | Unset = UNSET
    temperature_unit: LDAPSyncPluginTempUnit | Unset = UNSET
    ui_theme: LDAPSyncPluginUITheme | Unset = UNSET
    visibility_of_hosts_or_services: (
        LDAPSyncPluginVisibilityOfHostsOrServices | Unset
    ) = UNSET
    contact_group_membership: LDAPContactGroupMembership | Unset = UNSET
    groups_to_custom_user_attributes: LDAPGroupsToAttributes | Unset = UNSET
    groups_to_roles: LDAPGroupsToRolesWithCustomRoles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alias, Unset):
            alias = self.alias.to_dict()

        authentication_expiration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication_expiration, Unset):
            authentication_expiration = self.authentication_expiration.to_dict()

        disable_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_notifications, Unset):
            disable_notifications = self.disable_notifications.to_dict()

        email_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_address, Unset):
            email_address = self.email_address.to_dict()

        mega_menu_icons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mega_menu_icons, Unset):
            mega_menu_icons = self.mega_menu_icons.to_dict()

        navigation_bar_icons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.navigation_bar_icons, Unset):
            navigation_bar_icons = self.navigation_bar_icons.to_dict()

        pager: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        show_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.show_mode, Unset):
            show_mode = self.show_mode.to_dict()

        ui_sidebar_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_sidebar_position, Unset):
            ui_sidebar_position = self.ui_sidebar_position.to_dict()

        start_url: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_url, Unset):
            start_url = self.start_url.to_dict()

        temperature_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.temperature_unit, Unset):
            temperature_unit = self.temperature_unit.to_dict()

        ui_theme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_theme, Unset):
            ui_theme = self.ui_theme.to_dict()

        visibility_of_hosts_or_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_of_hosts_or_services, Unset):
            visibility_of_hosts_or_services = (
                self.visibility_of_hosts_or_services.to_dict()
            )

        contact_group_membership: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_group_membership, Unset):
            contact_group_membership = self.contact_group_membership.to_dict()

        groups_to_custom_user_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups_to_custom_user_attributes, Unset):
            groups_to_custom_user_attributes = (
                self.groups_to_custom_user_attributes.to_dict()
            )

        groups_to_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups_to_roles, Unset):
            groups_to_roles = self.groups_to_roles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if authentication_expiration is not UNSET:
            field_dict["authentication_expiration"] = authentication_expiration
        if disable_notifications is not UNSET:
            field_dict["disable_notifications"] = disable_notifications
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if mega_menu_icons is not UNSET:
            field_dict["mega_menu_icons"] = mega_menu_icons
        if navigation_bar_icons is not UNSET:
            field_dict["navigation_bar_icons"] = navigation_bar_icons
        if pager is not UNSET:
            field_dict["pager"] = pager
        if show_mode is not UNSET:
            field_dict["show_mode"] = show_mode
        if ui_sidebar_position is not UNSET:
            field_dict["ui_sidebar_position"] = ui_sidebar_position
        if start_url is not UNSET:
            field_dict["start_url"] = start_url
        if temperature_unit is not UNSET:
            field_dict["temperature_unit"] = temperature_unit
        if ui_theme is not UNSET:
            field_dict["ui_theme"] = ui_theme
        if visibility_of_hosts_or_services is not UNSET:
            field_dict["visibility_of_hosts_or_services"] = (
                visibility_of_hosts_or_services
            )
        if contact_group_membership is not UNSET:
            field_dict["contact_group_membership"] = contact_group_membership
        if groups_to_custom_user_attributes is not UNSET:
            field_dict["groups_to_custom_user_attributes"] = (
                groups_to_custom_user_attributes
            )
        if groups_to_roles is not UNSET:
            field_dict["groups_to_roles"] = groups_to_roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_contact_group_membership import LDAPContactGroupMembership
        from ..models.ldap_groups_to_attributes import LDAPGroupsToAttributes
        from ..models.ldap_groups_to_roles_with_custom_roles import (
            LDAPGroupsToRolesWithCustomRoles,
        )
        from ..models.ldap_sync_plugin_alias import LDAPSyncPluginAlias
        from ..models.ldap_sync_plugin_auth_exp import LDAPSyncPluginAuthExp
        from ..models.ldap_sync_plugin_disable_notifications import (
            LDAPSyncPluginDisableNotifications,
        )
        from ..models.ldap_sync_plugin_email_address import LDAPSyncPluginEmailAddress
        from ..models.ldap_sync_plugin_menu_icons import LDAPSyncPluginMenuIcons
        from ..models.ldap_sync_plugin_nav_bar_icons import LDAPSyncPluginNavBarIcons
        from ..models.ldap_sync_plugin_pager import LDAPSyncPluginPager
        from ..models.ldap_sync_plugin_show_mode import LDAPSyncPluginShowMode
        from ..models.ldap_sync_plugin_side_bar_position import (
            LDAPSyncPluginSideBarPosition,
        )
        from ..models.ldap_sync_plugin_start_url import LDAPSyncPluginStartURL
        from ..models.ldap_sync_plugin_temp_unit import LDAPSyncPluginTempUnit
        from ..models.ldap_sync_plugin_ui_theme import LDAPSyncPluginUITheme
        from ..models.ldap_sync_plugin_visibility_of_hosts_or_services import (
            LDAPSyncPluginVisibilityOfHostsOrServices,
        )

        d = dict(src_dict)
        _alias = d.pop("alias", UNSET)
        alias: LDAPSyncPluginAlias | Unset
        if isinstance(_alias, Unset):
            alias = UNSET
        else:
            alias = LDAPSyncPluginAlias.from_dict(_alias)

        _authentication_expiration = d.pop("authentication_expiration", UNSET)
        authentication_expiration: LDAPSyncPluginAuthExp | Unset
        if isinstance(_authentication_expiration, Unset):
            authentication_expiration = UNSET
        else:
            authentication_expiration = LDAPSyncPluginAuthExp.from_dict(
                _authentication_expiration
            )

        _disable_notifications = d.pop("disable_notifications", UNSET)
        disable_notifications: LDAPSyncPluginDisableNotifications | Unset
        if isinstance(_disable_notifications, Unset):
            disable_notifications = UNSET
        else:
            disable_notifications = LDAPSyncPluginDisableNotifications.from_dict(
                _disable_notifications
            )

        _email_address = d.pop("email_address", UNSET)
        email_address: LDAPSyncPluginEmailAddress | Unset
        if isinstance(_email_address, Unset):
            email_address = UNSET
        else:
            email_address = LDAPSyncPluginEmailAddress.from_dict(_email_address)

        _mega_menu_icons = d.pop("mega_menu_icons", UNSET)
        mega_menu_icons: LDAPSyncPluginMenuIcons | Unset
        if isinstance(_mega_menu_icons, Unset):
            mega_menu_icons = UNSET
        else:
            mega_menu_icons = LDAPSyncPluginMenuIcons.from_dict(_mega_menu_icons)

        _navigation_bar_icons = d.pop("navigation_bar_icons", UNSET)
        navigation_bar_icons: LDAPSyncPluginNavBarIcons | Unset
        if isinstance(_navigation_bar_icons, Unset):
            navigation_bar_icons = UNSET
        else:
            navigation_bar_icons = LDAPSyncPluginNavBarIcons.from_dict(
                _navigation_bar_icons
            )

        _pager = d.pop("pager", UNSET)
        pager: LDAPSyncPluginPager | Unset
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = LDAPSyncPluginPager.from_dict(_pager)

        _show_mode = d.pop("show_mode", UNSET)
        show_mode: LDAPSyncPluginShowMode | Unset
        if isinstance(_show_mode, Unset):
            show_mode = UNSET
        else:
            show_mode = LDAPSyncPluginShowMode.from_dict(_show_mode)

        _ui_sidebar_position = d.pop("ui_sidebar_position", UNSET)
        ui_sidebar_position: LDAPSyncPluginSideBarPosition | Unset
        if isinstance(_ui_sidebar_position, Unset):
            ui_sidebar_position = UNSET
        else:
            ui_sidebar_position = LDAPSyncPluginSideBarPosition.from_dict(
                _ui_sidebar_position
            )

        _start_url = d.pop("start_url", UNSET)
        start_url: LDAPSyncPluginStartURL | Unset
        if isinstance(_start_url, Unset):
            start_url = UNSET
        else:
            start_url = LDAPSyncPluginStartURL.from_dict(_start_url)

        _temperature_unit = d.pop("temperature_unit", UNSET)
        temperature_unit: LDAPSyncPluginTempUnit | Unset
        if isinstance(_temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = LDAPSyncPluginTempUnit.from_dict(_temperature_unit)

        _ui_theme = d.pop("ui_theme", UNSET)
        ui_theme: LDAPSyncPluginUITheme | Unset
        if isinstance(_ui_theme, Unset):
            ui_theme = UNSET
        else:
            ui_theme = LDAPSyncPluginUITheme.from_dict(_ui_theme)

        _visibility_of_hosts_or_services = d.pop(
            "visibility_of_hosts_or_services", UNSET
        )
        visibility_of_hosts_or_services: (
            LDAPSyncPluginVisibilityOfHostsOrServices | Unset
        )
        if isinstance(_visibility_of_hosts_or_services, Unset):
            visibility_of_hosts_or_services = UNSET
        else:
            visibility_of_hosts_or_services = (
                LDAPSyncPluginVisibilityOfHostsOrServices.from_dict(
                    _visibility_of_hosts_or_services
                )
            )

        _contact_group_membership = d.pop("contact_group_membership", UNSET)
        contact_group_membership: LDAPContactGroupMembership | Unset
        if isinstance(_contact_group_membership, Unset):
            contact_group_membership = UNSET
        else:
            contact_group_membership = LDAPContactGroupMembership.from_dict(
                _contact_group_membership
            )

        _groups_to_custom_user_attributes = d.pop(
            "groups_to_custom_user_attributes", UNSET
        )
        groups_to_custom_user_attributes: LDAPGroupsToAttributes | Unset
        if isinstance(_groups_to_custom_user_attributes, Unset):
            groups_to_custom_user_attributes = UNSET
        else:
            groups_to_custom_user_attributes = LDAPGroupsToAttributes.from_dict(
                _groups_to_custom_user_attributes
            )

        _groups_to_roles = d.pop("groups_to_roles", UNSET)
        groups_to_roles: LDAPGroupsToRolesWithCustomRoles | Unset
        if isinstance(_groups_to_roles, Unset):
            groups_to_roles = UNSET
        else:
            groups_to_roles = LDAPGroupsToRolesWithCustomRoles.from_dict(
                _groups_to_roles
            )

        ldap_sync_plugins_with_custom_attributes = cls(
            alias=alias,
            authentication_expiration=authentication_expiration,
            disable_notifications=disable_notifications,
            email_address=email_address,
            mega_menu_icons=mega_menu_icons,
            navigation_bar_icons=navigation_bar_icons,
            pager=pager,
            show_mode=show_mode,
            ui_sidebar_position=ui_sidebar_position,
            start_url=start_url,
            temperature_unit=temperature_unit,
            ui_theme=ui_theme,
            visibility_of_hosts_or_services=visibility_of_hosts_or_services,
            contact_group_membership=contact_group_membership,
            groups_to_custom_user_attributes=groups_to_custom_user_attributes,
            groups_to_roles=groups_to_roles,
        )

        ldap_sync_plugins_with_custom_attributes.additional_properties = d
        return ldap_sync_plugins_with_custom_attributes

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
