from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.installed_versions_rest_api import InstalledVersionsRestApi
    from ..models.installed_versions_versions import InstalledVersionsVersions


T = TypeVar("T", bound="InstalledVersions")


@_attrs_define
class InstalledVersions:
    """
    Attributes:
        site (str | Unset): The site where this API call was made on. Example: production.
        group (str | Unset): The Apache WSGI application group this call was made on. Example: de.
        rest_api (InstalledVersionsRestApi | Unset): The REST-API version Example: {'revision': '1.0.0'}.
        versions (InstalledVersionsVersions | Unset): Some version numbers Example: {'checkmk': '1.8.0p1'}.
        edition (str | Unset): The Checkmk edition. Example: raw.
        demo (bool | Unset): Whether this is a demo version or not.
    """

    site: str | Unset = UNSET
    group: str | Unset = UNSET
    rest_api: InstalledVersionsRestApi | Unset = UNSET
    versions: InstalledVersionsVersions | Unset = UNSET
    edition: str | Unset = UNSET
    demo: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        group = self.group

        rest_api: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rest_api, Unset):
            rest_api = self.rest_api.to_dict()

        versions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions.to_dict()

        edition = self.edition

        demo = self.demo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if group is not UNSET:
            field_dict["group"] = group
        if rest_api is not UNSET:
            field_dict["rest_api"] = rest_api
        if versions is not UNSET:
            field_dict["versions"] = versions
        if edition is not UNSET:
            field_dict["edition"] = edition
        if demo is not UNSET:
            field_dict["demo"] = demo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installed_versions_rest_api import InstalledVersionsRestApi
        from ..models.installed_versions_versions import InstalledVersionsVersions

        d = dict(src_dict)
        site = d.pop("site", UNSET)

        group = d.pop("group", UNSET)

        _rest_api = d.pop("rest_api", UNSET)
        rest_api: InstalledVersionsRestApi | Unset
        if isinstance(_rest_api, Unset):
            rest_api = UNSET
        else:
            rest_api = InstalledVersionsRestApi.from_dict(_rest_api)

        _versions = d.pop("versions", UNSET)
        versions: InstalledVersionsVersions | Unset
        if isinstance(_versions, Unset):
            versions = UNSET
        else:
            versions = InstalledVersionsVersions.from_dict(_versions)

        edition = d.pop("edition", UNSET)

        demo = d.pop("demo", UNSET)

        installed_versions = cls(
            site=site,
            group=group,
            rest_api=rest_api,
            versions=versions,
            edition=edition,
            demo=demo,
        )

        installed_versions.additional_properties = d
        return installed_versions

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
