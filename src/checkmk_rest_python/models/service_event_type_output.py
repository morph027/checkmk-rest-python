from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceEventTypeOutput")


@_attrs_define
class ServiceEventTypeOutput:
    """
    Attributes:
        start_or_end_of_flapping_state (bool | Unset):  Example: True.
        start_or_end_of_scheduled_downtime (bool | Unset):  Example: True.
        acknowledgement_of_problem (bool | Unset):
        alert_handler_execution_successful (bool | Unset):  Example: True.
        alert_handler_execution_failed (bool | Unset):
        ok_warn (bool | Unset):  Example: True.
        ok_ok (bool | Unset):  Example: True.
        ok_crit (bool | Unset):
        ok_unknown (bool | Unset):  Example: True.
        warn_ok (bool | Unset):
        warn_crit (bool | Unset):
        warn_unknown (bool | Unset):
        crit_ok (bool | Unset):  Example: True.
        crit_warn (bool | Unset):  Example: True.
        crit_unknown (bool | Unset):  Example: True.
        unknown_ok (bool | Unset):  Example: True.
        unknown_warn (bool | Unset):  Example: True.
        unknown_crit (bool | Unset):  Example: True.
        any_ok (bool | Unset):
        any_warn (bool | Unset):
        any_crit (bool | Unset):  Example: True.
        any_unknown (bool | Unset):
    """

    start_or_end_of_flapping_state: bool | Unset = UNSET
    start_or_end_of_scheduled_downtime: bool | Unset = UNSET
    acknowledgement_of_problem: bool | Unset = UNSET
    alert_handler_execution_successful: bool | Unset = UNSET
    alert_handler_execution_failed: bool | Unset = UNSET
    ok_warn: bool | Unset = UNSET
    ok_ok: bool | Unset = UNSET
    ok_crit: bool | Unset = UNSET
    ok_unknown: bool | Unset = UNSET
    warn_ok: bool | Unset = UNSET
    warn_crit: bool | Unset = UNSET
    warn_unknown: bool | Unset = UNSET
    crit_ok: bool | Unset = UNSET
    crit_warn: bool | Unset = UNSET
    crit_unknown: bool | Unset = UNSET
    unknown_ok: bool | Unset = UNSET
    unknown_warn: bool | Unset = UNSET
    unknown_crit: bool | Unset = UNSET
    any_ok: bool | Unset = UNSET
    any_warn: bool | Unset = UNSET
    any_crit: bool | Unset = UNSET
    any_unknown: bool | Unset = UNSET
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

        service_event_type_output = cls(
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

        service_event_type_output.additional_properties = d
        return service_event_type_output

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
