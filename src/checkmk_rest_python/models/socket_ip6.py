from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.socket_ip6_socket_type import SocketIP6SocketType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SocketIP6")


@_attrs_define
class SocketIP6:
    """
    Attributes:
        socket_type (SocketIP6SocketType): The connection name. This can be tcp, tcp6, unix or local. Example: tcp.
        port (int): The TCP port to connect to. Example: 6790.
        encrypted (bool): To enable an encrypted connection. Example: True.
        host (str): The IP or domain name of the host. Example: 5402:1db8:95a3:0000:0000:9a2e:0480:8334.
        verify (bool | Unset): Verify server certificate. Example: True.
    """

    socket_type: SocketIP6SocketType
    port: int
    encrypted: bool
    host: str
    verify: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        socket_type = self.socket_type.value

        port = self.port

        encrypted = self.encrypted

        host = self.host

        verify = self.verify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socket_type": socket_type,
                "port": port,
                "encrypted": encrypted,
                "host": host,
            }
        )
        if verify is not UNSET:
            field_dict["verify"] = verify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        socket_type = SocketIP6SocketType(d.pop("socket_type"))

        port = d.pop("port")

        encrypted = d.pop("encrypted")

        host = d.pop("host")

        verify = d.pop("verify", UNSET)

        socket_ip6 = cls(
            socket_type=socket_type,
            port=port,
            encrypted=encrypted,
            host=host,
            verify=verify,
        )

        socket_ip6.additional_properties = d
        return socket_ip6

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
