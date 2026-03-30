from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuxTagAttrsResponse")


@_attrs_define
class AuxTagAttrsResponse:
    """
    Attributes:
        topic (str): Different tags can be grouped in topics to make the visualization and selections in the GUI more
            comfortable Example: Monitoring agents.
        help_ (str): The help of the Auxiliary tag Example: AuxTagExampleHelp.
    """

    topic: str
    help_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        help_ = self.help_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topic": topic,
                "help": help_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic = d.pop("topic")

        help_ = d.pop("help")

        aux_tag_attrs_response = cls(
            topic=topic,
            help_=help_,
        )

        aux_tag_attrs_response.additional_properties = d
        return aux_tag_attrs_response

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
