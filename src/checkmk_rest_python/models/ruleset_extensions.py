from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RulesetExtensions")


@_attrs_define
class RulesetExtensions:
    r"""
    Attributes:
        folder (str): The path name of the folder.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: ~router.
        name (str | Unset): The name of the ruleset Example: host_groups.
        number_of_rules (int | Unset): The number of rules of this ruleset. Example: 5.
    """

    folder: str
    name: str | Unset = UNSET
    number_of_rules: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder

        name = self.name

        number_of_rules = self.number_of_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder": folder,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if number_of_rules is not UNSET:
            field_dict["number_of_rules"] = number_of_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder = d.pop("folder")

        name = d.pop("name", UNSET)

        number_of_rules = d.pop("number_of_rules", UNSET)

        ruleset_extensions = cls(
            folder=folder,
            name=name,
            number_of_rules=number_of_rules,
        )

        ruleset_extensions.additional_properties = d
        return ruleset_extensions

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
