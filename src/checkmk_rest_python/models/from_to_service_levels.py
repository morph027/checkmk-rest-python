from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FromToServiceLevels")


@_attrs_define
class FromToServiceLevels:
    """
    Attributes:
        from_level (int): A service level represented as an integer Example: 10.
        to_level (int): A service level represented as an integer Example: 10.
    """

    from_level: int
    to_level: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_level = self.from_level

        to_level = self.to_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_level": from_level,
                "to_level": to_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_level = d.pop("from_level")

        to_level = d.pop("to_level")

        from_to_service_levels = cls(
            from_level=from_level,
            to_level=to_level,
        )

        from_to_service_levels.additional_properties = d
        return from_to_service_levels

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
