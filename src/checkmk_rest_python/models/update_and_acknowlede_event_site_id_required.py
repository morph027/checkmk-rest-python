from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_and_acknowlede_event_site_id_required_phase import (
    UpdateAndAcknowledeEventSiteIDRequiredPhase,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAndAcknowledeEventSiteIDRequired")


@_attrs_define
class UpdateAndAcknowledeEventSiteIDRequired:
    """
    Attributes:
        site_id (str): An existing site id Example: mysite.
        phase (UpdateAndAcknowledeEventSiteIDRequiredPhase | Unset): To change the phase of an event Default:
            UpdateAndAcknowledeEventSiteIDRequiredPhase.ACK. Example: ack.
        change_comment (str | Unset): Event comment. Example: Comment now acked.
        change_contact (str | Unset): Contact information. Example: Mr Monitor.
    """

    site_id: str
    phase: UpdateAndAcknowledeEventSiteIDRequiredPhase | Unset = (
        UpdateAndAcknowledeEventSiteIDRequiredPhase.ACK
    )
    change_comment: str | Unset = UNSET
    change_contact: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        change_comment = self.change_comment

        change_contact = self.change_contact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
            }
        )
        if phase is not UNSET:
            field_dict["phase"] = phase
        if change_comment is not UNSET:
            field_dict["change_comment"] = change_comment
        if change_contact is not UNSET:
            field_dict["change_contact"] = change_contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        _phase = d.pop("phase", UNSET)
        phase: UpdateAndAcknowledeEventSiteIDRequiredPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = UpdateAndAcknowledeEventSiteIDRequiredPhase(_phase)

        change_comment = d.pop("change_comment", UNSET)

        change_contact = d.pop("change_contact", UNSET)

        update_and_acknowlede_event_site_id_required = cls(
            site_id=site_id,
            phase=phase,
            change_comment=change_comment,
            change_contact=change_contact,
        )

        update_and_acknowlede_event_site_id_required.additional_properties = d
        return update_and_acknowlede_event_site_id_required

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
