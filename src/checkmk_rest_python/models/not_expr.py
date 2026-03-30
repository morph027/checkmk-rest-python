from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr


T = TypeVar("T", bound="NotExpr")


@_attrs_define
class NotExpr:
    """
    Attributes:
        op (str | Unset): The operator. In this case `not`.
        expr (BinaryExpr | LogicalExpr | NotExpr | Unset):
    """

    op: str | Unset = UNSET
    expr: BinaryExpr | LogicalExpr | NotExpr | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr

        op = self.op

        expr: dict[str, Any] | Unset
        if isinstance(self.expr, Unset):
            expr = UNSET
        elif isinstance(self.expr, LogicalExpr):
            expr = self.expr.to_dict()
        elif isinstance(self.expr, NotExpr):
            expr = self.expr.to_dict()
        else:
            expr = self.expr.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if expr is not UNSET:
            field_dict["expr"] = expr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr

        d = dict(src_dict)
        op = d.pop("op", UNSET)

        def _parse_expr(data: object) -> BinaryExpr | LogicalExpr | NotExpr | Unset:
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

        expr = _parse_expr(d.pop("expr", UNSET))

        not_expr = cls(
            op=op,
            expr=expr,
        )

        not_expr.additional_properties = d
        return not_expr

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
