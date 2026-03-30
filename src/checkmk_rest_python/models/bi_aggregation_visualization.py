from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BIAggregationVisualization")


@_attrs_define
class BIAggregationVisualization:
    """
    Attributes:
        ignore_rule_styles (bool): Ignore rule styles.
        layout_id (str): ID of the layout. Example: radial_layout2.
        line_style (str): Line style to use. Example: round.
    """

    ignore_rule_styles: bool
    layout_id: str
    line_style: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ignore_rule_styles = self.ignore_rule_styles

        layout_id = self.layout_id

        line_style = self.line_style

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ignore_rule_styles": ignore_rule_styles,
                "layout_id": layout_id,
                "line_style": line_style,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore_rule_styles = d.pop("ignore_rule_styles")

        layout_id = d.pop("layout_id")

        line_style = d.pop("line_style")

        bi_aggregation_visualization = cls(
            ignore_rule_styles=ignore_rule_styles,
            layout_id=layout_id,
            line_style=line_style,
        )

        bi_aggregation_visualization.additional_properties = d
        return bi_aggregation_visualization

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
