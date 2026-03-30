from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_node_vis_radial_style_config import BINodeVisRadialStyleConfig


T = TypeVar("T", bound="BINodeVisRadialStyle")


@_attrs_define
class BINodeVisRadialStyle:
    """
    Attributes:
        type_ (Any): Visualize child nodes radially. Default: 'radial'.
        style_config (BINodeVisRadialStyleConfig):
    """

    style_config: BINodeVisRadialStyleConfig
    type_: Any = "radial"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        style_config = self.style_config.to_dict()

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
        from ..models.bi_node_vis_radial_style_config import BINodeVisRadialStyleConfig

        d = dict(src_dict)
        type_ = d.pop("type")

        style_config = BINodeVisRadialStyleConfig.from_dict(d.pop("style_config"))

        bi_node_vis_radial_style = cls(
            type_=type_,
            style_config=style_config,
        )

        bi_node_vis_radial_style.additional_properties = d
        return bi_node_vis_radial_style

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
