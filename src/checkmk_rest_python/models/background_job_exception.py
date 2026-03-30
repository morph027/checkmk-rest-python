from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackgroundJobException")


@_attrs_define
class BackgroundJobException:
    """
    Attributes:
        message (str | Unset): The exception message Example: An exception message.
        traceback (str | Unset): The traceback of the exception Example: The traceback of the background job exception.
    """

    message: str | Unset = UNSET
    traceback: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        traceback = self.traceback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if traceback is not UNSET:
            field_dict["traceback"] = traceback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        traceback = d.pop("traceback", UNSET)

        background_job_exception = cls(
            message=message,
            traceback=traceback,
        )

        background_job_exception.additional_properties = d
        return background_job_exception

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
