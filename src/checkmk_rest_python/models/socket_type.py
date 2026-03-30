from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.socket_type_socket_type import SocketTypeSocketType

T = TypeVar("T", bound="SocketType")


@_attrs_define
class SocketType:
    """
    Attributes:
        socket_type (SocketTypeSocketType): The connection name. This can be tcp, tcp6, unix or local. Example: tcp.
    """

    socket_type: SocketTypeSocketType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        socket_type = self.socket_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "socket_type": socket_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        socket_type = SocketTypeSocketType(d.pop("socket_type"))

        socket_type = cls(
            socket_type=socket_type,
        )

        socket_type.additional_properties = d
        return socket_type

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
