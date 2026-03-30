from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickSetupStageOverviewResponse")


@_attrs_define
class QuickSetupStageOverviewResponse:
    """
    Attributes:
        title (str | Unset): The title of a stage Example: Prepare AWS for Checkmk.
        sub_title (None | str | Unset): The sub-title of a stage Example: aws.
    """

    title: str | Unset = UNSET
    sub_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        sub_title: None | str | Unset
        if isinstance(self.sub_title, Unset):
            sub_title = UNSET
        else:
            sub_title = self.sub_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if sub_title is not UNSET:
            field_dict["sub_title"] = sub_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_sub_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_title = _parse_sub_title(d.pop("sub_title", UNSET))

        quick_setup_stage_overview_response = cls(
            title=title,
            sub_title=sub_title,
        )

        quick_setup_stage_overview_response.additional_properties = d
        return quick_setup_stage_overview_response

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
