from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BIAggregationStateRequest")


@_attrs_define
class BIAggregationStateRequest:
    """
    Attributes:
        filter_names (list[str] | Unset): Filter by names Example: ['Host foo'].
        filter_groups (list[str] | Unset): Filter by group Example: ['My Group'].
    """

    filter_names: list[str] | Unset = UNSET
    filter_groups: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_names: list[str] | Unset = UNSET
        if not isinstance(self.filter_names, Unset):
            filter_names = self.filter_names

        filter_groups: list[str] | Unset = UNSET
        if not isinstance(self.filter_groups, Unset):
            filter_groups = self.filter_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_names is not UNSET:
            field_dict["filter_names"] = filter_names
        if filter_groups is not UNSET:
            field_dict["filter_groups"] = filter_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_names = cast(list[str], d.pop("filter_names", UNSET))

        filter_groups = cast(list[str], d.pop("filter_groups", UNSET))

        bi_aggregation_state_request = cls(
            filter_names=filter_names,
            filter_groups=filter_groups,
        )

        bi_aggregation_state_request.additional_properties = d
        return bi_aggregation_state_request

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
