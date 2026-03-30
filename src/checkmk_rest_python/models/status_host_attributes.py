from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusHostAttributes")


@_attrs_define
class StatusHostAttributes:
    """
    Attributes:
        status_host_set (str): enabled for 'use the following status host' and disabled for 'no status host'. Example:
            True.
        site (str | Unset): The site ID of the status host. Example: prod.
        host (str | Unset): The host name of the status host. Example: host_1.
    """

    status_host_set: str
    site: str | Unset = UNSET
    host: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_host_set = self.status_host_set

        site = self.site

        host = self.host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_host_set": status_host_set,
            }
        )
        if site is not UNSET:
            field_dict["site"] = site
        if host is not UNSET:
            field_dict["host"] = host

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_host_set = d.pop("status_host_set")

        site = d.pop("site", UNSET)

        host = d.pop("host", UNSET)

        status_host_attributes = cls(
            status_host_set=status_host_set,
            site=site,
            host=host,
        )

        status_host_attributes.additional_properties = d
        return status_host_attributes

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
