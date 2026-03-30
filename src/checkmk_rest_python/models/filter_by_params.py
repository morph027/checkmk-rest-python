from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_by_params_filter_type import FilterByParamsFilterType

if TYPE_CHECKING:
    from ..models.filter_params import FilterParams


T = TypeVar("T", bound="FilterByParams")


@_attrs_define
class FilterByParams:
    """
    Attributes:
        filter_type (FilterByParamsFilterType): The way you would like to filter events. Example: by_id.
        filters (FilterParams):
    """

    filter_type: FilterByParamsFilterType
    filters: FilterParams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type.value

        filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_params import FilterParams

        d = dict(src_dict)
        filter_type = FilterByParamsFilterType(d.pop("filter_type"))

        filters = FilterParams.from_dict(d.pop("filters"))

        filter_by_params = cls(
            filter_type=filter_type,
            filters=filters,
        )

        filter_by_params.additional_properties = d
        return filter_by_params

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
