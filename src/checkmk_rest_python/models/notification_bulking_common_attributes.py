from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_bulking_common_attributes_notification_bulks_based_on_item import (
    NotificationBulkingCommonAttributesNotificationBulksBasedOnItem,
)
from ..models.notification_bulking_common_attributes_state import (
    NotificationBulkingCommonAttributesState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput


T = TypeVar("T", bound="NotificationBulkingCommonAttributes")


@_attrs_define
class NotificationBulkingCommonAttributes:
    """
    Attributes:
        state (NotificationBulkingCommonAttributesState | Unset): To enable or disable this field Example: enabled.
        time_horizon (int | Unset): Notifications are kept back for bulking at most for this time (seconds) Example: 60.
        max_bulk_size (int | Unset): At most that many notifications are kept back for bulking. A value of 1 essentially
            turns off notification bulking. Example: 1000.
        notification_bulks_based_on (list[NotificationBulkingCommonAttributesNotificationBulksBasedOnItem] | Unset):
        notification_bulks_based_on_custom_macros (list[str] | Unset): If you enter the names of host/service-custom
            macros here then for each different combination of values of those macros a separate bulk will be created.
            Service macros match first, if no service macro is found, the host macros are searched. This can be used in
            combination with the grouping by folder, host etc. Omit any leading underscore. Note: If you are using Nagios as
            a core you need to make sure that the values of the required macros are present in the notification context.
            This is done in check_mk_templates.cfg. If you macro is _FOO then you need to add the variables NOTIFY_HOST_FOO
            and NOTIFY_SERVICE_FOO. You may paste a text from your clipboard which contains several parts separated by ';'
            characters into the last input field. The text will then be split by these separators and the single parts are
            added into dedicated input fields
        subject_for_bulk_notifications (CheckboxWithStrValueOutput | Unset):
    """

    state: NotificationBulkingCommonAttributesState | Unset = UNSET
    time_horizon: int | Unset = UNSET
    max_bulk_size: int | Unset = UNSET
    notification_bulks_based_on: (
        list[NotificationBulkingCommonAttributesNotificationBulksBasedOnItem] | Unset
    ) = UNSET
    notification_bulks_based_on_custom_macros: list[str] | Unset = UNSET
    subject_for_bulk_notifications: CheckboxWithStrValueOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        time_horizon = self.time_horizon

        max_bulk_size = self.max_bulk_size

        notification_bulks_based_on: list[str] | Unset = UNSET
        if not isinstance(self.notification_bulks_based_on, Unset):
            notification_bulks_based_on = []
            for (
                notification_bulks_based_on_item_data
            ) in self.notification_bulks_based_on:
                notification_bulks_based_on_item = (
                    notification_bulks_based_on_item_data.value
                )
                notification_bulks_based_on.append(notification_bulks_based_on_item)

        notification_bulks_based_on_custom_macros: list[str] | Unset = UNSET
        if not isinstance(self.notification_bulks_based_on_custom_macros, Unset):
            notification_bulks_based_on_custom_macros = (
                self.notification_bulks_based_on_custom_macros
            )

        subject_for_bulk_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subject_for_bulk_notifications, Unset):
            subject_for_bulk_notifications = (
                self.subject_for_bulk_notifications.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if time_horizon is not UNSET:
            field_dict["time_horizon"] = time_horizon
        if max_bulk_size is not UNSET:
            field_dict["max_bulk_size"] = max_bulk_size
        if notification_bulks_based_on is not UNSET:
            field_dict["notification_bulks_based_on"] = notification_bulks_based_on
        if notification_bulks_based_on_custom_macros is not UNSET:
            field_dict["notification_bulks_based_on_custom_macros"] = (
                notification_bulks_based_on_custom_macros
            )
        if subject_for_bulk_notifications is not UNSET:
            field_dict["subject_for_bulk_notifications"] = (
                subject_for_bulk_notifications
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: NotificationBulkingCommonAttributesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NotificationBulkingCommonAttributesState(_state)

        time_horizon = d.pop("time_horizon", UNSET)

        max_bulk_size = d.pop("max_bulk_size", UNSET)

        _notification_bulks_based_on = d.pop("notification_bulks_based_on", UNSET)
        notification_bulks_based_on: (
            list[NotificationBulkingCommonAttributesNotificationBulksBasedOnItem]
            | Unset
        ) = UNSET
        if _notification_bulks_based_on is not UNSET:
            notification_bulks_based_on = []
            for notification_bulks_based_on_item_data in _notification_bulks_based_on:
                notification_bulks_based_on_item = (
                    NotificationBulkingCommonAttributesNotificationBulksBasedOnItem(
                        notification_bulks_based_on_item_data
                    )
                )

                notification_bulks_based_on.append(notification_bulks_based_on_item)

        notification_bulks_based_on_custom_macros = cast(
            list[str], d.pop("notification_bulks_based_on_custom_macros", UNSET)
        )

        _subject_for_bulk_notifications = d.pop("subject_for_bulk_notifications", UNSET)
        subject_for_bulk_notifications: CheckboxWithStrValueOutput | Unset
        if isinstance(_subject_for_bulk_notifications, Unset):
            subject_for_bulk_notifications = UNSET
        else:
            subject_for_bulk_notifications = CheckboxWithStrValueOutput.from_dict(
                _subject_for_bulk_notifications
            )

        notification_bulking_common_attributes = cls(
            state=state,
            time_horizon=time_horizon,
            max_bulk_size=max_bulk_size,
            notification_bulks_based_on=notification_bulks_based_on,
            notification_bulks_based_on_custom_macros=notification_bulks_based_on_custom_macros,
            subject_for_bulk_notifications=subject_for_bulk_notifications,
        )

        notification_bulking_common_attributes.additional_properties = d
        return notification_bulking_common_attributes

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
