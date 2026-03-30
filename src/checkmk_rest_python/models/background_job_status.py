from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_log_info import StatusLogInfo


T = TypeVar("T", bound="BackgroundJobStatus")


@_attrs_define
class BackgroundJobStatus:
    """
    Attributes:
        state (str): The state of the background job Example: finished.
        log_info (StatusLogInfo | Unset):
    """

    state: str
    log_info: StatusLogInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        log_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_info, Unset):
            log_info = self.log_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if log_info is not UNSET:
            field_dict["log_info"] = log_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_log_info import StatusLogInfo

        d = dict(src_dict)
        state = d.pop("state")

        _log_info = d.pop("log_info", UNSET)
        log_info: StatusLogInfo | Unset
        if isinstance(_log_info, Unset):
            log_info = UNSET
        else:
            log_info = StatusLogInfo.from_dict(_log_info)

        background_job_status = cls(
            state=state,
            log_info=log_info,
        )

        background_job_status.additional_properties = d
        return background_job_status

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
