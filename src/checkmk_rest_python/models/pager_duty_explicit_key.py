from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pager_duty_explicit_key_option import PagerDutyExplicitKeyOption

T = TypeVar("T", bound="PagerDutyExplicitKey")


@_attrs_define
class PagerDutyExplicitKey:
    """
    Attributes:
        option (PagerDutyExplicitKeyOption):  Example: store.
        key (str):  Example: some_key_example.
    """

    option: PagerDutyExplicitKeyOption
    key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = PagerDutyExplicitKeyOption(d.pop("option"))

        key = d.pop("key")

        pager_duty_explicit_key = cls(
            option=option,
            key=key,
        )

        pager_duty_explicit_key.additional_properties = d
        return pager_duty_explicit_key

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
