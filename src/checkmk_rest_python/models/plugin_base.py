from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plugin_base_option import PluginBaseOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_base_plugin_params import PluginBasePluginParams


T = TypeVar("T", bound="PluginBase")


@_attrs_define
class PluginBase:
    """
    Attributes:
        option (PluginBaseOption | Unset):  Example: cancel_previous_notifications.
        plugin_params (PluginBasePluginParams | Unset): The plug-in name and configuration parameters defined.
    """

    option: PluginBaseOption | Unset = UNSET
    plugin_params: PluginBasePluginParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option: str | Unset = UNSET
        if not isinstance(self.option, Unset):
            option = self.option.value

        plugin_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plugin_params, Unset):
            plugin_params = self.plugin_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option is not UNSET:
            field_dict["option"] = option
        if plugin_params is not UNSET:
            field_dict["plugin_params"] = plugin_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_base_plugin_params import PluginBasePluginParams

        d = dict(src_dict)
        _option = d.pop("option", UNSET)
        option: PluginBaseOption | Unset
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = PluginBaseOption(_option)

        _plugin_params = d.pop("plugin_params", UNSET)
        plugin_params: PluginBasePluginParams | Unset
        if isinstance(_plugin_params, Unset):
            plugin_params = UNSET
        else:
            plugin_params = PluginBasePluginParams.from_dict(_plugin_params)

        plugin_base = cls(
            option=option,
            plugin_params=plugin_params,
        )

        plugin_base.additional_properties = d
        return plugin_base

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
