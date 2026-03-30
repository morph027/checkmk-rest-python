from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpectrumPluginBase")


@_attrs_define
class SpectrumPluginBase:
    """
    Attributes:
        plugin_name (Any): The Spectrum plug-in. Default: 'spectrum'. Example: spectrum.
        destination_ip (str): IP address of the Spectrum server receiving the SNMP trap Example: 127.0.0.1.
        snmp_community (str): SNMP community for the SNMP trap. The password entered here is stored in plain text within
            the monitoring site. This usually needed because the monitoring process needs to have access to the unencrypted
            password because it needs to submit it to authenticate with remote systems
        base_oid (str | Unset): The base OID for the trap content Default: '1.3.6.1.4.1.1234'. Example:
            1.3.6.1.4.1.1234.
    """

    destination_ip: str
    snmp_community: str
    plugin_name: Any = "spectrum"
    base_oid: str | Unset = "1.3.6.1.4.1.1234"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_name = self.plugin_name

        destination_ip = self.destination_ip

        snmp_community = self.snmp_community

        base_oid = self.base_oid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
                "destination_ip": destination_ip,
                "snmp_community": snmp_community,
            }
        )
        if base_oid is not UNSET:
            field_dict["base_oid"] = base_oid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        destination_ip = d.pop("destination_ip")

        snmp_community = d.pop("snmp_community")

        base_oid = d.pop("base_oid", UNSET)

        spectrum_plugin_base = cls(
            plugin_name=plugin_name,
            destination_ip=destination_ip,
            snmp_community=snmp_community,
            base_oid=base_oid,
        )

        spectrum_plugin_base.additional_properties = d
        return spectrum_plugin_base

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
