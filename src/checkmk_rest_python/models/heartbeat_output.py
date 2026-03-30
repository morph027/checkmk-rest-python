from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeartbeatOutput")


@_attrs_define
class HeartbeatOutput:
    """
    Attributes:
        interval (int | Unset): The heartbeat interval for the TCP connection. Example: 5.
        timeout (float | Unset): The heartbeat timeout for the TCP connection. Example: 2.0.
    """

    interval: int | Unset = UNSET
    timeout: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        timeout = self.timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interval is not UNSET:
            field_dict["interval"] = interval
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval = d.pop("interval", UNSET)

        timeout = d.pop("timeout", UNSET)

        heartbeat_output = cls(
            interval=interval,
            timeout=timeout,
        )

        heartbeat_output.additional_properties = d
        return heartbeat_output

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
