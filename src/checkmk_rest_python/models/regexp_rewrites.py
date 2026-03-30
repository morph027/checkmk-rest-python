from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegexpRewrites")


@_attrs_define
class RegexpRewrites:
    r"""
    Attributes:
        search (str): The search regexp. May contain match-groups, conditional matches, etc. This follows the Python
            regular expression syntax.

            For details see:

             * https://docs.python.org/3/library/re.html
        replace_with (str): The replacement string. Match-groups can only be identified by `\1`, `\2`, etc. Highest
            supported match group is `\99`. Named lookups are not supported.
    """

    search: str
    replace_with: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search = self.search

        replace_with = self.replace_with

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search": search,
                "replace_with": replace_with,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("search")

        replace_with = d.pop("replace_with")

        regexp_rewrites = cls(
            search=search,
            replace_with=replace_with,
        )

        regexp_rewrites.additional_properties = d
        return regexp_rewrites

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
