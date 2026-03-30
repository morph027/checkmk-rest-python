from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.translate_names_convert_case import TranslateNamesConvertCase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.direct_mapping import DirectMapping
    from ..models.regexp_rewrites import RegexpRewrites


T = TypeVar("T", bound="TranslateNames")


@_attrs_define
class TranslateNames:
    """
    Attributes:
        convert_case (TranslateNamesConvertCase | Unset): Convert all detected host names to upper- or lower-case.

             * `nop` - Do not convert anything
             * `lower` - Convert all host names to lowercase.
             * `upper` - Convert all host names to uppercase. Default: TranslateNamesConvertCase.NOP.
        drop_domain (bool | Unset): Drop the rest of the domain, only keep the host name. Will not affect IP addresses.

            Examples:

             * `192.168.0.1` -> `192.168.0.1`
             * `foobar.example.com` -> `foobar`
             * `example.com` -> `example`
             * `example` -> `example`

            This will be executed **after**:

             * `convert_case`
        regexp_rewrites (list[RegexpRewrites] | Unset): Rewrite discovered host names with multiple regular expressions.
            The replacements will be done one after another in the order they appear in the list. If not anchored at the end
            by a `$` character, the regexpwill be anchored at the end implicitly by adding a `$` character.

            These will be executed **after**:

             * `convert_case`
             * `drop_domain`
        hostname_replacement (list[DirectMapping] | Unset): Replace one value with another.

            These will be executed **after**:

             * `convert_case`
             * `drop_domain`
             * `regexp_rewrites`
    """

    convert_case: TranslateNamesConvertCase | Unset = TranslateNamesConvertCase.NOP
    drop_domain: bool | Unset = UNSET
    regexp_rewrites: list[RegexpRewrites] | Unset = UNSET
    hostname_replacement: list[DirectMapping] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convert_case: str | Unset = UNSET
        if not isinstance(self.convert_case, Unset):
            convert_case = self.convert_case.value

        drop_domain = self.drop_domain

        regexp_rewrites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regexp_rewrites, Unset):
            regexp_rewrites = []
            for regexp_rewrites_item_data in self.regexp_rewrites:
                regexp_rewrites_item = regexp_rewrites_item_data.to_dict()
                regexp_rewrites.append(regexp_rewrites_item)

        hostname_replacement: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hostname_replacement, Unset):
            hostname_replacement = []
            for hostname_replacement_item_data in self.hostname_replacement:
                hostname_replacement_item = hostname_replacement_item_data.to_dict()
                hostname_replacement.append(hostname_replacement_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if convert_case is not UNSET:
            field_dict["convert_case"] = convert_case
        if drop_domain is not UNSET:
            field_dict["drop_domain"] = drop_domain
        if regexp_rewrites is not UNSET:
            field_dict["regexp_rewrites"] = regexp_rewrites
        if hostname_replacement is not UNSET:
            field_dict["hostname_replacement"] = hostname_replacement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.direct_mapping import DirectMapping
        from ..models.regexp_rewrites import RegexpRewrites

        d = dict(src_dict)
        _convert_case = d.pop("convert_case", UNSET)
        convert_case: TranslateNamesConvertCase | Unset
        if isinstance(_convert_case, Unset):
            convert_case = UNSET
        else:
            convert_case = TranslateNamesConvertCase(_convert_case)

        drop_domain = d.pop("drop_domain", UNSET)

        _regexp_rewrites = d.pop("regexp_rewrites", UNSET)
        regexp_rewrites: list[RegexpRewrites] | Unset = UNSET
        if _regexp_rewrites is not UNSET:
            regexp_rewrites = []
            for regexp_rewrites_item_data in _regexp_rewrites:
                regexp_rewrites_item = RegexpRewrites.from_dict(
                    regexp_rewrites_item_data
                )

                regexp_rewrites.append(regexp_rewrites_item)

        _hostname_replacement = d.pop("hostname_replacement", UNSET)
        hostname_replacement: list[DirectMapping] | Unset = UNSET
        if _hostname_replacement is not UNSET:
            hostname_replacement = []
            for hostname_replacement_item_data in _hostname_replacement:
                hostname_replacement_item = DirectMapping.from_dict(
                    hostname_replacement_item_data
                )

                hostname_replacement.append(hostname_replacement_item)

        translate_names = cls(
            convert_case=convert_case,
            drop_domain=drop_domain,
            regexp_rewrites=regexp_rewrites,
            hostname_replacement=hostname_replacement,
        )

        translate_names.additional_properties = d
        return translate_names

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
