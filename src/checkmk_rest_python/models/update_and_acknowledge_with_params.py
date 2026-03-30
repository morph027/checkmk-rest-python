from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_and_acknowledge_with_params_filter_type import (
    UpdateAndAcknowledgeWithParamsFilterType,
)
from ..models.update_and_acknowledge_with_params_phase import (
    UpdateAndAcknowledgeWithParamsPhase,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_params_update_and_acknowledge import (
        FilterParamsUpdateAndAcknowledge,
    )


T = TypeVar("T", bound="UpdateAndAcknowledgeWithParams")


@_attrs_define
class UpdateAndAcknowledgeWithParams:
    """
    Attributes:
        filter_type (UpdateAndAcknowledgeWithParamsFilterType): The way you would like to filter events. Example: all.
        filters (FilterParamsUpdateAndAcknowledge):
        phase (UpdateAndAcknowledgeWithParamsPhase | Unset): To change the phase of an event Default:
            UpdateAndAcknowledgeWithParamsPhase.ACK. Example: ack.
        change_comment (str | Unset): Event comment. Example: Comment now acked.
        change_contact (str | Unset): Contact information. Example: Mr Monitor.
        site_id (str | Unset): An existing site id Example: mysite.
    """

    filter_type: UpdateAndAcknowledgeWithParamsFilterType
    filters: FilterParamsUpdateAndAcknowledge
    phase: UpdateAndAcknowledgeWithParamsPhase | Unset = (
        UpdateAndAcknowledgeWithParamsPhase.ACK
    )
    change_comment: str | Unset = UNSET
    change_contact: str | Unset = UNSET
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_type = self.filter_type.value

        filters = self.filters.to_dict()

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        change_comment = self.change_comment

        change_contact = self.change_contact

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter_type": filter_type,
                "filters": filters,
            }
        )
        if phase is not UNSET:
            field_dict["phase"] = phase
        if change_comment is not UNSET:
            field_dict["change_comment"] = change_comment
        if change_contact is not UNSET:
            field_dict["change_contact"] = change_contact
        if site_id is not UNSET:
            field_dict["site_id"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_params_update_and_acknowledge import (
            FilterParamsUpdateAndAcknowledge,
        )

        d = dict(src_dict)
        filter_type = UpdateAndAcknowledgeWithParamsFilterType(d.pop("filter_type"))

        filters = FilterParamsUpdateAndAcknowledge.from_dict(d.pop("filters"))

        _phase = d.pop("phase", UNSET)
        phase: UpdateAndAcknowledgeWithParamsPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = UpdateAndAcknowledgeWithParamsPhase(_phase)

        change_comment = d.pop("change_comment", UNSET)

        change_contact = d.pop("change_contact", UNSET)

        site_id = d.pop("site_id", UNSET)

        update_and_acknowledge_with_params = cls(
            filter_type=filter_type,
            filters=filters,
            phase=phase,
            change_comment=change_comment,
            change_contact=change_contact,
            site_id=site_id,
        )

        update_and_acknowledge_with_params.additional_properties = d
        return update_and_acknowledge_with_params

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
