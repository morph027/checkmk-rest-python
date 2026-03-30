from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_users_create_users import LDAPUsersCreateUsers
from ..models.ldap_users_search_scope import LDAPUsersSearchScope
from ..models.ldap_users_umlauts_in_user_ids import LDAPUsersUmlautsInUserIds
from ..models.ldap_users_user_id_case import LDAPUsersUserIdCase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_user_group_filter import LDAPUserGroupFilter
    from ..models.ldap_user_id_attribute import LDAPUserIDAttribute
    from ..models.ldap_user_search_filter import LDAPUserSearchFilter


T = TypeVar("T", bound="LDAPUsers")


@_attrs_define
class LDAPUsers:
    """
    Attributes:
        user_base_dn (str | Unset): Give a base distinguished name here. All user accounts to synchronize must be
            located below this one. Example: OU=users,DC=example,DC=com.
        search_scope (LDAPUsersSearchScope | Unset): Scope to be used in LDAP searches. In most cases Search whole
            subtree below the base DN is the best choice. It searches for matching objects recursively. Example:
            search_whole_subtree.
        search_filter (LDAPUserSearchFilter | Unset):
        filter_group (LDAPUserGroupFilter | Unset):
        user_id_attribute (LDAPUserIDAttribute | Unset):
        user_id_case (LDAPUsersUserIdCase | Unset): Convert imported User-IDs to lower case during synchronization or
            leave as is. Example: convert_to_lowercase.
        umlauts_in_user_ids (LDAPUsersUmlautsInUserIds | Unset): Checkmk does not support special characters in User-
            IDs. However, to deal with LDAP users having umlauts in their User-IDs you previously had the choice to replace
            umlauts with other characters. This option is still available for backward compatibility, but you are advised to
            use the 'keep_umlauts' option for new installations. Example: keep_umlauts.
        create_users (LDAPUsersCreateUsers | Unset): Create user accounts during sync or on the first login Example:
            on_sync.
    """

    user_base_dn: str | Unset = UNSET
    search_scope: LDAPUsersSearchScope | Unset = UNSET
    search_filter: LDAPUserSearchFilter | Unset = UNSET
    filter_group: LDAPUserGroupFilter | Unset = UNSET
    user_id_attribute: LDAPUserIDAttribute | Unset = UNSET
    user_id_case: LDAPUsersUserIdCase | Unset = UNSET
    umlauts_in_user_ids: LDAPUsersUmlautsInUserIds | Unset = UNSET
    create_users: LDAPUsersCreateUsers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_base_dn = self.user_base_dn

        search_scope: str | Unset = UNSET
        if not isinstance(self.search_scope, Unset):
            search_scope = self.search_scope.value

        search_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_filter, Unset):
            search_filter = self.search_filter.to_dict()

        filter_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_group, Unset):
            filter_group = self.filter_group.to_dict()

        user_id_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_id_attribute, Unset):
            user_id_attribute = self.user_id_attribute.to_dict()

        user_id_case: str | Unset = UNSET
        if not isinstance(self.user_id_case, Unset):
            user_id_case = self.user_id_case.value

        umlauts_in_user_ids: str | Unset = UNSET
        if not isinstance(self.umlauts_in_user_ids, Unset):
            umlauts_in_user_ids = self.umlauts_in_user_ids.value

        create_users: str | Unset = UNSET
        if not isinstance(self.create_users, Unset):
            create_users = self.create_users.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_base_dn is not UNSET:
            field_dict["user_base_dn"] = user_base_dn
        if search_scope is not UNSET:
            field_dict["search_scope"] = search_scope
        if search_filter is not UNSET:
            field_dict["search_filter"] = search_filter
        if filter_group is not UNSET:
            field_dict["filter_group"] = filter_group
        if user_id_attribute is not UNSET:
            field_dict["user_id_attribute"] = user_id_attribute
        if user_id_case is not UNSET:
            field_dict["user_id_case"] = user_id_case
        if umlauts_in_user_ids is not UNSET:
            field_dict["umlauts_in_user_ids"] = umlauts_in_user_ids
        if create_users is not UNSET:
            field_dict["create_users"] = create_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_user_group_filter import LDAPUserGroupFilter
        from ..models.ldap_user_id_attribute import LDAPUserIDAttribute
        from ..models.ldap_user_search_filter import LDAPUserSearchFilter

        d = dict(src_dict)
        user_base_dn = d.pop("user_base_dn", UNSET)

        _search_scope = d.pop("search_scope", UNSET)
        search_scope: LDAPUsersSearchScope | Unset
        if isinstance(_search_scope, Unset):
            search_scope = UNSET
        else:
            search_scope = LDAPUsersSearchScope(_search_scope)

        _search_filter = d.pop("search_filter", UNSET)
        search_filter: LDAPUserSearchFilter | Unset
        if isinstance(_search_filter, Unset):
            search_filter = UNSET
        else:
            search_filter = LDAPUserSearchFilter.from_dict(_search_filter)

        _filter_group = d.pop("filter_group", UNSET)
        filter_group: LDAPUserGroupFilter | Unset
        if isinstance(_filter_group, Unset):
            filter_group = UNSET
        else:
            filter_group = LDAPUserGroupFilter.from_dict(_filter_group)

        _user_id_attribute = d.pop("user_id_attribute", UNSET)
        user_id_attribute: LDAPUserIDAttribute | Unset
        if isinstance(_user_id_attribute, Unset):
            user_id_attribute = UNSET
        else:
            user_id_attribute = LDAPUserIDAttribute.from_dict(_user_id_attribute)

        _user_id_case = d.pop("user_id_case", UNSET)
        user_id_case: LDAPUsersUserIdCase | Unset
        if isinstance(_user_id_case, Unset):
            user_id_case = UNSET
        else:
            user_id_case = LDAPUsersUserIdCase(_user_id_case)

        _umlauts_in_user_ids = d.pop("umlauts_in_user_ids", UNSET)
        umlauts_in_user_ids: LDAPUsersUmlautsInUserIds | Unset
        if isinstance(_umlauts_in_user_ids, Unset):
            umlauts_in_user_ids = UNSET
        else:
            umlauts_in_user_ids = LDAPUsersUmlautsInUserIds(_umlauts_in_user_ids)

        _create_users = d.pop("create_users", UNSET)
        create_users: LDAPUsersCreateUsers | Unset
        if isinstance(_create_users, Unset):
            create_users = UNSET
        else:
            create_users = LDAPUsersCreateUsers(_create_users)

        ldap_users = cls(
            user_base_dn=user_base_dn,
            search_scope=search_scope,
            search_filter=search_filter,
            filter_group=filter_group,
            user_id_attribute=user_id_attribute,
            user_id_case=user_id_case,
            umlauts_in_user_ids=umlauts_in_user_ids,
            create_users=create_users,
        )

        ldap_users.additional_properties = d
        return ldap_users

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
