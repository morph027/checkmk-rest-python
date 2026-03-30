from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserContactOption")


@_attrs_define
class UserContactOption:
    """
    Attributes:
        email (str): The mail address of the user. Required if the user is a monitoringcontact and receives
            notifications via mail. Example: user@example.com.
        fallback_contact (bool | Unset): In case none of your notification rules handles a certain event a notification
            will be sent to the specified email Default: False.
    """

    email: str
    fallback_contact: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        fallback_contact = self.fallback_contact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if fallback_contact is not UNSET:
            field_dict["fallback_contact"] = fallback_contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        fallback_contact = d.pop("fallback_contact", UNSET)

        user_contact_option = cls(
            email=email,
            fallback_contact=fallback_contact,
        )

        user_contact_option.additional_properties = d
        return user_contact_option

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
