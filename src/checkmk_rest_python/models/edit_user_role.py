from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_user_role_new_permissions import EditUserRoleNewPermissions


T = TypeVar("T", bound="EditUserRole")


@_attrs_define
class EditUserRole:
    """
    Attributes:
        new_role_id (str | Unset): New role_id for the userrole that must be unique. Example: new_userrole_id.
        new_alias (str | Unset): New alias for the userrole that must be unique. Example: new_userrole_alias.
        new_basedon (str | Unset): A built-in user role that you want the user role to be based on. Example: guest.
        new_permissions (EditUserRoleNewPermissions | Unset): A map of permission names to their state.  The following
            values can be set: 'yes' - the permission is active for this role.'no' - the permission is deactivated for this
            role, even if it was active in the role it was based on.'default' - takes the activation state from the role
            this role was based on.  Example: {'general.edit_profile': 'yes', 'general.message': 'no'}.
    """

    new_role_id: str | Unset = UNSET
    new_alias: str | Unset = UNSET
    new_basedon: str | Unset = UNSET
    new_permissions: EditUserRoleNewPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_role_id = self.new_role_id

        new_alias = self.new_alias

        new_basedon = self.new_basedon

        new_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_permissions, Unset):
            new_permissions = self.new_permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_role_id is not UNSET:
            field_dict["new_role_id"] = new_role_id
        if new_alias is not UNSET:
            field_dict["new_alias"] = new_alias
        if new_basedon is not UNSET:
            field_dict["new_basedon"] = new_basedon
        if new_permissions is not UNSET:
            field_dict["new_permissions"] = new_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_user_role_new_permissions import EditUserRoleNewPermissions

        d = dict(src_dict)
        new_role_id = d.pop("new_role_id", UNSET)

        new_alias = d.pop("new_alias", UNSET)

        new_basedon = d.pop("new_basedon", UNSET)

        _new_permissions = d.pop("new_permissions", UNSET)
        new_permissions: EditUserRoleNewPermissions | Unset
        if isinstance(_new_permissions, Unset):
            new_permissions = UNSET
        else:
            new_permissions = EditUserRoleNewPermissions.from_dict(_new_permissions)

        edit_user_role = cls(
            new_role_id=new_role_id,
            new_alias=new_alias,
            new_basedon=new_basedon,
            new_permissions=new_permissions,
        )

        edit_user_role.additional_properties = d
        return edit_user_role

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
