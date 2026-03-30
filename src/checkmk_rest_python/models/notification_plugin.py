from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_bulking_checkbox import NotificationBulkingCheckbox
    from ..models.plugin_base import PluginBase


T = TypeVar("T", bound="NotificationPlugin")


@_attrs_define
class NotificationPlugin:
    """
    Attributes:
        notify_plugin (PluginBase | Unset):
        notification_bulking (NotificationBulkingCheckbox | Unset):
    """

    notify_plugin: PluginBase | Unset = UNSET
    notification_bulking: NotificationBulkingCheckbox | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notify_plugin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notify_plugin, Unset):
            notify_plugin = self.notify_plugin.to_dict()

        notification_bulking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_bulking, Unset):
            notification_bulking = self.notification_bulking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notify_plugin is not UNSET:
            field_dict["notify_plugin"] = notify_plugin
        if notification_bulking is not UNSET:
            field_dict["notification_bulking"] = notification_bulking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_bulking_checkbox import NotificationBulkingCheckbox
        from ..models.plugin_base import PluginBase

        d = dict(src_dict)
        _notify_plugin = d.pop("notify_plugin", UNSET)
        notify_plugin: PluginBase | Unset
        if isinstance(_notify_plugin, Unset):
            notify_plugin = UNSET
        else:
            notify_plugin = PluginBase.from_dict(_notify_plugin)

        _notification_bulking = d.pop("notification_bulking", UNSET)
        notification_bulking: NotificationBulkingCheckbox | Unset
        if isinstance(_notification_bulking, Unset):
            notification_bulking = UNSET
        else:
            notification_bulking = NotificationBulkingCheckbox.from_dict(
                _notification_bulking
            )

        notification_plugin = cls(
            notify_plugin=notify_plugin,
            notification_bulking=notification_bulking,
        )

        notification_plugin.additional_properties = d
        return notification_plugin

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
