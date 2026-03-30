from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_with_list_of_str_output import CheckboxWithListOfStrOutput
    from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput
    from ..models.checkbox_with_sys_log_priority_output import (
        CheckboxWithSysLogPriorityOutput,
    )


T = TypeVar("T", bound="EventConsoleAlertAttrsResponse")


@_attrs_define
class EventConsoleAlertAttrsResponse:
    """
    Attributes:
        match_rule_ids (CheckboxWithListOfStrOutput | Unset):
        match_syslog_priority (CheckboxWithSysLogPriorityOutput | Unset):
        match_syslog_facility (CheckboxWithStrValueOutput | Unset):
        match_event_comment (CheckboxWithStrValueOutput | Unset):
    """

    match_rule_ids: CheckboxWithListOfStrOutput | Unset = UNSET
    match_syslog_priority: CheckboxWithSysLogPriorityOutput | Unset = UNSET
    match_syslog_facility: CheckboxWithStrValueOutput | Unset = UNSET
    match_event_comment: CheckboxWithStrValueOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_rule_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_rule_ids, Unset):
            match_rule_ids = self.match_rule_ids.to_dict()

        match_syslog_priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_syslog_priority, Unset):
            match_syslog_priority = self.match_syslog_priority.to_dict()

        match_syslog_facility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_syslog_facility, Unset):
            match_syslog_facility = self.match_syslog_facility.to_dict()

        match_event_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_event_comment, Unset):
            match_event_comment = self.match_event_comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_rule_ids is not UNSET:
            field_dict["match_rule_ids"] = match_rule_ids
        if match_syslog_priority is not UNSET:
            field_dict["match_syslog_priority"] = match_syslog_priority
        if match_syslog_facility is not UNSET:
            field_dict["match_syslog_facility"] = match_syslog_facility
        if match_event_comment is not UNSET:
            field_dict["match_event_comment"] = match_event_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_with_list_of_str_output import (
            CheckboxWithListOfStrOutput,
        )
        from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput
        from ..models.checkbox_with_sys_log_priority_output import (
            CheckboxWithSysLogPriorityOutput,
        )

        d = dict(src_dict)
        _match_rule_ids = d.pop("match_rule_ids", UNSET)
        match_rule_ids: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_rule_ids, Unset):
            match_rule_ids = UNSET
        else:
            match_rule_ids = CheckboxWithListOfStrOutput.from_dict(_match_rule_ids)

        _match_syslog_priority = d.pop("match_syslog_priority", UNSET)
        match_syslog_priority: CheckboxWithSysLogPriorityOutput | Unset
        if isinstance(_match_syslog_priority, Unset):
            match_syslog_priority = UNSET
        else:
            match_syslog_priority = CheckboxWithSysLogPriorityOutput.from_dict(
                _match_syslog_priority
            )

        _match_syslog_facility = d.pop("match_syslog_facility", UNSET)
        match_syslog_facility: CheckboxWithStrValueOutput | Unset
        if isinstance(_match_syslog_facility, Unset):
            match_syslog_facility = UNSET
        else:
            match_syslog_facility = CheckboxWithStrValueOutput.from_dict(
                _match_syslog_facility
            )

        _match_event_comment = d.pop("match_event_comment", UNSET)
        match_event_comment: CheckboxWithStrValueOutput | Unset
        if isinstance(_match_event_comment, Unset):
            match_event_comment = UNSET
        else:
            match_event_comment = CheckboxWithStrValueOutput.from_dict(
                _match_event_comment
            )

        event_console_alert_attrs_response = cls(
            match_rule_ids=match_rule_ids,
            match_syslog_priority=match_syslog_priority,
            match_syslog_facility=match_syslog_facility,
            match_event_comment=match_event_comment,
        )

        event_console_alert_attrs_response.additional_properties = d
        return event_console_alert_attrs_response

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
