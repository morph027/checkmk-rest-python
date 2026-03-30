from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.metric import Metric
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="GraphCollection")


@_attrs_define
class GraphCollection:
    """
    Attributes:
        time_range (TimeRange):
        step (int): The interval between two samples in seconds. Example: 60.
        metrics (list[Metric]): The actual graph data. Example: [{'color': '#ffffff', 'data_points': [1.0, 2.0, 3.0,
            1.0], 'line_type': 'area', 'title': 'RAM used'}].
    """

    time_range: TimeRange
    step: int
    metrics: list[Metric]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_range = self.time_range.to_dict()

        step = self.step

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_range": time_range,
                "step": step,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric import Metric
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        time_range = TimeRange.from_dict(d.pop("time_range"))

        step = d.pop("step")

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = Metric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        graph_collection = cls(
            time_range=time_range,
            step=step,
            metrics=metrics,
        )

        graph_collection.additional_properties = d
        return graph_collection

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
