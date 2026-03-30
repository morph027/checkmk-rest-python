from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_user_role_new_permissions_additional_property import (
    EditUserRoleNewPermissionsAdditionalProperty,
)

T = TypeVar("T", bound="EditUserRoleNewPermissions")


@_attrs_define
class EditUserRoleNewPermissions:
    """A map of permission names to their state.  The following values can be set: 'yes' - the permission is active for
    this role.'no' - the permission is deactivated for this role, even if it was active in the role it was based
    on.'default' - takes the activation state from the role this role was based on.

        Example:
            {'general.edit_profile': 'yes', 'general.message': 'no'}

    """

    additional_properties: dict[str, EditUserRoleNewPermissionsAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        edit_user_role_new_permissions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = EditUserRoleNewPermissionsAdditionalProperty(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        edit_user_role_new_permissions.additional_properties = additional_properties
        return edit_user_role_new_permissions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> EditUserRoleNewPermissionsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: EditUserRoleNewPermissionsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
