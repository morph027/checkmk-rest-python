from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BINodeVisRadialStyleConfig")


@_attrs_define
class BINodeVisRadialStyleConfig:
    """
    Attributes:
        degree (int): Limits the child nodes to be within this angle.
        radius (int): Distance between nodes.
        rotation (int): Starting point of the angle, in degrees.
    """

    degree: int
    radius: int
    rotation: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        degree = self.degree

        radius = self.radius

        rotation = self.rotation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "degree": degree,
                "radius": radius,
                "rotation": rotation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        degree = d.pop("degree")

        radius = d.pop("radius")

        rotation = d.pop("rotation")

        bi_node_vis_radial_style_config = cls(
            degree=degree,
            radius=radius,
            rotation=rotation,
        )

        bi_node_vis_radial_style_config.additional_properties = d
        return bi_node_vis_radial_style_config

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
