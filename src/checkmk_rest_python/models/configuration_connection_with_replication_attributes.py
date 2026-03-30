from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_sync_base import UserSyncBase
    from ..models.user_sync_with_ldap_connection import UserSyncWithLdapConnection


T = TypeVar("T", bound="ConfigurationConnectionWithReplicationAttributes")


@_attrs_define
class ConfigurationConnectionWithReplicationAttributes:
    """
    Attributes:
        enable_replication (Any): Replication allows you to manage several monitoring sites with a logically centralized
            setup. Remote sites receive their configuration from the central sites. Default: True. Example: True.
        url_of_remote_site (str): URL of the remote Checkmk including /check_mk/. This URL is in many cases the same as
            the URL-Prefix but with check_mk/ appended, but it must always be an absolute URL. Example:
            http://remote_site_1/check_mk/.
        disable_remote_configuration (bool): It is a good idea to disable access to Setup completely on the remote site.
            Otherwise a user who does not now about the replication could make local changes that are overridden at the next
            configuration activation. Example: True.
        ignore_tls_errors (bool): This might be needed to make the synchronization accept problems with SSL certificates
            when using an SSL secured connection.
        direct_login_to_web_gui_allowed (bool): When enabled, this site is marked for synchronisation every time a web
            GUI related option is changed and users are allowed to login to the web GUI of this site. Example: True.
        user_sync (UserSyncBase | UserSyncWithLdapConnection):
        replicate_event_console (bool): This option enables the distribution of global settings and rules of the Event
            Console to the remote site. Any change in the local Event Console settings will mark the site as need sync. A
            synchronization will automatically reload the Event Console of the remote site. Example: True.
        replicate_extensions (bool): If you enable the replication of MKPs then during each Activate Changes MKPs that
            are installed on your central site and all other files below the ~/local/ directory will be also transferred to
            the remote site. Note: all other MKPs and files below ~/local/ on the remote site will be removed. Example:
            True.
        message_broker_port (int): The port used by the message broker to exchange messages. Example: 5672.
        is_trusted (bool | Unset): When this option is enabled the central site might get compromised by a rogue remote
            site. If you disable this option, some features, such as HTML rendering in service descriptions for the services
            monitored on this remote site, will no longer work. In case the sites are managed by different groups of people,
            especially when belonging to different organizations, we recommend to disable this setting.
    """

    url_of_remote_site: str
    disable_remote_configuration: bool
    ignore_tls_errors: bool
    direct_login_to_web_gui_allowed: bool
    user_sync: UserSyncBase | UserSyncWithLdapConnection
    replicate_event_console: bool
    replicate_extensions: bool
    message_broker_port: int
    enable_replication: Any = True
    is_trusted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_sync_with_ldap_connection import UserSyncWithLdapConnection

        enable_replication = self.enable_replication

        url_of_remote_site = self.url_of_remote_site

        disable_remote_configuration = self.disable_remote_configuration

        ignore_tls_errors = self.ignore_tls_errors

        direct_login_to_web_gui_allowed = self.direct_login_to_web_gui_allowed

        user_sync: dict[str, Any]
        if isinstance(self.user_sync, UserSyncWithLdapConnection):
            user_sync = self.user_sync.to_dict()
        else:
            user_sync = self.user_sync.to_dict()

        replicate_event_console = self.replicate_event_console

        replicate_extensions = self.replicate_extensions

        message_broker_port = self.message_broker_port

        is_trusted = self.is_trusted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable_replication": enable_replication,
                "url_of_remote_site": url_of_remote_site,
                "disable_remote_configuration": disable_remote_configuration,
                "ignore_tls_errors": ignore_tls_errors,
                "direct_login_to_web_gui_allowed": direct_login_to_web_gui_allowed,
                "user_sync": user_sync,
                "replicate_event_console": replicate_event_console,
                "replicate_extensions": replicate_extensions,
                "message_broker_port": message_broker_port,
            }
        )
        if is_trusted is not UNSET:
            field_dict["is_trusted"] = is_trusted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_sync_base import UserSyncBase
        from ..models.user_sync_with_ldap_connection import UserSyncWithLdapConnection

        d = dict(src_dict)
        enable_replication = d.pop("enable_replication")

        url_of_remote_site = d.pop("url_of_remote_site")

        disable_remote_configuration = d.pop("disable_remote_configuration")

        ignore_tls_errors = d.pop("ignore_tls_errors")

        direct_login_to_web_gui_allowed = d.pop("direct_login_to_web_gui_allowed")

        def _parse_user_sync(data: object) -> UserSyncBase | UserSyncWithLdapConnection:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_user_sync_attributes_type_0 = (
                    UserSyncWithLdapConnection.from_dict(data)
                )

                return componentsschemas_user_sync_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_user_sync_attributes_type_1 = UserSyncBase.from_dict(data)

            return componentsschemas_user_sync_attributes_type_1

        user_sync = _parse_user_sync(d.pop("user_sync"))

        replicate_event_console = d.pop("replicate_event_console")

        replicate_extensions = d.pop("replicate_extensions")

        message_broker_port = d.pop("message_broker_port")

        is_trusted = d.pop("is_trusted", UNSET)

        configuration_connection_with_replication_attributes = cls(
            enable_replication=enable_replication,
            url_of_remote_site=url_of_remote_site,
            disable_remote_configuration=disable_remote_configuration,
            ignore_tls_errors=ignore_tls_errors,
            direct_login_to_web_gui_allowed=direct_login_to_web_gui_allowed,
            user_sync=user_sync,
            replicate_event_console=replicate_event_console,
            replicate_extensions=replicate_extensions,
            message_broker_port=message_broker_port,
            is_trusted=is_trusted,
        )

        configuration_connection_with_replication_attributes.additional_properties = d
        return configuration_connection_with_replication_attributes

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
