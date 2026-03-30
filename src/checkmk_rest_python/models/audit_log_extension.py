from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogExtension")


@_attrs_define
class AuditLogExtension:
    """
    Attributes:
        time (int | Unset): Timestamp of when the event occurred
        user_id (str | Unset): User id of whom provoked the event
        action (str | Unset): Action that was performed
        summary (str | Unset): Summary of the event
        details (str | Unset): Details of the event
        object_type (None | str | Unset): Object type associated to the event
        object_name (None | str | Unset): Object name associated to the event
    """

    time: int | Unset = UNSET
    user_id: str | Unset = UNSET
    action: str | Unset = UNSET
    summary: str | Unset = UNSET
    details: str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    object_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        user_id = self.user_id

        action = self.action

        summary = self.summary

        details = self.details

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        object_name: None | str | Unset
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if action is not UNSET:
            field_dict["action"] = action
        if summary is not UNSET:
            field_dict["summary"] = summary
        if details is not UNSET:
            field_dict["details"] = details
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if object_name is not UNSET:
            field_dict["object_name"] = object_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        user_id = d.pop("user_id", UNSET)

        action = d.pop("action", UNSET)

        summary = d.pop("summary", UNSET)

        details = d.pop("details", UNSET)

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_object_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_name = _parse_object_name(d.pop("object_name", UNSET))

        audit_log_extension = cls(
            time=time,
            user_id=user_id,
            action=action,
            summary=summary,
            details=details,
            object_type=object_type,
            object_name=object_name,
        )

        audit_log_extension.additional_properties = d
        return audit_log_extension

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
