from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserRole")


@_attrs_define
class CreateUserRole:
    """
    Attributes:
        role_id (str): Existing userrole that you want to clone. Example: admin.
        new_role_id (str | Unset): The new role id for the newly created user role. Example: limited_permissions_user.
        new_alias (str | Unset): A new alias that you want to give to the newly created user role. Example: user_a.
    """

    role_id: str
    new_role_id: str | Unset = UNSET
    new_alias: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        new_role_id = self.new_role_id

        new_alias = self.new_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_id": role_id,
            }
        )
        if new_role_id is not UNSET:
            field_dict["new_role_id"] = new_role_id
        if new_alias is not UNSET:
            field_dict["new_alias"] = new_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role_id = d.pop("role_id")

        new_role_id = d.pop("new_role_id", UNSET)

        new_alias = d.pop("new_alias", UNSET)

        create_user_role = cls(
            role_id=role_id,
            new_role_id=new_role_id,
            new_alias=new_alias,
        )

        create_user_role.additional_properties = d
        return create_user_role

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
