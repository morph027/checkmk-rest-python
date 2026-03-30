from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostEventType")


@_attrs_define
class HostEventType:
    """
    Attributes:
        start_or_end_of_flapping_state (bool | Unset):  Default: False. Example: True.
        start_or_end_of_scheduled_downtime (bool | Unset):  Default: False. Example: True.
        acknowledgement_of_problem (bool | Unset):  Default: False.
        alert_handler_execution_successful (bool | Unset):  Default: False. Example: True.
        alert_handler_execution_failed (bool | Unset):  Default: False.
        up_down (bool | Unset):  Default: False. Example: True.
        up_unreachable (bool | Unset):  Default: False.
        down_up (bool | Unset):  Default: False. Example: True.
        down_unreachable (bool | Unset):  Default: False.
        unreachable_down (bool | Unset):  Default: False.
        unreachable_up (bool | Unset):  Default: False.
        any_up (bool | Unset):  Default: True.
        any_down (bool | Unset):  Default: True. Example: True.
        any_unreachable (bool | Unset):  Default: False. Example: True.
    """

    start_or_end_of_flapping_state: bool | Unset = False
    start_or_end_of_scheduled_downtime: bool | Unset = False
    acknowledgement_of_problem: bool | Unset = False
    alert_handler_execution_successful: bool | Unset = False
    alert_handler_execution_failed: bool | Unset = False
    up_down: bool | Unset = False
    up_unreachable: bool | Unset = False
    down_up: bool | Unset = False
    down_unreachable: bool | Unset = False
    unreachable_down: bool | Unset = False
    unreachable_up: bool | Unset = False
    any_up: bool | Unset = True
    any_down: bool | Unset = True
    any_unreachable: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_or_end_of_flapping_state = self.start_or_end_of_flapping_state

        start_or_end_of_scheduled_downtime = self.start_or_end_of_scheduled_downtime

        acknowledgement_of_problem = self.acknowledgement_of_problem

        alert_handler_execution_successful = self.alert_handler_execution_successful

        alert_handler_execution_failed = self.alert_handler_execution_failed

        up_down = self.up_down

        up_unreachable = self.up_unreachable

        down_up = self.down_up

        down_unreachable = self.down_unreachable

        unreachable_down = self.unreachable_down

        unreachable_up = self.unreachable_up

        any_up = self.any_up

        any_down = self.any_down

        any_unreachable = self.any_unreachable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_or_end_of_flapping_state is not UNSET:
            field_dict["start_or_end_of_flapping_state"] = (
                start_or_end_of_flapping_state
            )
        if start_or_end_of_scheduled_downtime is not UNSET:
            field_dict["start_or_end_of_scheduled_downtime"] = (
                start_or_end_of_scheduled_downtime
            )
        if acknowledgement_of_problem is not UNSET:
            field_dict["acknowledgement_of_problem"] = acknowledgement_of_problem
        if alert_handler_execution_successful is not UNSET:
            field_dict["alert_handler_execution_successful"] = (
                alert_handler_execution_successful
            )
        if alert_handler_execution_failed is not UNSET:
            field_dict["alert_handler_execution_failed"] = (
                alert_handler_execution_failed
            )
        if up_down is not UNSET:
            field_dict["up_down"] = up_down
        if up_unreachable is not UNSET:
            field_dict["up_unreachable"] = up_unreachable
        if down_up is not UNSET:
            field_dict["down_up"] = down_up
        if down_unreachable is not UNSET:
            field_dict["down_unreachable"] = down_unreachable
        if unreachable_down is not UNSET:
            field_dict["unreachable_down"] = unreachable_down
        if unreachable_up is not UNSET:
            field_dict["unreachable_up"] = unreachable_up
        if any_up is not UNSET:
            field_dict["any_up"] = any_up
        if any_down is not UNSET:
            field_dict["any_down"] = any_down
        if any_unreachable is not UNSET:
            field_dict["any_unreachable"] = any_unreachable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_or_end_of_flapping_state = d.pop("start_or_end_of_flapping_state", UNSET)

        start_or_end_of_scheduled_downtime = d.pop(
            "start_or_end_of_scheduled_downtime", UNSET
        )

        acknowledgement_of_problem = d.pop("acknowledgement_of_problem", UNSET)

        alert_handler_execution_successful = d.pop(
            "alert_handler_execution_successful", UNSET
        )

        alert_handler_execution_failed = d.pop("alert_handler_execution_failed", UNSET)

        up_down = d.pop("up_down", UNSET)

        up_unreachable = d.pop("up_unreachable", UNSET)

        down_up = d.pop("down_up", UNSET)

        down_unreachable = d.pop("down_unreachable", UNSET)

        unreachable_down = d.pop("unreachable_down", UNSET)

        unreachable_up = d.pop("unreachable_up", UNSET)

        any_up = d.pop("any_up", UNSET)

        any_down = d.pop("any_down", UNSET)

        any_unreachable = d.pop("any_unreachable", UNSET)

        host_event_type = cls(
            start_or_end_of_flapping_state=start_or_end_of_flapping_state,
            start_or_end_of_scheduled_downtime=start_or_end_of_scheduled_downtime,
            acknowledgement_of_problem=acknowledgement_of_problem,
            alert_handler_execution_successful=alert_handler_execution_successful,
            alert_handler_execution_failed=alert_handler_execution_failed,
            up_down=up_down,
            up_unreachable=up_unreachable,
            down_up=down_up,
            down_unreachable=down_unreachable,
            unreachable_down=unreachable_down,
            unreachable_up=unreachable_up,
            any_up=any_up,
            any_down=any_down,
            any_unreachable=any_unreachable,
        )

        host_event_type.additional_properties = d
        return host_event_type

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
