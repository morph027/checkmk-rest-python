from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ilert_password_store_id_option import IlertPasswordStoreIDOption

T = TypeVar("T", bound="IlertPasswordStoreID")


@_attrs_define
class IlertPasswordStoreID:
    """
    Attributes:
        option (IlertPasswordStoreIDOption):  Example: store.
        store_id (str): A password store ID Example: stored_password_1.
    """

    option: IlertPasswordStoreIDOption
    store_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        store_id = self.store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "store_id": store_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = IlertPasswordStoreIDOption(d.pop("option"))

        store_id = d.pop("store_id")

        ilert_password_store_id = cls(
            option=option,
            store_id=store_id,
        )

        ilert_password_store_id.additional_properties = d
        return ilert_password_store_id

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
