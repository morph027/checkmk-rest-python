from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPNetwork")


@_attrs_define
class IPNetwork:
    """
    Attributes:
        type_ (Any | Unset): A single IPv4 network in CIDR notation. Default: 'ip_network'.
        network (str | Unset): A IPv4 network in CIDR notation. Minimum prefix length is 8 bit, maximum prefix length is
            30 bit.

            Valid examples:

             * `192.168.0.0/24`
             * `192.168.0.0/255.255.255.0`
    """

    type_: Any | Unset = "ip_network"
    network: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        network = self.network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        network = d.pop("network", UNSET)

        ip_network = cls(
            type_=type_,
            network=network,
        )

        ip_network.additional_properties = d
        return ip_network

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
