from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.background_job_status_1_state import BackgroundJobStatus1State

if TYPE_CHECKING:
    from ..models.job_logs import JobLogs


T = TypeVar("T", bound="BackgroundJobStatus1")


@_attrs_define
class BackgroundJobStatus1:
    """
    Attributes:
        active (bool): This field indicates if the background job is active or not. Example: True.
        state (BackgroundJobStatus1State): This field indicates the current state of the background job. Example:
            initialized.
        logs (JobLogs):
    """

    active: bool
    state: BackgroundJobStatus1State
    logs: JobLogs
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        state = self.state.value

        logs = self.logs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "state": state,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_logs import JobLogs

        d = dict(src_dict)
        active = d.pop("active")

        state = BackgroundJobStatus1State(d.pop("state"))

        logs = JobLogs.from_dict(d.pop("logs"))

        background_job_status_1 = cls(
            active=active,
            state=state,
            logs=logs,
        )

        background_job_status_1.additional_properties = d
        return background_job_status_1

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
