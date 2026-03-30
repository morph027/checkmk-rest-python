from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snm_pv_3_auth_privacy_auth_protocol import SNMPv3AuthPrivacyAuthProtocol
from ..models.snm_pv_3_auth_privacy_privacy_protocol import (
    SNMPv3AuthPrivacyPrivacyProtocol,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SNMPv3AuthPrivacy")


@_attrs_define
class SNMPv3AuthPrivacy:
    """
    Attributes:
        auth_protocol (SNMPv3AuthPrivacyAuthProtocol): Authentication protocol.
        security_name (str): Security name
        auth_password (str): Authentication pass phrase.
        privacy_protocol (SNMPv3AuthPrivacyPrivacyProtocol): The privacy protocol. The only supported values in the Raw
            Edition are CBC-DES and AES-128. If selected, privacy_password needs to be supplied as well.
        privacy_password (str): Privacy pass phrase. If filled, privacy_protocol needs to be selected as well.
        type_ (Any | Unset): SNMPv3 with authentication and privacy. Default: 'authPriv'.
    """

    auth_protocol: SNMPv3AuthPrivacyAuthProtocol
    security_name: str
    auth_password: str
    privacy_protocol: SNMPv3AuthPrivacyPrivacyProtocol
    privacy_password: str
    type_: Any | Unset = "authPriv"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_protocol = self.auth_protocol.value

        security_name = self.security_name

        auth_password = self.auth_password

        privacy_protocol = self.privacy_protocol.value

        privacy_password = self.privacy_password

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_protocol": auth_protocol,
                "security_name": security_name,
                "auth_password": auth_password,
                "privacy_protocol": privacy_protocol,
                "privacy_password": privacy_password,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_protocol = SNMPv3AuthPrivacyAuthProtocol(d.pop("auth_protocol"))

        security_name = d.pop("security_name")

        auth_password = d.pop("auth_password")

        privacy_protocol = SNMPv3AuthPrivacyPrivacyProtocol(d.pop("privacy_protocol"))

        privacy_password = d.pop("privacy_password")

        type_ = d.pop("type", UNSET)

        snm_pv_3_auth_privacy = cls(
            auth_protocol=auth_protocol,
            security_name=security_name,
            auth_password=auth_password,
            privacy_protocol=privacy_protocol,
            privacy_password=privacy_password,
            type_=type_,
        )

        snm_pv_3_auth_privacy.additional_properties = d
        return snm_pv_3_auth_privacy

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
