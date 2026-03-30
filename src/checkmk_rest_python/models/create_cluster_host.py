from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cluster_create_attribute import ClusterCreateAttribute
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="CreateClusterHost")


@_attrs_define
class CreateClusterHost:
    r"""
    Attributes:
        host_name (str): The hostname of the cluster host. Example: example.com.
        folder (str): The path name of the folder.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: /.
        nodes (list[str]): Nodes where the newly created host should be the cluster-container of. Example: ['host1',
            'host2', 'host3'].
        attributes (ClusterCreateAttribute | CustomHostAttributes | TagGroupAttributes | Unset): Attributes to set on
            the newly created host. Example: {'ipaddress': '192.168.0.123'}.
    """

    host_name: str
    folder: str
    nodes: list[str]
    attributes: (
        ClusterCreateAttribute | CustomHostAttributes | TagGroupAttributes | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cluster_create_attribute import ClusterCreateAttribute
        from ..models.custom_host_attributes import CustomHostAttributes

        host_name = self.host_name

        folder = self.folder

        nodes = self.nodes

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, ClusterCreateAttribute):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, CustomHostAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_name": host_name,
                "folder": folder,
                "nodes": nodes,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cluster_create_attribute import ClusterCreateAttribute
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        host_name = d.pop("host_name")

        folder = d.pop("folder")

        nodes = cast(list[str], d.pop("nodes"))

        def _parse_attributes(
            data: object,
        ) -> ClusterCreateAttribute | CustomHostAttributes | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = ClusterCreateAttribute.from_dict(data)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_1 = CustomHostAttributes.from_dict(data)

                return attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            attributes_type_2 = TagGroupAttributes.from_dict(data)

            return attributes_type_2

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        create_cluster_host = cls(
            host_name=host_name,
            folder=folder,
            nodes=nodes,
            attributes=attributes,
        )

        create_cluster_host.additional_properties = d
        return create_cluster_host

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
