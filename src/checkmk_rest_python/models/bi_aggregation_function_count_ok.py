from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_aggregation_function_count_settings import (
        BIAggregationFunctionCountSettings,
    )


T = TypeVar("T", bound="BIAggregationFunctionCountOK")


@_attrs_define
class BIAggregationFunctionCountOK:
    """
    Attributes:
        type_ (Any): Count states from child nodes, defaulting to CRIT if both levels aren't met. Default: 'count_ok'.
        levels_ok (BIAggregationFunctionCountSettings):
        levels_warn (BIAggregationFunctionCountSettings):
    """

    levels_ok: BIAggregationFunctionCountSettings
    levels_warn: BIAggregationFunctionCountSettings
    type_: Any = "count_ok"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        levels_ok = self.levels_ok.to_dict()

        levels_warn = self.levels_warn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "levels_ok": levels_ok,
                "levels_warn": levels_warn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_aggregation_function_count_settings import (
            BIAggregationFunctionCountSettings,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        levels_ok = BIAggregationFunctionCountSettings.from_dict(d.pop("levels_ok"))

        levels_warn = BIAggregationFunctionCountSettings.from_dict(d.pop("levels_warn"))

        bi_aggregation_function_count_ok = cls(
            type_=type_,
            levels_ok=levels_ok,
            levels_warn=levels_warn,
        )

        bi_aggregation_function_count_ok.additional_properties = d
        return bi_aggregation_function_count_ok

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
