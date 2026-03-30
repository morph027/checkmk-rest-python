from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_bulking_always_notification_bulks_based_on_item import (
    NotificationBulkingAlwaysNotificationBulksBasedOnItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_str_value import CheckboxWithStrValue


T = TypeVar("T", bound="NotificationBulkingAlways")


@_attrs_define
class NotificationBulkingAlways:
    """
    Attributes:
        subject_for_bulk_notifications (Checkbox | CheckboxWithStrValue):
        max_bulk_size (int): At most that many notifications are kept back for bulking. A value of 1 essentially turns
            off notification bulking. Example: 1000.
        notification_bulks_based_on (list[NotificationBulkingAlwaysNotificationBulksBasedOnItem]):
        time_horizon (int): Notifications are kept back for bulking at most for this time (seconds) Example: 60.
        notification_bulks_based_on_custom_macros (list[str] | Unset):
    """

    subject_for_bulk_notifications: Checkbox | CheckboxWithStrValue
    max_bulk_size: int
    notification_bulks_based_on: list[
        NotificationBulkingAlwaysNotificationBulksBasedOnItem
    ]
    time_horizon: int
    notification_bulks_based_on_custom_macros: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        subject_for_bulk_notifications: dict[str, Any]
        if isinstance(self.subject_for_bulk_notifications, Checkbox):
            subject_for_bulk_notifications = (
                self.subject_for_bulk_notifications.to_dict()
            )
        else:
            subject_for_bulk_notifications = (
                self.subject_for_bulk_notifications.to_dict()
            )

        max_bulk_size = self.max_bulk_size

        notification_bulks_based_on = []
        for notification_bulks_based_on_item_data in self.notification_bulks_based_on:
            notification_bulks_based_on_item = (
                notification_bulks_based_on_item_data.value
            )
            notification_bulks_based_on.append(notification_bulks_based_on_item)

        time_horizon = self.time_horizon

        notification_bulks_based_on_custom_macros: list[str] | Unset = UNSET
        if not isinstance(self.notification_bulks_based_on_custom_macros, Unset):
            notification_bulks_based_on_custom_macros = (
                self.notification_bulks_based_on_custom_macros
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_for_bulk_notifications": subject_for_bulk_notifications,
                "max_bulk_size": max_bulk_size,
                "notification_bulks_based_on": notification_bulks_based_on,
                "time_horizon": time_horizon,
            }
        )
        if notification_bulks_based_on_custom_macros is not UNSET:
            field_dict["notification_bulks_based_on_custom_macros"] = (
                notification_bulks_based_on_custom_macros
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_str_value import CheckboxWithStrValue

        d = dict(src_dict)

        def _parse_subject_for_bulk_notifications(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        subject_for_bulk_notifications = _parse_subject_for_bulk_notifications(
            d.pop("subject_for_bulk_notifications")
        )

        max_bulk_size = d.pop("max_bulk_size")

        notification_bulks_based_on = []
        _notification_bulks_based_on = d.pop("notification_bulks_based_on")
        for notification_bulks_based_on_item_data in _notification_bulks_based_on:
            notification_bulks_based_on_item = (
                NotificationBulkingAlwaysNotificationBulksBasedOnItem(
                    notification_bulks_based_on_item_data
                )
            )

            notification_bulks_based_on.append(notification_bulks_based_on_item)

        time_horizon = d.pop("time_horizon")

        notification_bulks_based_on_custom_macros = cast(
            list[str], d.pop("notification_bulks_based_on_custom_macros", UNSET)
        )

        notification_bulking_always = cls(
            subject_for_bulk_notifications=subject_for_bulk_notifications,
            max_bulk_size=max_bulk_size,
            notification_bulks_based_on=notification_bulks_based_on,
            time_horizon=time_horizon,
            notification_bulks_based_on_custom_macros=notification_bulks_based_on_custom_macros,
        )

        notification_bulking_always.additional_properties = d
        return notification_bulking_always

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
