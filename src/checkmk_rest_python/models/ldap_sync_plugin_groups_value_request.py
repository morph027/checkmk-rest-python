from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_checkbox_custom_time_range_enabled_request import (
        LDAPCheckboxCustomTimeRangeEnabledRequest,
    )
    from ..models.ldap_checkbox_disabled_request import LDAPCheckboxDisabledRequest


T = TypeVar("T", bound="LDAPSyncPluginGroupsValueRequest")


@_attrs_define
class LDAPSyncPluginGroupsValueRequest:
    """
    Attributes:
        custom_time_range (LDAPCheckboxCustomTimeRangeEnabledRequest | LDAPCheckboxDisabledRequest):
        temporarily_disable_all_notifications (bool | Unset): When this option is active you will not get any alerts or
            other notifications via email, SMS or similar. This overrides all other notification settings and rules, so make
            sure that you know what you're doing. Moreover you can specify a time range where no notifications are
            generated. Default: False.
    """

    custom_time_range: (
        LDAPCheckboxCustomTimeRangeEnabledRequest | LDAPCheckboxDisabledRequest
    )
    temporarily_disable_all_notifications: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ldap_checkbox_custom_time_range_enabled_request import (
            LDAPCheckboxCustomTimeRangeEnabledRequest,
        )

        custom_time_range: dict[str, Any]
        if isinstance(
            self.custom_time_range, LDAPCheckboxCustomTimeRangeEnabledRequest
        ):
            custom_time_range = self.custom_time_range.to_dict()
        else:
            custom_time_range = self.custom_time_range.to_dict()

        temporarily_disable_all_notifications = (
            self.temporarily_disable_all_notifications
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_time_range": custom_time_range,
            }
        )
        if temporarily_disable_all_notifications is not UNSET:
            field_dict["temporarily_disable_all_notifications"] = (
                temporarily_disable_all_notifications
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_checkbox_custom_time_range_enabled_request import (
            LDAPCheckboxCustomTimeRangeEnabledRequest,
        )
        from ..models.ldap_checkbox_disabled_request import LDAPCheckboxDisabledRequest

        d = dict(src_dict)

        def _parse_custom_time_range(
            data: object,
        ) -> LDAPCheckboxCustomTimeRangeEnabledRequest | LDAPCheckboxDisabledRequest:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ldap_custom_time_range_selector_type_0 = (
                    LDAPCheckboxCustomTimeRangeEnabledRequest.from_dict(data)
                )

                return componentsschemas_ldap_custom_time_range_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ldap_custom_time_range_selector_type_1 = (
                LDAPCheckboxDisabledRequest.from_dict(data)
            )

            return componentsschemas_ldap_custom_time_range_selector_type_1

        custom_time_range = _parse_custom_time_range(d.pop("custom_time_range"))

        temporarily_disable_all_notifications = d.pop(
            "temporarily_disable_all_notifications", UNSET
        )

        ldap_sync_plugin_groups_value_request = cls(
            custom_time_range=custom_time_range,
            temporarily_disable_all_notifications=temporarily_disable_all_notifications,
        )

        ldap_sync_plugin_groups_value_request.additional_properties = d
        return ldap_sync_plugin_groups_value_request

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
