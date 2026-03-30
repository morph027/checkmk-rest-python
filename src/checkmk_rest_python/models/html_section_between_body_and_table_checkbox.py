from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.html_section_between_body_and_table_checkbox_state import (
    HtmlSectionBetweenBodyAndTableCheckboxState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="HtmlSectionBetweenBodyAndTableCheckbox")


@_attrs_define
class HtmlSectionBetweenBodyAndTableCheckbox:
    """
    Attributes:
        state (HtmlSectionBetweenBodyAndTableCheckboxState | Unset): To enable or disable this field Example: enabled.
        value (str | Unset): Insert HTML section between body and table Example: <HTMLTAG>CONTENT</HTMLTAG>.
    """

    state: HtmlSectionBetweenBodyAndTableCheckboxState | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: HtmlSectionBetweenBodyAndTableCheckboxState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = HtmlSectionBetweenBodyAndTableCheckboxState(_state)

        value = d.pop("value", UNSET)

        html_section_between_body_and_table_checkbox = cls(
            state=state,
            value=value,
        )

        html_section_between_body_and_table_checkbox.additional_properties = d
        return html_section_between_body_and_table_checkbox

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
