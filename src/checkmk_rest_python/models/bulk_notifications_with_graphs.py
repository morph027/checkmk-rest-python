from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_notifications_with_graphs_state import (
    BulkNotificationsWithGraphsState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkNotificationsWithGraphs")


@_attrs_define
class BulkNotificationsWithGraphs:
    """
    Attributes:
        value (int): Sets a limit for the number of notifications in a bulk for which graphs are displayed. If you do
            not use bulk notifications this option is ignored. Note that each graph increases the size of the mail and takes
            time to renderon the monitoring server. Therefore, large bulks may exceed the maximum size for attachements or
            the plug-in may run into a timeout so that a failed notification is produced Example: 5.
        state (BulkNotificationsWithGraphsState | Unset): To enable or disable this field Example: enabled.
    """

    value: int
    state: BulkNotificationsWithGraphsState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        _state = d.pop("state", UNSET)
        state: BulkNotificationsWithGraphsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BulkNotificationsWithGraphsState(_state)

        bulk_notifications_with_graphs = cls(
            value=value,
            state=state,
        )

        bulk_notifications_with_graphs.additional_properties = d
        return bulk_notifications_with_graphs

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
