from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_setup_button import QuickSetupButton


T = TypeVar("T", bound="Action")


@_attrs_define
class Action:
    """
    Attributes:
        id (str | Unset): The action id Example: action.
        button (QuickSetupButton | Unset):
        load_wait_label (str | Unset): A string to display while waiting for the next stage Example: Please wait....
    """

    id: str | Unset = UNSET
    button: QuickSetupButton | Unset = UNSET
    load_wait_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        button: dict[str, Any] | Unset = UNSET
        if not isinstance(self.button, Unset):
            button = self.button.to_dict()

        load_wait_label = self.load_wait_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if button is not UNSET:
            field_dict["button"] = button
        if load_wait_label is not UNSET:
            field_dict["load_wait_label"] = load_wait_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_setup_button import QuickSetupButton

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _button = d.pop("button", UNSET)
        button: QuickSetupButton | Unset
        if isinstance(_button, Unset):
            button = UNSET
        else:
            button = QuickSetupButton.from_dict(_button)

        load_wait_label = d.pop("load_wait_label", UNSET)

        action = cls(
            id=id,
            button=button,
            load_wait_label=load_wait_label,
        )

        action.additional_properties = d
        return action

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
