from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.when_to_bulk_when_to_bulk import WhenToBulkWhenToBulk
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_bulking import NotificationBulking


T = TypeVar("T", bound="WhenToBulk")


@_attrs_define
class WhenToBulk:
    """
    Attributes:
        when_to_bulk (WhenToBulkWhenToBulk | Unset): Bulking can always happen or during a set time period Example:
            always.
        params (NotificationBulking | Unset):
    """

    when_to_bulk: WhenToBulkWhenToBulk | Unset = UNSET
    params: NotificationBulking | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        when_to_bulk: str | Unset = UNSET
        if not isinstance(self.when_to_bulk, Unset):
            when_to_bulk = self.when_to_bulk.value

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if when_to_bulk is not UNSET:
            field_dict["when_to_bulk"] = when_to_bulk
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_bulking import NotificationBulking

        d = dict(src_dict)
        _when_to_bulk = d.pop("when_to_bulk", UNSET)
        when_to_bulk: WhenToBulkWhenToBulk | Unset
        if isinstance(_when_to_bulk, Unset):
            when_to_bulk = UNSET
        else:
            when_to_bulk = WhenToBulkWhenToBulk(_when_to_bulk)

        _params = d.pop("params", UNSET)
        params: NotificationBulking | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = NotificationBulking.from_dict(_params)

        when_to_bulk = cls(
            when_to_bulk=when_to_bulk,
            params=params,
        )

        when_to_bulk.additional_properties = d
        return when_to_bulk

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
