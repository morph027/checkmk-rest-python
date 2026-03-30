from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_store_token import AuthStoreToken
    from ..models.basic_auth_explicit import BasicAuthExplicit
    from ..models.basic_auth_store_password import BasicAuthStorePassword
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.explicit_token import ExplicitToken
    from ..models.graphs_per_notification import GraphsPerNotification


T = TypeVar("T", bound="JiraPluginCreate")


@_attrs_define
class JiraPluginCreate:
    """
    Attributes:
        plugin_name (Any): The Jira plug-in. Default: 'jira_issues'. Example: jira_issues.
        auth (AuthStoreToken | BasicAuthExplicit | BasicAuthStorePassword | ExplicitToken):
        host_custom_id (str): The numerical Jira custom field ID for host problems
        service_custom_id (str): The numerical Jira custom field ID for service problems
        monitoring_url (str): Configure the base URL for the monitoring web GUI here. Include the site name. Used for
            linking to Checkmk out of Jira
        jira_url (str | Unset): Configure the Jira URL here Example: http://jira_url_example.com.
        disable_ssl_cert_verification (Checkbox | Unset):
        project_id (str | Unset): The numerical Jira project ID. If not set, it will be retrieved from a custom user
            attribute named jiraproject. If that is not set, the notification will fail Default: ''.
        issue_type_id (str | Unset): The numerical Jira issue type ID. If not set, it will be retrieved from a custom
            user attribute named jiraissuetype. If that is not set, the notification will fail Default: ''.
        site_custom_id (Checkbox | CheckboxWithStrValue | Unset):
        priority_id (Checkbox | CheckboxWithStrValue | Unset):
        host_summary (Checkbox | CheckboxWithStrValue | Unset):
        service_summary (Checkbox | CheckboxWithStrValue | Unset):
        label (Checkbox | CheckboxWithStrValue | Unset):
        graphs_per_notification (Checkbox | GraphsPerNotification | Unset):
        resolution_id (Checkbox | CheckboxWithStrValue | Unset):
        optional_timeout (Checkbox | CheckboxWithStrValue | Unset):
    """

    auth: AuthStoreToken | BasicAuthExplicit | BasicAuthStorePassword | ExplicitToken
    host_custom_id: str
    service_custom_id: str
    monitoring_url: str
    plugin_name: Any = "jira_issues"
    jira_url: str | Unset = UNSET
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    project_id: str | Unset = ""
    issue_type_id: str | Unset = ""
    site_custom_id: Checkbox | CheckboxWithStrValue | Unset = UNSET
    priority_id: Checkbox | CheckboxWithStrValue | Unset = UNSET
    host_summary: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_summary: Checkbox | CheckboxWithStrValue | Unset = UNSET
    label: Checkbox | CheckboxWithStrValue | Unset = UNSET
    graphs_per_notification: Checkbox | GraphsPerNotification | Unset = UNSET
    resolution_id: Checkbox | CheckboxWithStrValue | Unset = UNSET
    optional_timeout: Checkbox | CheckboxWithStrValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_auth_explicit import BasicAuthExplicit
        from ..models.basic_auth_store_password import BasicAuthStorePassword
        from ..models.checkbox import Checkbox
        from ..models.explicit_token import ExplicitToken

        plugin_name = self.plugin_name

        auth: dict[str, Any]
        if isinstance(self.auth, BasicAuthStorePassword):
            auth = self.auth.to_dict()
        elif isinstance(self.auth, BasicAuthExplicit):
            auth = self.auth.to_dict()
        elif isinstance(self.auth, ExplicitToken):
            auth = self.auth.to_dict()
        else:
            auth = self.auth.to_dict()

        host_custom_id = self.host_custom_id

        service_custom_id = self.service_custom_id

        monitoring_url = self.monitoring_url

        jira_url = self.jira_url

        disable_ssl_cert_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = self.disable_ssl_cert_verification.to_dict()

        project_id = self.project_id

        issue_type_id = self.issue_type_id

        site_custom_id: dict[str, Any] | Unset
        if isinstance(self.site_custom_id, Unset):
            site_custom_id = UNSET
        elif isinstance(self.site_custom_id, Checkbox):
            site_custom_id = self.site_custom_id.to_dict()
        else:
            site_custom_id = self.site_custom_id.to_dict()

        priority_id: dict[str, Any] | Unset
        if isinstance(self.priority_id, Unset):
            priority_id = UNSET
        elif isinstance(self.priority_id, Checkbox):
            priority_id = self.priority_id.to_dict()
        else:
            priority_id = self.priority_id.to_dict()

        host_summary: dict[str, Any] | Unset
        if isinstance(self.host_summary, Unset):
            host_summary = UNSET
        elif isinstance(self.host_summary, Checkbox):
            host_summary = self.host_summary.to_dict()
        else:
            host_summary = self.host_summary.to_dict()

        service_summary: dict[str, Any] | Unset
        if isinstance(self.service_summary, Unset):
            service_summary = UNSET
        elif isinstance(self.service_summary, Checkbox):
            service_summary = self.service_summary.to_dict()
        else:
            service_summary = self.service_summary.to_dict()

        label: dict[str, Any] | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, Checkbox):
            label = self.label.to_dict()
        else:
            label = self.label.to_dict()

        graphs_per_notification: dict[str, Any] | Unset
        if isinstance(self.graphs_per_notification, Unset):
            graphs_per_notification = UNSET
        elif isinstance(self.graphs_per_notification, Checkbox):
            graphs_per_notification = self.graphs_per_notification.to_dict()
        else:
            graphs_per_notification = self.graphs_per_notification.to_dict()

        resolution_id: dict[str, Any] | Unset
        if isinstance(self.resolution_id, Unset):
            resolution_id = UNSET
        elif isinstance(self.resolution_id, Checkbox):
            resolution_id = self.resolution_id.to_dict()
        else:
            resolution_id = self.resolution_id.to_dict()

        optional_timeout: dict[str, Any] | Unset
        if isinstance(self.optional_timeout, Unset):
            optional_timeout = UNSET
        elif isinstance(self.optional_timeout, Checkbox):
            optional_timeout = self.optional_timeout.to_dict()
        else:
            optional_timeout = self.optional_timeout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
                "auth": auth,
                "host_custom_id": host_custom_id,
                "service_custom_id": service_custom_id,
                "monitoring_url": monitoring_url,
            }
        )
        if jira_url is not UNSET:
            field_dict["jira_url"] = jira_url
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if issue_type_id is not UNSET:
            field_dict["issue_type_id"] = issue_type_id
        if site_custom_id is not UNSET:
            field_dict["site_custom_id"] = site_custom_id
        if priority_id is not UNSET:
            field_dict["priority_id"] = priority_id
        if host_summary is not UNSET:
            field_dict["host_summary"] = host_summary
        if service_summary is not UNSET:
            field_dict["service_summary"] = service_summary
        if label is not UNSET:
            field_dict["label"] = label
        if graphs_per_notification is not UNSET:
            field_dict["graphs_per_notification"] = graphs_per_notification
        if resolution_id is not UNSET:
            field_dict["resolution_id"] = resolution_id
        if optional_timeout is not UNSET:
            field_dict["optional_timeout"] = optional_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_store_token import AuthStoreToken
        from ..models.basic_auth_explicit import BasicAuthExplicit
        from ..models.basic_auth_store_password import BasicAuthStorePassword
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.explicit_token import ExplicitToken
        from ..models.graphs_per_notification import GraphsPerNotification

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_auth(
            data: object,
        ) -> (
            AuthStoreToken | BasicAuthExplicit | BasicAuthStorePassword | ExplicitToken
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_selector_type_0 = (
                    BasicAuthStorePassword.from_dict(data)
                )

                return componentsschemas_auth_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_selector_type_1 = BasicAuthExplicit.from_dict(
                    data
                )

                return componentsschemas_auth_selector_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_selector_type_2 = ExplicitToken.from_dict(data)

                return componentsschemas_auth_selector_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_auth_selector_type_3 = AuthStoreToken.from_dict(data)

            return componentsschemas_auth_selector_type_3

        auth = _parse_auth(d.pop("auth"))

        host_custom_id = d.pop("host_custom_id")

        service_custom_id = d.pop("service_custom_id")

        monitoring_url = d.pop("monitoring_url")

        jira_url = d.pop("jira_url", UNSET)

        _disable_ssl_cert_verification = d.pop("disable_ssl_cert_verification", UNSET)
        disable_ssl_cert_verification: Checkbox | Unset
        if isinstance(_disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = UNSET
        else:
            disable_ssl_cert_verification = Checkbox.from_dict(
                _disable_ssl_cert_verification
            )

        project_id = d.pop("project_id", UNSET)

        issue_type_id = d.pop("issue_type_id", UNSET)

        def _parse_site_custom_id(
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

        site_custom_id = _parse_site_custom_id(d.pop("site_custom_id", UNSET))

        def _parse_priority_id(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        priority_id = _parse_priority_id(d.pop("priority_id", UNSET))

        def _parse_host_summary(
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

        host_summary = _parse_host_summary(d.pop("host_summary", UNSET))

        def _parse_service_summary(
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

        service_summary = _parse_service_summary(d.pop("service_summary", UNSET))

        def _parse_label(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        label = _parse_label(d.pop("label", UNSET))

        def _parse_graphs_per_notification(
            data: object,
        ) -> Checkbox | GraphsPerNotification | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_graphs_per_notification_one_of_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_graphs_per_notification_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_graphs_per_notification_one_of_type_1 = (
                GraphsPerNotification.from_dict(data)
            )

            return componentsschemas_graphs_per_notification_one_of_type_1

        graphs_per_notification = _parse_graphs_per_notification(
            d.pop("graphs_per_notification", UNSET)
        )

        def _parse_resolution_id(
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

        resolution_id = _parse_resolution_id(d.pop("resolution_id", UNSET))

        def _parse_optional_timeout(
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

        optional_timeout = _parse_optional_timeout(d.pop("optional_timeout", UNSET))

        jira_plugin_create = cls(
            plugin_name=plugin_name,
            auth=auth,
            host_custom_id=host_custom_id,
            service_custom_id=service_custom_id,
            monitoring_url=monitoring_url,
            jira_url=jira_url,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            project_id=project_id,
            issue_type_id=issue_type_id,
            site_custom_id=site_custom_id,
            priority_id=priority_id,
            host_summary=host_summary,
            service_summary=service_summary,
            label=label,
            graphs_per_notification=graphs_per_notification,
            resolution_id=resolution_id,
            optional_timeout=optional_timeout,
        )

        jira_plugin_create.additional_properties = d
        return jira_plugin_create

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
