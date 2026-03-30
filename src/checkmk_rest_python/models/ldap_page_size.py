from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_page_size_state import LDAPPageSizeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPPageSize")


@_attrs_define
class LDAPPageSize:
    """
    Attributes:
        state (LDAPPageSizeState | Unset):  Example: enabled.
        size (int | Unset): LDAP searches can be performed in paginated mode, for example to improve the performance.
            This enables pagination and configures the size of the pages. Example: 1000.
    """

    state: LDAPPageSizeState | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPPageSizeState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPPageSizeState(_state)

        size = d.pop("size", UNSET)

        ldap_page_size = cls(
            state=state,
            size=size,
        )

        ldap_page_size.additional_properties = d
        return ldap_page_size

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
