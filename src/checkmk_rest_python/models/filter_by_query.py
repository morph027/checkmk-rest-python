from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_by_query_filter_type import FilterByQueryFilterType

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="FilterByQuery")


@_attrs_define
class FilterByQuery:
    """
    Attributes:
        filter_type (FilterByQueryFilterType): The way you would like to filter events. Example: by_id.
        query (BinaryExpr | LogicalExpr | NotExpr):
    """

    filter_type: FilterByQueryFilterType
    query: BinaryExpr | LogicalExpr | NotExpr
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        filter_type = self.filter_type.value

        query: dict[str, Any]
        if isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "query": query,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        filter_type = FilterByQueryFilterType(d.pop("filter_type"))

        def _parse_query(data: object) -> BinaryExpr | LogicalExpr | NotExpr:
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

        query = _parse_query(d.pop("query"))

        filter_by_query = cls(
            filter_type=filter_type,
            query=query,
        )

        filter_by_query.additional_properties = d
        return filter_by_query

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
