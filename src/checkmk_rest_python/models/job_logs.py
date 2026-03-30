from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobLogs")


@_attrs_define
class JobLogs:
    """
    Attributes:
        result (list[str] | Unset): The list of result related logs
        progress (list[str] | Unset): The list of progress related logs
    """

    result: list[str] | Unset = UNSET
    progress: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result: list[str] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result

        progress: list[str] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = cast(list[str], d.pop("result", UNSET))

        progress = cast(list[str], d.pop("progress", UNSET))

        job_logs = cls(
            result=result,
            progress=progress,
        )

        job_logs.additional_properties = d
        return job_logs

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
