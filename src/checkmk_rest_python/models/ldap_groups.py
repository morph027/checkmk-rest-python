from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_groups_search_scope import LDAPGroupsSearchScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_group_search_filter import LDAPGroupSearchFilter
    from ..models.ldap_member_attribute_value import LDAPMemberAttributeValue


T = TypeVar("T", bound="LDAPGroups")


@_attrs_define
class LDAPGroups:
    """
    Attributes:
        group_base_dn (str | Unset): Give a base distinguished name here. All groups used must be located below this
            one. Example: OU=groups,DC=example,DC=com.
        search_scope (LDAPGroupsSearchScope | Unset): Scope to be used in group related LDAP searches. In most cases
            Search whole subtree below the base DN is the best choice. It searches for matching objects in the given base
            recursively.
        search_filter (LDAPGroupSearchFilter | Unset):
        member_attribute (LDAPMemberAttributeValue | Unset):
    """

    group_base_dn: str | Unset = UNSET
    search_scope: LDAPGroupsSearchScope | Unset = UNSET
    search_filter: LDAPGroupSearchFilter | Unset = UNSET
    member_attribute: LDAPMemberAttributeValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_base_dn = self.group_base_dn

        search_scope: str | Unset = UNSET
        if not isinstance(self.search_scope, Unset):
            search_scope = self.search_scope.value

        search_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_filter, Unset):
            search_filter = self.search_filter.to_dict()

        member_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member_attribute, Unset):
            member_attribute = self.member_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_base_dn is not UNSET:
            field_dict["group_base_dn"] = group_base_dn
        if search_scope is not UNSET:
            field_dict["search_scope"] = search_scope
        if search_filter is not UNSET:
            field_dict["search_filter"] = search_filter
        if member_attribute is not UNSET:
            field_dict["member_attribute"] = member_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_group_search_filter import LDAPGroupSearchFilter
        from ..models.ldap_member_attribute_value import LDAPMemberAttributeValue

        d = dict(src_dict)
        group_base_dn = d.pop("group_base_dn", UNSET)

        _search_scope = d.pop("search_scope", UNSET)
        search_scope: LDAPGroupsSearchScope | Unset
        if isinstance(_search_scope, Unset):
            search_scope = UNSET
        else:
            search_scope = LDAPGroupsSearchScope(_search_scope)

        _search_filter = d.pop("search_filter", UNSET)
        search_filter: LDAPGroupSearchFilter | Unset
        if isinstance(_search_filter, Unset):
            search_filter = UNSET
        else:
            search_filter = LDAPGroupSearchFilter.from_dict(_search_filter)

        _member_attribute = d.pop("member_attribute", UNSET)
        member_attribute: LDAPMemberAttributeValue | Unset
        if isinstance(_member_attribute, Unset):
            member_attribute = UNSET
        else:
            member_attribute = LDAPMemberAttributeValue.from_dict(_member_attribute)

        ldap_groups = cls(
            group_base_dn=group_base_dn,
            search_scope=search_scope,
            search_filter=search_filter,
            member_attribute=member_attribute,
        )

        ldap_groups.additional_properties = d
        return ldap_groups

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
