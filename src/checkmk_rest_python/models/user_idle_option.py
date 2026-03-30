from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_idle_option_option import UserIdleOptionOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserIdleOption")


@_attrs_define
class UserIdleOption:
    """
    Attributes:
        option (UserIdleOptionOption): This field indicates if the idle timeout uses the global configuration, is
            disabled or uses an individual duration
        duration (int | Unset): The duration in seconds of the individual idle timeout if individual is selected as idle
            timeout option. Example: 3600.
    """

    option: UserIdleOptionOption
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = UserIdleOptionOption(d.pop("option"))

        duration = d.pop("duration", UNSET)

        user_idle_option = cls(
            option=option,
            duration=duration,
        )

        user_idle_option.additional_properties = d
        return user_idle_option

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
