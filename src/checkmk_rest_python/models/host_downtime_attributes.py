from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.fixed_downtime_mode import FixedDowntimeMode
    from ..models.flexible_downtime_mode import FlexibleDowntimeMode


T = TypeVar("T", bound="HostDowntimeAttributes")


@_attrs_define
class HostDowntimeAttributes:
    """
    Attributes:
        site_id (str): The site id of the downtime. Example: mysite.
        host_name (str): The host name. Example: cmk.abc.ch.
        author (str): The author of the downtime. Example: Mr Bojangles.
        start_time (datetime.datetime): The start time of the downtime. Example: 2023-08-04T08:58:01+00:00.
        end_time (datetime.datetime): The end time of the downtime. Example: 2023-08-04T09:18:01+00:00.
        recurring (bool): Indicates if this downtime is time-repetitive Example: True.
        comment (str): A comment text. Example: Down for update.
        mode (FixedDowntimeMode | FlexibleDowntimeMode):
        is_service (Any): Host downtime entry Default: False.
    """

    site_id: str
    host_name: str
    author: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    recurring: bool
    comment: str
    mode: FixedDowntimeMode | FlexibleDowntimeMode
    is_service: Any = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fixed_downtime_mode import FixedDowntimeMode

        site_id = self.site_id

        host_name = self.host_name

        author = self.author

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        recurring = self.recurring

        comment = self.comment

        mode: dict[str, Any]
        if isinstance(self.mode, FixedDowntimeMode):
            mode = self.mode.to_dict()
        else:
            mode = self.mode.to_dict()

        is_service = self.is_service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
                "host_name": host_name,
                "author": author,
                "start_time": start_time,
                "end_time": end_time,
                "recurring": recurring,
                "comment": comment,
                "mode": mode,
                "is_service": is_service,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fixed_downtime_mode import FixedDowntimeMode
        from ..models.flexible_downtime_mode import FlexibleDowntimeMode

        d = dict(src_dict)
        site_id = d.pop("site_id")

        host_name = d.pop("host_name")

        author = d.pop("author")

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        recurring = d.pop("recurring")

        comment = d.pop("comment")

        def _parse_mode(data: object) -> FixedDowntimeMode | FlexibleDowntimeMode:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_downtime_mode_type_0 = FixedDowntimeMode.from_dict(
                    data
                )

                return componentsschemas_downtime_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_downtime_mode_type_1 = FlexibleDowntimeMode.from_dict(
                data
            )

            return componentsschemas_downtime_mode_type_1

        mode = _parse_mode(d.pop("mode"))

        is_service = d.pop("is_service")

        host_downtime_attributes = cls(
            site_id=site_id,
            host_name=host_name,
            author=author,
            start_time=start_time,
            end_time=end_time,
            recurring=recurring,
            comment=comment,
            mode=mode,
            is_service=is_service,
        )

        host_downtime_attributes.additional_properties = d
        return host_downtime_attributes

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
