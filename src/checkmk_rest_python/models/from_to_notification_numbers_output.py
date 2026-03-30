from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FromToNotificationNumbersOutput")


@_attrs_define
class FromToNotificationNumbersOutput:
    """
    Attributes:
        beginning_from (int | Unset): Let through notifications counting from this number. The first notification always
            has the number 1 Example: 1.
        up_to (int | Unset): Let through notifications counting upto this number Example: 999999.
    """

    beginning_from: int | Unset = UNSET
    up_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beginning_from = self.beginning_from

        up_to = self.up_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beginning_from is not UNSET:
            field_dict["beginning_from"] = beginning_from
        if up_to is not UNSET:
            field_dict["up_to"] = up_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        beginning_from = d.pop("beginning_from", UNSET)

        up_to = d.pop("up_to", UNSET)

        from_to_notification_numbers_output = cls(
            beginning_from=beginning_from,
            up_to=up_to,
        )

        from_to_notification_numbers_output.additional_properties = d
        return from_to_notification_numbers_output

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
