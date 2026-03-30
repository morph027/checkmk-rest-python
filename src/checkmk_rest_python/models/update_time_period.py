from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_period_exception import TimePeriodException
    from ..models.time_range_active import TimeRangeActive


T = TypeVar("T", bound="UpdateTimePeriod")


@_attrs_define
class UpdateTimePeriod:
    """
    Attributes:
        alias (str | Unset): An alias for the time period Example: new_alias.
        active_time_ranges (list[TimeRangeActive] | Unset): The list of active time ranges which replaces the existing
            list of time ranges Example: [{'day': 'monday', 'time_ranges': [{'start': '12:00:00', 'end': '14:00:00'}]}].
        exceptions (list[TimePeriodException] | Unset): A list of additional time ranges to be added. Example: [{'date':
            '2020-01-01', 'time_ranges': [{'start': '14:00:00', 'end': '18:00:00'}]}].
        exclude (list[str] | Unset): A list of time period names whose periods are excluded. Example: ['time_name'].
    """

    alias: str | Unset = UNSET
    active_time_ranges: list[TimeRangeActive] | Unset = UNSET
    exceptions: list[TimePeriodException] | Unset = UNSET
    exclude: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        active_time_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_time_ranges, Unset):
            active_time_ranges = []
            for active_time_ranges_item_data in self.active_time_ranges:
                active_time_ranges_item = active_time_ranges_item_data.to_dict()
                active_time_ranges.append(active_time_ranges_item)

        exceptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exceptions, Unset):
            exceptions = []
            for exceptions_item_data in self.exceptions:
                exceptions_item = exceptions_item_data.to_dict()
                exceptions.append(exceptions_item)

        exclude: list[str] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if active_time_ranges is not UNSET:
            field_dict["active_time_ranges"] = active_time_ranges
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_period_exception import TimePeriodException
        from ..models.time_range_active import TimeRangeActive

        d = dict(src_dict)
        alias = d.pop("alias", UNSET)

        _active_time_ranges = d.pop("active_time_ranges", UNSET)
        active_time_ranges: list[TimeRangeActive] | Unset = UNSET
        if _active_time_ranges is not UNSET:
            active_time_ranges = []
            for active_time_ranges_item_data in _active_time_ranges:
                active_time_ranges_item = TimeRangeActive.from_dict(
                    active_time_ranges_item_data
                )

                active_time_ranges.append(active_time_ranges_item)

        _exceptions = d.pop("exceptions", UNSET)
        exceptions: list[TimePeriodException] | Unset = UNSET
        if _exceptions is not UNSET:
            exceptions = []
            for exceptions_item_data in _exceptions:
                exceptions_item = TimePeriodException.from_dict(exceptions_item_data)

                exceptions.append(exceptions_item)

        exclude = cast(list[str], d.pop("exclude", UNSET))

        update_time_period = cls(
            alias=alias,
            active_time_ranges=active_time_ranges,
            exceptions=exceptions,
            exclude=exclude,
        )

        update_time_period.additional_properties = d
        return update_time_period

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
