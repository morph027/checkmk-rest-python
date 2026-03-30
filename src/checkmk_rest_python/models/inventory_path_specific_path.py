from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.no_restriction import NoRestriction
    from ..models.restrict_all import RestrictAll
    from ..models.restrict_values import RestrictValues


T = TypeVar("T", bound="InventoryPathSpecificPath")


@_attrs_define
class InventoryPathSpecificPath:
    """
    Attributes:
        path (str): Path to category.
        attributes (NoRestriction | RestrictAll | RestrictValues | Unset):
        columns (NoRestriction | RestrictAll | RestrictValues | Unset):
        nodes (NoRestriction | RestrictAll | RestrictValues | Unset):
    """

    path: str
    attributes: NoRestriction | RestrictAll | RestrictValues | Unset = UNSET
    columns: NoRestriction | RestrictAll | RestrictValues | Unset = UNSET
    nodes: NoRestriction | RestrictAll | RestrictValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.no_restriction import NoRestriction
        from ..models.restrict_all import RestrictAll

        path = self.path

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, NoRestriction):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, RestrictAll):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        columns: dict[str, Any] | Unset
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, NoRestriction):
            columns = self.columns.to_dict()
        elif isinstance(self.columns, RestrictAll):
            columns = self.columns.to_dict()
        else:
            columns = self.columns.to_dict()

        nodes: dict[str, Any] | Unset
        if isinstance(self.nodes, Unset):
            nodes = UNSET
        elif isinstance(self.nodes, NoRestriction):
            nodes = self.nodes.to_dict()
        elif isinstance(self.nodes, RestrictAll):
            nodes = self.nodes.to_dict()
        else:
            nodes = self.nodes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if columns is not UNSET:
            field_dict["columns"] = columns
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.no_restriction import NoRestriction
        from ..models.restrict_all import RestrictAll
        from ..models.restrict_values import RestrictValues

        d = dict(src_dict)
        path = d.pop("path")

        def _parse_attributes(
            data: object,
        ) -> NoRestriction | RestrictAll | RestrictValues | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_0 = NoRestriction.from_dict(
                    data
                )

                return componentsschemas_path_restriction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_1 = RestrictAll.from_dict(data)

                return componentsschemas_path_restriction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_path_restriction_type_2 = RestrictValues.from_dict(data)

            return componentsschemas_path_restriction_type_2

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        def _parse_columns(
            data: object,
        ) -> NoRestriction | RestrictAll | RestrictValues | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_0 = NoRestriction.from_dict(
                    data
                )

                return componentsschemas_path_restriction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_1 = RestrictAll.from_dict(data)

                return componentsschemas_path_restriction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_path_restriction_type_2 = RestrictValues.from_dict(data)

            return componentsschemas_path_restriction_type_2

        columns = _parse_columns(d.pop("columns", UNSET))

        def _parse_nodes(
            data: object,
        ) -> NoRestriction | RestrictAll | RestrictValues | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_0 = NoRestriction.from_dict(
                    data
                )

                return componentsschemas_path_restriction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_path_restriction_type_1 = RestrictAll.from_dict(data)

                return componentsschemas_path_restriction_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_path_restriction_type_2 = RestrictValues.from_dict(data)

            return componentsschemas_path_restriction_type_2

        nodes = _parse_nodes(d.pop("nodes", UNSET))

        inventory_path_specific_path = cls(
            path=path,
            attributes=attributes,
            columns=columns,
            nodes=nodes,
        )

        inventory_path_specific_path.additional_properties = d
        return inventory_path_specific_path

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
