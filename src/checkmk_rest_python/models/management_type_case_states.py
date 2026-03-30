from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_type_case_states_start_predefined import (
    ManagementTypeCaseStatesStartPredefined,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagementTypeCaseStates")


@_attrs_define
class ManagementTypeCaseStates:
    """
    Attributes:
        start_predefined (ManagementTypeCaseStatesStartPredefined | Unset):  Example: new.
        start_integer (int | Unset):  Example: 1.
    """

    start_predefined: ManagementTypeCaseStatesStartPredefined | Unset = UNSET
    start_integer: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_predefined: str | Unset = UNSET
        if not isinstance(self.start_predefined, Unset):
            start_predefined = self.start_predefined.value

        start_integer = self.start_integer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_predefined is not UNSET:
            field_dict["start_predefined"] = start_predefined
        if start_integer is not UNSET:
            field_dict["start_integer"] = start_integer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_predefined = d.pop("start_predefined", UNSET)
        start_predefined: ManagementTypeCaseStatesStartPredefined | Unset
        if isinstance(_start_predefined, Unset):
            start_predefined = UNSET
        else:
            start_predefined = ManagementTypeCaseStatesStartPredefined(
                _start_predefined
            )

        start_integer = d.pop("start_integer", UNSET)

        management_type_case_states = cls(
            start_predefined=start_predefined,
            start_integer=start_integer,
        )

        management_type_case_states.additional_properties = d
        return management_type_case_states

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
