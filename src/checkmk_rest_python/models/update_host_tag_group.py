from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_tag import HostTag


T = TypeVar("T", bound="UpdateHostTagGroup")


@_attrs_define
class UpdateHostTagGroup:
    """
    Attributes:
        title (str | Unset): A title for the host tag Example: Kubernetes.
        topic (str | Unset): Different tags can be grouped in a topic Example: Data Sources.
        help_ (str | Unset): A help description for the tag group Example: Kubernetes Pods.
        tags (list[HostTag] | Unset): A list of host tags belonging to the host tag group Example: [{'id': 'pod',
            'title': 'Pod'}].
        repair (bool | Unset): The host tag group can be in use by other hosts. Setting repair to True gives permission
            to automatically update the tag from the affected hosts. Default: False.
    """

    title: str | Unset = UNSET
    topic: str | Unset = UNSET
    help_: str | Unset = UNSET
    tags: list[HostTag] | Unset = UNSET
    repair: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        topic = self.topic

        help_ = self.help_

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        repair = self.repair

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if topic is not UNSET:
            field_dict["topic"] = topic
        if help_ is not UNSET:
            field_dict["help"] = help_
        if tags is not UNSET:
            field_dict["tags"] = tags
        if repair is not UNSET:
            field_dict["repair"] = repair

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_tag import HostTag

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        topic = d.pop("topic", UNSET)

        help_ = d.pop("help", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: list[HostTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = HostTag.from_dict(tags_item_data)

                tags.append(tags_item)

        repair = d.pop("repair", UNSET)

        update_host_tag_group = cls(
            title=title,
            topic=topic,
            help_=help_,
            tags=tags,
            repair=repair,
        )

        update_host_tag_group.additional_properties = d
        return update_host_tag_group

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
