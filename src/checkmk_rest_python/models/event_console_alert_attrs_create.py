from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_list_of_rule_ids import CheckboxWithListOfRuleIds
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.checkbox_with_sys_log_facility import CheckboxWithSysLogFacility
    from ..models.checkbox_with_sys_log_priority import CheckboxWithSysLogPriority


T = TypeVar("T", bound="EventConsoleAlertAttrsCreate")


@_attrs_define
class EventConsoleAlertAttrsCreate:
    """
    Attributes:
        match_rule_ids (Checkbox | CheckboxWithListOfRuleIds | Unset):
        match_syslog_priority (Checkbox | CheckboxWithSysLogPriority | Unset):
        match_syslog_facility (Checkbox | CheckboxWithSysLogFacility | Unset):
        match_event_comment (Checkbox | CheckboxWithStrValue | Unset):
    """

    match_rule_ids: Checkbox | CheckboxWithListOfRuleIds | Unset = UNSET
    match_syslog_priority: Checkbox | CheckboxWithSysLogPriority | Unset = UNSET
    match_syslog_facility: Checkbox | CheckboxWithSysLogFacility | Unset = UNSET
    match_event_comment: Checkbox | CheckboxWithStrValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        match_rule_ids: dict[str, Any] | Unset
        if isinstance(self.match_rule_ids, Unset):
            match_rule_ids = UNSET
        elif isinstance(self.match_rule_ids, Checkbox):
            match_rule_ids = self.match_rule_ids.to_dict()
        else:
            match_rule_ids = self.match_rule_ids.to_dict()

        match_syslog_priority: dict[str, Any] | Unset
        if isinstance(self.match_syslog_priority, Unset):
            match_syslog_priority = UNSET
        elif isinstance(self.match_syslog_priority, Checkbox):
            match_syslog_priority = self.match_syslog_priority.to_dict()
        else:
            match_syslog_priority = self.match_syslog_priority.to_dict()

        match_syslog_facility: dict[str, Any] | Unset
        if isinstance(self.match_syslog_facility, Unset):
            match_syslog_facility = UNSET
        elif isinstance(self.match_syslog_facility, Checkbox):
            match_syslog_facility = self.match_syslog_facility.to_dict()
        else:
            match_syslog_facility = self.match_syslog_facility.to_dict()

        match_event_comment: dict[str, Any] | Unset
        if isinstance(self.match_event_comment, Unset):
            match_event_comment = UNSET
        elif isinstance(self.match_event_comment, Checkbox):
            match_event_comment = self.match_event_comment.to_dict()
        else:
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
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_list_of_rule_ids import CheckboxWithListOfRuleIds
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.checkbox_with_sys_log_facility import CheckboxWithSysLogFacility
        from ..models.checkbox_with_sys_log_priority import CheckboxWithSysLogPriority

        d = dict(src_dict)

        def _parse_match_rule_ids(
            data: object,
        ) -> Checkbox | CheckboxWithListOfRuleIds | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_rule_ids_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_rule_ids_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_rule_ids_one_of_type_1 = (
                CheckboxWithListOfRuleIds.from_dict(data)
            )

            return componentsschemas_match_rule_ids_one_of_type_1

        match_rule_ids = _parse_match_rule_ids(d.pop("match_rule_ids", UNSET))

        def _parse_match_syslog_priority(
            data: object,
        ) -> Checkbox | CheckboxWithSysLogPriority | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_sys_log_pri_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_sys_log_pri_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_sys_log_pri_one_of_type_1 = (
                CheckboxWithSysLogPriority.from_dict(data)
            )

            return componentsschemas_match_sys_log_pri_one_of_type_1

        match_syslog_priority = _parse_match_syslog_priority(
            d.pop("match_syslog_priority", UNSET)
        )

        def _parse_match_syslog_facility(
            data: object,
        ) -> Checkbox | CheckboxWithSysLogFacility | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_sys_log_fac_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_sys_log_fac_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_sys_log_fac_one_of_type_1 = (
                CheckboxWithSysLogFacility.from_dict(data)
            )

            return componentsschemas_match_sys_log_fac_one_of_type_1

        match_syslog_facility = _parse_match_syslog_facility(
            d.pop("match_syslog_facility", UNSET)
        )

        def _parse_match_event_comment(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        match_event_comment = _parse_match_event_comment(
            d.pop("match_event_comment", UNSET)
        )

        event_console_alert_attrs_create = cls(
            match_rule_ids=match_rule_ids,
            match_syslog_priority=match_syslog_priority,
            match_syslog_facility=match_syslog_facility,
            match_event_comment=match_event_comment,
        )

        event_console_alert_attrs_create.additional_properties = d
        return event_console_alert_attrs_create

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
