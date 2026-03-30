from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plugin_name_built_in_or_custom import PluginNameBuiltInOrCustom


T = TypeVar("T", bound="PluginWithoutParams")


@_attrs_define
class PluginWithoutParams:
    """
    Attributes:
        option (Any): Cancel previous notifications Default: 'cancel_previous_notifications'. Example:
            cancel_previous_notifications.
        plugin_params (PluginNameBuiltInOrCustom):
    """

    plugin_params: PluginNameBuiltInOrCustom
    option: Any = "cancel_previous_notifications"
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
        from ..models.plugin_name_built_in_or_custom import PluginNameBuiltInOrCustom

        d = dict(src_dict)
        option = d.pop("option")

        plugin_params = PluginNameBuiltInOrCustom.from_dict(d.pop("plugin_params"))

        plugin_without_params = cls(
            option=option,
            plugin_params=plugin_params,
        )

        plugin_without_params.additional_properties = d
        return plugin_without_params

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
