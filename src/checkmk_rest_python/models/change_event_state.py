from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_event_state_new_state import ChangeEventStateNewState

T = TypeVar("T", bound="ChangeEventState")


@_attrs_define
class ChangeEventState:
    """
    Attributes:
        site_id (str): An existing site id Example: mysite.
        new_state (ChangeEventStateNewState): The state Example: ok.
    """

    site_id: str
    new_state: ChangeEventStateNewState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        new_state = self.new_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
                "new_state": new_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        new_state = ChangeEventStateNewState(d.pop("new_state"))

        change_event_state = cls(
            site_id=site_id,
            new_state=new_state,
        )

        change_event_state.additional_properties = d
        return change_event_state

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
