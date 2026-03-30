from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.socket_unix_attributes_socket_type import SocketUnixAttributesSocketType

T = TypeVar("T", bound="SocketUnixAttributes")


@_attrs_define
class SocketUnixAttributes:
    """
    Attributes:
        socket_type (SocketUnixAttributesSocketType): The connection name. This can be tcp, tcp6, unix or local.
            Example: tcp.
        path (str): When the connection name is unix, this is the path to the unix socket. Example:
            /path/to/your/unix_socket.
    """

    socket_type: SocketUnixAttributesSocketType
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        socket_type = self.socket_type.value

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socket_type": socket_type,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        socket_type = SocketUnixAttributesSocketType(d.pop("socket_type"))

        path = d.pop("path")

        socket_unix_attributes = cls(
            socket_type=socket_type,
            path=path,
        )

        socket_unix_attributes.additional_properties = d
        return socket_unix_attributes

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
