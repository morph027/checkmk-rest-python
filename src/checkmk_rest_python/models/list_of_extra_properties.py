from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_of_extra_properties_state import ListOfExtraPropertiesState
from ..models.list_of_extra_properties_value_item import ListOfExtraPropertiesValueItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListOfExtraProperties")


@_attrs_define
class ListOfExtraProperties:
    """
    Attributes:
        state (ListOfExtraPropertiesState | Unset): To enable or disable this field Example: enabled.
        value (list[ListOfExtraPropertiesValueItem] | Unset):
    """

    state: ListOfExtraPropertiesState | Unset = UNSET
    value: list[ListOfExtraPropertiesValueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: list[str] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.value
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
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: ListOfExtraPropertiesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ListOfExtraPropertiesState(_state)

        _value = d.pop("value", UNSET)
        value: list[ListOfExtraPropertiesValueItem] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = ListOfExtraPropertiesValueItem(value_item_data)

                value.append(value_item)

        list_of_extra_properties = cls(
            state=state,
            value=value,
        )

        list_of_extra_properties.additional_properties = d
        return list_of_extra_properties

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
