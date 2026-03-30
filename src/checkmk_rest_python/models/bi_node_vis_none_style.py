from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BINodeVisNoneStyle")


@_attrs_define
class BINodeVisNoneStyle:
    """
    Attributes:
        type_ (Any): No specific child node visualization. Default: 'none'.
        style_config (Any): No configuration options for this style. Default: {}.
    """

    type_: Any = "none"
    style_config: Any = {}
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        style_config = self.style_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "style_config": style_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        style_config = d.pop("style_config")

        bi_node_vis_none_style = cls(
            type_=type_,
            style_config=style_config,
        )

        bi_node_vis_none_style.additional_properties = d
        return bi_node_vis_none_style

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
