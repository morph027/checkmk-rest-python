from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_attributes_output import ProxyAttributesOutput
    from ..models.socket_attributes_output import SocketAttributesOutput
    from ..models.status_host_attributes import StatusHostAttributes


T = TypeVar("T", bound="StatusConnectionAttributesOutput")


@_attrs_define
class StatusConnectionAttributesOutput:
    """
    Attributes:
        connection (SocketAttributesOutput):
        proxy (ProxyAttributesOutput):
        connect_timeout (int): The time that the GUI waits for a connection to the site to be established before the
            site is considered to be unreachable. Example: 2.
        persistent_connection (bool | Unset): If you enable persistent connections then Multisite will try to keep open
            the connection to the remote sites. Example: True.
        url_prefix (str | Unset): The URL prefix will be prepended to links of addons like NagVis when a link to such
            applications points to a host or service on that site. Example: /remote_1/.
        status_host (StatusHostAttributes | Unset):
        disable_in_status_gui (bool | Unset): If you disable a connection, then no data of this site will be shown in
            the status GUI. The replication is not affected by this, however.
    """

    connection: SocketAttributesOutput
    proxy: ProxyAttributesOutput
    connect_timeout: int
    persistent_connection: bool | Unset = UNSET
    url_prefix: str | Unset = UNSET
    status_host: StatusHostAttributes | Unset = UNSET
    disable_in_status_gui: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection = self.connection.to_dict()

        proxy = self.proxy.to_dict()

        connect_timeout = self.connect_timeout

        persistent_connection = self.persistent_connection

        url_prefix = self.url_prefix

        status_host: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_host, Unset):
            status_host = self.status_host.to_dict()

        disable_in_status_gui = self.disable_in_status_gui

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection": connection,
                "proxy": proxy,
                "connect_timeout": connect_timeout,
            }
        )
        if persistent_connection is not UNSET:
            field_dict["persistent_connection"] = persistent_connection
        if url_prefix is not UNSET:
            field_dict["url_prefix"] = url_prefix
        if status_host is not UNSET:
            field_dict["status_host"] = status_host
        if disable_in_status_gui is not UNSET:
            field_dict["disable_in_status_gui"] = disable_in_status_gui

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_attributes_output import ProxyAttributesOutput
        from ..models.socket_attributes_output import SocketAttributesOutput
        from ..models.status_host_attributes import StatusHostAttributes

        d = dict(src_dict)
        connection = SocketAttributesOutput.from_dict(d.pop("connection"))

        proxy = ProxyAttributesOutput.from_dict(d.pop("proxy"))

        connect_timeout = d.pop("connect_timeout")

        persistent_connection = d.pop("persistent_connection", UNSET)

        url_prefix = d.pop("url_prefix", UNSET)

        _status_host = d.pop("status_host", UNSET)
        status_host: StatusHostAttributes | Unset
        if isinstance(_status_host, Unset):
            status_host = UNSET
        else:
            status_host = StatusHostAttributes.from_dict(_status_host)

        disable_in_status_gui = d.pop("disable_in_status_gui", UNSET)

        status_connection_attributes_output = cls(
            connection=connection,
            proxy=proxy,
            connect_timeout=connect_timeout,
            persistent_connection=persistent_connection,
            url_prefix=url_prefix,
            status_host=status_host,
            disable_in_status_gui=disable_in_status_gui,
        )

        status_connection_attributes_output.additional_properties = d
        return status_connection_attributes_output

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
