from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostTagOutput")


@_attrs_define
class HostTagOutput:
    """
    Attributes:
        id (None | str | Unset): The unique identifier of this host tag
        title (str | Unset): The title of this host tag
        aux_tags (list[str] | Unset): The auxiliary tags this tag included in.
    """

    id: None | str | Unset = UNSET
    title: str | Unset = UNSET
    aux_tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        title = self.title

        aux_tags: list[str] | Unset = UNSET
        if not isinstance(self.aux_tags, Unset):
            aux_tags = self.aux_tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if aux_tags is not UNSET:
            field_dict["aux_tags"] = aux_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        title = d.pop("title", UNSET)

        aux_tags = cast(list[str], d.pop("aux_tags", UNSET))

        host_tag_output = cls(
            id=id,
            title=title,
            aux_tags=aux_tags,
        )

        host_tag_output.additional_properties = d
        return host_tag_output

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
