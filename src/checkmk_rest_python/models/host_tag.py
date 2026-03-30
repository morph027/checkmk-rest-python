from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostTag")


@_attrs_define
class HostTag:
    """
    Attributes:
        title (str): The title of the tag Example: Tag.
        id (None | str | Unset): An unique id for the tag Example: tag_id.
        aux_tags (list[None | str] | Unset): The list of auxiliary tag ids. Built-in tags (ip-v4, ip-v6, snmp, tcp,
            ping) and custom defined tags are allowed. Example: ['ip-v4, ip-v6'].
    """

    title: str
    id: None | str | Unset = UNSET
    aux_tags: list[None | str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        aux_tags: list[None | str] | Unset = UNSET
        if not isinstance(self.aux_tags, Unset):
            aux_tags = []
            for aux_tags_item_data in self.aux_tags:
                aux_tags_item: None | str
                aux_tags_item = aux_tags_item_data
                aux_tags.append(aux_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aux_tags is not UNSET:
            field_dict["aux_tags"] = aux_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _aux_tags = d.pop("aux_tags", UNSET)
        aux_tags: list[None | str] | Unset = UNSET
        if _aux_tags is not UNSET:
            aux_tags = []
            for aux_tags_item_data in _aux_tags:

                def _parse_aux_tags_item(data: object) -> None | str:
                    if data is None:
                        return data
                    return cast(None | str, data)

                aux_tags_item = _parse_aux_tags_item(aux_tags_item_data)

                aux_tags.append(aux_tags_item)

        host_tag = cls(
            title=title,
            id=id,
            aux_tags=aux_tags,
        )

        host_tag.additional_properties = d
        return host_tag

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
