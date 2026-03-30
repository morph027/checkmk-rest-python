from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connection_mode_connection_mode import ConnectionModeConnectionMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionMode")


@_attrs_define
class ConnectionMode:
    """
    Attributes:
        connection_mode (ConnectionModeConnectionMode | Unset): This configures the communication direction of this
            host.
             * `pull-agent` (default) - The server will try to contact the monitored host and pull the data by initializing
            a TCP connection
             * `push-agent` - the host is expected to send the data to the monitoring server without being triggered
    """

    connection_mode: ConnectionModeConnectionMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_mode: str | Unset = UNSET
        if not isinstance(self.connection_mode, Unset):
            connection_mode = self.connection_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_mode is not UNSET:
            field_dict["connection_mode"] = connection_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _connection_mode = d.pop("connection_mode", UNSET)
        connection_mode: ConnectionModeConnectionMode | Unset
        if isinstance(_connection_mode, Unset):
            connection_mode = UNSET
        else:
            connection_mode = ConnectionModeConnectionMode(_connection_mode)

        connection_mode = cls(
            connection_mode=connection_mode,
        )

        connection_mode.additional_properties = d
        return connection_mode

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
