from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.use_live_status_daemon_use_livestatus_daemon import (
    UseLiveStatusDaemonUseLivestatusDaemon,
)

T = TypeVar("T", bound="UseLiveStatusDaemon")


@_attrs_define
class UseLiveStatusDaemon:
    """
    Attributes:
        use_livestatus_daemon (UseLiveStatusDaemonUseLivestatusDaemon): Use livestatus daemon with direct connection or
            with livestatus proxy. Example: True.
    """

    use_livestatus_daemon: UseLiveStatusDaemonUseLivestatusDaemon
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_livestatus_daemon = self.use_livestatus_daemon.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use_livestatus_daemon": use_livestatus_daemon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_livestatus_daemon = UseLiveStatusDaemonUseLivestatusDaemon(
            d.pop("use_livestatus_daemon")
        )

        use_live_status_daemon = cls(
            use_livestatus_daemon=use_livestatus_daemon,
        )

        use_live_status_daemon.additional_properties = d
        return use_live_status_daemon

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
