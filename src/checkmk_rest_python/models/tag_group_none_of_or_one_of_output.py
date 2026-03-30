from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tag_group_none_of_or_one_of_output_operator import (
    TagGroupNoneOfOrOneOfOutputOperator,
)
from ..models.tag_group_none_of_or_one_of_output_tag_type import (
    TagGroupNoneOfOrOneOfOutputTagType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TagGroupNoneOfOrOneOfOutput")


@_attrs_define
class TagGroupNoneOfOrOneOfOutput:
    """
    Attributes:
        tag_type (TagGroupNoneOfOrOneOfOutputTagType | Unset): Identifies the type of host tag. Example: tag_group.
        tag_group_id (str | Unset): If the tag_type is 'tag_group', the id of that group is shown here. Example: agent.
        operator (TagGroupNoneOfOrOneOfOutputOperator | Unset):
        tag_ids (list[None | str] | Unset):  Example: ['ip-v4-only', 'ip-v6-only'].
    """

    tag_type: TagGroupNoneOfOrOneOfOutputTagType | Unset = UNSET
    tag_group_id: str | Unset = UNSET
    operator: TagGroupNoneOfOrOneOfOutputOperator | Unset = UNSET
    tag_ids: list[None | str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_type: str | Unset = UNSET
        if not isinstance(self.tag_type, Unset):
            tag_type = self.tag_type.value

        tag_group_id = self.tag_group_id

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        tag_ids: list[None | str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = []
            for tag_ids_item_data in self.tag_ids:
                tag_ids_item: None | str
                tag_ids_item = tag_ids_item_data
                tag_ids.append(tag_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_type is not UNSET:
            field_dict["tag_type"] = tag_type
        if tag_group_id is not UNSET:
            field_dict["tag_group_id"] = tag_group_id
        if operator is not UNSET:
            field_dict["operator"] = operator
        if tag_ids is not UNSET:
            field_dict["tag_ids"] = tag_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tag_type = d.pop("tag_type", UNSET)
        tag_type: TagGroupNoneOfOrOneOfOutputTagType | Unset
        if isinstance(_tag_type, Unset):
            tag_type = UNSET
        else:
            tag_type = TagGroupNoneOfOrOneOfOutputTagType(_tag_type)

        tag_group_id = d.pop("tag_group_id", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: TagGroupNoneOfOrOneOfOutputOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = TagGroupNoneOfOrOneOfOutputOperator(_operator)

        _tag_ids = d.pop("tag_ids", UNSET)
        tag_ids: list[None | str] | Unset = UNSET
        if _tag_ids is not UNSET:
            tag_ids = []
            for tag_ids_item_data in _tag_ids:

                def _parse_tag_ids_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                tag_ids_item = _parse_tag_ids_item(tag_ids_item_data)

                tag_ids.append(tag_ids_item)

        tag_group_none_of_or_one_of_output = cls(
            tag_type=tag_type,
            tag_group_id=tag_group_id,
            operator=operator,
            tag_ids=tag_ids,
        )

        tag_group_none_of_or_one_of_output.additional_properties = d
        return tag_group_none_of_or_one_of_output

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
