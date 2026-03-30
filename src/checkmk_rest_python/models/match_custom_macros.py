from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_custom_macros_state import MatchCustomMacrosState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_macro import CustomMacro


T = TypeVar("T", bound="MatchCustomMacros")


@_attrs_define
class MatchCustomMacros:
    """
    Attributes:
        state (MatchCustomMacrosState | Unset): To enable or disable this field Example: enabled.
        value (list[CustomMacro] | Unset):
    """

    state: MatchCustomMacrosState | Unset = UNSET
    value: list[CustomMacro] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

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
        from ..models.custom_macro import CustomMacro

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: MatchCustomMacrosState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MatchCustomMacrosState(_state)

        _value = d.pop("value", UNSET)
        value: list[CustomMacro] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = CustomMacro.from_dict(value_item_data)

                value.append(value_item)

        match_custom_macros = cls(
            state=state,
            value=value,
        )

        match_custom_macros.additional_properties = d
        return match_custom_macros

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
