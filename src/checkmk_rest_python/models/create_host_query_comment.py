from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_host_query_comment_comment_type import (
    CreateHostQueryCommentCommentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="CreateHostQueryComment")


@_attrs_define
class CreateHostQueryComment:
    """
    Attributes:
        comment (str): The comment which will be stored for the host. Example: Windows.
        comment_type (CreateHostQueryCommentCommentType): How you would like to leave a comment. Example: host.
        persistent (bool | Unset): If set, the comment will persist a restart. Default: False.
        query (BinaryExpr | LogicalExpr | NotExpr | Unset):
    """

    comment: str
    comment_type: CreateHostQueryCommentCommentType
    persistent: bool | Unset = False
    query: BinaryExpr | LogicalExpr | NotExpr | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        comment = self.comment

        comment_type = self.comment_type.value

        persistent = self.persistent

        query: dict[str, Any] | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "comment_type": comment_type,
            }
        )
        if persistent is not UNSET:
            field_dict["persistent"] = persistent
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        comment = d.pop("comment")

        comment_type = CreateHostQueryCommentCommentType(d.pop("comment_type"))

        persistent = d.pop("persistent", UNSET)

        def _parse_query(data: object) -> BinaryExpr | LogicalExpr | NotExpr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_0 = LogicalExpr.from_dict(data)

                return componentsschemas_expr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_2 = NotExpr.from_dict(data)

                return componentsschemas_expr_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_expr_type_3 = BinaryExpr.from_dict(data)

            return componentsschemas_expr_type_3

        query = _parse_query(d.pop("query", UNSET))

        create_host_query_comment = cls(
            comment=comment,
            comment_type=comment_type,
            persistent=persistent,
            query=query,
        )

        create_host_query_comment.additional_properties = d
        return create_host_query_comment

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
