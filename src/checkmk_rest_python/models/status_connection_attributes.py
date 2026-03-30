from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_attributes import ProxyAttributes
    from ..models.socket_ip4 import SocketIP4
    from ..models.socket_ip6 import SocketIP6
    from ..models.socket_type import SocketType
    from ..models.socket_unix_attributes import SocketUnixAttributes
    from ..models.status_host_attributes_base import StatusHostAttributesBase
    from ..models.status_host_attributes_set import StatusHostAttributesSet
    from ..models.use_live_status_daemon import UseLiveStatusDaemon


T = TypeVar("T", bound="StatusConnectionAttributes")


@_attrs_define
class StatusConnectionAttributes:
    """
    Attributes:
        connection (SocketIP4 | SocketIP6 | SocketType | SocketUnixAttributes):
        proxy (ProxyAttributes | UseLiveStatusDaemon):
        connect_timeout (int): The time that the GUI waits for a connection to the site to be established before the
            site is considered to be unreachable. Example: 2.
        status_host (StatusHostAttributesBase | StatusHostAttributesSet):
        persistent_connection (bool | Unset): If you enable persistent connections then Multisite will try to keep open
            the connection to the remote sites. Default: False.
        url_prefix (str | Unset): The URL prefix will be prepended to links of addons like NagVis when a link to such
            applications points to a host or service on that site. Default: ''. Example: /remote_1/.
        disable_in_status_gui (bool | Unset): If you disable a connection, then no data of this site will be shown in
            the status GUI. The replication is not affected by this, however. Default: False.
    """

    connection: SocketIP4 | SocketIP6 | SocketType | SocketUnixAttributes
    proxy: ProxyAttributes | UseLiveStatusDaemon
    connect_timeout: int
    status_host: StatusHostAttributesBase | StatusHostAttributesSet
    persistent_connection: bool | Unset = False
    url_prefix: str | Unset = ""
    disable_in_status_gui: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.socket_ip4 import SocketIP4
        from ..models.socket_ip6 import SocketIP6
        from ..models.socket_unix_attributes import SocketUnixAttributes
        from ..models.status_host_attributes_set import StatusHostAttributesSet
        from ..models.use_live_status_daemon import UseLiveStatusDaemon

        connection: dict[str, Any]
        if isinstance(self.connection, SocketIP4):
            connection = self.connection.to_dict()
        elif isinstance(self.connection, SocketIP6):
            connection = self.connection.to_dict()
        elif isinstance(self.connection, SocketUnixAttributes):
            connection = self.connection.to_dict()
        else:
            connection = self.connection.to_dict()

        proxy: dict[str, Any]
        if isinstance(self.proxy, UseLiveStatusDaemon):
            proxy = self.proxy.to_dict()
        else:
            proxy = self.proxy.to_dict()

        connect_timeout = self.connect_timeout

        status_host: dict[str, Any]
        if isinstance(self.status_host, StatusHostAttributesSet):
            status_host = self.status_host.to_dict()
        else:
            status_host = self.status_host.to_dict()

        persistent_connection = self.persistent_connection

        url_prefix = self.url_prefix

        disable_in_status_gui = self.disable_in_status_gui

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "proxy": proxy,
                "connect_timeout": connect_timeout,
                "status_host": status_host,
            }
        )
        if persistent_connection is not UNSET:
            field_dict["persistent_connection"] = persistent_connection
        if url_prefix is not UNSET:
            field_dict["url_prefix"] = url_prefix
        if disable_in_status_gui is not UNSET:
            field_dict["disable_in_status_gui"] = disable_in_status_gui

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_attributes import ProxyAttributes
        from ..models.socket_ip4 import SocketIP4
        from ..models.socket_ip6 import SocketIP6
        from ..models.socket_type import SocketType
        from ..models.socket_unix_attributes import SocketUnixAttributes
        from ..models.status_host_attributes_base import StatusHostAttributesBase
        from ..models.status_host_attributes_set import StatusHostAttributesSet
        from ..models.use_live_status_daemon import UseLiveStatusDaemon

        d = dict(src_dict)

        def _parse_connection(
            data: object,
        ) -> SocketIP4 | SocketIP6 | SocketType | SocketUnixAttributes:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_socket_attributes_type_0 = SocketIP4.from_dict(data)

                return componentsschemas_socket_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_socket_attributes_type_1 = SocketIP6.from_dict(data)

                return componentsschemas_socket_attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_socket_attributes_type_2 = (
                    SocketUnixAttributes.from_dict(data)
                )

                return componentsschemas_socket_attributes_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_socket_attributes_type_3 = SocketType.from_dict(data)

            return componentsschemas_socket_attributes_type_3

        connection = _parse_connection(d.pop("connection"))

        def _parse_proxy(data: object) -> ProxyAttributes | UseLiveStatusDaemon:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_proxy_or_direct_type_0 = (
                    UseLiveStatusDaemon.from_dict(data)
                )

                return componentsschemas_proxy_or_direct_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_proxy_or_direct_type_1 = ProxyAttributes.from_dict(data)

            return componentsschemas_proxy_or_direct_type_1

        proxy = _parse_proxy(d.pop("proxy"))

        connect_timeout = d.pop("connect_timeout")

        def _parse_status_host(
            data: object,
        ) -> StatusHostAttributesBase | StatusHostAttributesSet:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_status_host_set_type_0 = (
                    StatusHostAttributesSet.from_dict(data)
                )

                return componentsschemas_status_host_set_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_status_host_set_type_1 = (
                StatusHostAttributesBase.from_dict(data)
            )

            return componentsschemas_status_host_set_type_1

        status_host = _parse_status_host(d.pop("status_host"))

        persistent_connection = d.pop("persistent_connection", UNSET)

        url_prefix = d.pop("url_prefix", UNSET)

        disable_in_status_gui = d.pop("disable_in_status_gui", UNSET)

        status_connection_attributes = cls(
            connection=connection,
            proxy=proxy,
            connect_timeout=connect_timeout,
            status_host=status_host,
            persistent_connection=persistent_connection,
            url_prefix=url_prefix,
            disable_in_status_gui=disable_in_status_gui,
        )

        status_connection_attributes.additional_properties = d
        return status_connection_attributes

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
