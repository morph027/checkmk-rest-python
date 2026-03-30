from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_host_comment_comment_type import CreateHostCommentCommentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateHostComment")


@_attrs_define
class CreateHostComment:
    """
    Attributes:
        comment (str): The comment which will be stored for the host. Example: Windows.
        comment_type (CreateHostCommentCommentType): How you would like to leave a comment. Example: host.
        host_name (str): The host name Example: example.com.
        persistent (bool | Unset): If set, the comment will persist a restart. Default: False.
    """

    comment: str
    comment_type: CreateHostCommentCommentType
    host_name: str
    persistent: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        comment_type = self.comment_type.value

        host_name = self.host_name

        persistent = self.persistent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "comment_type": comment_type,
                "host_name": host_name,
            }
        )
        if persistent is not UNSET:
            field_dict["persistent"] = persistent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        comment_type = CreateHostCommentCommentType(d.pop("comment_type"))

        host_name = d.pop("host_name")

        persistent = d.pop("persistent", UNSET)

        create_host_comment = cls(
            comment=comment,
            comment_type=comment_type,
            host_name=host_name,
            persistent=persistent,
        )

        create_host_comment.additional_properties = d
        return create_host_comment

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
