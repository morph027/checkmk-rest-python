from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.host_create_attribute import HostCreateAttribute
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="CreateHost")


@_attrs_define
class CreateHost:
    r"""
    Attributes:
        host_name (str): The hostname or IP address of the host to be created. Example: example.com.
        folder (str): The path name of the folder.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: /.
        attributes (CustomHostAttributes | HostCreateAttribute | TagGroupAttributes | Unset): Attributes to set on the
            newly created host. Example: {'ipaddress': '192.168.0.123'}.
    """

    host_name: str
    folder: str
    attributes: (
        CustomHostAttributes | HostCreateAttribute | TagGroupAttributes | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_create_attribute import HostCreateAttribute

        host_name = self.host_name

        folder = self.folder

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, HostCreateAttribute):
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
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_create_attribute import HostCreateAttribute
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        host_name = d.pop("host_name")

        folder = d.pop("folder")

        def _parse_attributes(
            data: object,
        ) -> CustomHostAttributes | HostCreateAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = HostCreateAttribute.from_dict(data)

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

        create_host = cls(
            host_name=host_name,
            folder=folder,
            attributes=attributes,
        )

        create_host.additional_properties = d
        return create_host

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
