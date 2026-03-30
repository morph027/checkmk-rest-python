from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.custom_plugin_with_params import CustomPluginWithParams
    from ..models.notification_bulking_value import NotificationBulkingValue
    from ..models.plugin_with_params import PluginWithParams
    from ..models.plugin_without_params import PluginWithoutParams


T = TypeVar("T", bound="RuleNotificationMethod")


@_attrs_define
class RuleNotificationMethod:
    """
    Attributes:
        notify_plugin (CustomPluginWithParams | PluginWithoutParams | PluginWithParams):
        notification_bulking (Checkbox | NotificationBulkingValue | Unset):
    """

    notify_plugin: CustomPluginWithParams | PluginWithoutParams | PluginWithParams
    notification_bulking: Checkbox | NotificationBulkingValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.plugin_with_params import PluginWithParams
        from ..models.plugin_without_params import PluginWithoutParams

        notify_plugin: dict[str, Any]
        if isinstance(self.notify_plugin, PluginWithoutParams):
            notify_plugin = self.notify_plugin.to_dict()
        elif isinstance(self.notify_plugin, PluginWithParams):
            notify_plugin = self.notify_plugin.to_dict()
        else:
            notify_plugin = self.notify_plugin.to_dict()

        notification_bulking: dict[str, Any] | Unset
        if isinstance(self.notification_bulking, Unset):
            notification_bulking = UNSET
        elif isinstance(self.notification_bulking, Checkbox):
            notification_bulking = self.notification_bulking.to_dict()
        else:
            notification_bulking = self.notification_bulking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notify_plugin": notify_plugin,
            }
        )
        if notification_bulking is not UNSET:
            field_dict["notification_bulking"] = notification_bulking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.custom_plugin_with_params import CustomPluginWithParams
        from ..models.notification_bulking_value import NotificationBulkingValue
        from ..models.plugin_with_params import PluginWithParams
        from ..models.plugin_without_params import PluginWithoutParams

        d = dict(src_dict)

        def _parse_notify_plugin(
            data: object,
        ) -> CustomPluginWithParams | PluginWithoutParams | PluginWithParams:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_options_selector_type_0 = (
                    PluginWithoutParams.from_dict(data)
                )

                return componentsschemas_plugin_options_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_options_selector_type_1 = (
                    PluginWithParams.from_dict(data)
                )

                return componentsschemas_plugin_options_selector_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_options_selector_type_2 = (
                CustomPluginWithParams.from_dict(data)
            )

            return componentsschemas_plugin_options_selector_type_2

        notify_plugin = _parse_notify_plugin(d.pop("notify_plugin"))

        def _parse_notification_bulking(
            data: object,
        ) -> Checkbox | NotificationBulkingValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_notification_bulk_type_0 = Checkbox.from_dict(data)

                return componentsschemas_notification_bulk_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_notification_bulk_type_1 = (
                NotificationBulkingValue.from_dict(data)
            )

            return componentsschemas_notification_bulk_type_1

        notification_bulking = _parse_notification_bulking(
            d.pop("notification_bulking", UNSET)
        )

        rule_notification_method = cls(
            notify_plugin=notify_plugin,
            notification_bulking=notification_bulking,
        )

        rule_notification_method.additional_properties = d
        return rule_notification_method

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
