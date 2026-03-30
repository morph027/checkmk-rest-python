from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PasswordExtension")


@_attrs_define
class PasswordExtension:
    """
    Attributes:
        comment (str | Unset): An optional comment to explain the purpose of this password. Example: Kommentar.
        documentation_url (str | Unset): A URL pointing to documentation or any other page. Example: localhost.
        owned_by (str | Unset): Deprecated - use `editable_by` instead. The owner of the password who is able to edit,
            delete and use existing passwords. Example: admin.
        editable_by (str | Unset): The owner of the password who is able to edit, delete and use existing passwords.
            Example: admin.
        shared (list[str] | Unset): Each password is owned by a group of users which are able to edit, delete and use
            existing passwords. Example: ['all'].
    """

    comment: str | Unset = UNSET
    documentation_url: str | Unset = UNSET
    owned_by: str | Unset = UNSET
    editable_by: str | Unset = UNSET
    shared: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        documentation_url = self.documentation_url

        owned_by = self.owned_by

        editable_by = self.editable_by

        shared: list[str] | Unset = UNSET
        if not isinstance(self.shared, Unset):
            shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if owned_by is not UNSET:
            field_dict["owned_by"] = owned_by
        if editable_by is not UNSET:
            field_dict["editable_by"] = editable_by
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        owned_by = d.pop("owned_by", UNSET)

        editable_by = d.pop("editable_by", UNSET)

        shared = cast(list[str], d.pop("shared", UNSET))

        password_extension = cls(
            comment=comment,
            documentation_url=documentation_url,
            owned_by=owned_by,
            editable_by=editable_by,
            shared=shared,
        )

        password_extension.additional_properties = d
        return password_extension

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
