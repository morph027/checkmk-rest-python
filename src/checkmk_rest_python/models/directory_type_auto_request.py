from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.directory_type_auto_request_type import DirectoryTypeAutoRequestType

T = TypeVar("T", bound="DirectoryTypeAutoRequest")


@_attrs_define
class DirectoryTypeAutoRequest:
    """
    Attributes:
        type_ (DirectoryTypeAutoRequestType): Select the software the LDAP directory is based on. Example:
            active_directory_manual.
        domain (str): Configure the DNS domain name of your Active directory domain here, Checkmk will then query this
            domain for it's closest domain controller to communicate with. Example: your_domain.com.
    """

    type_: DirectoryTypeAutoRequestType
    domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "domain": domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DirectoryTypeAutoRequestType(d.pop("type"))

        domain = d.pop("domain")

        directory_type_auto_request = cls(
            type_=type_,
            domain=domain,
        )

        directory_type_auto_request.additional_properties = d
        return directory_type_auto_request

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
