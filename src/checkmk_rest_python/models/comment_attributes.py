from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentAttributes")


@_attrs_define
class CommentAttributes:
    """
    Attributes:
        host_name (str): The host name.
        id (int): The comment ID
        author (str): The author of the comment
        comment (str): The comment itself
        persistent (bool): If true, the comment will be persisted
        entry_time (str): The timestamp from when the comment was created.
        is_service (bool): True if the comment is from a service or else it's False.
        site_id (str): The site id of the downtime. Example: production.
        service_description (str | Unset): The service name the comment belongs to.
    """

    host_name: str
    id: int
    author: str
    comment: str
    persistent: bool
    entry_time: str
    is_service: bool
    site_id: str
    service_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host_name = self.host_name

        id = self.id

        author = self.author

        comment = self.comment

        persistent = self.persistent

        entry_time = self.entry_time

        is_service = self.is_service

        site_id = self.site_id

        service_description = self.service_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_name": host_name,
                "id": id,
                "author": author,
                "comment": comment,
                "persistent": persistent,
                "entry_time": entry_time,
                "is_service": is_service,
                "site_id": site_id,
            }
        )
        if service_description is not UNSET:
            field_dict["service_description"] = service_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_name = d.pop("host_name")

        id = d.pop("id")

        author = d.pop("author")

        comment = d.pop("comment")

        persistent = d.pop("persistent")

        entry_time = d.pop("entry_time")

        is_service = d.pop("is_service")

        site_id = d.pop("site_id")

        service_description = d.pop("service_description", UNSET)

        comment_attributes = cls(
            host_name=host_name,
            id=id,
            author=author,
            comment=comment,
            persistent=persistent,
            entry_time=entry_time,
            is_service=is_service,
            site_id=site_id,
            service_description=service_description,
        )

        comment_attributes.additional_properties = d
        return comment_attributes

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
