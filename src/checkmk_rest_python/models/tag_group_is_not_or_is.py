from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_group_is_not_or_is_operator import TagGroupIsNotOrIsOperator
from ..models.tag_group_is_not_or_is_tag_type import TagGroupIsNotOrIsTagType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TagGroupIsNotOrIs")


@_attrs_define
class TagGroupIsNotOrIs:
    """
    Attributes:
        tag_type (TagGroupIsNotOrIsTagType):  Example: aux_tag.
        tag_group_id (str): Tag group ids are available via the host tag group endpoint. Example: agent.
        operator (TagGroupIsNotOrIsOperator | Unset):
        tag_id (None | str | Unset): Tag groups tag ids are available via the host tag group endpoint. Example: checkmk-
            agent.
    """

    tag_type: TagGroupIsNotOrIsTagType
    tag_group_id: str
    operator: TagGroupIsNotOrIsOperator | Unset = UNSET
    tag_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_type = self.tag_type.value

        tag_group_id = self.tag_group_id

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        tag_id: None | str | Unset
        if isinstance(self.tag_id, Unset):
            tag_id = UNSET
        else:
            tag_id = self.tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_type": tag_type,
                "tag_group_id": tag_group_id,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_type = TagGroupIsNotOrIsTagType(d.pop("tag_type"))

        tag_group_id = d.pop("tag_group_id")

        _operator = d.pop("operator", UNSET)
        operator: TagGroupIsNotOrIsOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = TagGroupIsNotOrIsOperator(_operator)

        def _parse_tag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tag_id = _parse_tag_id(d.pop("tag_id", UNSET))

        tag_group_is_not_or_is = cls(
            tag_type=tag_type,
            tag_group_id=tag_group_id,
            operator=operator,
            tag_id=tag_id,
        )

        tag_group_is_not_or_is.additional_properties = d
        return tag_group_is_not_or_is

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
