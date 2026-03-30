from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_state_with_params_filter_type import (
    ChangeStateWithParamsFilterType,
)
from ..models.change_state_with_params_new_state import ChangeStateWithParamsNewState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_params import FilterParams


T = TypeVar("T", bound="ChangeStateWithParams")


@_attrs_define
class ChangeStateWithParams:
    """
    Attributes:
        filter_type (ChangeStateWithParamsFilterType): The way you would like to filter events. Example: params.
        new_state (ChangeStateWithParamsNewState): The state Example: ok.
        filters (FilterParams):
        site_id (str | Unset): An existing site id Example: mysite.
    """

    filter_type: ChangeStateWithParamsFilterType
    new_state: ChangeStateWithParamsNewState
    filters: FilterParams
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type.value

        new_state = self.new_state.value

        filters = self.filters.to_dict()

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "new_state": new_state,
                "filters": filters,
            }
        )
        if site_id is not UNSET:
            field_dict["site_id"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_params import FilterParams

        d = dict(src_dict)
        filter_type = ChangeStateWithParamsFilterType(d.pop("filter_type"))

        new_state = ChangeStateWithParamsNewState(d.pop("new_state"))

        filters = FilterParams.from_dict(d.pop("filters"))

        site_id = d.pop("site_id", UNSET)

        change_state_with_params = cls(
            filter_type=filter_type,
            new_state=new_state,
            filters=filters,
            site_id=site_id,
        )

        change_state_with_params.additional_properties = d
        return change_state_with_params

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
