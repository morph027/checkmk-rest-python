from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_path_allow_all import InventoryPathAllowAll
    from ..models.inventory_path_forbid_all import InventoryPathForbidAll
    from ..models.inventory_path_specific_paths import InventoryPathSpecificPaths


T = TypeVar("T", bound="ContactGroupExtensions")


@_attrs_define
class ContactGroupExtensions:
    """
    Attributes:
        inventory_paths (InventoryPathAllowAll | InventoryPathForbidAll | InventoryPathSpecificPaths | Unset):
    """

    inventory_paths: (
        InventoryPathAllowAll
        | InventoryPathForbidAll
        | InventoryPathSpecificPaths
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_path_allow_all import InventoryPathAllowAll
        from ..models.inventory_path_forbid_all import InventoryPathForbidAll

        inventory_paths: dict[str, Any] | Unset
        if isinstance(self.inventory_paths, Unset):
            inventory_paths = UNSET
        elif isinstance(self.inventory_paths, InventoryPathAllowAll):
            inventory_paths = self.inventory_paths.to_dict()
        elif isinstance(self.inventory_paths, InventoryPathForbidAll):
            inventory_paths = self.inventory_paths.to_dict()
        else:
            inventory_paths = self.inventory_paths.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_paths is not UNSET:
            field_dict["inventory_paths"] = inventory_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_path_allow_all import InventoryPathAllowAll
        from ..models.inventory_path_forbid_all import InventoryPathForbidAll
        from ..models.inventory_path_specific_paths import InventoryPathSpecificPaths

        d = dict(src_dict)

        def _parse_inventory_paths(
            data: object,
        ) -> (
            InventoryPathAllowAll
            | InventoryPathForbidAll
            | InventoryPathSpecificPaths
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_inventory_paths_type_0 = (
                    InventoryPathAllowAll.from_dict(data)
                )

                return componentsschemas_inventory_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_inventory_paths_type_1 = (
                    InventoryPathForbidAll.from_dict(data)
                )

                return componentsschemas_inventory_paths_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_inventory_paths_type_2 = (
                InventoryPathSpecificPaths.from_dict(data)
            )

            return componentsschemas_inventory_paths_type_2

        inventory_paths = _parse_inventory_paths(d.pop("inventory_paths", UNSET))

        contact_group_extensions = cls(
            inventory_paths=inventory_paths,
        )

        contact_group_extensions.additional_properties = d
        return contact_group_extensions

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
