from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enable_synchronous_delivery_via_smtp_encryption import (
    EnableSynchronousDeliveryViaSMTPEncryption,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication_value import AuthenticationValue
    from ..models.checkbox import Checkbox


T = TypeVar("T", bound="EnableSynchronousDeliveryViaSMTP")


@_attrs_define
class EnableSynchronousDeliveryViaSMTP:
    """
    Attributes:
        auth (AuthenticationValue | Checkbox | Unset):
        encryption (EnableSynchronousDeliveryViaSMTPEncryption | Unset): The encryption type for the SMTP connection.
            Example: ssl_tls.
        port (int | Unset):  Example: 25.
        smarthosts (list[str] | Unset):
    """

    auth: AuthenticationValue | Checkbox | Unset = UNSET
    encryption: EnableSynchronousDeliveryViaSMTPEncryption | Unset = UNSET
    port: int | Unset = UNSET
    smarthosts: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        auth: dict[str, Any] | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, Checkbox):
            auth = self.auth.to_dict()
        else:
            auth = self.auth.to_dict()

        encryption: str | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        port = self.port

        smarthosts: list[str] | Unset = UNSET
        if not isinstance(self.smarthosts, Unset):
            smarthosts = self.smarthosts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if port is not UNSET:
            field_dict["port"] = port
        if smarthosts is not UNSET:
            field_dict["smarthosts"] = smarthosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication_value import AuthenticationValue
        from ..models.checkbox import Checkbox

        d = dict(src_dict)

        def _parse_auth(data: object) -> AuthenticationValue | Checkbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_auth_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_auth_one_of_type_1 = AuthenticationValue.from_dict(data)

            return componentsschemas_auth_one_of_type_1

        auth = _parse_auth(d.pop("auth", UNSET))

        _encryption = d.pop("encryption", UNSET)
        encryption: EnableSynchronousDeliveryViaSMTPEncryption | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = EnableSynchronousDeliveryViaSMTPEncryption(_encryption)

        port = d.pop("port", UNSET)

        smarthosts = cast(list[str], d.pop("smarthosts", UNSET))

        enable_synchronous_delivery_via_smtp = cls(
            auth=auth,
            encryption=encryption,
            port=port,
            smarthosts=smarthosts,
        )

        enable_synchronous_delivery_via_smtp.additional_properties = d
        return enable_synchronous_delivery_via_smtp

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
