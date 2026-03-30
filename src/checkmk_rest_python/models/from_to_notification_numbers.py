from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FromToNotificationNumbers")


@_attrs_define
class FromToNotificationNumbers:
    """
    Attributes:
        beginning_from (int): Let through notifications counting from this number. The first notification always has the
            number 1 Example: 1.
        up_to (int): Let through notifications counting upto this number Example: 999999.
    """

    beginning_from: int
    up_to: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beginning_from = self.beginning_from

        up_to = self.up_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beginning_from": beginning_from,
                "up_to": up_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        beginning_from = d.pop("beginning_from")

        up_to = d.pop("up_to")

        from_to_notification_numbers = cls(
            beginning_from=beginning_from,
            up_to=up_to,
        )

        from_to_notification_numbers.additional_properties = d
        return from_to_notification_numbers

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
