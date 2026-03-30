from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ilert_api_key_option import IlertAPIKeyOption

T = TypeVar("T", bound="IlertAPIKey")


@_attrs_define
class IlertAPIKey:
    """
    Attributes:
        option (IlertAPIKeyOption):  Example: store.
        key (str):  Example: example_api_key.
    """

    option: IlertAPIKeyOption
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
        option = IlertAPIKeyOption(d.pop("option"))

        key = d.pop("key")

        ilert_api_key = cls(
            option=option,
            key=key,
        )

        ilert_api_key.additional_properties = d
        return ilert_api_key

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
