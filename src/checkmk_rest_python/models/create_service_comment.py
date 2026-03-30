from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_service_comment_comment_type import CreateServiceCommentCommentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateServiceComment")


@_attrs_define
class CreateServiceComment:
    """
    Attributes:
        comment (str): The comment which will be stored for the host. Example: Windows.
        comment_type (CreateServiceCommentCommentType): How you would like to leave a comment. Example: service.
        host_name (str): The host name Example: example.com.
        service_description (str): The service name for which the comment is for. No exception is raised when the
            specified service name does not exist Example: Memory.
        persistent (bool | Unset): If set, the comment will persist a restart. Default: False.
    """

    comment: str
    comment_type: CreateServiceCommentCommentType
    host_name: str
    service_description: str
    persistent: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        comment_type = self.comment_type.value

        host_name = self.host_name

        service_description = self.service_description

        persistent = self.persistent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "comment_type": comment_type,
                "host_name": host_name,
                "service_description": service_description,
            }
        )
        if persistent is not UNSET:
            field_dict["persistent"] = persistent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        comment_type = CreateServiceCommentCommentType(d.pop("comment_type"))

        host_name = d.pop("host_name")

        service_description = d.pop("service_description")

        persistent = d.pop("persistent", UNSET)

        create_service_comment = cls(
            comment=comment,
            comment_type=comment_type,
            host_name=host_name,
            service_description=service_description,
            persistent=persistent,
        )

        create_service_comment.additional_properties = d
        return create_service_comment

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
