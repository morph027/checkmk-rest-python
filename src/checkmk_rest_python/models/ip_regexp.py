from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPRegexp")


@_attrs_define
class IPRegexp:
    """
    Attributes:
        type_ (Any | Unset): IPv4 addresses which match a regexp pattern Default: 'ip_regex_list'.
        regexp_list (list[str] | Unset): A list of regular expressions which are matched against the found IP addresses.
            The matches will be excluded from the result.
    """

    type_: Any | Unset = "ip_regex_list"
    regexp_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        regexp_list: list[str] | Unset = UNSET
        if not isinstance(self.regexp_list, Unset):
            regexp_list = self.regexp_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if regexp_list is not UNSET:
            field_dict["regexp_list"] = regexp_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        regexp_list = cast(list[str], d.pop("regexp_list", UNSET))

        ip_regexp = cls(
            type_=type_,
            regexp_list=regexp_list,
        )

        ip_regexp.additional_properties = d
        return ip_regexp

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
