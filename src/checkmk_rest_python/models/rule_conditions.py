from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_event_console_alerts import CheckboxEventConsoleAlerts
    from ..models.checkbox_host_event_type import CheckboxHostEventType
    from ..models.checkbox_match_host_tags import CheckboxMatchHostTags
    from ..models.checkbox_restrict_notification_numbers import (
        CheckboxRestrictNotificationNumbers,
    )
    from ..models.checkbox_service_event_type import CheckboxServiceEventType
    from ..models.checkbox_throttle_periodic_notifcations import (
        CheckboxThrottlePeriodicNotifcations,
    )
    from ..models.checkbox_with_folder_str import CheckboxWithFolderStr
    from ..models.checkbox_with_from_to_service_levels import (
        CheckboxWithFromToServiceLevels,
    )
    from ..models.checkbox_with_list_of_check_types import CheckboxWithListOfCheckTypes
    from ..models.checkbox_with_list_of_contact_groups import (
        CheckboxWithListOfContactGroups,
    )
    from ..models.checkbox_with_list_of_host_groups import CheckboxWithListOfHostGroups
    from ..models.checkbox_with_list_of_hosts import CheckboxWithListOfHosts
    from ..models.checkbox_with_list_of_labels import CheckboxWithListOfLabels
    from ..models.checkbox_with_list_of_service_groups import (
        CheckboxWithListOfServiceGroups,
    )
    from ..models.checkbox_with_list_of_service_groups_regex import (
        CheckboxWithListOfServiceGroupsRegex,
    )
    from ..models.checkbox_with_list_of_sites import CheckboxWithListOfSites
    from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.checkbox_with_time_period import CheckboxWithTimePeriod


T = TypeVar("T", bound="RuleConditions")


@_attrs_define
class RuleConditions:
    """
    Attributes:
        match_sites (Checkbox | CheckboxWithListOfSites | Unset):
        match_folder (Checkbox | CheckboxWithFolderStr | Unset):
        match_host_tags (Checkbox | CheckboxMatchHostTags | Unset):
        match_host_labels (Checkbox | CheckboxWithListOfLabels | Unset):
        match_host_groups (Checkbox | CheckboxWithListOfHostGroups | Unset):
        match_hosts (Checkbox | CheckboxWithListOfHosts | Unset):
        match_exclude_hosts (Checkbox | CheckboxWithListOfHosts | Unset):
        match_service_labels (Checkbox | CheckboxWithListOfLabels | Unset):
        match_service_groups (Checkbox | CheckboxWithListOfServiceGroups | Unset):
        match_exclude_service_groups (Checkbox | CheckboxWithListOfServiceGroups | Unset):
        match_service_groups_regex (Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset):
        match_exclude_service_groups_regex (Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset):
        match_services (Checkbox | CheckboxWithListOfStr | Unset):
        match_exclude_services (Checkbox | CheckboxWithListOfStr | Unset):
        match_check_types (Checkbox | CheckboxWithListOfCheckTypes | Unset):
        match_plugin_output (Checkbox | CheckboxWithStrValue | Unset):
        match_contact_groups (Checkbox | CheckboxWithListOfContactGroups | Unset):
        match_service_levels (Checkbox | CheckboxWithFromToServiceLevels | Unset):
        match_only_during_time_period (Checkbox | CheckboxWithTimePeriod | Unset):
        match_host_event_type (Checkbox | CheckboxHostEventType | Unset):
        match_service_event_type (Checkbox | CheckboxServiceEventType | Unset):
        restrict_to_notification_numbers (Checkbox | CheckboxRestrictNotificationNumbers | Unset):
        throttle_periodic_notifications (Checkbox | CheckboxThrottlePeriodicNotifcations | Unset):
        match_notification_comment (Checkbox | CheckboxWithStrValue | Unset):
        event_console_alerts (Checkbox | CheckboxEventConsoleAlerts | Unset):
    """

    match_sites: Checkbox | CheckboxWithListOfSites | Unset = UNSET
    match_folder: Checkbox | CheckboxWithFolderStr | Unset = UNSET
    match_host_tags: Checkbox | CheckboxMatchHostTags | Unset = UNSET
    match_host_labels: Checkbox | CheckboxWithListOfLabels | Unset = UNSET
    match_host_groups: Checkbox | CheckboxWithListOfHostGroups | Unset = UNSET
    match_hosts: Checkbox | CheckboxWithListOfHosts | Unset = UNSET
    match_exclude_hosts: Checkbox | CheckboxWithListOfHosts | Unset = UNSET
    match_service_labels: Checkbox | CheckboxWithListOfLabels | Unset = UNSET
    match_service_groups: Checkbox | CheckboxWithListOfServiceGroups | Unset = UNSET
    match_exclude_service_groups: Checkbox | CheckboxWithListOfServiceGroups | Unset = (
        UNSET
    )
    match_service_groups_regex: (
        Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset
    ) = UNSET
    match_exclude_service_groups_regex: (
        Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset
    ) = UNSET
    match_services: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    match_exclude_services: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    match_check_types: Checkbox | CheckboxWithListOfCheckTypes | Unset = UNSET
    match_plugin_output: Checkbox | CheckboxWithStrValue | Unset = UNSET
    match_contact_groups: Checkbox | CheckboxWithListOfContactGroups | Unset = UNSET
    match_service_levels: Checkbox | CheckboxWithFromToServiceLevels | Unset = UNSET
    match_only_during_time_period: Checkbox | CheckboxWithTimePeriod | Unset = UNSET
    match_host_event_type: Checkbox | CheckboxHostEventType | Unset = UNSET
    match_service_event_type: Checkbox | CheckboxServiceEventType | Unset = UNSET
    restrict_to_notification_numbers: (
        Checkbox | CheckboxRestrictNotificationNumbers | Unset
    ) = UNSET
    throttle_periodic_notifications: (
        Checkbox | CheckboxThrottlePeriodicNotifcations | Unset
    ) = UNSET
    match_notification_comment: Checkbox | CheckboxWithStrValue | Unset = UNSET
    event_console_alerts: Checkbox | CheckboxEventConsoleAlerts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        match_sites: dict[str, Any] | Unset
        if isinstance(self.match_sites, Unset):
            match_sites = UNSET
        elif isinstance(self.match_sites, Checkbox):
            match_sites = self.match_sites.to_dict()
        else:
            match_sites = self.match_sites.to_dict()

        match_folder: dict[str, Any] | Unset
        if isinstance(self.match_folder, Unset):
            match_folder = UNSET
        elif isinstance(self.match_folder, Checkbox):
            match_folder = self.match_folder.to_dict()
        else:
            match_folder = self.match_folder.to_dict()

        match_host_tags: dict[str, Any] | Unset
        if isinstance(self.match_host_tags, Unset):
            match_host_tags = UNSET
        elif isinstance(self.match_host_tags, Checkbox):
            match_host_tags = self.match_host_tags.to_dict()
        else:
            match_host_tags = self.match_host_tags.to_dict()

        match_host_labels: dict[str, Any] | Unset
        if isinstance(self.match_host_labels, Unset):
            match_host_labels = UNSET
        elif isinstance(self.match_host_labels, Checkbox):
            match_host_labels = self.match_host_labels.to_dict()
        else:
            match_host_labels = self.match_host_labels.to_dict()

        match_host_groups: dict[str, Any] | Unset
        if isinstance(self.match_host_groups, Unset):
            match_host_groups = UNSET
        elif isinstance(self.match_host_groups, Checkbox):
            match_host_groups = self.match_host_groups.to_dict()
        else:
            match_host_groups = self.match_host_groups.to_dict()

        match_hosts: dict[str, Any] | Unset
        if isinstance(self.match_hosts, Unset):
            match_hosts = UNSET
        elif isinstance(self.match_hosts, Checkbox):
            match_hosts = self.match_hosts.to_dict()
        else:
            match_hosts = self.match_hosts.to_dict()

        match_exclude_hosts: dict[str, Any] | Unset
        if isinstance(self.match_exclude_hosts, Unset):
            match_exclude_hosts = UNSET
        elif isinstance(self.match_exclude_hosts, Checkbox):
            match_exclude_hosts = self.match_exclude_hosts.to_dict()
        else:
            match_exclude_hosts = self.match_exclude_hosts.to_dict()

        match_service_labels: dict[str, Any] | Unset
        if isinstance(self.match_service_labels, Unset):
            match_service_labels = UNSET
        elif isinstance(self.match_service_labels, Checkbox):
            match_service_labels = self.match_service_labels.to_dict()
        else:
            match_service_labels = self.match_service_labels.to_dict()

        match_service_groups: dict[str, Any] | Unset
        if isinstance(self.match_service_groups, Unset):
            match_service_groups = UNSET
        elif isinstance(self.match_service_groups, Checkbox):
            match_service_groups = self.match_service_groups.to_dict()
        else:
            match_service_groups = self.match_service_groups.to_dict()

        match_exclude_service_groups: dict[str, Any] | Unset
        if isinstance(self.match_exclude_service_groups, Unset):
            match_exclude_service_groups = UNSET
        elif isinstance(self.match_exclude_service_groups, Checkbox):
            match_exclude_service_groups = self.match_exclude_service_groups.to_dict()
        else:
            match_exclude_service_groups = self.match_exclude_service_groups.to_dict()

        match_service_groups_regex: dict[str, Any] | Unset
        if isinstance(self.match_service_groups_regex, Unset):
            match_service_groups_regex = UNSET
        elif isinstance(self.match_service_groups_regex, Checkbox):
            match_service_groups_regex = self.match_service_groups_regex.to_dict()
        else:
            match_service_groups_regex = self.match_service_groups_regex.to_dict()

        match_exclude_service_groups_regex: dict[str, Any] | Unset
        if isinstance(self.match_exclude_service_groups_regex, Unset):
            match_exclude_service_groups_regex = UNSET
        elif isinstance(self.match_exclude_service_groups_regex, Checkbox):
            match_exclude_service_groups_regex = (
                self.match_exclude_service_groups_regex.to_dict()
            )
        else:
            match_exclude_service_groups_regex = (
                self.match_exclude_service_groups_regex.to_dict()
            )

        match_services: dict[str, Any] | Unset
        if isinstance(self.match_services, Unset):
            match_services = UNSET
        elif isinstance(self.match_services, Checkbox):
            match_services = self.match_services.to_dict()
        else:
            match_services = self.match_services.to_dict()

        match_exclude_services: dict[str, Any] | Unset
        if isinstance(self.match_exclude_services, Unset):
            match_exclude_services = UNSET
        elif isinstance(self.match_exclude_services, Checkbox):
            match_exclude_services = self.match_exclude_services.to_dict()
        else:
            match_exclude_services = self.match_exclude_services.to_dict()

        match_check_types: dict[str, Any] | Unset
        if isinstance(self.match_check_types, Unset):
            match_check_types = UNSET
        elif isinstance(self.match_check_types, Checkbox):
            match_check_types = self.match_check_types.to_dict()
        else:
            match_check_types = self.match_check_types.to_dict()

        match_plugin_output: dict[str, Any] | Unset
        if isinstance(self.match_plugin_output, Unset):
            match_plugin_output = UNSET
        elif isinstance(self.match_plugin_output, Checkbox):
            match_plugin_output = self.match_plugin_output.to_dict()
        else:
            match_plugin_output = self.match_plugin_output.to_dict()

        match_contact_groups: dict[str, Any] | Unset
        if isinstance(self.match_contact_groups, Unset):
            match_contact_groups = UNSET
        elif isinstance(self.match_contact_groups, Checkbox):
            match_contact_groups = self.match_contact_groups.to_dict()
        else:
            match_contact_groups = self.match_contact_groups.to_dict()

        match_service_levels: dict[str, Any] | Unset
        if isinstance(self.match_service_levels, Unset):
            match_service_levels = UNSET
        elif isinstance(self.match_service_levels, Checkbox):
            match_service_levels = self.match_service_levels.to_dict()
        else:
            match_service_levels = self.match_service_levels.to_dict()

        match_only_during_time_period: dict[str, Any] | Unset
        if isinstance(self.match_only_during_time_period, Unset):
            match_only_during_time_period = UNSET
        elif isinstance(self.match_only_during_time_period, Checkbox):
            match_only_during_time_period = self.match_only_during_time_period.to_dict()
        else:
            match_only_during_time_period = self.match_only_during_time_period.to_dict()

        match_host_event_type: dict[str, Any] | Unset
        if isinstance(self.match_host_event_type, Unset):
            match_host_event_type = UNSET
        elif isinstance(self.match_host_event_type, Checkbox):
            match_host_event_type = self.match_host_event_type.to_dict()
        else:
            match_host_event_type = self.match_host_event_type.to_dict()

        match_service_event_type: dict[str, Any] | Unset
        if isinstance(self.match_service_event_type, Unset):
            match_service_event_type = UNSET
        elif isinstance(self.match_service_event_type, Checkbox):
            match_service_event_type = self.match_service_event_type.to_dict()
        else:
            match_service_event_type = self.match_service_event_type.to_dict()

        restrict_to_notification_numbers: dict[str, Any] | Unset
        if isinstance(self.restrict_to_notification_numbers, Unset):
            restrict_to_notification_numbers = UNSET
        elif isinstance(self.restrict_to_notification_numbers, Checkbox):
            restrict_to_notification_numbers = (
                self.restrict_to_notification_numbers.to_dict()
            )
        else:
            restrict_to_notification_numbers = (
                self.restrict_to_notification_numbers.to_dict()
            )

        throttle_periodic_notifications: dict[str, Any] | Unset
        if isinstance(self.throttle_periodic_notifications, Unset):
            throttle_periodic_notifications = UNSET
        elif isinstance(self.throttle_periodic_notifications, Checkbox):
            throttle_periodic_notifications = (
                self.throttle_periodic_notifications.to_dict()
            )
        else:
            throttle_periodic_notifications = (
                self.throttle_periodic_notifications.to_dict()
            )

        match_notification_comment: dict[str, Any] | Unset
        if isinstance(self.match_notification_comment, Unset):
            match_notification_comment = UNSET
        elif isinstance(self.match_notification_comment, Checkbox):
            match_notification_comment = self.match_notification_comment.to_dict()
        else:
            match_notification_comment = self.match_notification_comment.to_dict()

        event_console_alerts: dict[str, Any] | Unset
        if isinstance(self.event_console_alerts, Unset):
            event_console_alerts = UNSET
        elif isinstance(self.event_console_alerts, Checkbox):
            event_console_alerts = self.event_console_alerts.to_dict()
        else:
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
        from ..models.checkbox import Checkbox
        from ..models.checkbox_event_console_alerts import CheckboxEventConsoleAlerts
        from ..models.checkbox_host_event_type import CheckboxHostEventType
        from ..models.checkbox_match_host_tags import CheckboxMatchHostTags
        from ..models.checkbox_restrict_notification_numbers import (
            CheckboxRestrictNotificationNumbers,
        )
        from ..models.checkbox_service_event_type import CheckboxServiceEventType
        from ..models.checkbox_throttle_periodic_notifcations import (
            CheckboxThrottlePeriodicNotifcations,
        )
        from ..models.checkbox_with_folder_str import CheckboxWithFolderStr
        from ..models.checkbox_with_from_to_service_levels import (
            CheckboxWithFromToServiceLevels,
        )
        from ..models.checkbox_with_list_of_check_types import (
            CheckboxWithListOfCheckTypes,
        )
        from ..models.checkbox_with_list_of_contact_groups import (
            CheckboxWithListOfContactGroups,
        )
        from ..models.checkbox_with_list_of_host_groups import (
            CheckboxWithListOfHostGroups,
        )
        from ..models.checkbox_with_list_of_hosts import CheckboxWithListOfHosts
        from ..models.checkbox_with_list_of_labels import CheckboxWithListOfLabels
        from ..models.checkbox_with_list_of_service_groups import (
            CheckboxWithListOfServiceGroups,
        )
        from ..models.checkbox_with_list_of_service_groups_regex import (
            CheckboxWithListOfServiceGroupsRegex,
        )
        from ..models.checkbox_with_list_of_sites import CheckboxWithListOfSites
        from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.checkbox_with_time_period import CheckboxWithTimePeriod

        d = dict(src_dict)

        def _parse_match_sites(
            data: object,
        ) -> Checkbox | CheckboxWithListOfSites | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_sites_checkbox_type_0 = Checkbox.from_dict(data)

                return componentsschemas_match_sites_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_sites_checkbox_type_1 = (
                CheckboxWithListOfSites.from_dict(data)
            )

            return componentsschemas_match_sites_checkbox_type_1

        match_sites = _parse_match_sites(d.pop("match_sites", UNSET))

        def _parse_match_folder(
            data: object,
        ) -> Checkbox | CheckboxWithFolderStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_folder_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_folder_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_folder_checkbox_type_1 = (
                CheckboxWithFolderStr.from_dict(data)
            )

            return componentsschemas_match_folder_checkbox_type_1

        match_folder = _parse_match_folder(d.pop("match_folder", UNSET))

        def _parse_match_host_tags(
            data: object,
        ) -> Checkbox | CheckboxMatchHostTags | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_host_tags_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_host_tags_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_host_tags_checkbox_type_1 = (
                CheckboxMatchHostTags.from_dict(data)
            )

            return componentsschemas_match_host_tags_checkbox_type_1

        match_host_tags = _parse_match_host_tags(d.pop("match_host_tags", UNSET))

        def _parse_match_host_labels(
            data: object,
        ) -> Checkbox | CheckboxWithListOfLabels | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_labels_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_labels_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_labels_checkbox_type_1 = (
                CheckboxWithListOfLabels.from_dict(data)
            )

            return componentsschemas_match_labels_checkbox_type_1

        match_host_labels = _parse_match_host_labels(d.pop("match_host_labels", UNSET))

        def _parse_match_host_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfHostGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_host_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_host_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_host_groups_checkbox_type_1 = (
                CheckboxWithListOfHostGroups.from_dict(data)
            )

            return componentsschemas_match_host_groups_checkbox_type_1

        match_host_groups = _parse_match_host_groups(d.pop("match_host_groups", UNSET))

        def _parse_match_hosts(
            data: object,
        ) -> Checkbox | CheckboxWithListOfHosts | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_hosts_checkbox_type_0 = Checkbox.from_dict(data)

                return componentsschemas_match_hosts_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_hosts_checkbox_type_1 = (
                CheckboxWithListOfHosts.from_dict(data)
            )

            return componentsschemas_match_hosts_checkbox_type_1

        match_hosts = _parse_match_hosts(d.pop("match_hosts", UNSET))

        def _parse_match_exclude_hosts(
            data: object,
        ) -> Checkbox | CheckboxWithListOfHosts | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_hosts_checkbox_type_0 = Checkbox.from_dict(data)

                return componentsschemas_match_hosts_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_hosts_checkbox_type_1 = (
                CheckboxWithListOfHosts.from_dict(data)
            )

            return componentsschemas_match_hosts_checkbox_type_1

        match_exclude_hosts = _parse_match_exclude_hosts(
            d.pop("match_exclude_hosts", UNSET)
        )

        def _parse_match_service_labels(
            data: object,
        ) -> Checkbox | CheckboxWithListOfLabels | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_labels_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_labels_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_labels_checkbox_type_1 = (
                CheckboxWithListOfLabels.from_dict(data)
            )

            return componentsschemas_match_labels_checkbox_type_1

        match_service_labels = _parse_match_service_labels(
            d.pop("match_service_labels", UNSET)
        )

        def _parse_match_service_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfServiceGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_groups_checkbox_type_1 = (
                CheckboxWithListOfServiceGroups.from_dict(data)
            )

            return componentsschemas_match_service_groups_checkbox_type_1

        match_service_groups = _parse_match_service_groups(
            d.pop("match_service_groups", UNSET)
        )

        def _parse_match_exclude_service_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfServiceGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_groups_checkbox_type_1 = (
                CheckboxWithListOfServiceGroups.from_dict(data)
            )

            return componentsschemas_match_service_groups_checkbox_type_1

        match_exclude_service_groups = _parse_match_exclude_service_groups(
            d.pop("match_exclude_service_groups", UNSET)
        )

        def _parse_match_service_groups_regex(
            data: object,
        ) -> Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_group_regex_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_group_regex_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_group_regex_checkbox_type_1 = (
                CheckboxWithListOfServiceGroupsRegex.from_dict(data)
            )

            return componentsschemas_match_service_group_regex_checkbox_type_1

        match_service_groups_regex = _parse_match_service_groups_regex(
            d.pop("match_service_groups_regex", UNSET)
        )

        def _parse_match_exclude_service_groups_regex(
            data: object,
        ) -> Checkbox | CheckboxWithListOfServiceGroupsRegex | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_group_regex_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_group_regex_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_group_regex_checkbox_type_1 = (
                CheckboxWithListOfServiceGroupsRegex.from_dict(data)
            )

            return componentsschemas_match_service_group_regex_checkbox_type_1

        match_exclude_service_groups_regex = _parse_match_exclude_service_groups_regex(
            d.pop("match_exclude_service_groups_regex", UNSET)
        )

        def _parse_match_services(
            data: object,
        ) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_services_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_services_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_services_checkbox_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_match_services_checkbox_type_1

        match_services = _parse_match_services(d.pop("match_services", UNSET))

        def _parse_match_exclude_services(
            data: object,
        ) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_services_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_match_services_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_services_checkbox_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_match_services_checkbox_type_1

        match_exclude_services = _parse_match_exclude_services(
            d.pop("match_exclude_services", UNSET)
        )

        def _parse_match_check_types(
            data: object,
        ) -> Checkbox | CheckboxWithListOfCheckTypes | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_check_types_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_check_types_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_check_types_checkbox_type_1 = (
                CheckboxWithListOfCheckTypes.from_dict(data)
            )

            return componentsschemas_match_check_types_checkbox_type_1

        match_check_types = _parse_match_check_types(d.pop("match_check_types", UNSET))

        def _parse_match_plugin_output(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_string_checkbox_type_0 = Checkbox.from_dict(data)

                return componentsschemas_string_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_string_checkbox_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_string_checkbox_type_1

        match_plugin_output = _parse_match_plugin_output(
            d.pop("match_plugin_output", UNSET)
        )

        def _parse_match_contact_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfContactGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_contact_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_contact_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_contact_groups_checkbox_type_1 = (
                CheckboxWithListOfContactGroups.from_dict(data)
            )

            return componentsschemas_match_contact_groups_checkbox_type_1

        match_contact_groups = _parse_match_contact_groups(
            d.pop("match_contact_groups", UNSET)
        )

        def _parse_match_service_levels(
            data: object,
        ) -> Checkbox | CheckboxWithFromToServiceLevels | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_levels_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_levels_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_levels_checkbox_type_1 = (
                CheckboxWithFromToServiceLevels.from_dict(data)
            )

            return componentsschemas_match_service_levels_checkbox_type_1

        match_service_levels = _parse_match_service_levels(
            d.pop("match_service_levels", UNSET)
        )

        def _parse_match_only_during_time_period(
            data: object,
        ) -> Checkbox | CheckboxWithTimePeriod | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_time_period_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_time_period_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_time_period_checkbox_type_1 = (
                CheckboxWithTimePeriod.from_dict(data)
            )

            return componentsschemas_match_time_period_checkbox_type_1

        match_only_during_time_period = _parse_match_only_during_time_period(
            d.pop("match_only_during_time_period", UNSET)
        )

        def _parse_match_host_event_type(
            data: object,
        ) -> Checkbox | CheckboxHostEventType | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_host_event_type_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_host_event_type_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_host_event_type_checkbox_type_1 = (
                CheckboxHostEventType.from_dict(data)
            )

            return componentsschemas_match_host_event_type_checkbox_type_1

        match_host_event_type = _parse_match_host_event_type(
            d.pop("match_host_event_type", UNSET)
        )

        def _parse_match_service_event_type(
            data: object,
        ) -> Checkbox | CheckboxServiceEventType | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_match_service_event_type_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_match_service_event_type_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_match_service_event_type_checkbox_type_1 = (
                CheckboxServiceEventType.from_dict(data)
            )

            return componentsschemas_match_service_event_type_checkbox_type_1

        match_service_event_type = _parse_match_service_event_type(
            d.pop("match_service_event_type", UNSET)
        )

        def _parse_restrict_to_notification_numbers(
            data: object,
        ) -> Checkbox | CheckboxRestrictNotificationNumbers | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_restrict_notification_num_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_restrict_notification_num_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_restrict_notification_num_checkbox_type_1 = (
                CheckboxRestrictNotificationNumbers.from_dict(data)
            )

            return componentsschemas_restrict_notification_num_checkbox_type_1

        restrict_to_notification_numbers = _parse_restrict_to_notification_numbers(
            d.pop("restrict_to_notification_numbers", UNSET)
        )

        def _parse_throttle_periodic_notifications(
            data: object,
        ) -> Checkbox | CheckboxThrottlePeriodicNotifcations | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_thorttle_periodic_notifications_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_thorttle_periodic_notifications_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_thorttle_periodic_notifications_checkbox_type_1 = (
                CheckboxThrottlePeriodicNotifcations.from_dict(data)
            )

            return componentsschemas_thorttle_periodic_notifications_checkbox_type_1

        throttle_periodic_notifications = _parse_throttle_periodic_notifications(
            d.pop("throttle_periodic_notifications", UNSET)
        )

        def _parse_match_notification_comment(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_string_checkbox_type_0 = Checkbox.from_dict(data)

                return componentsschemas_string_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_string_checkbox_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_string_checkbox_type_1

        match_notification_comment = _parse_match_notification_comment(
            d.pop("match_notification_comment", UNSET)
        )

        def _parse_event_console_alerts(
            data: object,
        ) -> Checkbox | CheckboxEventConsoleAlerts | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_event_console_alert_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_event_console_alert_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_event_console_alert_checkbox_type_1 = (
                CheckboxEventConsoleAlerts.from_dict(data)
            )

            return componentsschemas_event_console_alert_checkbox_type_1

        event_console_alerts = _parse_event_console_alerts(
            d.pop("event_console_alerts", UNSET)
        )

        rule_conditions = cls(
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

        rule_conditions.additional_properties = d
        return rule_conditions

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
