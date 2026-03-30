from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_by_id_filter_type import FilterByIdFilterType

T = TypeVar("T", bound="FilterById")


@_attrs_define
class FilterById:
    """
    Attributes:
        filter_type (FilterByIdFilterType): The way you would like to filter events. Example: by_id.
        site_id (str): An existing site id Example: mysite.
        event_id (int): The event console ID Example: 1.
    """

    filter_type: FilterByIdFilterType
    site_id: str
    event_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type.value

        site_id = self.site_id

        event_id = self.event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "site_id": site_id,
                "event_id": event_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_type = FilterByIdFilterType(d.pop("filter_type"))

        site_id = d.pop("site_id")

        event_id = d.pop("event_id")

        filter_by_id = cls(
            filter_type=filter_type,
            site_id=site_id,
            event_id=event_id,
        )

        filter_by_id.additional_properties = d
        return filter_by_id

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
