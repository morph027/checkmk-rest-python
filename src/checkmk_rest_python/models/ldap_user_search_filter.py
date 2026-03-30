from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_user_search_filter_state import LDAPUserSearchFilterState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPUserSearchFilter")


@_attrs_define
class LDAPUserSearchFilter:
    """
    Attributes:
        state (LDAPUserSearchFilterState | Unset):  Example: enabled.
        filter_ (str | Unset): Using this option you can define an optional LDAP filter which is used during LDAP
            searches. It can be used to only handle a subset of the users below the given base DN. Example:
            (&(objectclass=user)(objectcategory=person)).
    """

    state: LDAPUserSearchFilterState | Unset = UNSET
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
        state: LDAPUserSearchFilterState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPUserSearchFilterState(_state)

        filter_ = d.pop("filter", UNSET)

        ldap_user_search_filter = cls(
            state=state,
            filter_=filter_,
        )

        ldap_user_search_filter.additional_properties = d
        return ldap_user_search_filter

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
