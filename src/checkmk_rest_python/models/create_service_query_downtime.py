from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_service_query_downtime_downtime_type import (
    CreateServiceQueryDowntimeDowntimeType,
)
from ..models.create_service_query_downtime_recur import CreateServiceQueryDowntimeRecur
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="CreateServiceQueryDowntime")


@_attrs_define
class CreateServiceQueryDowntime:
    """
    Attributes:
        start_time (str): The start datetime of the new downtime. The format has to conform to the ISO 8601 profile
            Example: 2017-07-21T17:32:28Z.
        end_time (str): The end datetime of the new downtime. The format has to conform to the ISO 8601 profile Example:
            2017-07-21T17:32:28Z.
        downtime_type (CreateServiceQueryDowntimeDowntimeType): The type of downtime to create.

            Valid options are:

             * `service` - Schedule downtimes for services whose names are listed in service_descriptions and belongs to the
            host identified by name or IP address in host_name.
             * `servicegroup` - Schedule downtimes for all services in a given service group
             * `service_by_query` - Schedule downtimes for services matching the query
             Example: service.
        query (BinaryExpr | LogicalExpr | NotExpr):
        recur (CreateServiceQueryDowntimeRecur | Unset): The recurring mode of the new downtime. Available modes are:
            * fixed     * hour     * day     * week     * second_week     * fourth_week     * weekday_start     *
            weekday_end     * day_of_month  This only works when using the Enterprise Editions. Defaults to 'fixed'.
            Default: CreateServiceQueryDowntimeRecur.FIXED. Example: hour.
        duration (int | Unset): Duration in minutes. When set, the downtime does not begin automatically at a nominated
            time, but when a real problem status appears for the service. Consequencely, the start_time/end_time is only the
            time window in which the scheduled downtime can begin. Default: 0. Example: 60.
        comment (str | Unset):  Example: Security updates.
    """

    start_time: str
    end_time: str
    downtime_type: CreateServiceQueryDowntimeDowntimeType
    query: BinaryExpr | LogicalExpr | NotExpr
    recur: CreateServiceQueryDowntimeRecur | Unset = (
        CreateServiceQueryDowntimeRecur.FIXED
    )
    duration: int | Unset = 0
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        start_time = self.start_time

        end_time = self.end_time

        downtime_type = self.downtime_type.value

        query: dict[str, Any]
        if isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        recur: str | Unset = UNSET
        if not isinstance(self.recur, Unset):
            recur = self.recur.value

        duration = self.duration

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "end_time": end_time,
                "downtime_type": downtime_type,
                "query": query,
            }
        )
        if recur is not UNSET:
            field_dict["recur"] = recur
        if duration is not UNSET:
            field_dict["duration"] = duration
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        downtime_type = CreateServiceQueryDowntimeDowntimeType(d.pop("downtime_type"))

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

        _recur = d.pop("recur", UNSET)
        recur: CreateServiceQueryDowntimeRecur | Unset
        if isinstance(_recur, Unset):
            recur = UNSET
        else:
            recur = CreateServiceQueryDowntimeRecur(_recur)

        duration = d.pop("duration", UNSET)

        comment = d.pop("comment", UNSET)

        create_service_query_downtime = cls(
            start_time=start_time,
            end_time=end_time,
            downtime_type=downtime_type,
            query=query,
            recur=recur,
            duration=duration,
            comment=comment,
        )

        create_service_query_downtime.additional_properties = d
        return create_service_query_downtime

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
