from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_output import CheckboxOutput


T = TypeVar("T", bound="RulePropertiesAttributes")


@_attrs_define
class RulePropertiesAttributes:
    """
    Attributes:
        description (str | Unset): A description or title of this rule. Example: Notify all contacts of a host/service
            via HTML email.
        comment (str | Unset): An optional comment that may be used to explain the purpose of this object. Example: An
            example comment.
        documentation_url (str | Unset): An optional URL pointing to documentation or any other page. This will be
            displayed as an icon and open a new page when clicked. Example: http://link/to/documentation.
        do_not_apply_this_rule (CheckboxOutput | Unset):
        allow_users_to_deactivate (CheckboxOutput | Unset):
    """

    description: str | Unset = UNSET
    comment: str | Unset = UNSET
    documentation_url: str | Unset = UNSET
    do_not_apply_this_rule: CheckboxOutput | Unset = UNSET
    allow_users_to_deactivate: CheckboxOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        comment = self.comment

        documentation_url = self.documentation_url

        do_not_apply_this_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.do_not_apply_this_rule, Unset):
            do_not_apply_this_rule = self.do_not_apply_this_rule.to_dict()

        allow_users_to_deactivate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allow_users_to_deactivate, Unset):
            allow_users_to_deactivate = self.allow_users_to_deactivate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if comment is not UNSET:
            field_dict["comment"] = comment
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if do_not_apply_this_rule is not UNSET:
            field_dict["do_not_apply_this_rule"] = do_not_apply_this_rule
        if allow_users_to_deactivate is not UNSET:
            field_dict["allow_users_to_deactivate"] = allow_users_to_deactivate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_output import CheckboxOutput

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        comment = d.pop("comment", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        _do_not_apply_this_rule = d.pop("do_not_apply_this_rule", UNSET)
        do_not_apply_this_rule: CheckboxOutput | Unset
        if isinstance(_do_not_apply_this_rule, Unset):
            do_not_apply_this_rule = UNSET
        else:
            do_not_apply_this_rule = CheckboxOutput.from_dict(_do_not_apply_this_rule)

        _allow_users_to_deactivate = d.pop("allow_users_to_deactivate", UNSET)
        allow_users_to_deactivate: CheckboxOutput | Unset
        if isinstance(_allow_users_to_deactivate, Unset):
            allow_users_to_deactivate = UNSET
        else:
            allow_users_to_deactivate = CheckboxOutput.from_dict(
                _allow_users_to_deactivate
            )

        rule_properties_attributes = cls(
            description=description,
            comment=comment,
            documentation_url=documentation_url,
            do_not_apply_this_rule=do_not_apply_this_rule,
            allow_users_to_deactivate=allow_users_to_deactivate,
        )

        rule_properties_attributes.additional_properties = d
        return rule_properties_attributes

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
