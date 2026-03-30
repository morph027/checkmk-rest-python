from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_metric_reduce import GetMetricReduce
from ..models.get_metric_type import GetMetricType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="GetMetric")


@_attrs_define
class GetMetric:
    """
    Attributes:
        time_range (TimeRange):
        host_name (str): The host name to use. Example: my.cool.host.
        service_description (str): The service, whose data to request. Example: Check_MK.
        type_ (GetMetricType): Specify whether you want to receive a single metric (via metric_id), or a predefined
            graph containing multiple metrics (via graph_id). Example: single_metric.
        metric_id (str): The ID of the single metric.After activating the "Show internal IDs" in the "display options"
            of the Service view, you can see the ID of a single metric in the legend of the graph. Example: cmk_time_agent.
        reduce (GetMetricReduce | Unset): Specify how to reduce a segment of data points to a single data point of the
            output metric. This can be useful to find spikes in your data that would be smoothed out by computing the
            average. Default: GetMetricReduce.AVERAGE. Example: max.
        site (str | Unset): The name of the site. Even though this is optional, specifying a site will greatly improve
            performance in large distributed systems. Example: mysite.
    """

    time_range: TimeRange
    host_name: str
    service_description: str
    type_: GetMetricType
    metric_id: str
    reduce: GetMetricReduce | Unset = GetMetricReduce.AVERAGE
    site: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_range = self.time_range.to_dict()

        host_name = self.host_name

        service_description = self.service_description

        type_ = self.type_.value

        metric_id = self.metric_id

        reduce: str | Unset = UNSET
        if not isinstance(self.reduce, Unset):
            reduce = self.reduce.value

        site = self.site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_range": time_range,
                "host_name": host_name,
                "service_description": service_description,
                "type": type_,
                "metric_id": metric_id,
            }
        )
        if reduce is not UNSET:
            field_dict["reduce"] = reduce
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        time_range = TimeRange.from_dict(d.pop("time_range"))

        host_name = d.pop("host_name")

        service_description = d.pop("service_description")

        type_ = GetMetricType(d.pop("type"))

        metric_id = d.pop("metric_id")

        _reduce = d.pop("reduce", UNSET)
        reduce: GetMetricReduce | Unset
        if isinstance(_reduce, Unset):
            reduce = UNSET
        else:
            reduce = GetMetricReduce(_reduce)

        site = d.pop("site", UNSET)

        get_metric = cls(
            time_range=time_range,
            host_name=host_name,
            service_description=service_description,
            type_=type_,
            metric_id=metric_id,
            reduce=reduce,
            site=site,
        )

        get_metric.additional_properties = d
        return get_metric

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
