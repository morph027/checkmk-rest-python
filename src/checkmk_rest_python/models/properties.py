from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Properties")


@_attrs_define
class Properties:
    """
    Attributes:
        description (str | Unset): A description for this rule to inform other users about its intent. Example: This
            rule is here to foo the bar hosts..
        comment (str | Unset): Any comment string. Example: Created yesterday due to foo hosts behaving weird..
        documentation_url (str | Unset): An URL (e.g. an internal Wiki entry) which explains this rule. Example:
            http://example.com/wiki/ConfiguringFooBarHosts.
        disabled (bool | Unset): When set to False, the rule will be evaluated. Default is False. Default: False.
    """

    description: str | Unset = UNSET
    comment: str | Unset = UNSET
    documentation_url: str | Unset = UNSET
    disabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        comment = self.comment

        documentation_url = self.documentation_url

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if comment is not UNSET:
            field_dict["comment"] = comment
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        comment = d.pop("comment", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        disabled = d.pop("disabled", UNSET)

        properties = cls(
            description=description,
            comment=comment,
            documentation_url=documentation_url,
            disabled=disabled,
        )

        properties.additional_properties = d
        return properties

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
