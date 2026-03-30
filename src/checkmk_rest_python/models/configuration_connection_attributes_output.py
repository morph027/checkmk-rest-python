from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_sync_attributes_output import UserSyncAttributesOutput


T = TypeVar("T", bound="ConfigurationConnectionAttributesOutput")


@_attrs_define
class ConfigurationConnectionAttributesOutput:
    """
    Attributes:
        enable_replication (bool | Unset): Replication allows you to manage several monitoring sites with a logically
            centralized setup. Remote sites receive their configuration from the central sites. Example: True.
        url_of_remote_site (str | Unset): URL of the remote Checkmk including /check_mk/. This URL is in many cases the
            same as the URL-Prefix but with check_mk/ appended, but it must always be an absolute URL. Example:
            http://remote_site_1/check_mk/.
        disable_remote_configuration (bool | Unset): It is a good idea to disable access to Setup completely on the
            remote site. Otherwise a user who does not now about the replication could make local changes that are
            overridden at the next configuration activation. Example: True.
        ignore_tls_errors (bool | Unset): This might be needed to make the synchronization accept problems with SSL
            certificates when using an SSL secured connection.
        direct_login_to_web_gui_allowed (bool | Unset): When enabled, this site is marked for synchronisation every time
            a web GUI related option is changed and users are allowed to login to the web GUI of this site. Example: True.
        user_sync (UserSyncAttributesOutput | Unset):
        replicate_event_console (bool | Unset): This option enables the distribution of global settings and rules of the
            Event Console to the remote site. Any change in the local Event Console settings will mark the site as need
            sync. A synchronization will automatically reload the Event Console of the remote site. Example: True.
        replicate_extensions (bool | Unset): If you enable the replication of MKPs then during each Activate Changes
            MKPs that are installed on your central site and all other files below the ~/local/ directory will be also
            transferred to the remote site. Note: all other MKPs and files below ~/local/ on the remote site will be
            removed. Example: True.
        message_broker_port (int | Unset): The port used for the message broker to exchange messages. Example: 5672.
        is_trusted (bool | Unset): When this option is enabled the central site might get compromised by a rogue remote
            site. If you disable this option some features like rendering HTML in service descriptions will not work for
            services monitored on this site.
    """

    enable_replication: bool | Unset = UNSET
    url_of_remote_site: str | Unset = UNSET
    disable_remote_configuration: bool | Unset = UNSET
    ignore_tls_errors: bool | Unset = UNSET
    direct_login_to_web_gui_allowed: bool | Unset = UNSET
    user_sync: UserSyncAttributesOutput | Unset = UNSET
    replicate_event_console: bool | Unset = UNSET
    replicate_extensions: bool | Unset = UNSET
    message_broker_port: int | Unset = UNSET
    is_trusted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_replication = self.enable_replication

        url_of_remote_site = self.url_of_remote_site

        disable_remote_configuration = self.disable_remote_configuration

        ignore_tls_errors = self.ignore_tls_errors

        direct_login_to_web_gui_allowed = self.direct_login_to_web_gui_allowed

        user_sync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_sync, Unset):
            user_sync = self.user_sync.to_dict()

        replicate_event_console = self.replicate_event_console

        replicate_extensions = self.replicate_extensions

        message_broker_port = self.message_broker_port

        is_trusted = self.is_trusted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_replication is not UNSET:
            field_dict["enable_replication"] = enable_replication
        if url_of_remote_site is not UNSET:
            field_dict["url_of_remote_site"] = url_of_remote_site
        if disable_remote_configuration is not UNSET:
            field_dict["disable_remote_configuration"] = disable_remote_configuration
        if ignore_tls_errors is not UNSET:
            field_dict["ignore_tls_errors"] = ignore_tls_errors
        if direct_login_to_web_gui_allowed is not UNSET:
            field_dict["direct_login_to_web_gui_allowed"] = (
                direct_login_to_web_gui_allowed
            )
        if user_sync is not UNSET:
            field_dict["user_sync"] = user_sync
        if replicate_event_console is not UNSET:
            field_dict["replicate_event_console"] = replicate_event_console
        if replicate_extensions is not UNSET:
            field_dict["replicate_extensions"] = replicate_extensions
        if message_broker_port is not UNSET:
            field_dict["message_broker_port"] = message_broker_port
        if is_trusted is not UNSET:
            field_dict["is_trusted"] = is_trusted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_sync_attributes_output import UserSyncAttributesOutput

        d = dict(src_dict)
        enable_replication = d.pop("enable_replication", UNSET)

        url_of_remote_site = d.pop("url_of_remote_site", UNSET)

        disable_remote_configuration = d.pop("disable_remote_configuration", UNSET)

        ignore_tls_errors = d.pop("ignore_tls_errors", UNSET)

        direct_login_to_web_gui_allowed = d.pop(
            "direct_login_to_web_gui_allowed", UNSET
        )

        _user_sync = d.pop("user_sync", UNSET)
        user_sync: UserSyncAttributesOutput | Unset
        if isinstance(_user_sync, Unset):
            user_sync = UNSET
        else:
            user_sync = UserSyncAttributesOutput.from_dict(_user_sync)

        replicate_event_console = d.pop("replicate_event_console", UNSET)

        replicate_extensions = d.pop("replicate_extensions", UNSET)

        message_broker_port = d.pop("message_broker_port", UNSET)

        is_trusted = d.pop("is_trusted", UNSET)

        configuration_connection_attributes_output = cls(
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

        configuration_connection_attributes_output.additional_properties = d
        return configuration_connection_attributes_output

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
