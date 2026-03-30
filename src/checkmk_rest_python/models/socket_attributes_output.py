from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocketAttributesOutput")


@_attrs_define
class SocketAttributesOutput:
    """
    Attributes:
        socket_type (str): The connection name. This can be tcp, tcp6, unix or local. Example: tcp.
        path (str | Unset): When the connection name is unix, this is the path to the unix socket. Example:
            /path/to/your/unix_socket.
        host (str | Unset): The IP or domain name of the host. Example: 127.0.0.1.
        port (int | Unset): The TCP port to connect to. Example: 6792.
        encrypted (bool | Unset): To enable an encrypted connection. Example: True.
        verify (bool | Unset): Verify server certificate. Example: True.
    """

    socket_type: str
    path: str | Unset = UNSET
    host: str | Unset = UNSET
    port: int | Unset = UNSET
    encrypted: bool | Unset = UNSET
    verify: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        socket_type = self.socket_type

        path = self.path

        host = self.host

        port = self.port

        encrypted = self.encrypted

        verify = self.verify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socket_type": socket_type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if verify is not UNSET:
            field_dict["verify"] = verify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        socket_type = d.pop("socket_type")

        path = d.pop("path", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        verify = d.pop("verify", UNSET)

        socket_attributes_output = cls(
            socket_type=socket_type,
            path=path,
            host=host,
            port=port,
            encrypted=encrypted,
            verify=verify,
        )

        socket_attributes_output.additional_properties = d
        return socket_attributes_output

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
