from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.no_gateway_hosts_option import NoGatewayHostsOption

T = TypeVar("T", bound="NoGatewayHosts")


@_attrs_define
class NoGatewayHosts:
    """
    Attributes:
        option (NoGatewayHostsOption): Creation of gateway hosts option Example: no_gateway_hosts.
    """

    option: NoGatewayHostsOption
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = NoGatewayHostsOption(d.pop("option"))

        no_gateway_hosts = cls(
            option=option,
        )

        no_gateway_hosts.additional_properties = d
        return no_gateway_hosts

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
