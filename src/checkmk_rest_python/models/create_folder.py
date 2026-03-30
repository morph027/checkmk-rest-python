from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.folder_create_attribute import FolderCreateAttribute
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="CreateFolder")


@_attrs_define
class CreateFolder:
    r"""
    Attributes:
        title (str): The folder title as displayed in the user interface. Example: Production Hosts.
        parent (str): The folder in which the new folder shall be placed in. The root-folder is specified by '/'.

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: /.
        name (str | Unset): The filesystem directory name (not path!) of the folder. No slashes are allowed. Example:
            production.
        attributes (CustomHostAttributes | FolderCreateAttribute | TagGroupAttributes | Unset): Specific attributes to
            apply for all hosts in this folder (among other things). Example: {'tag_criticality': 'prod'}.
    """

    title: str
    parent: str
    name: str | Unset = UNSET
    attributes: (
        CustomHostAttributes | FolderCreateAttribute | TagGroupAttributes | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.folder_create_attribute import FolderCreateAttribute

        title = self.title

        parent = self.parent

        name = self.name

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, FolderCreateAttribute):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, CustomHostAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "parent": parent,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.folder_create_attribute import FolderCreateAttribute
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        title = d.pop("title")

        parent = d.pop("parent")

        name = d.pop("name", UNSET)

        def _parse_attributes(
            data: object,
        ) -> CustomHostAttributes | FolderCreateAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = FolderCreateAttribute.from_dict(data)

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

        create_folder = cls(
            title=title,
            parent=parent,
            name=name,
            attributes=attributes,
        )

        create_folder.additional_properties = d
        return create_folder

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
