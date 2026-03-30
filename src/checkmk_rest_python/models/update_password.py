from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePassword")


@_attrs_define
class UpdatePassword:
    """
    Attributes:
        title (str | Unset): The name of your password for easy recognition. Example: Kubernetes login.
        comment (str | Unset): An optional comment to explain the purpose of this password. Example: Kommentar.
        documentation_url (str | Unset): An optional URL pointing to documentation or any other page. You can use either
            global URLs (beginning with http://), absolute local urls (beginning with /) or relative URLs (that are relative
            to check_mk/). Example: localhost.
        password (str | Unset): The password string Example: password.
        owner (str | Unset): Deprecated - use `editable_by` instead. Each password is owned by a group of users which
            are able to edit, delete and use existing passwords. Example: admin.
        editable_by (str | Unset): Each password is owned by a group of users which are able to edit, delete and use
            existing passwords. Example: admin.
        shared (list[str] | Unset): Each password is owned by a group of users which are able to edit, delete and use
            existing passwords. Example: ['all'].
    """

    title: str | Unset = UNSET
    comment: str | Unset = UNSET
    documentation_url: str | Unset = UNSET
    password: str | Unset = UNSET
    owner: str | Unset = UNSET
    editable_by: str | Unset = UNSET
    shared: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        comment = self.comment

        documentation_url = self.documentation_url

        password = self.password

        owner = self.owner

        editable_by = self.editable_by

        shared: list[str] | Unset = UNSET
        if not isinstance(self.shared, Unset):
            shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if comment is not UNSET:
            field_dict["comment"] = comment
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if password is not UNSET:
            field_dict["password"] = password
        if owner is not UNSET:
            field_dict["owner"] = owner
        if editable_by is not UNSET:
            field_dict["editable_by"] = editable_by
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        comment = d.pop("comment", UNSET)

        documentation_url = d.pop("documentation_url", UNSET)

        password = d.pop("password", UNSET)

        owner = d.pop("owner", UNSET)

        editable_by = d.pop("editable_by", UNSET)

        shared = cast(list[str], d.pop("shared", UNSET))

        update_password = cls(
            title=title,
            comment=comment,
            documentation_url=documentation_url,
            password=password,
            owner=owner,
            editable_by=editable_by,
            shared=shared,
        )

        update_password.additional_properties = d
        return update_password

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
