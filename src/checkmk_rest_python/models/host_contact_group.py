from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostContactGroup")


@_attrs_define
class HostContactGroup:
    """
    Attributes:
        groups (list[str]): A list of contact groups.
        use (bool | Unset): Add these contact groups to the host. Default: False.
        use_for_services (bool | Unset): <p>Always add host contact groups also to its services.</p>With this option
            contact groups that are added to hosts are always being added to services, as well. This only makes a difference
            if you have assigned other contact groups to services via rules in <i>Host & Service Parameters</i>. As long as
            you do not have any such rule a service always inherits all contact groups from its host. Default: False.
        recurse_use (bool | Unset): Add these groups as contacts to all hosts in all sub-folders of this folder.
            Default: False.
        recurse_perms (bool | Unset): Give these groups also permission on all sub-folders. Default: False.
    """

    groups: list[str]
    use: bool | Unset = False
    use_for_services: bool | Unset = False
    recurse_use: bool | Unset = False
    recurse_perms: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = self.groups

        use = self.use

        use_for_services = self.use_for_services

        recurse_use = self.recurse_use

        recurse_perms = self.recurse_perms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
            }
        )
        if use is not UNSET:
            field_dict["use"] = use
        if use_for_services is not UNSET:
            field_dict["use_for_services"] = use_for_services
        if recurse_use is not UNSET:
            field_dict["recurse_use"] = recurse_use
        if recurse_perms is not UNSET:
            field_dict["recurse_perms"] = recurse_perms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        groups = cast(list[str], d.pop("groups"))

        use = d.pop("use", UNSET)

        use_for_services = d.pop("use_for_services", UNSET)

        recurse_use = d.pop("recurse_use", UNSET)

        recurse_perms = d.pop("recurse_perms", UNSET)

        host_contact_group = cls(
            groups=groups,
            use=use,
            use_for_services=use_for_services,
            recurse_use=recurse_use,
            recurse_perms=recurse_perms,
        )

        host_contact_group.additional_properties = d
        return host_contact_group

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
