from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_rule_attributes import NotificationRuleAttributes


T = TypeVar("T", bound="NotificationRuleConfig")


@_attrs_define
class NotificationRuleConfig:
    """
    Attributes:
        rule_config (NotificationRuleAttributes | Unset):
    """

    rule_config: NotificationRuleAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule_config, Unset):
            rule_config = self.rule_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_config is not UNSET:
            field_dict["rule_config"] = rule_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_rule_attributes import NotificationRuleAttributes

        d = dict(src_dict)
        _rule_config = d.pop("rule_config", UNSET)
        rule_config: NotificationRuleAttributes | Unset
        if isinstance(_rule_config, Unset):
            rule_config = UNSET
        else:
            rule_config = NotificationRuleAttributes.from_dict(_rule_config)

        notification_rule_config = cls(
            rule_config=rule_config,
        )

        notification_rule_config.additional_properties = d
        return notification_rule_config

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
