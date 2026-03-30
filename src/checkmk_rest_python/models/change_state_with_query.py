from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_state_with_query_filter_type import ChangeStateWithQueryFilterType
from ..models.change_state_with_query_new_state import ChangeStateWithQueryNewState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="ChangeStateWithQuery")


@_attrs_define
class ChangeStateWithQuery:
    """
    Attributes:
        filter_type (ChangeStateWithQueryFilterType): The way you would like to filter events. Example: params.
        new_state (ChangeStateWithQueryNewState): The state Example: ok.
        query (BinaryExpr | LogicalExpr | NotExpr):
        site_id (str | Unset): An existing site id Example: mysite.
    """

    filter_type: ChangeStateWithQueryFilterType
    new_state: ChangeStateWithQueryNewState
    query: BinaryExpr | LogicalExpr | NotExpr
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        filter_type = self.filter_type.value

        new_state = self.new_state.value

        query: dict[str, Any]
        if isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "new_state": new_state,
                "query": query,
            }
        )
        if site_id is not UNSET:
            field_dict["site_id"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        filter_type = ChangeStateWithQueryFilterType(d.pop("filter_type"))

        new_state = ChangeStateWithQueryNewState(d.pop("new_state"))

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

        site_id = d.pop("site_id", UNSET)

        change_state_with_query = cls(
            filter_type=filter_type,
            new_state=new_state,
            query=query,
            site_id=site_id,
        )

        change_state_with_query.additional_properties = d
        return change_state_with_query

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
