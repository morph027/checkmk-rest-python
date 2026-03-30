from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_tag_output import HostTagOutput


T = TypeVar("T", bound="HostTagExtensions")


@_attrs_define
class HostTagExtensions:
    """
    Attributes:
        topic (str | Unset): The topic this host tag group is organized in.
        tags (list[HostTagOutput] | Unset): The list of tags in this group.
        help_ (str | Unset): A help description for the tag group
    """

    topic: str | Unset = UNSET
    tags: list[HostTagOutput] | Unset = UNSET
    help_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        help_ = self.help_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topic is not UNSET:
            field_dict["topic"] = topic
        if tags is not UNSET:
            field_dict["tags"] = tags
        if help_ is not UNSET:
            field_dict["help"] = help_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_tag_output import HostTagOutput

        d = dict(src_dict)
        topic = d.pop("topic", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[HostTagOutput] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = HostTagOutput.from_dict(tags_item_data)

                tags.append(tags_item)

        help_ = d.pop("help", UNSET)

        host_tag_extensions = cls(
            topic=topic,
            tags=tags,
            help_=help_,
        )

        host_tag_extensions.additional_properties = d
        return host_tag_extensions

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
