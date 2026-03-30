from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuxTagAttrsCreate")


@_attrs_define
class AuxTagAttrsCreate:
    """
    Attributes:
        aux_tag_id (None | str): An auxiliary tag id Example: ip-v4.
        topic (str): Different tags can be grouped in topics to make the visualization and selections in the GUI more
            comfortable Example: Monitoring agents.
        title (str): The title of the Auxiliary tag Example: AuxTagExampleTitle.
        help_ (str | Unset): The help of the Auxiliary tag Default: ''. Example: AuxTagExampleHelp.
    """

    aux_tag_id: None | str
    topic: str
    title: str
    help_: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aux_tag_id: None | str
        aux_tag_id = self.aux_tag_id

        topic = self.topic

        title = self.title

        help_ = self.help_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aux_tag_id": aux_tag_id,
                "topic": topic,
                "title": title,
            }
        )
        if help_ is not UNSET:
            field_dict["help"] = help_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_aux_tag_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        aux_tag_id = _parse_aux_tag_id(d.pop("aux_tag_id"))

        topic = d.pop("topic")

        title = d.pop("title")

        help_ = d.pop("help", UNSET)

        aux_tag_attrs_create = cls(
            aux_tag_id=aux_tag_id,
            topic=topic,
            title=title,
            help_=help_,
        )

        aux_tag_attrs_create.additional_properties = d
        return aux_tag_attrs_create

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
