from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPAddressRange")


@_attrs_define
class IPAddressRange:
    """
    Attributes:
        type_ (Any | Unset): A range of addresses. Default: 'ip_range'.
        from_address (str | Unset): The first IPv4 address of this range.
        to_address (str | Unset): The last IPv4 address of this range.
    """

    type_: Any | Unset = "ip_range"
    from_address: str | Unset = UNSET
    to_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        from_address = self.from_address

        to_address = self.to_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if from_address is not UNSET:
            field_dict["from_address"] = from_address
        if to_address is not UNSET:
            field_dict["to_address"] = to_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        from_address = d.pop("from_address", UNSET)

        to_address = d.pop("to_address", UNSET)

        ip_address_range = cls(
            type_=type_,
            from_address=from_address,
            to_address=to_address,
        )

        ip_address_range.additional_properties = d
        return ip_address_range

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
