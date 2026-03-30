from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyTCPOutput")


@_attrs_define
class ProxyTCPOutput:
    """
    Attributes:
        port (int | Unset): The livestatus proxy TCP port. Example: 6560.
        only_from (list[str] | Unset): Restrict access to these IP addresses. Example: ['192.123.32.1', '192.123.32.2'].
        tls (bool | Unset): Encrypt TCP Livestatus connections. Example: True.
    """

    port: int | Unset = UNSET
    only_from: list[str] | Unset = UNSET
    tls: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        only_from: list[str] | Unset = UNSET
        if not isinstance(self.only_from, Unset):
            only_from = self.only_from

        tls = self.tls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if only_from is not UNSET:
            field_dict["only_from"] = only_from
        if tls is not UNSET:
            field_dict["tls"] = tls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        only_from = cast(list[str], d.pop("only_from", UNSET))

        tls = d.pop("tls", UNSET)

        proxy_tcp_output = cls(
            port=port,
            only_from=only_from,
            tls=tls,
        )

        proxy_tcp_output.additional_properties = d
        return proxy_tcp_output

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
