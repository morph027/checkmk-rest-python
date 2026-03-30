from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Metric")


@_attrs_define
class Metric:
    """
    Attributes:
        data_points (list[float]): The samples of the metric. Example: [3752390000.0, 3746380000.0, 3770930000.0,
            3773230000.0, 3796020000.0, 3787010000.0, 3777880000.0, 3781040000.0, 3798920000.0, 3805910000.0].
        line_type (str): The line type to use. Example: area.
        title (str): The title of the graph. Example: RAM used.
        color (str | Unset): The color of the metric as displayed in Checkmk. Color is in HTML notation. Example:
            #80ff40.
    """

    data_points: list[float]
    line_type: str
    title: str
    color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_points = self.data_points

        line_type = self.line_type

        title = self.title

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_points": data_points,
                "line_type": line_type,
                "title": title,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_points = cast(list[float], d.pop("data_points"))

        line_type = d.pop("line_type")

        title = d.pop("title")

        color = d.pop("color", UNSET)

        metric = cls(
            data_points=data_points,
            line_type=line_type,
            title=title,
            color=color,
        )

        metric.additional_properties = d
        return metric

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
