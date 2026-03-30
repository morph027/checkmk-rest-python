from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateChanges")


@_attrs_define
class ActivateChanges:
    """
    Attributes:
        redirect (bool | Unset): After starting the activation, redirect immediately to the 'Wait for completion'
            endpoint. Default: False.
        sites (list[str] | Unset): The names of the sites on which the configuration shall be activated. An empty list
            means all sites which have pending changes. Example: ['production'].
        force_foreign_changes (bool | Unset): Will activate changes even if the user who made those changes is not the
            currently logged in user. Default: False.
    """

    redirect: bool | Unset = False
    sites: list[str] | Unset = UNSET
    force_foreign_changes: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redirect = self.redirect

        sites: list[str] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        force_foreign_changes = self.force_foreign_changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if sites is not UNSET:
            field_dict["sites"] = sites
        if force_foreign_changes is not UNSET:
            field_dict["force_foreign_changes"] = force_foreign_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redirect = d.pop("redirect", UNSET)

        sites = cast(list[str], d.pop("sites", UNSET))

        force_foreign_changes = d.pop("force_foreign_changes", UNSET)

        activate_changes = cls(
            redirect=redirect,
            sites=sites,
            force_foreign_changes=force_foreign_changes,
        )

        activate_changes.additional_properties = d
        return activate_changes

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
