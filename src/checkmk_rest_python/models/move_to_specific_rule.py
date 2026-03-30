from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveToSpecificRule")


@_attrs_define
class MoveToSpecificRule:
    """
    Attributes:
        position (str | Unset): The type of position to move to.
                    Note that you cannot move rules before rules managed by a Quick setup. In the case of
                    `top_of_folder` your rule will instead be after all managed rules. If you specify a managed
                    rule in `after_specific_rule` or `before_specific_rule` you will receive an error. Example:
            top_of_folder.
        rule_id (str | Unset): The UUID of the rule to move after/before. Example: f8b74720-a454-4242-99c4-62994ef0f2bf.
    """

    position: str | Unset = UNSET
    rule_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        rule_id = self.rule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        move_to_specific_rule = cls(
            position=position,
            rule_id=rule_id,
        )

        move_to_specific_rule.additional_properties = d
        return move_to_specific_rule

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
