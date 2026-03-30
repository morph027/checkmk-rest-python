from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_member_attribute_value_state import LDAPMemberAttributeValueState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPMemberAttributeValue")


@_attrs_define
class LDAPMemberAttributeValue:
    """
    Attributes:
        state (LDAPMemberAttributeValueState | Unset):  Example: enabled.
        attribute (str | Unset): The attribute used to identify users group memberships. Example: example_member.
    """

    state: LDAPMemberAttributeValueState | Unset = UNSET
    attribute: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        attribute = self.attribute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if attribute is not UNSET:
            field_dict["attribute"] = attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPMemberAttributeValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPMemberAttributeValueState(_state)

        attribute = d.pop("attribute", UNSET)

        ldap_member_attribute_value = cls(
            state=state,
            attribute=attribute,
        )

        ldap_member_attribute_value.additional_properties = d
        return ldap_member_attribute_value

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
