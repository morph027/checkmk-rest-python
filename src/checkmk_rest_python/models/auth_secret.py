from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_secret_auth_type import AuthSecretAuthType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthSecret")


@_attrs_define
class AuthSecret:
    """
    Attributes:
        auth_type (AuthSecretAuthType | Unset): The authentication type Example: password.
        secret (str | Unset): For accounts used by automation processes (such as fetching data from views for further
            procession). This is the automation secret Example: DEYQEQQPYCFFBYH@AVMC.
        store_automation_secret (bool | Unset): If set to True, the secret will be stored unhashed in order to reuse it
            in rules. Default: False.
    """

    auth_type: AuthSecretAuthType | Unset = UNSET
    secret: str | Unset = UNSET
    store_automation_secret: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        secret = self.secret

        store_automation_secret = self.store_automation_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if secret is not UNSET:
            field_dict["secret"] = secret
        if store_automation_secret is not UNSET:
            field_dict["store_automation_secret"] = store_automation_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_type = d.pop("auth_type", UNSET)
        auth_type: AuthSecretAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = AuthSecretAuthType(_auth_type)

        secret = d.pop("secret", UNSET)

        store_automation_secret = d.pop("store_automation_secret", UNSET)

        auth_secret = cls(
            auth_type=auth_type,
            secret=secret,
            store_automation_secret=store_automation_secret,
        )

        auth_secret.additional_properties = d
        return auth_secret

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
