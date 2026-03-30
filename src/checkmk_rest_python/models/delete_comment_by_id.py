from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_comment_by_id_delete_type import DeleteCommentByIdDeleteType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCommentById")


@_attrs_define
class DeleteCommentById:
    """
    Attributes:
        delete_type (DeleteCommentByIdDeleteType): How you would like to delete comments. Example: delete_by_query.
        site_id (str): The ID of an existing site Example: production.
        comment_id (int | Unset): An integer representing a comment ID. Example: 21.
    """

    delete_type: DeleteCommentByIdDeleteType
    site_id: str
    comment_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        site_id = self.site_id

        comment_id = self.comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete_type": delete_type,
                "site_id": site_id,
            }
        )
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteCommentByIdDeleteType(d.pop("delete_type"))

        site_id = d.pop("site_id")

        comment_id = d.pop("comment_id", UNSET)

        delete_comment_by_id = cls(
            delete_type=delete_type,
            site_id=site_id,
            comment_id=comment_id,
        )

        delete_comment_by_id.additional_properties = d
        return delete_comment_by_id

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
