from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_user_group_filter_state import LDAPUserGroupFilterState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPUserGroupFilter")


@_attrs_define
class LDAPUserGroupFilter:
    """
    Attributes:
        state (LDAPUserGroupFilterState | Unset):  Example: enabled.
        filter_ (str | Unset): Define the DN of a group object which is used to filter the users. Example: CN=cmk-
            users,OU=groups,DC=example,DC=com.
    """

    state: LDAPUserGroupFilterState | Unset = UNSET
    filter_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPUserGroupFilterState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPUserGroupFilterState(_state)

        filter_ = d.pop("filter", UNSET)

        ldap_user_group_filter = cls(
            state=state,
            filter_=filter_,
        )

        ldap_user_group_filter.additional_properties = d
        return ldap_user_group_filter

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
