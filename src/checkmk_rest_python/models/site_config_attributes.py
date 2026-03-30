from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_settings_attributes import BasicSettingsAttributes
    from ..models.configuration_connection_attributes_output import (
        ConfigurationConnectionAttributesOutput,
    )
    from ..models.status_connection_attributes_output import (
        StatusConnectionAttributesOutput,
    )


T = TypeVar("T", bound="SiteConfigAttributes")


@_attrs_define
class SiteConfigAttributes:
    """
    Attributes:
        basic_settings (BasicSettingsAttributes | Unset):
        status_connection (StatusConnectionAttributesOutput | Unset):
        configuration_connection (ConfigurationConnectionAttributesOutput | Unset):
        logged_in (bool | Unset): If a remote site is currently logged in, this will be True, if not it will be False.
            For the main site, nothing is returned. Example: True.
    """

    basic_settings: BasicSettingsAttributes | Unset = UNSET
    status_connection: StatusConnectionAttributesOutput | Unset = UNSET
    configuration_connection: ConfigurationConnectionAttributesOutput | Unset = UNSET
    logged_in: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basic_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_settings, Unset):
            basic_settings = self.basic_settings.to_dict()

        status_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_connection, Unset):
            status_connection = self.status_connection.to_dict()

        configuration_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_connection, Unset):
            configuration_connection = self.configuration_connection.to_dict()

        logged_in = self.logged_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic_settings is not UNSET:
            field_dict["basic_settings"] = basic_settings
        if status_connection is not UNSET:
            field_dict["status_connection"] = status_connection
        if configuration_connection is not UNSET:
            field_dict["configuration_connection"] = configuration_connection
        if logged_in is not UNSET:
            field_dict["logged_in"] = logged_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_settings_attributes import BasicSettingsAttributes
        from ..models.configuration_connection_attributes_output import (
            ConfigurationConnectionAttributesOutput,
        )
        from ..models.status_connection_attributes_output import (
            StatusConnectionAttributesOutput,
        )

        d = dict(src_dict)
        _basic_settings = d.pop("basic_settings", UNSET)
        basic_settings: BasicSettingsAttributes | Unset
        if isinstance(_basic_settings, Unset):
            basic_settings = UNSET
        else:
            basic_settings = BasicSettingsAttributes.from_dict(_basic_settings)

        _status_connection = d.pop("status_connection", UNSET)
        status_connection: StatusConnectionAttributesOutput | Unset
        if isinstance(_status_connection, Unset):
            status_connection = UNSET
        else:
            status_connection = StatusConnectionAttributesOutput.from_dict(
                _status_connection
            )

        _configuration_connection = d.pop("configuration_connection", UNSET)
        configuration_connection: ConfigurationConnectionAttributesOutput | Unset
        if isinstance(_configuration_connection, Unset):
            configuration_connection = UNSET
        else:
            configuration_connection = (
                ConfigurationConnectionAttributesOutput.from_dict(
                    _configuration_connection
                )
            )

        logged_in = d.pop("logged_in", UNSET)

        site_config_attributes = cls(
            basic_settings=basic_settings,
            status_connection=status_connection,
            configuration_connection=configuration_connection,
            logged_in=logged_in,
        )

        site_config_attributes.additional_properties = d
        return site_config_attributes

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
