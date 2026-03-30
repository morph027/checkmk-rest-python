from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bi_aggregation_function_best_restrict_state import (
    BIAggregationFunctionBestRestrictState,
)

T = TypeVar("T", bound="BIAggregationFunctionBest")


@_attrs_define
class BIAggregationFunctionBest:
    """
    Attributes:
        type_ (Any): Take the best state from all child nodes. Default: 'best'.
        count (int): Take the nth best state.
        restrict_state (BIAggregationFunctionBestRestrictState): Maximum severity for this node.
    """

    count: int
    restrict_state: BIAggregationFunctionBestRestrictState
    type_: Any = "best"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        count = self.count

        restrict_state = self.restrict_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "count": count,
                "restrict_state": restrict_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        count = d.pop("count")

        restrict_state = BIAggregationFunctionBestRestrictState(d.pop("restrict_state"))

        bi_aggregation_function_best = cls(
            type_=type_,
            count=count,
            restrict_state=restrict_state,
        )

        bi_aggregation_function_best.additional_properties = d
        return bi_aggregation_function_best

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
