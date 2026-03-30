from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BindCredentialsStoreIdRequest")


@_attrs_define
class BindCredentialsStoreIdRequest:
    """
    Attributes:
        state (Any): This config parameter is enabled. Default: 'enabled'. Example: enabled.
        type_ (Any):  Default: 'store'.
        password_store_id (str): A password store id from the user account which is used to bind to the LDAP server.
            This user account must have read access to the LDAP directory. Example: your_password_store_id.
        bind_dn (str | Unset): The distinguished name of the user account which is used to bind to the LDAP server. This
            user account must have read access to the LDAP directory. Default: ''. Example:
            CN=bind_user,OU=users,DC=example,DC=com.
    """

    password_store_id: str
    state: Any = "enabled"
    type_: Any = "store"
    bind_dn: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        type_ = self.type_

        password_store_id = self.password_store_id

        bind_dn = self.bind_dn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "type": type_,
                "password_store_id": password_store_id,
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

        password_store_id = d.pop("password_store_id")

        bind_dn = d.pop("bind_dn", UNSET)

        bind_credentials_store_id_request = cls(
            state=state,
            type_=type_,
            password_store_id=password_store_id,
            bind_dn=bind_dn,
        )

        bind_credentials_store_id_request.additional_properties = d
        return bind_credentials_store_id_request

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
