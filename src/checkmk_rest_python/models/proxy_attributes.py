from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_attributes_use_livestatus_daemon import (
    ProxyAttributesUseLivestatusDaemon,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_params import ProxyParams
    from ..models.proxy_tcp import ProxyTcp


T = TypeVar("T", bound="ProxyAttributes")


@_attrs_define
class ProxyAttributes:
    """
    Attributes:
        use_livestatus_daemon (ProxyAttributesUseLivestatusDaemon): Use livestatus daemon with direct connection or with
            livestatus proxy. Example: True.
        global_settings (bool): When use_livestatus_daemon is set to 'with_proxy', you can set this to True to use
            global setting or False to use custom parameters. Example: True.
        tcp (ProxyTcp | Unset):
        params (ProxyParams | Unset):
    """

    use_livestatus_daemon: ProxyAttributesUseLivestatusDaemon
    global_settings: bool
    tcp: ProxyTcp | Unset = UNSET
    params: ProxyParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_livestatus_daemon = self.use_livestatus_daemon.value

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
                "global_settings": global_settings,
            }
        )
        if tcp is not UNSET:
            field_dict["tcp"] = tcp
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_params import ProxyParams
        from ..models.proxy_tcp import ProxyTcp

        d = dict(src_dict)
        use_livestatus_daemon = ProxyAttributesUseLivestatusDaemon(
            d.pop("use_livestatus_daemon")
        )

        global_settings = d.pop("global_settings")

        _tcp = d.pop("tcp", UNSET)
        tcp: ProxyTcp | Unset
        if isinstance(_tcp, Unset):
            tcp = UNSET
        else:
            tcp = ProxyTcp.from_dict(_tcp)

        _params = d.pop("params", UNSET)
        params: ProxyParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ProxyParams.from_dict(_params)

        proxy_attributes = cls(
            use_livestatus_daemon=use_livestatus_daemon,
            global_settings=global_settings,
            tcp=tcp,
            params=params,
        )

        proxy_attributes.additional_properties = d
        return proxy_attributes

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
