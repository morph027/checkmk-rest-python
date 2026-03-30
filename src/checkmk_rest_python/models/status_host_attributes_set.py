from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_host_attributes_set_status_host_set import (
    StatusHostAttributesSetStatusHostSet,
)

T = TypeVar("T", bound="StatusHostAttributesSet")


@_attrs_define
class StatusHostAttributesSet:
    """
    Attributes:
        status_host_set (StatusHostAttributesSetStatusHostSet): enabled for 'use the following status host' and disabled
            for 'no status host'
        site (str): The site ID of the status host. Example: prod.
        host (str): The host name of the status host. Example: host_1.
    """

    status_host_set: StatusHostAttributesSetStatusHostSet
    site: str
    host: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_host_set = self.status_host_set.value

        site = self.site

        host = self.host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_host_set": status_host_set,
                "site": site,
                "host": host,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_host_set = StatusHostAttributesSetStatusHostSet(d.pop("status_host_set"))

        site = d.pop("site")

        host = d.pop("host")

        status_host_attributes_set = cls(
            status_host_set=status_host_set,
            site=site,
            host=host,
        )

        status_host_attributes_set.additional_properties = d
        return status_host_attributes_set

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
