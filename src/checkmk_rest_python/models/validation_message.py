from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationMessage")


@_attrs_define
class ValidationMessage:
    """
    Attributes:
        location (list[str] | Unset): Location of the error
        message (str | Unset): Error message
        invalid_value (str | Unset): Invalid value
    """

    location: list[str] | Unset = UNSET
    message: str | Unset = UNSET
    invalid_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location: list[str] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location

        message = self.message

        invalid_value = self.invalid_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if message is not UNSET:
            field_dict["message"] = message
        if invalid_value is not UNSET:
            field_dict["invalid_value"] = invalid_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = cast(list[str], d.pop("location", UNSET))

        message = d.pop("message", UNSET)

        invalid_value = d.pop("invalid_value", UNSET)

        validation_message = cls(
            location=location,
            message=message,
            invalid_value=invalid_value,
        )

        validation_message.additional_properties = d
        return validation_message

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
