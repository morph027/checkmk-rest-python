from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.acknowledge_host_group_problem_acknowledge_type import (
    AcknowledgeHostGroupProblemAcknowledgeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AcknowledgeHostGroupProblem")


@_attrs_define
class AcknowledgeHostGroupProblem:
    """
    Attributes:
        comment (str): Comment to be stored alongside the acknowledgement. Example: This was expected..
        acknowledge_type (AcknowledgeHostGroupProblemAcknowledgeType): Select all hosts in a host group. Example:
            hostgroup.
        hostgroup_name (str): Host group name for which this acknowledgement is for. Example: Servers.
        sticky (bool | Unset): If set, only a state-change to the UP/OK state will discard the acknowledgement.
            Otherwise, it will be discarded on any state-change. Default: True.
        persistent (bool | Unset): If set, the comment will persist a restart. Default: False.
        notify (bool | Unset): If set, notifications will be sent out to the configured contacts. Default: True.
        expire_on (datetime.datetime | Unset): If set, the acknowledgement will expire at this time. The timezone will
            default to UTC. Example: 2025-05-20T07:30:00Z.
    """

    comment: str
    acknowledge_type: AcknowledgeHostGroupProblemAcknowledgeType
    hostgroup_name: str
    sticky: bool | Unset = True
    persistent: bool | Unset = False
    notify: bool | Unset = True
    expire_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        acknowledge_type = self.acknowledge_type.value

        hostgroup_name = self.hostgroup_name

        sticky = self.sticky

        persistent = self.persistent

        notify = self.notify

        expire_on: str | Unset = UNSET
        if not isinstance(self.expire_on, Unset):
            expire_on = self.expire_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "acknowledge_type": acknowledge_type,
                "hostgroup_name": hostgroup_name,
            }
        )
        if sticky is not UNSET:
            field_dict["sticky"] = sticky
        if persistent is not UNSET:
            field_dict["persistent"] = persistent
        if notify is not UNSET:
            field_dict["notify"] = notify
        if expire_on is not UNSET:
            field_dict["expire_on"] = expire_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment")

        acknowledge_type = AcknowledgeHostGroupProblemAcknowledgeType(
            d.pop("acknowledge_type")
        )

        hostgroup_name = d.pop("hostgroup_name")

        sticky = d.pop("sticky", UNSET)

        persistent = d.pop("persistent", UNSET)

        notify = d.pop("notify", UNSET)

        _expire_on = d.pop("expire_on", UNSET)
        expire_on: datetime.datetime | Unset
        if isinstance(_expire_on, Unset):
            expire_on = UNSET
        else:
            expire_on = isoparse(_expire_on)

        acknowledge_host_group_problem = cls(
            comment=comment,
            acknowledge_type=acknowledge_type,
            hostgroup_name=hostgroup_name,
            sticky=sticky,
            persistent=persistent,
            notify=notify,
            expire_on=expire_on,
        )

        acknowledge_host_group_problem.additional_properties = d
        return acknowledge_host_group_problem

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
