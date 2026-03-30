from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range_1 import TimeRange1


T = TypeVar("T", bound="TimePeriodException")


@_attrs_define
class TimePeriodException:
    """
    Attributes:
        date (datetime.date): The date of the time period exception.8601 profile Example: 2020-01-01.
        time_ranges (list[TimeRange1] | Unset):  Example: [{'start': '14:00', 'end': '18:00'}].
    """

    date: datetime.date
    time_ranges: list[TimeRange1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        time_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_ranges, Unset):
            time_ranges = []
            for time_ranges_item_data in self.time_ranges:
                time_ranges_item = time_ranges_item_data.to_dict()
                time_ranges.append(time_ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
            }
        )
        if time_ranges is not UNSET:
            field_dict["time_ranges"] = time_ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range_1 import TimeRange1

        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        _time_ranges = d.pop("time_ranges", UNSET)
        time_ranges: list[TimeRange1] | Unset = UNSET
        if _time_ranges is not UNSET:
            time_ranges = []
            for time_ranges_item_data in _time_ranges:
                time_ranges_item = TimeRange1.from_dict(time_ranges_item_data)

                time_ranges.append(time_ranges_item)

        time_period_exception = cls(
            date=date,
            time_ranges=time_ranges,
        )

        time_period_exception.additional_properties = d
        return time_period_exception

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
