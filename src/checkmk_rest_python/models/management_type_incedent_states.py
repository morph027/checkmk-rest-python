from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.management_type_incedent_states_end_predefined import (
    ManagementTypeIncedentStatesEndPredefined,
)
from ..models.management_type_incedent_states_start_predefined import (
    ManagementTypeIncedentStatesStartPredefined,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagementTypeIncedentStates")


@_attrs_define
class ManagementTypeIncedentStates:
    """
    Attributes:
        start_predefined (ManagementTypeIncedentStatesStartPredefined | Unset):  Example: hold.
        start_integer (int | Unset):  Example: 1.
        end_predefined (ManagementTypeIncedentStatesEndPredefined | Unset):  Example: resolved.
        end_integer (int | Unset):
    """

    start_predefined: ManagementTypeIncedentStatesStartPredefined | Unset = UNSET
    start_integer: int | Unset = UNSET
    end_predefined: ManagementTypeIncedentStatesEndPredefined | Unset = UNSET
    end_integer: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_predefined: str | Unset = UNSET
        if not isinstance(self.start_predefined, Unset):
            start_predefined = self.start_predefined.value

        start_integer = self.start_integer

        end_predefined: str | Unset = UNSET
        if not isinstance(self.end_predefined, Unset):
            end_predefined = self.end_predefined.value

        end_integer = self.end_integer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_predefined is not UNSET:
            field_dict["start_predefined"] = start_predefined
        if start_integer is not UNSET:
            field_dict["start_integer"] = start_integer
        if end_predefined is not UNSET:
            field_dict["end_predefined"] = end_predefined
        if end_integer is not UNSET:
            field_dict["end_integer"] = end_integer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_predefined = d.pop("start_predefined", UNSET)
        start_predefined: ManagementTypeIncedentStatesStartPredefined | Unset
        if isinstance(_start_predefined, Unset):
            start_predefined = UNSET
        else:
            start_predefined = ManagementTypeIncedentStatesStartPredefined(
                _start_predefined
            )

        start_integer = d.pop("start_integer", UNSET)

        _end_predefined = d.pop("end_predefined", UNSET)
        end_predefined: ManagementTypeIncedentStatesEndPredefined | Unset
        if isinstance(_end_predefined, Unset):
            end_predefined = UNSET
        else:
            end_predefined = ManagementTypeIncedentStatesEndPredefined(_end_predefined)

        end_integer = d.pop("end_integer", UNSET)

        management_type_incedent_states = cls(
            start_predefined=start_predefined,
            start_integer=start_integer,
            end_predefined=end_predefined,
            end_integer=end_integer,
        )

        management_type_incedent_states.additional_properties = d
        return management_type_incedent_states

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
