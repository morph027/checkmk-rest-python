from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_box_ip_address_value import CheckBoxIPAddressValue
    from ..models.checkbox import Checkbox
    from ..models.checkbox_sys_log_facility_to_use_value import (
        CheckboxSysLogFacilityToUseValue,
    )


T = TypeVar("T", bound="MkEventDPluginCreate")


@_attrs_define
class MkEventDPluginCreate:
    """
    Attributes:
        plugin_name (Any): The MkEventd plug-in. Default: 'mkeventd'. Example: mkeventd.
        syslog_facility_to_use (Checkbox | CheckboxSysLogFacilityToUseValue | Unset):
        ip_address_of_remote_event_console (Checkbox | CheckBoxIPAddressValue | Unset):
    """

    plugin_name: Any = "mkeventd"
    syslog_facility_to_use: Checkbox | CheckboxSysLogFacilityToUseValue | Unset = UNSET
    ip_address_of_remote_event_console: Checkbox | CheckBoxIPAddressValue | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        plugin_name = self.plugin_name

        syslog_facility_to_use: dict[str, Any] | Unset
        if isinstance(self.syslog_facility_to_use, Unset):
            syslog_facility_to_use = UNSET
        elif isinstance(self.syslog_facility_to_use, Checkbox):
            syslog_facility_to_use = self.syslog_facility_to_use.to_dict()
        else:
            syslog_facility_to_use = self.syslog_facility_to_use.to_dict()

        ip_address_of_remote_event_console: dict[str, Any] | Unset
        if isinstance(self.ip_address_of_remote_event_console, Unset):
            ip_address_of_remote_event_console = UNSET
        elif isinstance(self.ip_address_of_remote_event_console, Checkbox):
            ip_address_of_remote_event_console = (
                self.ip_address_of_remote_event_console.to_dict()
            )
        else:
            ip_address_of_remote_event_console = (
                self.ip_address_of_remote_event_console.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
            }
        )
        if syslog_facility_to_use is not UNSET:
            field_dict["syslog_facility_to_use"] = syslog_facility_to_use
        if ip_address_of_remote_event_console is not UNSET:
            field_dict["ip_address_of_remote_event_console"] = (
                ip_address_of_remote_event_console
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_box_ip_address_value import CheckBoxIPAddressValue
        from ..models.checkbox import Checkbox
        from ..models.checkbox_sys_log_facility_to_use_value import (
            CheckboxSysLogFacilityToUseValue,
        )

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_syslog_facility_to_use(
            data: object,
        ) -> Checkbox | CheckboxSysLogFacilityToUseValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sys_log_facility_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_sys_log_facility_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_sys_log_facility_one_of_type_1 = (
                CheckboxSysLogFacilityToUseValue.from_dict(data)
            )

            return componentsschemas_sys_log_facility_one_of_type_1

        syslog_facility_to_use = _parse_syslog_facility_to_use(
            d.pop("syslog_facility_to_use", UNSET)
        )

        def _parse_ip_address_of_remote_event_console(
            data: object,
        ) -> Checkbox | CheckBoxIPAddressValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ip_address_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_ip_address_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ip_address_one_of_type_1 = (
                CheckBoxIPAddressValue.from_dict(data)
            )

            return componentsschemas_ip_address_one_of_type_1

        ip_address_of_remote_event_console = _parse_ip_address_of_remote_event_console(
            d.pop("ip_address_of_remote_event_console", UNSET)
        )

        mk_event_d_plugin_create = cls(
            plugin_name=plugin_name,
            syslog_facility_to_use=syslog_facility_to_use,
            ip_address_of_remote_event_console=ip_address_of_remote_event_console,
        )

        mk_event_d_plugin_create.additional_properties = d
        return mk_event_d_plugin_create

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
