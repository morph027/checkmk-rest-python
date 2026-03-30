from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.folder_view_attribute import FolderViewAttribute
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="FolderExtensions")


@_attrs_define
class FolderExtensions:
    """
    Attributes:
        path (str | Unset): The full path of this folder, slash delimited.
        attributes (CustomHostAttributes | FolderViewAttribute | TagGroupAttributes | Unset): The folder's attributes.
            Hosts placed in this folder will inherit these attributes.
    """

    path: str | Unset = UNSET
    attributes: (
        CustomHostAttributes | FolderViewAttribute | TagGroupAttributes | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.folder_view_attribute import FolderViewAttribute

        path = self.path

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, FolderViewAttribute):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, CustomHostAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.folder_view_attribute import FolderViewAttribute
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        def _parse_attributes(
            data: object,
        ) -> CustomHostAttributes | FolderViewAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = FolderViewAttribute.from_dict(data)

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

        folder_extensions = cls(
            path=path,
            attributes=attributes,
        )

        folder_extensions.additional_properties = d
        return folder_extensions

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
