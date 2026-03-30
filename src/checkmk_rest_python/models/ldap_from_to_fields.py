from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ldap_from_to_fields_state import LDAPFromToFieldsState
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPFromToFields")


@_attrs_define
class LDAPFromToFields:
    """
    Attributes:
        from_time (datetime.datetime):  Example: 2024-02-29T17:32:28+00:00.
        to_time (datetime.datetime):  Example: 2024-02-29T12:53:34+00:00.
        state (LDAPFromToFieldsState | Unset):  Example: enabled.
    """

    from_time: datetime.datetime
    to_time: datetime.datetime
    state: LDAPFromToFieldsState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_time = self.from_time.isoformat()

        to_time = self.to_time.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_time": from_time,
                "to_time": to_time,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_time = isoparse(d.pop("from_time"))

        to_time = isoparse(d.pop("to_time"))

        _state = d.pop("state", UNSET)
        state: LDAPFromToFieldsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPFromToFieldsState(_state)

        ldap_from_to_fields = cls(
            from_time=from_time,
            to_time=to_time,
            state=state,
        )

        ldap_from_to_fields.additional_properties = d
        return ldap_from_to_fields

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
