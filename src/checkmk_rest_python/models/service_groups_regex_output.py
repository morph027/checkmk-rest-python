from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_groups_regex_output_match_type import (
    ServiceGroupsRegexOutputMatchType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceGroupsRegexOutput")


@_attrs_define
class ServiceGroupsRegexOutput:
    """
    Attributes:
        match_type (ServiceGroupsRegexOutputMatchType | Unset):  Example: match_alias.
        regex_list (list[str] | Unset): The text entered in this list is handled as a regular expression pattern
            Example: ['[A-Z]+123', '[A-Z]+456'].
    """

    match_type: ServiceGroupsRegexOutputMatchType | Unset = UNSET
    regex_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_type: str | Unset = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type.value

        regex_list: list[str] | Unset = UNSET
        if not isinstance(self.regex_list, Unset):
            regex_list = self.regex_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if regex_list is not UNSET:
            field_dict["regex_list"] = regex_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _match_type = d.pop("match_type", UNSET)
        match_type: ServiceGroupsRegexOutputMatchType | Unset
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = ServiceGroupsRegexOutputMatchType(_match_type)

        regex_list = cast(list[str], d.pop("regex_list", UNSET))

        service_groups_regex_output = cls(
            match_type=match_type,
            regex_list=regex_list,
        )

        service_groups_regex_output.additional_properties = d
        return service_groups_regex_output

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
