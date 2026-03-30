from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusLogInfo")


@_attrs_define
class StatusLogInfo:
    """
    Attributes:
        job_progress_update (list[str] | Unset): The progress update logs of the background job Example: ['Parsed
            configuration', 'Saved configuration'].
        job_result (list[str] | Unset): The result logs of the background job Example: ['Job finished'].
        job_exception (list[str] | Unset): The exception logs of the background job Example: ['error_1', 'error_2'].
    """

    job_progress_update: list[str] | Unset = UNSET
    job_result: list[str] | Unset = UNSET
    job_exception: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_progress_update: list[str] | Unset = UNSET
        if not isinstance(self.job_progress_update, Unset):
            job_progress_update = self.job_progress_update

        job_result: list[str] | Unset = UNSET
        if not isinstance(self.job_result, Unset):
            job_result = self.job_result

        job_exception: list[str] | Unset = UNSET
        if not isinstance(self.job_exception, Unset):
            job_exception = self.job_exception

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_progress_update is not UNSET:
            field_dict["JobProgressUpdate"] = job_progress_update
        if job_result is not UNSET:
            field_dict["JobResult"] = job_result
        if job_exception is not UNSET:
            field_dict["JobException"] = job_exception

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_progress_update = cast(list[str], d.pop("JobProgressUpdate", UNSET))

        job_result = cast(list[str], d.pop("JobResult", UNSET))

        job_exception = cast(list[str], d.pop("JobException", UNSET))

        status_log_info = cls(
            job_progress_update=job_progress_update,
            job_result=job_result,
            job_exception=job_exception,
        )

        status_log_info.additional_properties = d
        return status_log_info

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
