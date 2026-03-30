from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_host_attributes import CustomHostAttributes
    from ..models.host_update_attribute import HostUpdateAttribute
    from ..models.tag_group_attributes import TagGroupAttributes


T = TypeVar("T", bound="UpdateHostEntry")


@_attrs_define
class UpdateHostEntry:
    """
    Attributes:
        host_name (str): The hostname or IP address itself. Example: example.com.
        attributes (CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset): Replace all currently set
            attributes on the host, with these attributes. Any previously set attributes which are not given here will be
            removed. Can't be used together with update_attributes or remove_attributes fields. Example: {'ipaddress':
            '192.168.0.123'}.
        update_attributes (CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset): Just update the
            hosts attributes with these attributes. The previously set attributes will be overwritten. Can't be used
            together with attributes or remove_attributes fields. Example: {'ipaddress': '192.168.0.123'}.
        remove_attributes (list[str] | Unset): A list of attributes which should be removed. Can't be used together with
            attributes or update attributes fields. Example: ['tag_foobar'].
    """

    host_name: str
    attributes: (
        CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset
    ) = UNSET
    update_attributes: (
        CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset
    ) = UNSET
    remove_attributes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_update_attribute import HostUpdateAttribute

        host_name = self.host_name

        attributes: dict[str, Any] | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, HostUpdateAttribute):
            attributes = self.attributes.to_dict()
        elif isinstance(self.attributes, CustomHostAttributes):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes.to_dict()

        update_attributes: dict[str, Any] | Unset
        if isinstance(self.update_attributes, Unset):
            update_attributes = UNSET
        elif isinstance(self.update_attributes, HostUpdateAttribute):
            update_attributes = self.update_attributes.to_dict()
        elif isinstance(self.update_attributes, CustomHostAttributes):
            update_attributes = self.update_attributes.to_dict()
        else:
            update_attributes = self.update_attributes.to_dict()

        remove_attributes: list[str] | Unset = UNSET
        if not isinstance(self.remove_attributes, Unset):
            remove_attributes = self.remove_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_name": host_name,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if update_attributes is not UNSET:
            field_dict["update_attributes"] = update_attributes
        if remove_attributes is not UNSET:
            field_dict["remove_attributes"] = remove_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_host_attributes import CustomHostAttributes
        from ..models.host_update_attribute import HostUpdateAttribute
        from ..models.tag_group_attributes import TagGroupAttributes

        d = dict(src_dict)
        host_name = d.pop("host_name")

        def _parse_attributes(
            data: object,
        ) -> CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = HostUpdateAttribute.from_dict(data)

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

        def _parse_update_attributes(
            data: object,
        ) -> CustomHostAttributes | HostUpdateAttribute | TagGroupAttributes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_attributes_type_0 = HostUpdateAttribute.from_dict(data)

                return update_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_attributes_type_1 = CustomHostAttributes.from_dict(data)

                return update_attributes_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            update_attributes_type_2 = TagGroupAttributes.from_dict(data)

            return update_attributes_type_2

        update_attributes = _parse_update_attributes(d.pop("update_attributes", UNSET))

        remove_attributes = cast(list[str], d.pop("remove_attributes", UNSET))

        update_host_entry = cls(
            host_name=host_name,
            attributes=attributes,
            update_attributes=update_attributes,
            remove_attributes=remove_attributes,
        )

        update_host_entry.additional_properties = d
        return update_host_entry

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
