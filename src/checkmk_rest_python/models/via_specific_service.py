from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.via_specific_service_acknowledge_type import (
    ViaSpecificServiceAcknowledgeType,
)

T = TypeVar("T", bound="ViaSpecificService")


@_attrs_define
class ViaSpecificService:
    """
    Attributes:
        acknowledge_type (ViaSpecificServiceAcknowledgeType): Select a specific service on a host. Example: service.
        host_name (str): The name of the host. Example: example.com.
        service_description (str): The acknowledgement process will be applied to all matching service names Example:
            CPU load.
    """

    acknowledge_type: ViaSpecificServiceAcknowledgeType
    host_name: str
    service_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledge_type = self.acknowledge_type.value

        host_name = self.host_name

        service_description = self.service_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledge_type": acknowledge_type,
                "host_name": host_name,
                "service_description": service_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledge_type = ViaSpecificServiceAcknowledgeType(d.pop("acknowledge_type"))

        host_name = d.pop("host_name")

        service_description = d.pop("service_description")

        via_specific_service = cls(
            acknowledge_type=acknowledge_type,
            host_name=host_name,
            service_description=service_description,
        )

        via_specific_service.additional_properties = d
        return via_specific_service

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
