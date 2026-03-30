from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BIPackEndpoint")


@_attrs_define
class BIPackEndpoint:
    """
    Attributes:
        title (str): The title of the BI pack. Example: BI Title.
        contact_groups (list[str]): A list of contact group identifiers. Example: ['contact', 'contactgroup_b'].
        public (bool): Should the BI pack be public or not. Example: false.
    """

    title: str
    contact_groups: list[str]
    public: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        contact_groups = self.contact_groups

        public = self.public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "contact_groups": contact_groups,
                "public": public,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        contact_groups = cast(list[str], d.pop("contact_groups"))

        public = d.pop("public")

        bi_pack_endpoint = cls(
            title=title,
            contact_groups=contact_groups,
            public=public,
        )

        bi_pack_endpoint.additional_properties = d
        return bi_pack_endpoint

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
