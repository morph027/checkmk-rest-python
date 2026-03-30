from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_general_properties_update_request_rule_activation import (
    LDAPGeneralPropertiesUpdateRequestRuleActivation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPGeneralPropertiesUpdateRequest")


@_attrs_define
class LDAPGeneralPropertiesUpdateRequest:
    """
    Attributes:
        id (str): An LDAP connection ID string.
        description (str | Unset): Add a title or describe this rule Default: ''.
        comment (str | Unset): An optional comment to explain the purpose of this object. The comment is only visible in
            this dialog and can help other users to understand the intentions of the configured attributes. Default: ''.
        documentation_url (str | Unset): An optional URL linking documentation or any other page. An icon links to the
            page and opens in a new tab when clicked. You can use either global URLs (starting with http://), absolute local
            URLs (starting with /) or relative URLs (relative to check_mk/). Default: ''.
        rule_activation (LDAPGeneralPropertiesUpdateRequestRuleActivation | Unset): Selecting 'deactivated' will disable
            the rule, but it will remain in the configuration. Default:
            LDAPGeneralPropertiesUpdateRequestRuleActivation.ACTIVATED.
    """

    id: str
    description: str | Unset = ""
    comment: str | Unset = ""
    documentation_url: str | Unset = ""
    rule_activation: LDAPGeneralPropertiesUpdateRequestRuleActivation | Unset = (
        LDAPGeneralPropertiesUpdateRequestRuleActivation.ACTIVATED
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        comment = self.comment

        documentation_url = self.documentation_url

        rule_activation: str | Unset = UNSET
        if not isinstance(self.rule_activation, Unset):
            rule_activation = self.rule_activation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if comment is not UNSET:
            field_dict["comment"] = comment
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if rule_activation is not UNSET:
            field_dict["rule_activation"] = rule_activation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description", UNSET)

        comment = d.pop("comment", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        _rule_activation = d.pop("rule_activation", UNSET)
        rule_activation: LDAPGeneralPropertiesUpdateRequestRuleActivation | Unset
        if isinstance(_rule_activation, Unset):
            rule_activation = UNSET
        else:
            rule_activation = LDAPGeneralPropertiesUpdateRequestRuleActivation(
                _rule_activation
            )

        ldap_general_properties_update_request = cls(
            id=id,
            description=description,
            comment=comment,
            documentation_url=documentation_url,
            rule_activation=rule_activation,
        )

        ldap_general_properties_update_request.additional_properties = d
        return ldap_general_properties_update_request

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
