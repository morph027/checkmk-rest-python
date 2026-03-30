from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_group_is_not_or_is_output_operator import (
    TagGroupIsNotOrIsOutputOperator,
)
from ..models.tag_group_is_not_or_is_output_tag_type import (
    TagGroupIsNotOrIsOutputTagType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TagGroupIsNotOrIsOutput")


@_attrs_define
class TagGroupIsNotOrIsOutput:
    """
    Attributes:
        tag_type (TagGroupIsNotOrIsOutputTagType | Unset): Identifies the type of host tag. Example: tag_group.
        tag_group_id (str | Unset): If the tag_type is 'tag_group', the id of that group is shown here. Example: agent.
        operator (TagGroupIsNotOrIsOutputOperator | Unset):
        tag_id (None | str | Unset): Tag groups tag ids are available via the host tag group endpoint. Example: checkmk-
            agent.
    """

    tag_type: TagGroupIsNotOrIsOutputTagType | Unset = UNSET
    tag_group_id: str | Unset = UNSET
    operator: TagGroupIsNotOrIsOutputOperator | Unset = UNSET
    tag_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_type: str | Unset = UNSET
        if not isinstance(self.tag_type, Unset):
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
        field_dict.update({})
        if tag_type is not UNSET:
            field_dict["tag_type"] = tag_type
        if tag_group_id is not UNSET:
            field_dict["tag_group_id"] = tag_group_id
        if operator is not UNSET:
            field_dict["operator"] = operator
        if tag_id is not UNSET:
            field_dict["tag_id"] = tag_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tag_type = d.pop("tag_type", UNSET)
        tag_type: TagGroupIsNotOrIsOutputTagType | Unset
        if isinstance(_tag_type, Unset):
            tag_type = UNSET
        else:
            tag_type = TagGroupIsNotOrIsOutputTagType(_tag_type)

        tag_group_id = d.pop("tag_group_id", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: TagGroupIsNotOrIsOutputOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = TagGroupIsNotOrIsOutputOperator(_operator)

        def _parse_tag_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tag_id = _parse_tag_id(d.pop("tag_id", UNSET))

        tag_group_is_not_or_is_output = cls(
            tag_type=tag_type,
            tag_group_id=tag_group_id,
            operator=operator,
            tag_id=tag_id,
        )

        tag_group_is_not_or_is_output.additional_properties = d
        return tag_group_is_not_or_is_output

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
