from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authentication_value_state import AuthenticationValueState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication


T = TypeVar("T", bound="AuthenticationValue")


@_attrs_define
class AuthenticationValue:
    """
    Attributes:
        value (Authentication):
        state (AuthenticationValueState | Unset): To enable or disable this field Example: enabled.
    """

    value: Authentication
    state: AuthenticationValueState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication import Authentication

        d = dict(src_dict)
        value = Authentication.from_dict(d.pop("value"))

        _state = d.pop("state", UNSET)
        state: AuthenticationValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AuthenticationValueState(_state)

        authentication_value = cls(
            value=value,
            state=state,
        )

        authentication_value.additional_properties = d
        return authentication_value

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
