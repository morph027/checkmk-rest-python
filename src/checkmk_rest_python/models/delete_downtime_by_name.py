from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_downtime_by_name_delete_type import DeleteDowntimeByNameDeleteType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteDowntimeByName")


@_attrs_define
class DeleteDowntimeByName:
    """
    Attributes:
        delete_type (DeleteDowntimeByNameDeleteType): The option how to delete a downtime. Example: params.
        host_name (str): If set alone, then all downtimes of the host will be removed. Example: example.com.
        service_descriptions (list[str] | Unset): If set, the downtimes of the listed services of the specified host
            will be removed. If a service has multiple downtimes then all will be removed Example: ['CPU load', 'Memory'].
    """

    delete_type: DeleteDowntimeByNameDeleteType
    host_name: str
    service_descriptions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        host_name = self.host_name

        service_descriptions: list[str] | Unset = UNSET
        if not isinstance(self.service_descriptions, Unset):
            service_descriptions = self.service_descriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete_type": delete_type,
                "host_name": host_name,
            }
        )
        if service_descriptions is not UNSET:
            field_dict["service_descriptions"] = service_descriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteDowntimeByNameDeleteType(d.pop("delete_type"))

        host_name = d.pop("host_name")

        service_descriptions = cast(list[str], d.pop("service_descriptions", UNSET))

        delete_downtime_by_name = cls(
            delete_type=delete_type,
            host_name=host_name,
            service_descriptions=service_descriptions,
        )

        delete_downtime_by_name.additional_properties = d
        return delete_downtime_by_name

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
