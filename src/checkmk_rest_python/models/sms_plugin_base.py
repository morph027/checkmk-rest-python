from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SMSPluginBase")


@_attrs_define
class SMSPluginBase:
    """
    Attributes:
        plugin_name (Any): The SMS plug-in. Default: 'sms'. Example: sms.
        params (list[str] | Unset): The given parameters are available in scripts as NOTIFY_PARAMETER_1,
            NOTIFY_PARAMETER_2, etc. You may paste a text from your clipboard which contains several parts separated by ';'
            characters into the last input field. The text will then be split by these separators and the single parts are
            added into dedicated input fields. Example: ['NOTIFY_PARAMETER_1', 'NOTIFY_PARAMETER_1'].
    """

    plugin_name: Any = "sms"
    params: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_name = self.plugin_name

        params: list[str] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        params = cast(list[str], d.pop("params", UNSET))

        sms_plugin_base = cls(
            plugin_name=plugin_name,
            params=params,
        )

        sms_plugin_base.additional_properties = d
        return sms_plugin_base

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
