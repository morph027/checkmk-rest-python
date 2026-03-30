from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authentication_method import AuthenticationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="Authentication")


@_attrs_define
class Authentication:
    """
    Attributes:
        method (AuthenticationMethod | Unset): The authentication method is fixed at 'plaintext' for now. Default:
            AuthenticationMethod.PLAINTEXT. Example: plaintext.
        user (str | Unset): The username for the SMTP connection. Default: ''. Example: user_1.
        password (str | Unset): The password for the SMTP connection. Default: ''. Example: password.
    """

    method: AuthenticationMethod | Unset = AuthenticationMethod.PLAINTEXT
    user: str | Unset = ""
    password: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        user = self.user

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if user is not UNSET:
            field_dict["user"] = user
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: AuthenticationMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = AuthenticationMethod(_method)

        user = d.pop("user", UNSET)

        password = d.pop("password", UNSET)

        authentication = cls(
            method=method,
            user=user,
            password=password,
        )

        authentication.additional_properties = d
        return authentication

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
