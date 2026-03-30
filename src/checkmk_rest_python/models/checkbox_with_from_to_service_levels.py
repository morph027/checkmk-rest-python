from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_from_to_service_levels_state import (
    CheckboxWithFromToServiceLevelsState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.from_to_service_levels import FromToServiceLevels


T = TypeVar("T", bound="CheckboxWithFromToServiceLevels")


@_attrs_define
class CheckboxWithFromToServiceLevels:
    """
    Attributes:
        value (FromToServiceLevels):
        state (CheckboxWithFromToServiceLevelsState | Unset): To enable or disable this field Example: enabled.
    """

    value: FromToServiceLevels
    state: CheckboxWithFromToServiceLevelsState | Unset = UNSET
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
        from ..models.from_to_service_levels import FromToServiceLevels

        d = dict(src_dict)
        value = FromToServiceLevels.from_dict(d.pop("value"))

        _state = d.pop("state", UNSET)
        state: CheckboxWithFromToServiceLevelsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithFromToServiceLevelsState(_state)

        checkbox_with_from_to_service_levels = cls(
            value=value,
            state=state,
        )

        checkbox_with_from_to_service_levels.additional_properties = d
        return checkbox_with_from_to_service_levels

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
