from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_tag import HostTag


T = TypeVar("T", bound="InputHostTagGroup")


@_attrs_define
class InputHostTagGroup:
    """
    Attributes:
        id (str): An id for the host tag group Example: group_id.
        title (str): A title for the host tag Example: Kubernetes.
        tags (list[HostTag]): A list of host tags belonging to the host tag group Example: [{'id': 'pod', 'title':
            'Pod'}].
        topic (str | Unset): Different tags can be grouped in a topic Example: Data Sources.
        help_ (str | Unset): A help description for the tag group Default: ''. Example: Kubernetes Pods.
    """

    id: str
    title: str
    tags: list[HostTag]
    topic: str | Unset = UNSET
    help_: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        topic = self.topic

        help_ = self.help_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "tags": tags,
            }
        )
        if topic is not UNSET:
            field_dict["topic"] = topic
        if help_ is not UNSET:
            field_dict["help"] = help_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_tag import HostTag

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = HostTag.from_dict(tags_item_data)

            tags.append(tags_item)

        topic = d.pop("topic", UNSET)

        help_ = d.pop("help", UNSET)

        input_host_tag_group = cls(
            id=id,
            title=title,
            tags=tags,
            topic=topic,
            help_=help_,
        )

        input_host_tag_group.additional_properties = d
        return input_host_tag_group

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
