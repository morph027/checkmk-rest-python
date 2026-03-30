from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LockedBy")


@_attrs_define
class LockedBy:
    """
    Attributes:
        site_id (str): Site ID
        program_id (str): Program ID
        instance_id (str): Instance ID
    """

    site_id: str
    program_id: str
    instance_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        program_id = self.program_id

        instance_id = self.instance_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
                "program_id": program_id,
                "instance_id": instance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        program_id = d.pop("program_id")

        instance_id = d.pop("instance_id")

        locked_by = cls(
            site_id=site_id,
            program_id=program_id,
            instance_id=instance_id,
        )

        locked_by.additional_properties = d
        return locked_by

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
