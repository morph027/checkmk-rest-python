from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activation_site_status import ActivationSiteStatus
    from ..models.changes_fields import ChangesFields


T = TypeVar("T", bound="ActivationExtensionStatusFields")


@_attrs_define
class ActivationExtensionStatusFields:
    """
    Attributes:
        sites (list[str] | Unset): Sites affected by this activation Example: ['site1', 'site2'].
        is_running (bool | Unset): If the activation is still running
        force_foreign_changes (bool | Unset): A boolean flag indicating that even changes which do not originate from
            the user requesting the activation shall be activated
        time_started (datetime.datetime | Unset): The date and time the activation started. Example:
            2023-02-21T17:34:12+00:00.
        changes (list[ChangesFields] | Unset): The changes in this activation
        status_per_site (list[ActivationSiteStatus] | Unset): A list of sites with their activation status. Example:
            [{'site': 'mysite', 'status_text': 'Activating', 'status_details': 'Started at: 15:23:09. Finished at:
            15:23:13.', 'start_time': '2025-01-20T15:23:09.306846+00:00', 'end_time': '2025-01-20T15:23:13.306846+00:00'},
            {'site': 'morgen', 'status_text': 'Activating', 'status_details': 'Started at: 12:45:05. Finished at:
            12:46:12.', 'start_time': '2025-01-20T12:45:05.306846+00:00', 'end_time': '2025-01-20T12:45:12.306846+00:00'}].
    """

    sites: list[str] | Unset = UNSET
    is_running: bool | Unset = UNSET
    force_foreign_changes: bool | Unset = UNSET
    time_started: datetime.datetime | Unset = UNSET
    changes: list[ChangesFields] | Unset = UNSET
    status_per_site: list[ActivationSiteStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites: list[str] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        is_running = self.is_running

        force_foreign_changes = self.force_foreign_changes

        time_started: str | Unset = UNSET
        if not isinstance(self.time_started, Unset):
            time_started = self.time_started.isoformat()

        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        status_per_site: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_per_site, Unset):
            status_per_site = []
            for status_per_site_item_data in self.status_per_site:
                status_per_site_item = status_per_site_item_data.to_dict()
                status_per_site.append(status_per_site_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites
        if is_running is not UNSET:
            field_dict["is_running"] = is_running
        if force_foreign_changes is not UNSET:
            field_dict["force_foreign_changes"] = force_foreign_changes
        if time_started is not UNSET:
            field_dict["time_started"] = time_started
        if changes is not UNSET:
            field_dict["changes"] = changes
        if status_per_site is not UNSET:
            field_dict["status_per_site"] = status_per_site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activation_site_status import ActivationSiteStatus
        from ..models.changes_fields import ChangesFields

        d = dict(src_dict)
        sites = cast(list[str], d.pop("sites", UNSET))

        is_running = d.pop("is_running", UNSET)

        force_foreign_changes = d.pop("force_foreign_changes", UNSET)

        _time_started = d.pop("time_started", UNSET)
        time_started: datetime.datetime | Unset
        if isinstance(_time_started, Unset):
            time_started = UNSET
        else:
            time_started = isoparse(_time_started)

        _changes = d.pop("changes", UNSET)
        changes: list[ChangesFields] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = ChangesFields.from_dict(changes_item_data)

                changes.append(changes_item)

        _status_per_site = d.pop("status_per_site", UNSET)
        status_per_site: list[ActivationSiteStatus] | Unset = UNSET
        if _status_per_site is not UNSET:
            status_per_site = []
            for status_per_site_item_data in _status_per_site:
                status_per_site_item = ActivationSiteStatus.from_dict(
                    status_per_site_item_data
                )

                status_per_site.append(status_per_site_item)

        activation_extension_status_fields = cls(
            sites=sites,
            is_running=is_running,
            force_foreign_changes=force_foreign_changes,
            time_started=time_started,
            changes=changes,
            status_per_site=status_per_site,
        )

        activation_extension_status_fields.additional_properties = d
        return activation_extension_status_fields

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
