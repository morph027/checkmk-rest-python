from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quick_setup_stage_request_form_data import (
        QuickSetupStageRequestFormData,
    )


T = TypeVar("T", bound="QuickSetupStageRequest")


@_attrs_define
class QuickSetupStageRequest:
    """
    Attributes:
        form_data (QuickSetupStageRequestFormData): The form data entered by the user.
    """

    form_data: QuickSetupStageRequestFormData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_data = self.form_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "form_data": form_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_setup_stage_request_form_data import (
            QuickSetupStageRequestFormData,
        )

        d = dict(src_dict)
        form_data = QuickSetupStageRequestFormData.from_dict(d.pop("form_data"))

        quick_setup_stage_request = cls(
            form_data=form_data,
        )

        quick_setup_stage_request.additional_properties = d
        return quick_setup_stage_request

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
