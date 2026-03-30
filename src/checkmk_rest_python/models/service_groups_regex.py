from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_groups_regex_match_type import ServiceGroupsRegexMatchType

T = TypeVar("T", bound="ServiceGroupsRegex")


@_attrs_define
class ServiceGroupsRegex:
    """
    Attributes:
        match_type (ServiceGroupsRegexMatchType):  Example: match_alias.
        regex_list (list[str]): The text entered in this list is handled as a regular expression pattern Example:
            ['[A-Z]+123', '[A-Z]+456'].
    """

    match_type: ServiceGroupsRegexMatchType
    regex_list: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_type = self.match_type.value

        regex_list = self.regex_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match_type": match_type,
                "regex_list": regex_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_type = ServiceGroupsRegexMatchType(d.pop("match_type"))

        regex_list = cast(list[str], d.pop("regex_list"))

        service_groups_regex = cls(
            match_type=match_type,
            regex_list=regex_list,
        )

        service_groups_regex.additional_properties = d
        return service_groups_regex

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
