from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="ServiceParameters")


@_attrs_define
class ServiceParameters:
    """
    Attributes:
        sites (list[str] | Unset): Restrict the query to this particular site. Example: ['mysite'].
        columns (list[str] | Unset): The desired columns of the `services` table. If left empty, a default set of
            columns is used. Example: ['host_name', 'description'].
        query (BinaryExpr | LogicalExpr | NotExpr | Unset):
    """

    sites: list[str] | Unset = UNSET
    columns: list[str] | Unset = UNSET
    query: BinaryExpr | LogicalExpr | NotExpr | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        sites: list[str] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        columns: list[str] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        query: dict[str, Any] | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites
        if columns is not UNSET:
            field_dict["columns"] = columns
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        sites = cast(list[str], d.pop("sites", UNSET))

        columns = cast(list[str], d.pop("columns", UNSET))

        def _parse_query(data: object) -> BinaryExpr | LogicalExpr | NotExpr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_0 = LogicalExpr.from_dict(data)

                return componentsschemas_expr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_2 = NotExpr.from_dict(data)

                return componentsschemas_expr_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_expr_type_3 = BinaryExpr.from_dict(data)

            return componentsschemas_expr_type_3

        query = _parse_query(d.pop("query", UNSET))

        service_parameters = cls(
            sites=sites,
            columns=columns,
            query=query,
        )

        service_parameters.additional_properties = d
        return service_parameters

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
