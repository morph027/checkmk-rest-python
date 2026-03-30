from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="LDAPCheckboxCustomTimeRangeEnabledRequest")


@_attrs_define
class LDAPCheckboxCustomTimeRangeEnabledRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        from_time (datetime.datetime): The start of the time range Example: 2024-02-29T17:32:28+00:00.
        to_time (datetime.datetime): The end of the time range Example: 2024-03-04T12:12:56+00:00.
    """

    from_time: datetime.datetime
    to_time: datetime.datetime
    state: Any = "enabled"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        from_time = self.from_time.isoformat()

        to_time = self.to_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "from_time": from_time,
                "to_time": to_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        from_time = isoparse(d.pop("from_time"))

        to_time = isoparse(d.pop("to_time"))

        ldap_checkbox_custom_time_range_enabled_request = cls(
            state=state,
            from_time=from_time,
            to_time=to_time,
        )

        ldap_checkbox_custom_time_range_enabled_request.additional_properties = d
        return ldap_checkbox_custom_time_range_enabled_request

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
