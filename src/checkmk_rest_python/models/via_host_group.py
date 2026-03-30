from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.via_host_group_acknowledge_type import ViaHostGroupAcknowledgeType

T = TypeVar("T", bound="ViaHostGroup")


@_attrs_define
class ViaHostGroup:
    """
    Attributes:
        acknowledge_type (ViaHostGroupAcknowledgeType): Select all hosts in a host group. Example: hostgroup.
        hostgroup_name (str): Host group name for which this acknowledgement is for. Example: Servers.
    """

    acknowledge_type: ViaHostGroupAcknowledgeType
    hostgroup_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledge_type = self.acknowledge_type.value

        hostgroup_name = self.hostgroup_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledge_type": acknowledge_type,
                "hostgroup_name": hostgroup_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledge_type = ViaHostGroupAcknowledgeType(d.pop("acknowledge_type"))

        hostgroup_name = d.pop("hostgroup_name")

        via_host_group = cls(
            acknowledge_type=acknowledge_type,
            hostgroup_name=hostgroup_name,
        )

        via_host_group.additional_properties = d
        return via_host_group

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
