from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_period_when_to_bulk import TimePeriodWhenToBulk

if TYPE_CHECKING:
    from ..models.notification_bulking_time_period import NotificationBulkingTimePeriod


T = TypeVar("T", bound="TimePeriod")


@_attrs_define
class TimePeriod:
    """
    Attributes:
        when_to_bulk (TimePeriodWhenToBulk): Bulking can always happen or during a set time period Example: always.
        params (NotificationBulkingTimePeriod):
    """

    when_to_bulk: TimePeriodWhenToBulk
    params: NotificationBulkingTimePeriod
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        when_to_bulk = self.when_to_bulk.value

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "when_to_bulk": when_to_bulk,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_bulking_time_period import (
            NotificationBulkingTimePeriod,
        )

        d = dict(src_dict)
        when_to_bulk = TimePeriodWhenToBulk(d.pop("when_to_bulk"))

        params = NotificationBulkingTimePeriod.from_dict(d.pop("params"))

        time_period = cls(
            when_to_bulk=when_to_bulk,
            params=params,
        )

        time_period.additional_properties = d
        return time_period

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
