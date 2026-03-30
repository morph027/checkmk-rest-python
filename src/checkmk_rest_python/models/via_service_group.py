from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.via_service_group_acknowledge_type import ViaServiceGroupAcknowledgeType

T = TypeVar("T", bound="ViaServiceGroup")


@_attrs_define
class ViaServiceGroup:
    """
    Attributes:
        acknowledge_type (ViaServiceGroupAcknowledgeType): Select all services in a service group. Example:
            servicegroup.
        servicegroup_name (str): The name of the service group. Any host having a service in this group will be A
            downtime will be scheduled for all hosts in this group. Example: windows.
    """

    acknowledge_type: ViaServiceGroupAcknowledgeType
    servicegroup_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledge_type = self.acknowledge_type.value

        servicegroup_name = self.servicegroup_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledge_type": acknowledge_type,
                "servicegroup_name": servicegroup_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledge_type = ViaServiceGroupAcknowledgeType(d.pop("acknowledge_type"))

        servicegroup_name = d.pop("servicegroup_name")

        via_service_group = cls(
            acknowledge_type=acknowledge_type,
            servicegroup_name=servicegroup_name,
        )

        via_service_group.additional_properties = d
        return via_service_group

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
