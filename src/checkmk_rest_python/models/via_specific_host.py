from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.via_specific_host_acknowledge_type import ViaSpecificHostAcknowledgeType

T = TypeVar("T", bound="ViaSpecificHost")


@_attrs_define
class ViaSpecificHost:
    """
    Attributes:
        acknowledge_type (ViaSpecificHostAcknowledgeType): Select a specific host. Example: host.
        host_name (str): The name of the host. Example: example.com.
    """

    acknowledge_type: ViaSpecificHostAcknowledgeType
    host_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledge_type = self.acknowledge_type.value

        host_name = self.host_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledge_type": acknowledge_type,
                "host_name": host_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledge_type = ViaSpecificHostAcknowledgeType(d.pop("acknowledge_type"))

        host_name = d.pop("host_name")

        via_specific_host = cls(
            acknowledge_type=acknowledge_type,
            host_name=host_name,
        )

        via_specific_host.additional_properties = d
        return via_specific_host

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
