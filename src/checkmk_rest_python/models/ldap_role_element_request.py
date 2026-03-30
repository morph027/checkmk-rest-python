from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPRoleElementRequest")


@_attrs_define
class LDAPRoleElementRequest:
    """
    Attributes:
        group_dn (str): This group must be defined within the scope of the LDAP Group Settings Example: cmk-users.
        search_in (str | Unset): An existing ldap connection. Use 'this_connection' to select the current connection
            Default: 'this_connection'. Example: this_connection.
    """

    group_dn: str
    search_in: str | Unset = "this_connection"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_dn = self.group_dn

        search_in = self.search_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_dn": group_dn,
            }
        )
        if search_in is not UNSET:
            field_dict["search_in"] = search_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_dn = d.pop("group_dn")

        search_in = d.pop("search_in", UNSET)

        ldap_role_element_request = cls(
            group_dn=group_dn,
            search_in=search_in,
        )

        ldap_role_element_request.additional_properties = d
        return ldap_role_element_request

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
