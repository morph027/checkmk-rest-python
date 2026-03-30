from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceEventType")


@_attrs_define
class ServiceEventType:
    """
    Attributes:
        start_or_end_of_flapping_state (bool | Unset):  Default: False. Example: True.
        start_or_end_of_scheduled_downtime (bool | Unset):  Default: False. Example: True.
        acknowledgement_of_problem (bool | Unset):  Default: False.
        alert_handler_execution_successful (bool | Unset):  Default: False. Example: True.
        alert_handler_execution_failed (bool | Unset):  Default: False.
        ok_warn (bool | Unset):  Default: False. Example: True.
        ok_ok (bool | Unset):  Default: False. Example: True.
        ok_crit (bool | Unset):  Default: False.
        ok_unknown (bool | Unset):  Default: False. Example: True.
        warn_ok (bool | Unset):  Default: False.
        warn_crit (bool | Unset):  Default: False.
        warn_unknown (bool | Unset):  Default: False.
        crit_ok (bool | Unset):  Default: False. Example: True.
        crit_warn (bool | Unset):  Default: False. Example: True.
        crit_unknown (bool | Unset):  Default: False. Example: True.
        unknown_ok (bool | Unset):  Default: False. Example: True.
        unknown_warn (bool | Unset):  Default: False. Example: True.
        unknown_crit (bool | Unset):  Default: False. Example: True.
        any_ok (bool | Unset):  Default: True.
        any_warn (bool | Unset):  Default: True.
        any_crit (bool | Unset):  Default: True. Example: True.
        any_unknown (bool | Unset):  Default: False.
    """

    start_or_end_of_flapping_state: bool | Unset = False
    start_or_end_of_scheduled_downtime: bool | Unset = False
    acknowledgement_of_problem: bool | Unset = False
    alert_handler_execution_successful: bool | Unset = False
    alert_handler_execution_failed: bool | Unset = False
    ok_warn: bool | Unset = False
    ok_ok: bool | Unset = False
    ok_crit: bool | Unset = False
    ok_unknown: bool | Unset = False
    warn_ok: bool | Unset = False
    warn_crit: bool | Unset = False
    warn_unknown: bool | Unset = False
    crit_ok: bool | Unset = False
    crit_warn: bool | Unset = False
    crit_unknown: bool | Unset = False
    unknown_ok: bool | Unset = False
    unknown_warn: bool | Unset = False
    unknown_crit: bool | Unset = False
    any_ok: bool | Unset = True
    any_warn: bool | Unset = True
    any_crit: bool | Unset = True
    any_unknown: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_or_end_of_flapping_state = self.start_or_end_of_flapping_state

        start_or_end_of_scheduled_downtime = self.start_or_end_of_scheduled_downtime

        acknowledgement_of_problem = self.acknowledgement_of_problem

        alert_handler_execution_successful = self.alert_handler_execution_successful

        alert_handler_execution_failed = self.alert_handler_execution_failed

        ok_warn = self.ok_warn

        ok_ok = self.ok_ok

        ok_crit = self.ok_crit

        ok_unknown = self.ok_unknown

        warn_ok = self.warn_ok

        warn_crit = self.warn_crit

        warn_unknown = self.warn_unknown

        crit_ok = self.crit_ok

        crit_warn = self.crit_warn

        crit_unknown = self.crit_unknown

        unknown_ok = self.unknown_ok

        unknown_warn = self.unknown_warn

        unknown_crit = self.unknown_crit

        any_ok = self.any_ok

        any_warn = self.any_warn

        any_crit = self.any_crit

        any_unknown = self.any_unknown

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
        if ok_warn is not UNSET:
            field_dict["ok_warn"] = ok_warn
        if ok_ok is not UNSET:
            field_dict["ok_ok"] = ok_ok
        if ok_crit is not UNSET:
            field_dict["ok_crit"] = ok_crit
        if ok_unknown is not UNSET:
            field_dict["ok_unknown"] = ok_unknown
        if warn_ok is not UNSET:
            field_dict["warn_ok"] = warn_ok
        if warn_crit is not UNSET:
            field_dict["warn_crit"] = warn_crit
        if warn_unknown is not UNSET:
            field_dict["warn_unknown"] = warn_unknown
        if crit_ok is not UNSET:
            field_dict["crit_ok"] = crit_ok
        if crit_warn is not UNSET:
            field_dict["crit_warn"] = crit_warn
        if crit_unknown is not UNSET:
            field_dict["crit_unknown"] = crit_unknown
        if unknown_ok is not UNSET:
            field_dict["unknown_ok"] = unknown_ok
        if unknown_warn is not UNSET:
            field_dict["unknown_warn"] = unknown_warn
        if unknown_crit is not UNSET:
            field_dict["unknown_crit"] = unknown_crit
        if any_ok is not UNSET:
            field_dict["any_ok"] = any_ok
        if any_warn is not UNSET:
            field_dict["any_warn"] = any_warn
        if any_crit is not UNSET:
            field_dict["any_crit"] = any_crit
        if any_unknown is not UNSET:
            field_dict["any_unknown"] = any_unknown

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

        ok_warn = d.pop("ok_warn", UNSET)

        ok_ok = d.pop("ok_ok", UNSET)

        ok_crit = d.pop("ok_crit", UNSET)

        ok_unknown = d.pop("ok_unknown", UNSET)

        warn_ok = d.pop("warn_ok", UNSET)

        warn_crit = d.pop("warn_crit", UNSET)

        warn_unknown = d.pop("warn_unknown", UNSET)

        crit_ok = d.pop("crit_ok", UNSET)

        crit_warn = d.pop("crit_warn", UNSET)

        crit_unknown = d.pop("crit_unknown", UNSET)

        unknown_ok = d.pop("unknown_ok", UNSET)

        unknown_warn = d.pop("unknown_warn", UNSET)

        unknown_crit = d.pop("unknown_crit", UNSET)

        any_ok = d.pop("any_ok", UNSET)

        any_warn = d.pop("any_warn", UNSET)

        any_crit = d.pop("any_crit", UNSET)

        any_unknown = d.pop("any_unknown", UNSET)

        service_event_type = cls(
            start_or_end_of_flapping_state=start_or_end_of_flapping_state,
            start_or_end_of_scheduled_downtime=start_or_end_of_scheduled_downtime,
            acknowledgement_of_problem=acknowledgement_of_problem,
            alert_handler_execution_successful=alert_handler_execution_successful,
            alert_handler_execution_failed=alert_handler_execution_failed,
            ok_warn=ok_warn,
            ok_ok=ok_ok,
            ok_crit=ok_crit,
            ok_unknown=ok_unknown,
            warn_ok=warn_ok,
            warn_crit=warn_crit,
            warn_unknown=warn_unknown,
            crit_ok=crit_ok,
            crit_warn=crit_warn,
            crit_unknown=crit_unknown,
            unknown_ok=unknown_ok,
            unknown_warn=unknown_warn,
            unknown_crit=unknown_crit,
            any_ok=any_ok,
            any_warn=any_warn,
            any_crit=any_crit,
            any_unknown=any_unknown,
        )

        service_event_type.additional_properties = d
        return service_event_type

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
