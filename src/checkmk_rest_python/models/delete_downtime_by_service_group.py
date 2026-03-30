from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_downtime_by_service_group_delete_type import (
    DeleteDowntimeByServiceGroupDeleteType,
)

T = TypeVar("T", bound="DeleteDowntimeByServiceGroup")


@_attrs_define
class DeleteDowntimeByServiceGroup:
    """
    Attributes:
        delete_type (DeleteDowntimeByServiceGroupDeleteType): The option how to delete a downtime. Example: params.
        servicegroup_name (str): Name of a valid servicegroup, all current downtimes for services in this group will be
            deleted. Example: windows.
    """

    delete_type: DeleteDowntimeByServiceGroupDeleteType
    servicegroup_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        servicegroup_name = self.servicegroup_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete_type": delete_type,
                "servicegroup_name": servicegroup_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteDowntimeByServiceGroupDeleteType(d.pop("delete_type"))

        servicegroup_name = d.pop("servicegroup_name")

        delete_downtime_by_service_group = cls(
            delete_type=delete_type,
            servicegroup_name=servicegroup_name,
        )

        delete_downtime_by_service_group.additional_properties = d
        return delete_downtime_by_service_group

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
