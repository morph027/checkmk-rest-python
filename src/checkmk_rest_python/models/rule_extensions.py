from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditions import Conditions
    from ..models.properties import Properties


T = TypeVar("T", bound="RuleExtensions")


@_attrs_define
class RuleExtensions:
    r"""
    Attributes:
        folder (str): The path name of the folder.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: ~router.
        ruleset (str | Unset): The name of the ruleset.
        folder_index (int | Unset): The position of this rule in the chain in this folder.
        properties (Properties | Unset):
        value_raw (str | Unset): The raw parameter value for this rule. Example: {"ignore_fs_types": ["tmpfs"]}.
        conditions (Conditions | Unset):
    """

    folder: str
    ruleset: str | Unset = UNSET
    folder_index: int | Unset = UNSET
    properties: Properties | Unset = UNSET
    value_raw: str | Unset = UNSET
    conditions: Conditions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder = self.folder

        ruleset = self.ruleset

        folder_index = self.folder_index

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        value_raw = self.value_raw

        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folder": folder,
            }
        )
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset
        if folder_index is not UNSET:
            field_dict["folder_index"] = folder_index
        if properties is not UNSET:
            field_dict["properties"] = properties
        if value_raw is not UNSET:
            field_dict["value_raw"] = value_raw
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditions import Conditions
        from ..models.properties import Properties

        d = dict(src_dict)
        folder = d.pop("folder")

        ruleset = d.pop("ruleset", UNSET)

        folder_index = d.pop("folder_index", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = Properties.from_dict(_properties)

        value_raw = d.pop("value_raw", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: Conditions | Unset
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = Conditions.from_dict(_conditions)

        rule_extensions = cls(
            folder=folder,
            ruleset=ruleset,
            folder_index=folder_index,
            properties=properties,
            value_raw=value_raw,
            conditions=conditions,
        )

        rule_extensions.additional_properties = d
        return rule_extensions

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
