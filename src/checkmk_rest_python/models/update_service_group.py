from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_service_group_attributes import UpdateServiceGroupAttributes


T = TypeVar("T", bound="UpdateServiceGroup")


@_attrs_define
class UpdateServiceGroup:
    """
    Attributes:
        name (str): The name of the service group. Example: windows.
        attributes (UpdateServiceGroupAttributes):
    """

    name: str
    attributes: UpdateServiceGroupAttributes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_service_group_attributes import (
            UpdateServiceGroupAttributes,
        )

        d = dict(src_dict)
        name = d.pop("name")

        attributes = UpdateServiceGroupAttributes.from_dict(d.pop("attributes"))

        update_service_group = cls(
            name=name,
            attributes=attributes,
        )

        update_service_group.additional_properties = d
        return update_service_group

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
