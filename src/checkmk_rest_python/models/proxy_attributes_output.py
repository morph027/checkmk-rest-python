from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_params_output import ProxyParamsOutput
    from ..models.proxy_tcp_output import ProxyTCPOutput


T = TypeVar("T", bound="ProxyAttributesOutput")


@_attrs_define
class ProxyAttributesOutput:
    """
    Attributes:
        use_livestatus_daemon (str): Use livestatus daemon with direct connection or with livestatus proxy. Example:
            True.
        global_settings (bool | Unset): When Livestatus proxy daemon is set, you can enable this to use global setting
            and disable it to use custom parameters. Example: True.
        tcp (ProxyTCPOutput | Unset):
        params (ProxyParamsOutput | Unset):
    """

    use_livestatus_daemon: str
    global_settings: bool | Unset = UNSET
    tcp: ProxyTCPOutput | Unset = UNSET
    params: ProxyParamsOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_livestatus_daemon = self.use_livestatus_daemon

        global_settings = self.global_settings

        tcp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp, Unset):
            tcp = self.tcp.to_dict()

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use_livestatus_daemon": use_livestatus_daemon,
            }
        )
        if global_settings is not UNSET:
            field_dict["global_settings"] = global_settings
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_params_output import ProxyParamsOutput
        from ..models.proxy_tcp_output import ProxyTCPOutput

        d = dict(src_dict)
        use_livestatus_daemon = d.pop("use_livestatus_daemon")

        global_settings = d.pop("global_settings", UNSET)

        _tcp = d.pop("tcp", UNSET)
        tcp: ProxyTCPOutput | Unset
        if isinstance(_tcp, Unset):
            tcp = UNSET
        else:
            tcp = ProxyTCPOutput.from_dict(_tcp)

        _params = d.pop("params", UNSET)
        params: ProxyParamsOutput | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ProxyParamsOutput.from_dict(_params)

        proxy_attributes_output = cls(
            use_livestatus_daemon=use_livestatus_daemon,
            global_settings=global_settings,
            tcp=tcp,
            params=params,
        )

        proxy_attributes_output.additional_properties = d
        return proxy_attributes_output

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
