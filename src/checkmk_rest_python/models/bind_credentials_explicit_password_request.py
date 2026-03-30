from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BindCredentialsExplicitPasswordRequest")


@_attrs_define
class BindCredentialsExplicitPasswordRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        type_ (Any):  Default: 'explicit'.
        explicit_password (str): An explicit password of the user account which is used to bind to the LDAP server. This
            user account must have read access to the LDAP directory. Example: your_password.
        bind_dn (str | Unset): The distinguished name of the user account which is used to bind to the LDAP server. This
            user account must have read access to the LDAP directory. Default: ''. Example:
            CN=bind_user,OU=users,DC=example,DC=com.
    """

    explicit_password: str
    state: Any = "enabled"
    type_: Any = "explicit"
    bind_dn: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        type_ = self.type_

        explicit_password = self.explicit_password

        bind_dn = self.bind_dn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "type": type_,
                "explicit_password": explicit_password,
            }
        )
        if bind_dn is not UNSET:
            field_dict["bind_dn"] = bind_dn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state")

        type_ = d.pop("type")

        explicit_password = d.pop("explicit_password")

        bind_dn = d.pop("bind_dn", UNSET)

        bind_credentials_explicit_password_request = cls(
            state=state,
            type_=type_,
            explicit_password=explicit_password,
            bind_dn=bind_dn,
        )

        bind_credentials_explicit_password_request.additional_properties = d
        return bind_credentials_explicit_password_request

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
