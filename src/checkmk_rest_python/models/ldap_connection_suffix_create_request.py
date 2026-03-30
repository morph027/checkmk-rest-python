from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LDAPConnectionSuffixCreateRequest")


@_attrs_define
class LDAPConnectionSuffixCreateRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        suffix (str): The LDAP connection suffix can be used to distinguish equal named objects (name conflicts), for
            example user accounts, from different LDAP connections. Example: suffix_example.
    """

    suffix: str
    state: Any = "enabled"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        suffix = self.suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "suffix": suffix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        suffix = d.pop("suffix")

        ldap_connection_suffix_create_request = cls(
            state=state,
            suffix=suffix,
        )

        ldap_connection_suffix_create_request.additional_properties = d
        return ldap_connection_suffix_create_request

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
