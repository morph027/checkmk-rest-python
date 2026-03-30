from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BinaryExpr")


@_attrs_define
class BinaryExpr:
    """
    Attributes:
        op (str | Unset): The operator.
        left (str | Unset): The LiveStatus column name. Example: name.
        right (str | Unset): The value to compare the column to.
    """

    op: str | Unset = UNSET
    left: str | Unset = UNSET
    right: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op

        left = self.left

        right = self.right

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if op is not UNSET:
            field_dict["op"] = op
        if left is not UNSET:
            field_dict["left"] = left
        if right is not UNSET:
            field_dict["right"] = right

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = d.pop("op", UNSET)

        left = d.pop("left", UNSET)

        right = d.pop("right", UNSET)

        binary_expr = cls(
            op=op,
            left=left,
            right=right,
        )

        binary_expr.additional_properties = d
        return binary_expr

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
