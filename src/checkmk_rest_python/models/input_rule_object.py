from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_conditions import InputConditions
    from ..models.properties import Properties


T = TypeVar("T", bound="InputRuleObject")


@_attrs_define
class InputRuleObject:
    r"""
    Attributes:
        value_raw (str): The raw parameter value for this rule. To create the correct structure, for now use the 'export
            for API' menu item in the Rule Editor of the GUI. The value is expected to be a valid Python type. Example:
            {'cmk/os_family': 'linux'}.
        ruleset (str): Name of rule set. Example: host_label_rules.
        folder (str): The path name of the folder.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: ~hosts~linux.
        properties (Properties | Unset):
        conditions (InputConditions | Unset):
    """

    value_raw: str
    ruleset: str
    folder: str
    properties: Properties | Unset = UNSET
    conditions: InputConditions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_raw = self.value_raw

        ruleset = self.ruleset

        folder = self.folder

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value_raw": value_raw,
                "ruleset": ruleset,
                "folder": folder,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_conditions import InputConditions
        from ..models.properties import Properties

        d = dict(src_dict)
        value_raw = d.pop("value_raw")

        ruleset = d.pop("ruleset")

        folder = d.pop("folder")

        _properties = d.pop("properties", UNSET)
        properties: Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = Properties.from_dict(_properties)

        _conditions = d.pop("conditions", UNSET)
        conditions: InputConditions | Unset
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = InputConditions.from_dict(_conditions)

        input_rule_object = cls(
            value_raw=value_raw,
            ruleset=ruleset,
            folder=folder,
            properties=properties,
            conditions=conditions,
        )

        input_rule_object.additional_properties = d
        return input_rule_object

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
