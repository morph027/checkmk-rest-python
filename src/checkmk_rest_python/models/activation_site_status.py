from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activation_site_status_phase import ActivationSiteStatusPhase
from ..models.activation_site_status_state import ActivationSiteStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivationSiteStatus")


@_attrs_define
class ActivationSiteStatus:
    """
    Attributes:
        site (str | Unset): The site affected by this activation Example: mysite.
        phase (ActivationSiteStatusPhase | Unset): The phase Example: done.
        state (ActivationSiteStatusState | Unset): The state Example: success.
        status_text (None | str | Unset): The status text Example: Activating.
        status_details (str | Unset): The status details Example: Started at: 15:23:10. Finished at: 15:23:12..
        start_time (datetime.datetime | Unset): The date and time the activation started. Example:
            2025-03-03T17:31:24+00:00.
        end_time (datetime.datetime | None | Unset): The date and time the activation ended. Example:
            2023-03-03T17:31:41+00:00.
    """

    site: str | Unset = UNSET
    phase: ActivationSiteStatusPhase | Unset = UNSET
    state: ActivationSiteStatusState | Unset = UNSET
    status_text: None | str | Unset = UNSET
    status_details: str | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        status_text: None | str | Unset
        if isinstance(self.status_text, Unset):
            status_text = UNSET
        else:
            status_text = self.status_text

        status_details = self.status_details

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if phase is not UNSET:
            field_dict["phase"] = phase
        if state is not UNSET:
            field_dict["state"] = state
        if status_text is not UNSET:
            field_dict["status_text"] = status_text
        if status_details is not UNSET:
            field_dict["status_details"] = status_details
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site = d.pop("site", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: ActivationSiteStatusPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = ActivationSiteStatusPhase(_phase)

        _state = d.pop("state", UNSET)
        state: ActivationSiteStatusState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ActivationSiteStatusState(_state)

        def _parse_status_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_text = _parse_status_text(d.pop("status_text", UNSET))

        status_details = d.pop("status_details", UNSET)

        _start_time = d.pop("start_time", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        activation_site_status = cls(
            site=site,
            phase=phase,
            state=state,
            status_text=status_text,
            status_details=status_details,
            start_time=start_time,
            end_time=end_time,
        )

        activation_site_status.additional_properties = d
        return activation_site_status

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
