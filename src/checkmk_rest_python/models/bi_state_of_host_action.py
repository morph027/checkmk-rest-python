from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BIStateOfHostAction")


@_attrs_define
class BIStateOfHostAction:
    """
    Attributes:
        type_ (Any): Create nodes representing the state of hosts. Default: 'state_of_host'.
        host_regex (str): Host name regex. Example: testhost.
    """

    host_regex: str
    type_: Any = "state_of_host"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        host_regex = self.host_regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "host_regex": host_regex,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        host_regex = d.pop("host_regex")

        bi_state_of_host_action = cls(
            type_=type_,
            host_regex=host_regex,
        )

        bi_state_of_host_action.additional_properties = d
        return bi_state_of_host_action

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
