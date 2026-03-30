from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.http_proxy_global_option import HttpProxyGlobalOption

T = TypeVar("T", bound="HttpProxyGlobal")


@_attrs_define
class HttpProxyGlobal:
    """
    Attributes:
        option (HttpProxyGlobalOption):
        global_proxy_id (str): A global http proxy Example: proxy_id_1.
    """

    option: HttpProxyGlobalOption
    global_proxy_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        global_proxy_id = self.global_proxy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "global_proxy_id": global_proxy_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = HttpProxyGlobalOption(d.pop("option"))

        global_proxy_id = d.pop("global_proxy_id")

        http_proxy_global = cls(
            option=option,
            global_proxy_id=global_proxy_id,
        )

        http_proxy_global.additional_properties = d
        return http_proxy_global

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
