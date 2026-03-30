from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_rule_properties_state_messages import BIRulePropertiesStateMessages


T = TypeVar("T", bound="BIRuleProperties")


@_attrs_define
class BIRuleProperties:
    """
    Attributes:
        title (str): Title of the rule. Example: Rule title.
        comment (str): Rule comment. Example: Rule comment.
        docu_url (str): URL to more documentation. Example: Rule documentation.
        icon (str): Icon name for the rule. Example: icon1.png.
        state_messages (BIRulePropertiesStateMessages): State messages.
    """

    title: str
    comment: str
    docu_url: str
    icon: str
    state_messages: BIRulePropertiesStateMessages
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        comment = self.comment

        docu_url = self.docu_url

        icon = self.icon

        state_messages = self.state_messages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "comment": comment,
                "docu_url": docu_url,
                "icon": icon,
                "state_messages": state_messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_rule_properties_state_messages import (
            BIRulePropertiesStateMessages,
        )

        d = dict(src_dict)
        title = d.pop("title")

        comment = d.pop("comment")

        docu_url = d.pop("docu_url")

        icon = d.pop("icon")

        state_messages = BIRulePropertiesStateMessages.from_dict(
            d.pop("state_messages")
        )

        bi_rule_properties = cls(
            title=title,
            comment=comment,
            docu_url=docu_url,
            icon=icon,
            state_messages=state_messages,
        )

        bi_rule_properties.additional_properties = d
        return bi_rule_properties

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
