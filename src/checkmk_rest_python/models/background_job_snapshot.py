from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.background_job_status import BackgroundJobStatus


T = TypeVar("T", bound="BackgroundJobSnapshot")


@_attrs_define
class BackgroundJobSnapshot:
    """
    Attributes:
        site_id (str): The site ID where the background job is located Example: foobar.
        active (bool): This field indicates if the background job is running. Example: True.
        status (BackgroundJobStatus | Unset):
    """

    site_id: str
    active: bool
    status: BackgroundJobStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        active = self.active

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
                "active": active,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.background_job_status import BackgroundJobStatus

        d = dict(src_dict)
        site_id = d.pop("site_id")

        active = d.pop("active")

        _status = d.pop("status", UNSET)
        status: BackgroundJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackgroundJobStatus.from_dict(_status)

        background_job_snapshot = cls(
            site_id=site_id,
            active=active,
            status=status,
        )

        background_job_snapshot.additional_properties = d
        return background_job_snapshot

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
