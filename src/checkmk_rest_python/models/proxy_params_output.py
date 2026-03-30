from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heartbeat_output import HeartbeatOutput


T = TypeVar("T", bound="ProxyParamsOutput")


@_attrs_define
class ProxyParamsOutput:
    """
    Attributes:
        channels (int | Unset): The number of channels to keep open. Example: 5.
        heartbeat (HeartbeatOutput | Unset):
        channel_timeout (float | Unset): The timeout waiting for a free channel. Example: 3.0.
        query_timeout (float | Unset): The total query timeout. Example: 120.0.
        connect_retry (float | Unset): The cooling period after failed connect/heartbeat. Example: 4.0.
        cache (bool | Unset): Enable caching. Example: True.
    """

    channels: int | Unset = UNSET
    heartbeat: HeartbeatOutput | Unset = UNSET
    channel_timeout: float | Unset = UNSET
    query_timeout: float | Unset = UNSET
    connect_retry: float | Unset = UNSET
    cache: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = self.channels

        heartbeat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heartbeat, Unset):
            heartbeat = self.heartbeat.to_dict()

        channel_timeout = self.channel_timeout

        query_timeout = self.query_timeout

        connect_retry = self.connect_retry

        cache = self.cache

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if heartbeat is not UNSET:
            field_dict["heartbeat"] = heartbeat
        if channel_timeout is not UNSET:
            field_dict["channel_timeout"] = channel_timeout
        if query_timeout is not UNSET:
            field_dict["query_timeout"] = query_timeout
        if connect_retry is not UNSET:
            field_dict["connect_retry"] = connect_retry
        if cache is not UNSET:
            field_dict["cache"] = cache

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heartbeat_output import HeartbeatOutput

        d = dict(src_dict)
        channels = d.pop("channels", UNSET)

        _heartbeat = d.pop("heartbeat", UNSET)
        heartbeat: HeartbeatOutput | Unset
        if isinstance(_heartbeat, Unset):
            heartbeat = UNSET
        else:
            heartbeat = HeartbeatOutput.from_dict(_heartbeat)

        channel_timeout = d.pop("channel_timeout", UNSET)

        query_timeout = d.pop("query_timeout", UNSET)

        connect_retry = d.pop("connect_retry", UNSET)

        cache = d.pop("cache", UNSET)

        proxy_params_output = cls(
            channels=channels,
            heartbeat=heartbeat,
            channel_timeout=channel_timeout,
            query_timeout=query_timeout,
            connect_retry=connect_retry,
            cache=cache,
        )

        proxy_params_output.additional_properties = d
        return proxy_params_output

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
