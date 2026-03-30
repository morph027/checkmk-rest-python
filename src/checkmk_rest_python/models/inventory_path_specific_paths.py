from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_path_specific_path import InventoryPathSpecificPath


T = TypeVar("T", bound="InventoryPathSpecificPaths")


@_attrs_define
class InventoryPathSpecificPaths:
    """
    Attributes:
        paths (list[InventoryPathSpecificPath]): A list of paths to be allowed.
        type_ (Any | Unset): Allowed to see parts of the tree. Default: 'specific_paths'.
    """

    paths: list[InventoryPathSpecificPath]
    type_: Any | Unset = "specific_paths"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paths = []
        for paths_item_data in self.paths:
            paths_item = paths_item_data.to_dict()
            paths.append(paths_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paths": paths,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_path_specific_path import InventoryPathSpecificPath

        d = dict(src_dict)
        paths = []
        _paths = d.pop("paths")
        for paths_item_data in _paths:
            paths_item = InventoryPathSpecificPath.from_dict(paths_item_data)

            paths.append(paths_item)

        type_ = d.pop("type", UNSET)

        inventory_path_specific_paths = cls(
            paths=paths,
            type_=type_,
        )

        inventory_path_specific_paths.additional_properties = d
        return inventory_path_specific_paths

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
