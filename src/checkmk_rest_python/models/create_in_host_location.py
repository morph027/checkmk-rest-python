from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_in_host_location_option import CreateInHostLocationOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInHostLocation")


@_attrs_define
class CreateInHostLocation:
    """
    Attributes:
        option (CreateInHostLocationOption): Creation of gateway hosts option Example: no_gateway_hosts.
        hosts_alias (str | Unset): Alias for created gateway hosts Default: 'Created by parent scan'. Example: Created
            by parent scan.
    """

    option: CreateInHostLocationOption
    hosts_alias: str | Unset = "Created by parent scan"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        hosts_alias = self.hosts_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
            }
        )
        if hosts_alias is not UNSET:
            field_dict["hosts_alias"] = hosts_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = CreateInHostLocationOption(d.pop("option"))

        hosts_alias = d.pop("hosts_alias", UNSET)

        create_in_host_location = cls(
            option=option,
            hosts_alias=hosts_alias,
        )

        create_in_host_location.additional_properties = d
        return create_in_host_location

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
