from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_host_event_type_output import CheckboxHostEventTypeOutput
    from ..models.checkbox_match_host_tags_output import CheckboxMatchHostTagsOutput
    from ..models.checkbox_restrict_notification_numbers_output import (
        CheckboxRestrictNotificationNumbersOutput,
    )
    from ..models.checkbox_service_event_type_output import (
        CheckboxServiceEventTypeOutput,
    )
    from ..models.checkbox_throttle_periodic_notifcations_ouput import (
        CheckboxThrottlePeriodicNotifcationsOuput,
    )
    from ..models.checkbox_with_folder_str_output import CheckboxWithFolderStrOutput
    from ..models.checkbox_with_from_to_service_levels_output import (
        CheckboxWithFromToServiceLevelsOutput,
    )
    from ..models.checkbox_with_list_of_labels_output import (
        CheckboxWithListOfLabelsOutput,
    )
    from ..models.checkbox_with_list_of_service_groups_regex_output import (
        CheckboxWithListOfServiceGroupsRegexOutput,
    )
    from ..models.checkbox_with_list_of_str_output import CheckboxWithListOfStrOutput
    from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput
    from ..models.match_event_console_alerts_response import (
        MatchEventConsoleAlertsResponse,
    )


T = TypeVar("T", bound="ConditionsAttributes")


@_attrs_define
class ConditionsAttributes:
    """
    Attributes:
        match_sites (CheckboxWithListOfStrOutput | Unset):
        match_folder (CheckboxWithFolderStrOutput | Unset):
        match_host_tags (CheckboxMatchHostTagsOutput | Unset):
        match_host_labels (CheckboxWithListOfLabelsOutput | Unset):
        match_host_groups (CheckboxWithListOfStrOutput | Unset):
        match_hosts (CheckboxWithListOfStrOutput | Unset):
        match_exclude_hosts (CheckboxWithListOfStrOutput | Unset):
        match_service_labels (CheckboxWithListOfLabelsOutput | Unset):
        match_service_groups (CheckboxWithListOfStrOutput | Unset):
        match_exclude_service_groups (CheckboxWithListOfStrOutput | Unset):
        match_service_groups_regex (CheckboxWithListOfServiceGroupsRegexOutput | Unset):
        match_exclude_service_groups_regex (CheckboxWithListOfServiceGroupsRegexOutput | Unset):
        match_services (CheckboxWithListOfStrOutput | Unset):
        match_exclude_services (CheckboxWithListOfStrOutput | Unset):
        match_check_types (CheckboxWithListOfStrOutput | Unset):
        match_plugin_output (CheckboxWithStrValueOutput | Unset):
        match_contact_groups (CheckboxWithListOfStrOutput | Unset):
        match_service_levels (CheckboxWithFromToServiceLevelsOutput | Unset):
        match_only_during_time_period (CheckboxWithStrValueOutput | Unset):
        match_host_event_type (CheckboxHostEventTypeOutput | Unset):
        match_service_event_type (CheckboxServiceEventTypeOutput | Unset):
        restrict_to_notification_numbers (CheckboxRestrictNotificationNumbersOutput | Unset):
        throttle_periodic_notifications (CheckboxThrottlePeriodicNotifcationsOuput | Unset):
        match_notification_comment (CheckboxWithStrValueOutput | Unset):
        event_console_alerts (MatchEventConsoleAlertsResponse | Unset):
    """

    match_sites: CheckboxWithListOfStrOutput | Unset = UNSET
    match_folder: CheckboxWithFolderStrOutput | Unset = UNSET
    match_host_tags: CheckboxMatchHostTagsOutput | Unset = UNSET
    match_host_labels: CheckboxWithListOfLabelsOutput | Unset = UNSET
    match_host_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    match_hosts: CheckboxWithListOfStrOutput | Unset = UNSET
    match_exclude_hosts: CheckboxWithListOfStrOutput | Unset = UNSET
    match_service_labels: CheckboxWithListOfLabelsOutput | Unset = UNSET
    match_service_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    match_exclude_service_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    match_service_groups_regex: CheckboxWithListOfServiceGroupsRegexOutput | Unset = (
        UNSET
    )
    match_exclude_service_groups_regex: (
        CheckboxWithListOfServiceGroupsRegexOutput | Unset
    ) = UNSET
    match_services: CheckboxWithListOfStrOutput | Unset = UNSET
    match_exclude_services: CheckboxWithListOfStrOutput | Unset = UNSET
    match_check_types: CheckboxWithListOfStrOutput | Unset = UNSET
    match_plugin_output: CheckboxWithStrValueOutput | Unset = UNSET
    match_contact_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    match_service_levels: CheckboxWithFromToServiceLevelsOutput | Unset = UNSET
    match_only_during_time_period: CheckboxWithStrValueOutput | Unset = UNSET
    match_host_event_type: CheckboxHostEventTypeOutput | Unset = UNSET
    match_service_event_type: CheckboxServiceEventTypeOutput | Unset = UNSET
    restrict_to_notification_numbers: (
        CheckboxRestrictNotificationNumbersOutput | Unset
    ) = UNSET
    throttle_periodic_notifications: (
        CheckboxThrottlePeriodicNotifcationsOuput | Unset
    ) = UNSET
    match_notification_comment: CheckboxWithStrValueOutput | Unset = UNSET
    event_console_alerts: MatchEventConsoleAlertsResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_sites: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_sites, Unset):
            match_sites = self.match_sites.to_dict()

        match_folder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_folder, Unset):
            match_folder = self.match_folder.to_dict()

        match_host_tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_host_tags, Unset):
            match_host_tags = self.match_host_tags.to_dict()

        match_host_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_host_labels, Unset):
            match_host_labels = self.match_host_labels.to_dict()

        match_host_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_host_groups, Unset):
            match_host_groups = self.match_host_groups.to_dict()

        match_hosts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_hosts, Unset):
            match_hosts = self.match_hosts.to_dict()

        match_exclude_hosts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_exclude_hosts, Unset):
            match_exclude_hosts = self.match_exclude_hosts.to_dict()

        match_service_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_service_labels, Unset):
            match_service_labels = self.match_service_labels.to_dict()

        match_service_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_service_groups, Unset):
            match_service_groups = self.match_service_groups.to_dict()

        match_exclude_service_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_exclude_service_groups, Unset):
            match_exclude_service_groups = self.match_exclude_service_groups.to_dict()

        match_service_groups_regex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_service_groups_regex, Unset):
            match_service_groups_regex = self.match_service_groups_regex.to_dict()

        match_exclude_service_groups_regex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_exclude_service_groups_regex, Unset):
            match_exclude_service_groups_regex = (
                self.match_exclude_service_groups_regex.to_dict()
            )

        match_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_services, Unset):
            match_services = self.match_services.to_dict()

        match_exclude_services: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_exclude_services, Unset):
            match_exclude_services = self.match_exclude_services.to_dict()

        match_check_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_check_types, Unset):
            match_check_types = self.match_check_types.to_dict()

        match_plugin_output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_plugin_output, Unset):
            match_plugin_output = self.match_plugin_output.to_dict()

        match_contact_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_contact_groups, Unset):
            match_contact_groups = self.match_contact_groups.to_dict()

        match_service_levels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_service_levels, Unset):
            match_service_levels = self.match_service_levels.to_dict()

        match_only_during_time_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_only_during_time_period, Unset):
            match_only_during_time_period = self.match_only_during_time_period.to_dict()

        match_host_event_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_host_event_type, Unset):
            match_host_event_type = self.match_host_event_type.to_dict()

        match_service_event_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_service_event_type, Unset):
            match_service_event_type = self.match_service_event_type.to_dict()

        restrict_to_notification_numbers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrict_to_notification_numbers, Unset):
            restrict_to_notification_numbers = (
                self.restrict_to_notification_numbers.to_dict()
            )

        throttle_periodic_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.throttle_periodic_notifications, Unset):
            throttle_periodic_notifications = (
                self.throttle_periodic_notifications.to_dict()
            )

        match_notification_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match_notification_comment, Unset):
            match_notification_comment = self.match_notification_comment.to_dict()

        event_console_alerts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_console_alerts, Unset):
            event_console_alerts = self.event_console_alerts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_sites is not UNSET:
            field_dict["match_sites"] = match_sites
        if match_folder is not UNSET:
            field_dict["match_folder"] = match_folder
        if match_host_tags is not UNSET:
            field_dict["match_host_tags"] = match_host_tags
        if match_host_labels is not UNSET:
            field_dict["match_host_labels"] = match_host_labels
        if match_host_groups is not UNSET:
            field_dict["match_host_groups"] = match_host_groups
        if match_hosts is not UNSET:
            field_dict["match_hosts"] = match_hosts
        if match_exclude_hosts is not UNSET:
            field_dict["match_exclude_hosts"] = match_exclude_hosts
        if match_service_labels is not UNSET:
            field_dict["match_service_labels"] = match_service_labels
        if match_service_groups is not UNSET:
            field_dict["match_service_groups"] = match_service_groups
        if match_exclude_service_groups is not UNSET:
            field_dict["match_exclude_service_groups"] = match_exclude_service_groups
        if match_service_groups_regex is not UNSET:
            field_dict["match_service_groups_regex"] = match_service_groups_regex
        if match_exclude_service_groups_regex is not UNSET:
            field_dict["match_exclude_service_groups_regex"] = (
                match_exclude_service_groups_regex
            )
        if match_services is not UNSET:
            field_dict["match_services"] = match_services
        if match_exclude_services is not UNSET:
            field_dict["match_exclude_services"] = match_exclude_services
        if match_check_types is not UNSET:
            field_dict["match_check_types"] = match_check_types
        if match_plugin_output is not UNSET:
            field_dict["match_plugin_output"] = match_plugin_output
        if match_contact_groups is not UNSET:
            field_dict["match_contact_groups"] = match_contact_groups
        if match_service_levels is not UNSET:
            field_dict["match_service_levels"] = match_service_levels
        if match_only_during_time_period is not UNSET:
            field_dict["match_only_during_time_period"] = match_only_during_time_period
        if match_host_event_type is not UNSET:
            field_dict["match_host_event_type"] = match_host_event_type
        if match_service_event_type is not UNSET:
            field_dict["match_service_event_type"] = match_service_event_type
        if restrict_to_notification_numbers is not UNSET:
            field_dict["restrict_to_notification_numbers"] = (
                restrict_to_notification_numbers
            )
        if throttle_periodic_notifications is not UNSET:
            field_dict["throttle_periodic_notifications"] = (
                throttle_periodic_notifications
            )
        if match_notification_comment is not UNSET:
            field_dict["match_notification_comment"] = match_notification_comment
        if event_console_alerts is not UNSET:
            field_dict["event_console_alerts"] = event_console_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_host_event_type_output import CheckboxHostEventTypeOutput
        from ..models.checkbox_match_host_tags_output import CheckboxMatchHostTagsOutput
        from ..models.checkbox_restrict_notification_numbers_output import (
            CheckboxRestrictNotificationNumbersOutput,
        )
        from ..models.checkbox_service_event_type_output import (
            CheckboxServiceEventTypeOutput,
        )
        from ..models.checkbox_throttle_periodic_notifcations_ouput import (
            CheckboxThrottlePeriodicNotifcationsOuput,
        )
        from ..models.checkbox_with_folder_str_output import CheckboxWithFolderStrOutput
        from ..models.checkbox_with_from_to_service_levels_output import (
            CheckboxWithFromToServiceLevelsOutput,
        )
        from ..models.checkbox_with_list_of_labels_output import (
            CheckboxWithListOfLabelsOutput,
        )
        from ..models.checkbox_with_list_of_service_groups_regex_output import (
            CheckboxWithListOfServiceGroupsRegexOutput,
        )
        from ..models.checkbox_with_list_of_str_output import (
            CheckboxWithListOfStrOutput,
        )
        from ..models.checkbox_with_str_value_output import CheckboxWithStrValueOutput
        from ..models.match_event_console_alerts_response import (
            MatchEventConsoleAlertsResponse,
        )

        d = dict(src_dict)
        _match_sites = d.pop("match_sites", UNSET)
        match_sites: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_sites, Unset):
            match_sites = UNSET
        else:
            match_sites = CheckboxWithListOfStrOutput.from_dict(_match_sites)

        _match_folder = d.pop("match_folder", UNSET)
        match_folder: CheckboxWithFolderStrOutput | Unset
        if isinstance(_match_folder, Unset):
            match_folder = UNSET
        else:
            match_folder = CheckboxWithFolderStrOutput.from_dict(_match_folder)

        _match_host_tags = d.pop("match_host_tags", UNSET)
        match_host_tags: CheckboxMatchHostTagsOutput | Unset
        if isinstance(_match_host_tags, Unset):
            match_host_tags = UNSET
        else:
            match_host_tags = CheckboxMatchHostTagsOutput.from_dict(_match_host_tags)

        _match_host_labels = d.pop("match_host_labels", UNSET)
        match_host_labels: CheckboxWithListOfLabelsOutput | Unset
        if isinstance(_match_host_labels, Unset):
            match_host_labels = UNSET
        else:
            match_host_labels = CheckboxWithListOfLabelsOutput.from_dict(
                _match_host_labels
            )

        _match_host_groups = d.pop("match_host_groups", UNSET)
        match_host_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_host_groups, Unset):
            match_host_groups = UNSET
        else:
            match_host_groups = CheckboxWithListOfStrOutput.from_dict(
                _match_host_groups
            )

        _match_hosts = d.pop("match_hosts", UNSET)
        match_hosts: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_hosts, Unset):
            match_hosts = UNSET
        else:
            match_hosts = CheckboxWithListOfStrOutput.from_dict(_match_hosts)

        _match_exclude_hosts = d.pop("match_exclude_hosts", UNSET)
        match_exclude_hosts: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_exclude_hosts, Unset):
            match_exclude_hosts = UNSET
        else:
            match_exclude_hosts = CheckboxWithListOfStrOutput.from_dict(
                _match_exclude_hosts
            )

        _match_service_labels = d.pop("match_service_labels", UNSET)
        match_service_labels: CheckboxWithListOfLabelsOutput | Unset
        if isinstance(_match_service_labels, Unset):
            match_service_labels = UNSET
        else:
            match_service_labels = CheckboxWithListOfLabelsOutput.from_dict(
                _match_service_labels
            )

        _match_service_groups = d.pop("match_service_groups", UNSET)
        match_service_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_service_groups, Unset):
            match_service_groups = UNSET
        else:
            match_service_groups = CheckboxWithListOfStrOutput.from_dict(
                _match_service_groups
            )

        _match_exclude_service_groups = d.pop("match_exclude_service_groups", UNSET)
        match_exclude_service_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_exclude_service_groups, Unset):
            match_exclude_service_groups = UNSET
        else:
            match_exclude_service_groups = CheckboxWithListOfStrOutput.from_dict(
                _match_exclude_service_groups
            )

        _match_service_groups_regex = d.pop("match_service_groups_regex", UNSET)
        match_service_groups_regex: CheckboxWithListOfServiceGroupsRegexOutput | Unset
        if isinstance(_match_service_groups_regex, Unset):
            match_service_groups_regex = UNSET
        else:
            match_service_groups_regex = (
                CheckboxWithListOfServiceGroupsRegexOutput.from_dict(
                    _match_service_groups_regex
                )
            )

        _match_exclude_service_groups_regex = d.pop(
            "match_exclude_service_groups_regex", UNSET
        )
        match_exclude_service_groups_regex: (
            CheckboxWithListOfServiceGroupsRegexOutput | Unset
        )
        if isinstance(_match_exclude_service_groups_regex, Unset):
            match_exclude_service_groups_regex = UNSET
        else:
            match_exclude_service_groups_regex = (
                CheckboxWithListOfServiceGroupsRegexOutput.from_dict(
                    _match_exclude_service_groups_regex
                )
            )

        _match_services = d.pop("match_services", UNSET)
        match_services: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_services, Unset):
            match_services = UNSET
        else:
            match_services = CheckboxWithListOfStrOutput.from_dict(_match_services)

        _match_exclude_services = d.pop("match_exclude_services", UNSET)
        match_exclude_services: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_exclude_services, Unset):
            match_exclude_services = UNSET
        else:
            match_exclude_services = CheckboxWithListOfStrOutput.from_dict(
                _match_exclude_services
            )

        _match_check_types = d.pop("match_check_types", UNSET)
        match_check_types: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_check_types, Unset):
            match_check_types = UNSET
        else:
            match_check_types = CheckboxWithListOfStrOutput.from_dict(
                _match_check_types
            )

        _match_plugin_output = d.pop("match_plugin_output", UNSET)
        match_plugin_output: CheckboxWithStrValueOutput | Unset
        if isinstance(_match_plugin_output, Unset):
            match_plugin_output = UNSET
        else:
            match_plugin_output = CheckboxWithStrValueOutput.from_dict(
                _match_plugin_output
            )

        _match_contact_groups = d.pop("match_contact_groups", UNSET)
        match_contact_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_match_contact_groups, Unset):
            match_contact_groups = UNSET
        else:
            match_contact_groups = CheckboxWithListOfStrOutput.from_dict(
                _match_contact_groups
            )

        _match_service_levels = d.pop("match_service_levels", UNSET)
        match_service_levels: CheckboxWithFromToServiceLevelsOutput | Unset
        if isinstance(_match_service_levels, Unset):
            match_service_levels = UNSET
        else:
            match_service_levels = CheckboxWithFromToServiceLevelsOutput.from_dict(
                _match_service_levels
            )

        _match_only_during_time_period = d.pop("match_only_during_time_period", UNSET)
        match_only_during_time_period: CheckboxWithStrValueOutput | Unset
        if isinstance(_match_only_during_time_period, Unset):
            match_only_during_time_period = UNSET
        else:
            match_only_during_time_period = CheckboxWithStrValueOutput.from_dict(
                _match_only_during_time_period
            )

        _match_host_event_type = d.pop("match_host_event_type", UNSET)
        match_host_event_type: CheckboxHostEventTypeOutput | Unset
        if isinstance(_match_host_event_type, Unset):
            match_host_event_type = UNSET
        else:
            match_host_event_type = CheckboxHostEventTypeOutput.from_dict(
                _match_host_event_type
            )

        _match_service_event_type = d.pop("match_service_event_type", UNSET)
        match_service_event_type: CheckboxServiceEventTypeOutput | Unset
        if isinstance(_match_service_event_type, Unset):
            match_service_event_type = UNSET
        else:
            match_service_event_type = CheckboxServiceEventTypeOutput.from_dict(
                _match_service_event_type
            )

        _restrict_to_notification_numbers = d.pop(
            "restrict_to_notification_numbers", UNSET
        )
        restrict_to_notification_numbers: (
            CheckboxRestrictNotificationNumbersOutput | Unset
        )
        if isinstance(_restrict_to_notification_numbers, Unset):
            restrict_to_notification_numbers = UNSET
        else:
            restrict_to_notification_numbers = (
                CheckboxRestrictNotificationNumbersOutput.from_dict(
                    _restrict_to_notification_numbers
                )
            )

        _throttle_periodic_notifications = d.pop(
            "throttle_periodic_notifications", UNSET
        )
        throttle_periodic_notifications: (
            CheckboxThrottlePeriodicNotifcationsOuput | Unset
        )
        if isinstance(_throttle_periodic_notifications, Unset):
            throttle_periodic_notifications = UNSET
        else:
            throttle_periodic_notifications = (
                CheckboxThrottlePeriodicNotifcationsOuput.from_dict(
                    _throttle_periodic_notifications
                )
            )

        _match_notification_comment = d.pop("match_notification_comment", UNSET)
        match_notification_comment: CheckboxWithStrValueOutput | Unset
        if isinstance(_match_notification_comment, Unset):
            match_notification_comment = UNSET
        else:
            match_notification_comment = CheckboxWithStrValueOutput.from_dict(
                _match_notification_comment
            )

        _event_console_alerts = d.pop("event_console_alerts", UNSET)
        event_console_alerts: MatchEventConsoleAlertsResponse | Unset
        if isinstance(_event_console_alerts, Unset):
            event_console_alerts = UNSET
        else:
            event_console_alerts = MatchEventConsoleAlertsResponse.from_dict(
                _event_console_alerts
            )

        conditions_attributes = cls(
            match_sites=match_sites,
            match_folder=match_folder,
            match_host_tags=match_host_tags,
            match_host_labels=match_host_labels,
            match_host_groups=match_host_groups,
            match_hosts=match_hosts,
            match_exclude_hosts=match_exclude_hosts,
            match_service_labels=match_service_labels,
            match_service_groups=match_service_groups,
            match_exclude_service_groups=match_exclude_service_groups,
            match_service_groups_regex=match_service_groups_regex,
            match_exclude_service_groups_regex=match_exclude_service_groups_regex,
            match_services=match_services,
            match_exclude_services=match_exclude_services,
            match_check_types=match_check_types,
            match_plugin_output=match_plugin_output,
            match_contact_groups=match_contact_groups,
            match_service_levels=match_service_levels,
            match_only_during_time_period=match_only_during_time_period,
            match_host_event_type=match_host_event_type,
            match_service_event_type=match_service_event_type,
            restrict_to_notification_numbers=restrict_to_notification_numbers,
            throttle_periodic_notifications=throttle_periodic_notifications,
            match_notification_comment=match_notification_comment,
            event_console_alerts=event_console_alerts,
        )

        conditions_attributes.additional_properties = d
        return conditions_attributes

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
