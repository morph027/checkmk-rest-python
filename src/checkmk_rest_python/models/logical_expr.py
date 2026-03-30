from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="LogicalExpr")


@_attrs_define
class LogicalExpr:
    """
    Attributes:
        op (str | Unset): The operator.
        expr (list[BinaryExpr | LogicalExpr | NotExpr] | Unset):
    """

    op: str | Unset = UNSET
    expr: list[BinaryExpr | LogicalExpr | NotExpr] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.not_expr import NotExpr

        op = self.op

        expr: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expr, Unset):
            expr = []
            for expr_item_data in self.expr:
                expr_item: dict[str, Any]
                if isinstance(expr_item_data, LogicalExpr):
                    expr_item = expr_item_data.to_dict()
                elif isinstance(expr_item_data, NotExpr):
                    expr_item = expr_item_data.to_dict()
                else:
                    expr_item = expr_item_data.to_dict()

                expr.append(expr_item)

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
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        op = d.pop("op", UNSET)

        _expr = d.pop("expr", UNSET)
        expr: list[BinaryExpr | LogicalExpr | NotExpr] | Unset = UNSET
        if _expr is not UNSET:
            expr = []
            for expr_item_data in _expr:

                def _parse_expr_item(
                    data: object,
                ) -> BinaryExpr | LogicalExpr | NotExpr:
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

                expr_item = _parse_expr_item(expr_item_data)

                expr.append(expr_item)

        logical_expr = cls(
            op=op,
            expr=expr,
        )

        logical_expr.additional_properties = d
        return logical_expr

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
