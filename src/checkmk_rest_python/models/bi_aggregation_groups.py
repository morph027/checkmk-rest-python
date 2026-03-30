from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BIAggregationGroups")


@_attrs_define
class BIAggregationGroups:
    """
    Attributes:
        names (list[str] | Unset): List of group names. Example: ['group1', 'group2'].
        paths (list[list[str]] | Unset): List of group paths. Example: [['path', 'of', 'group1']].
    """

    names: list[str] | Unset = UNSET
    paths: list[list[str]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        names: list[str] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        paths: list[list[str]] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = []
            for paths_item_data in self.paths:
                paths_item = paths_item_data

                paths.append(paths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if names is not UNSET:
            field_dict["names"] = names
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        names = cast(list[str], d.pop("names", UNSET))

        _paths = d.pop("paths", UNSET)
        paths: list[list[str]] | Unset = UNSET
        if _paths is not UNSET:
            paths = []
            for paths_item_data in _paths:
                paths_item = cast(list[str], paths_item_data)

                paths.append(paths_item)

        bi_aggregation_groups = cls(
            names=names,
            paths=paths,
        )

        bi_aggregation_groups.additional_properties = d
        return bi_aggregation_groups

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
