from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.http_proxy_value_state import HttpProxyValueState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_proxy import HttpProxy
    from ..models.http_proxy_global import HttpProxyGlobal
    from ..models.http_proxy_url import HttpProxyUrl


T = TypeVar("T", bound="HttpProxyValue")


@_attrs_define
class HttpProxyValue:
    """
    Attributes:
        state (HttpProxyValueState | Unset): To enable or disable this field Example: enabled.
        value (HttpProxy | HttpProxyGlobal | HttpProxyUrl | Unset):
    """

    state: HttpProxyValueState | Unset = UNSET
    value: HttpProxy | HttpProxyGlobal | HttpProxyUrl | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_proxy import HttpProxy
        from ..models.http_proxy_url import HttpProxyUrl

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: dict[str, Any] | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, HttpProxy):
            value = self.value.to_dict()
        elif isinstance(self.value, HttpProxyUrl):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_proxy import HttpProxy
        from ..models.http_proxy_global import HttpProxyGlobal
        from ..models.http_proxy_url import HttpProxyUrl

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: HttpProxyValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = HttpProxyValueState(_state)

        def _parse_value(
            data: object,
        ) -> HttpProxy | HttpProxyGlobal | HttpProxyUrl | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_http_proxy_options_type_0 = HttpProxy.from_dict(data)

                return componentsschemas_http_proxy_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_http_proxy_options_type_2 = HttpProxyUrl.from_dict(
                    data
                )

                return componentsschemas_http_proxy_options_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_http_proxy_options_type_3 = HttpProxyGlobal.from_dict(
                data
            )

            return componentsschemas_http_proxy_options_type_3

        value = _parse_value(d.pop("value", UNSET))

        http_proxy_value = cls(
            state=state,
            value=value,
        )

        http_proxy_value.additional_properties = d
        return http_proxy_value

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
