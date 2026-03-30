from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.host_extensions_effective_attributes import (
        HostExtensionsEffectiveAttributes,
    )
    from ..models.host_extensions_effective_attributes_type_1_type_0 import (
        HostExtensionsEffectiveAttributesType1Type0,
    )
    from ..models.host_view_attribute import HostViewAttribute
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="HostExtensions")


@_attrs_define
class HostExtensions:
    r"""
    Attributes:
        folder (str | Unset): The folder, in which this host resides.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`.
        attributes (CustomHostAttributes | HostViewAttribute | TagGroupAttributes | Unset): Attributes of this host.
            Example: {'ipaddress': '192.168.0.123'}.
        effective_attributes (HostExtensionsEffectiveAttributes | HostExtensionsEffectiveAttributesType1Type0 | None |
            Unset): All attributes of this host and all parent folders. Example: {'tag_snmp_ds': None}.
        is_cluster (bool | Unset): If this is a cluster host, i.e. a container for other hosts.
        is_offline (bool | Unset): Whether the host is offline
        cluster_nodes (list[str] | None | Unset): In the case this is a cluster host, these are the cluster nodes.
    """

    folder: str | Unset = UNSET
    attributes: (
        CustomHostAttributes | HostViewAttribute | TagGroupAttributes | Unset
    ) = UNSET
    effective_attributes: (
        HostExtensionsEffectiveAttributes
        | HostExtensionsEffectiveAttributesType1Type0
        | None
        | Unset
    ) = UNSET
    is_cluster: bool | Unset = UNSET
    is_offline: bool | Unset = UNSET
    cluster_nodes: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_extensions_effective_attributes import (
            HostExtensionsEffectiveAttributes,
        )
        from ..models.host_extensions_effective_attributes_type_1_type_0 import (
            HostExtensionsEffectiveAttributesType1Type0,
        )
        from ..models.host_view_attribute import HostViewAttribute

        folder = self.folder

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, HostViewAttribute):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, CustomHostAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        effective_attributes: dict[str, Any] | None | Unset
        if isinstance(self.effective_attributes, Unset):
            effective_attributes = UNSET
        elif isinstance(self.effective_attributes, HostExtensionsEffectiveAttributes):
            effective_attributes = self.effective_attributes.to_dict()
        elif isinstance(
            self.effective_attributes, HostExtensionsEffectiveAttributesType1Type0
        ):
            effective_attributes = self.effective_attributes.to_dict()
        else:
            effective_attributes = self.effective_attributes

        is_cluster = self.is_cluster

        is_offline = self.is_offline

        cluster_nodes: list[str] | None | Unset
        if isinstance(self.cluster_nodes, Unset):
            cluster_nodes = UNSET
        elif isinstance(self.cluster_nodes, list):
            cluster_nodes = self.cluster_nodes

        else:
            cluster_nodes = self.cluster_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder is not UNSET:
            field_dict["folder"] = folder
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if effective_attributes is not UNSET:
            field_dict["effective_attributes"] = effective_attributes
        if is_cluster is not UNSET:
            field_dict["is_cluster"] = is_cluster
        if is_offline is not UNSET:
            field_dict["is_offline"] = is_offline
        if cluster_nodes is not UNSET:
            field_dict["cluster_nodes"] = cluster_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_extensions_effective_attributes import (
            HostExtensionsEffectiveAttributes,
        )
        from ..models.host_extensions_effective_attributes_type_1_type_0 import (
            HostExtensionsEffectiveAttributesType1Type0,
        )
        from ..models.host_view_attribute import HostViewAttribute
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        folder = d.pop("folder", UNSET)

        def _parse_attributes(
            data: object,
        ) -> CustomHostAttributes | HostViewAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = HostViewAttribute.from_dict(data)

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

        def _parse_effective_attributes(
            data: object,
        ) -> (
            HostExtensionsEffectiveAttributes
            | HostExtensionsEffectiveAttributesType1Type0
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_attributes_type_0 = (
                    HostExtensionsEffectiveAttributes.from_dict(data)
                )

                return effective_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_attributes_type_1_type_0 = (
                    HostExtensionsEffectiveAttributesType1Type0.from_dict(data)
                )

                return effective_attributes_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                HostExtensionsEffectiveAttributes
                | HostExtensionsEffectiveAttributesType1Type0
                | None
                | Unset,
                data,
            )

        effective_attributes = _parse_effective_attributes(
            d.pop("effective_attributes", UNSET)
        )

        is_cluster = d.pop("is_cluster", UNSET)

        is_offline = d.pop("is_offline", UNSET)

        def _parse_cluster_nodes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_nodes_type_0 = cast(list[str], data)

                return cluster_nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cluster_nodes = _parse_cluster_nodes(d.pop("cluster_nodes", UNSET))

        host_extensions = cls(
            folder=folder,
            attributes=attributes,
            effective_attributes=effective_attributes,
            is_cluster=is_cluster,
            is_offline=is_offline,
            cluster_nodes=cluster_nodes,
        )

        host_extensions.additional_properties = d
        return host_extensions

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
