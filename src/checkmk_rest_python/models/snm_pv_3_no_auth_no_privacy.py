from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SNMPv3NoAuthNoPrivacy")


@_attrs_define
class SNMPv3NoAuthNoPrivacy:
    """
    Attributes:
        security_name (str): Security name
        type_ (Any | Unset): The type of credentials to use. Default: 'noAuthNoPriv'.
    """

    security_name: str
    type_: Any | Unset = "noAuthNoPriv"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_name = self.security_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "security_name": security_name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_name = d.pop("security_name")

        type_ = d.pop("type", UNSET)

        snm_pv_3_no_auth_no_privacy = cls(
            security_name=security_name,
            type_=type_,
        )

        snm_pv_3_no_auth_no_privacy.additional_properties = d
        return snm_pv_3_no_auth_no_privacy

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
