from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_downtime_by_host_group_delete_type import (
    DeleteDowntimeByHostGroupDeleteType,
)

T = TypeVar("T", bound="DeleteDowntimeByHostGroup")


@_attrs_define
class DeleteDowntimeByHostGroup:
    """
    Attributes:
        delete_type (DeleteDowntimeByHostGroupDeleteType): The option how to delete a downtime. Example: params.
        hostgroup_name (str): Name of a valid hostgroup, all current downtimes for hosts in this group will be deleted.
            Example: windows.
    """

    delete_type: DeleteDowntimeByHostGroupDeleteType
    hostgroup_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        hostgroup_name = self.hostgroup_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete_type": delete_type,
                "hostgroup_name": hostgroup_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteDowntimeByHostGroupDeleteType(d.pop("delete_type"))

        hostgroup_name = d.pop("hostgroup_name")

        delete_downtime_by_host_group = cls(
            delete_type=delete_type,
            hostgroup_name=hostgroup_name,
        )

        delete_downtime_by_host_group.additional_properties = d
        return delete_downtime_by_host_group

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
