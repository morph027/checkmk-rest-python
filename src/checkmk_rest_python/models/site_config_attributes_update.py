from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.basic_settings_attributes_update import BasicSettingsAttributesUpdate
    from ..models.configuration_connection_with_replication_attributes import (
        ConfigurationConnectionWithReplicationAttributes,
    )
    from ..models.configuration_connection_without_replication_attributes import (
        ConfigurationConnectionWithoutReplicationAttributes,
    )
    from ..models.status_connection_attributes import StatusConnectionAttributes


T = TypeVar("T", bound="SiteConfigAttributesUpdate")


@_attrs_define
class SiteConfigAttributesUpdate:
    """
    Attributes:
        status_connection (StatusConnectionAttributes):
        configuration_connection (ConfigurationConnectionWithoutReplicationAttributes |
            ConfigurationConnectionWithReplicationAttributes):
        basic_settings (BasicSettingsAttributesUpdate):
    """

    status_connection: StatusConnectionAttributes
    configuration_connection: (
        ConfigurationConnectionWithoutReplicationAttributes
        | ConfigurationConnectionWithReplicationAttributes
    )
    basic_settings: BasicSettingsAttributesUpdate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.configuration_connection_with_replication_attributes import (
            ConfigurationConnectionWithReplicationAttributes,
        )

        status_connection = self.status_connection.to_dict()

        configuration_connection: dict[str, Any]
        if isinstance(
            self.configuration_connection,
            ConfigurationConnectionWithReplicationAttributes,
        ):
            configuration_connection = self.configuration_connection.to_dict()
        else:
            configuration_connection = self.configuration_connection.to_dict()

        basic_settings = self.basic_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_connection": status_connection,
                "configuration_connection": configuration_connection,
                "basic_settings": basic_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_settings_attributes_update import (
            BasicSettingsAttributesUpdate,
        )
        from ..models.configuration_connection_with_replication_attributes import (
            ConfigurationConnectionWithReplicationAttributes,
        )
        from ..models.configuration_connection_without_replication_attributes import (
            ConfigurationConnectionWithoutReplicationAttributes,
        )
        from ..models.status_connection_attributes import StatusConnectionAttributes

        d = dict(src_dict)
        status_connection = StatusConnectionAttributes.from_dict(
            d.pop("status_connection")
        )

        def _parse_configuration_connection(
            data: object,
        ) -> (
            ConfigurationConnectionWithoutReplicationAttributes
            | ConfigurationConnectionWithReplicationAttributes
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_configuration_connection_attributes_type_0 = (
                    ConfigurationConnectionWithReplicationAttributes.from_dict(data)
                )

                return componentsschemas_configuration_connection_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_configuration_connection_attributes_type_1 = (
                ConfigurationConnectionWithoutReplicationAttributes.from_dict(data)
            )

            return componentsschemas_configuration_connection_attributes_type_1

        configuration_connection = _parse_configuration_connection(
            d.pop("configuration_connection")
        )

        basic_settings = BasicSettingsAttributesUpdate.from_dict(
            d.pop("basic_settings")
        )

        site_config_attributes_update = cls(
            status_connection=status_connection,
            configuration_connection=configuration_connection,
            basic_settings=basic_settings,
        )

        site_config_attributes_update.additional_properties = d
        return site_config_attributes_update

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
