from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_user_id_attribute_state import LDAPUserIDAttributeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPUserIDAttribute")


@_attrs_define
class LDAPUserIDAttribute:
    """
    Attributes:
        state (LDAPUserIDAttributeState | Unset):  Example: enabled.
        attribute (str | Unset): The attribute used to identify the individual users. It must have unique values to make
            an user identifyable by the value of this attribute. Example: attribute_example.
    """

    state: LDAPUserIDAttributeState | Unset = UNSET
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
        state: LDAPUserIDAttributeState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPUserIDAttributeState(_state)

        attribute = d.pop("attribute", UNSET)

        ldap_user_id_attribute = cls(
            state=state,
            attribute=attribute,
        )

        ldap_user_id_attribute.additional_properties = d
        return ldap_user_id_attribute

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
