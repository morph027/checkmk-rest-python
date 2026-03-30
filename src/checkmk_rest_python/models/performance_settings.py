from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceSettings")


@_attrs_define
class PerformanceSettings:
    """
    Attributes:
        responses_timeout (int | Unset): Timeout for responses Default: 8. Example: 8.
        hop_probes (int | Unset): Number of probes per hop Default: 2. Example: 2.
        max_gateway_distance (int | Unset): Maximum distance (TTL) to gateway Default: 10. Example: 10.
        ping_probes (int | Unset): Number of ping probes Default: 5. Example: 5.
    """

    responses_timeout: int | Unset = 8
    hop_probes: int | Unset = 2
    max_gateway_distance: int | Unset = 10
    ping_probes: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responses_timeout = self.responses_timeout

        hop_probes = self.hop_probes

        max_gateway_distance = self.max_gateway_distance

        ping_probes = self.ping_probes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses_timeout is not UNSET:
            field_dict["responses_timeout"] = responses_timeout
        if hop_probes is not UNSET:
            field_dict["hop_probes"] = hop_probes
        if max_gateway_distance is not UNSET:
            field_dict["max_gateway_distance"] = max_gateway_distance
        if ping_probes is not UNSET:
            field_dict["ping_probes"] = ping_probes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        responses_timeout = d.pop("responses_timeout", UNSET)

        hop_probes = d.pop("hop_probes", UNSET)

        max_gateway_distance = d.pop("max_gateway_distance", UNSET)

        ping_probes = d.pop("ping_probes", UNSET)

        performance_settings = cls(
            responses_timeout=responses_timeout,
            hop_probes=hop_probes,
            max_gateway_distance=max_gateway_distance,
            ping_probes=ping_probes,
        )

        performance_settings.additional_properties = d
        return performance_settings

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
