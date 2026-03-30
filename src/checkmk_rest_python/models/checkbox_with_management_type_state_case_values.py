from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_with_management_type_state_case_values_state import (
    CheckboxWithManagementTypeStateCaseValuesState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_type_case_states import ManagementTypeCaseStates


T = TypeVar("T", bound="CheckboxWithManagementTypeStateCaseValues")


@_attrs_define
class CheckboxWithManagementTypeStateCaseValues:
    """
    Attributes:
        state (CheckboxWithManagementTypeStateCaseValuesState | Unset): To enable or disable this field Example:
            enabled.
        value (ManagementTypeCaseStates | Unset):
    """

    state: CheckboxWithManagementTypeStateCaseValuesState | Unset = UNSET
    value: ManagementTypeCaseStates | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
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
        from ..models.management_type_case_states import ManagementTypeCaseStates

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckboxWithManagementTypeStateCaseValuesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxWithManagementTypeStateCaseValuesState(_state)

        _value = d.pop("value", UNSET)
        value: ManagementTypeCaseStates | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ManagementTypeCaseStates.from_dict(_value)

        checkbox_with_management_type_state_case_values = cls(
            state=state,
            value=value,
        )

        checkbox_with_management_type_state_case_values.additional_properties = d
        return checkbox_with_management_type_state_case_values

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
