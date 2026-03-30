from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomMacroOutput")


@_attrs_define
class CustomMacroOutput:
    """
    Attributes:
        macro_name (str | Unset): The name of the macro Example: macro_1.
        match_regex (str | Unset): The text entered here is handled as a regular expression pattern Example: [A-Z]+.
    """

    macro_name: str | Unset = UNSET
    match_regex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        macro_name = self.macro_name

        match_regex = self.match_regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if macro_name is not UNSET:
            field_dict["macro_name"] = macro_name
        if match_regex is not UNSET:
            field_dict["match_regex"] = match_regex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        macro_name = d.pop("macro_name", UNSET)

        match_regex = d.pop("match_regex", UNSET)

        custom_macro_output = cls(
            macro_name=macro_name,
            match_regex=match_regex,
        )

        custom_macro_output.additional_properties = d
        return custom_macro_output

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
