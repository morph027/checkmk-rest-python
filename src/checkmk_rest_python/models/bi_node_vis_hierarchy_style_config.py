from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BINodeVisHierarchyStyleConfig")


@_attrs_define
class BINodeVisHierarchyStyleConfig:
    """
    Attributes:
        layer_height (int): Distance between layers. Example: 85.
        node_size (int): Distance between nodes within the same layer. Example: 40.
        rotation (int): Rotation of the hierarchy, in degrees. Example: 180.
    """

    layer_height: int
    node_size: int
    rotation: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layer_height = self.layer_height

        node_size = self.node_size

        rotation = self.rotation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layer_height": layer_height,
                "node_size": node_size,
                "rotation": rotation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        layer_height = d.pop("layer_height")

        node_size = d.pop("node_size")

        rotation = d.pop("rotation")

        bi_node_vis_hierarchy_style_config = cls(
            layer_height=layer_height,
            node_size=node_size,
            rotation=rotation,
        )

        bi_node_vis_hierarchy_style_config.additional_properties = d
        return bi_node_vis_hierarchy_style_config

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
