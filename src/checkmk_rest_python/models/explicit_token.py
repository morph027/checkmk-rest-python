from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.explicit_token_option import ExplicitTokenOption

T = TypeVar("T", bound="ExplicitToken")


@_attrs_define
class ExplicitToken:
    """
    Attributes:
        option (ExplicitTokenOption):  Example: password_store_id.
        token (str): Your personal access token Example: token_example.
    """

    option: ExplicitTokenOption
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = ExplicitTokenOption(d.pop("option"))

        token = d.pop("token")

        explicit_token = cls(
            option=option,
            token=token,
        )

        explicit_token.additional_properties = d
        return explicit_token

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
