from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangesFields")


@_attrs_define
class ChangesFields:
    """
    Attributes:
        id (UUID | Unset): The change identifier Example: ad9c9b13-52f2-4fb8-8f4f-7b2ae48c7984.
        user_id (None | str | Unset): The user who made the change Example: cmkadmin.
        action_name (str | Unset): The action carried out Example: edit-host.
        text (str | Unset):  Example: Modified host myhost..
        time (datetime.datetime | Unset): The date and time the change was made. Example: 2023-02-21T17:32:28+00:00.
    """

    id: UUID | Unset = UNSET
    user_id: None | str | Unset = UNSET
    action_name: str | Unset = UNSET
    text: str | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        action_name = self.action_name

        text = self.text

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if action_name is not UNSET:
            field_dict["action_name"] = action_name
        if text is not UNSET:
            field_dict["text"] = text
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        action_name = d.pop("action_name", UNSET)

        text = d.pop("text", UNSET)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        changes_fields = cls(
            id=id,
            user_id=user_id,
            action_name=action_name,
            text=text,
            time=time,
        )

        changes_fields.additional_properties = d
        return changes_fields

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
