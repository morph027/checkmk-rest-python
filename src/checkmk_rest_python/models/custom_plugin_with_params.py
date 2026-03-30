from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_plugin import CustomPlugin


T = TypeVar("T", bound="CustomPluginWithParams")


@_attrs_define
class CustomPluginWithParams:
    """
    Attributes:
        option (Any): Create notifications with custom parameters Default: 'create_notification_with_custom_parameters'.
            Example: create_notification_with_custom_parameters.
        plugin_params (CustomPlugin):
    """

    plugin_params: CustomPlugin
    option: Any = "create_notification_with_custom_parameters"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option

        plugin_params = self.plugin_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "plugin_params": plugin_params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_plugin import CustomPlugin

        d = dict(src_dict)
        option = d.pop("option")

        plugin_params = CustomPlugin.from_dict(d.pop("plugin_params"))

        custom_plugin_with_params = cls(
            option=option,
            plugin_params=plugin_params,
        )

        custom_plugin_with_params.additional_properties = d
        return custom_plugin_with_params

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
