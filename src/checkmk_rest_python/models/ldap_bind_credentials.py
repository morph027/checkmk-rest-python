from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_bind_credentials_state import LDAPBindCredentialsState
from ..models.ldap_bind_credentials_type import LDAPBindCredentialsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDAPBindCredentials")


@_attrs_define
class LDAPBindCredentials:
    """
    Attributes:
        state (LDAPBindCredentialsState | Unset):  Example: enabled.
        type_ (LDAPBindCredentialsType | Unset): A specific password or a password store id Example: explicit.
        bind_dn (str | Unset): The distinguished name of the user account which is used to bind to the LDAP server. This
            user account must have read access to the LDAP directory. Example: CN=bind_user,OU=users,DC=example,DC=com.
        explicit_password (str | Unset): An explicit password of the user account which is used to bind to the LDAP
            server. This user account must have read access to the LDAP directory. Example: your_password.
        password_store_id (str | Unset): A password store id from the user account which is used to bind to the LDAP
            server. This user account must have read access to the LDAP directory.
    """

    state: LDAPBindCredentialsState | Unset = UNSET
    type_: LDAPBindCredentialsType | Unset = UNSET
    bind_dn: str | Unset = UNSET
    explicit_password: str | Unset = UNSET
    password_store_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        bind_dn = self.bind_dn

        explicit_password = self.explicit_password

        password_store_id = self.password_store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if bind_dn is not UNSET:
            field_dict["bind_dn"] = bind_dn
        if explicit_password is not UNSET:
            field_dict["explicit_password"] = explicit_password
        if password_store_id is not UNSET:
            field_dict["password_store_id"] = password_store_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: LDAPBindCredentialsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = LDAPBindCredentialsState(_state)

        _type_ = d.pop("type", UNSET)
        type_: LDAPBindCredentialsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LDAPBindCredentialsType(_type_)

        bind_dn = d.pop("bind_dn", UNSET)

        explicit_password = d.pop("explicit_password", UNSET)

        password_store_id = d.pop("password_store_id", UNSET)

        ldap_bind_credentials = cls(
            state=state,
            type_=type_,
            bind_dn=bind_dn,
            explicit_password=explicit_password,
            password_store_id=password_store_id,
        )

        ldap_bind_credentials.additional_properties = d
        return ldap_bind_credentials

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
