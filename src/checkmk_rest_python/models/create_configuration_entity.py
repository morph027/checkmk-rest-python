from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_configuration_entity_entity_type import (
    CreateConfigurationEntityEntityType,
)

if TYPE_CHECKING:
    from ..models.create_configuration_entity_data import CreateConfigurationEntityData


T = TypeVar("T", bound="CreateConfigurationEntity")


@_attrs_define
class CreateConfigurationEntity:
    """
    Attributes:
        entity_type (CreateConfigurationEntityEntityType): Type of configuration entity Example: notification_parameter.
        entity_type_specifier (str): Specifier for the entity type Example: mail.
        data (CreateConfigurationEntityData): The data of the configuration entity
    """

    entity_type: CreateConfigurationEntityEntityType
    entity_type_specifier: str
    data: CreateConfigurationEntityData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type.value

        entity_type_specifier = self.entity_type_specifier

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_type": entity_type,
                "entity_type_specifier": entity_type_specifier,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_configuration_entity_data import (
            CreateConfigurationEntityData,
        )

        d = dict(src_dict)
        entity_type = CreateConfigurationEntityEntityType(d.pop("entity_type"))

        entity_type_specifier = d.pop("entity_type_specifier")

        data = CreateConfigurationEntityData.from_dict(d.pop("data"))

        create_configuration_entity = cls(
            entity_type=entity_type,
            entity_type_specifier=entity_type_specifier,
            data=data,
        )

        create_configuration_entity.additional_properties = d
        return create_configuration_entity

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
