from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.ms_teams_explicit_webhook_url import MSTeamsExplicitWebhookUrl
    from ..models.ms_teams_url_response import MSTeamsURLResponse


T = TypeVar("T", bound="MSTeamsPluginCreate")


@_attrs_define
class MSTeamsPluginCreate:
    """
    Attributes:
        plugin_name (Any): The MicrosoftTeams plug-in. Default: 'msteams'. Example: msteams.
        webhook_url (MSTeamsExplicitWebhookUrl | MSTeamsURLResponse):
        affected_host_groups (Checkbox | Unset):
        host_details (Checkbox | CheckboxWithStrValue | Unset):
        service_details (Checkbox | CheckboxWithStrValue | Unset):
        host_summary (Checkbox | CheckboxWithStrValue | Unset):
        service_summary (Checkbox | CheckboxWithStrValue | Unset):
        host_title (Checkbox | CheckboxWithStrValue | Unset):
        service_title (Checkbox | CheckboxWithStrValue | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
    """

    webhook_url: MSTeamsExplicitWebhookUrl | MSTeamsURLResponse
    plugin_name: Any = "msteams"
    affected_host_groups: Checkbox | Unset = UNSET
    host_details: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_details: Checkbox | CheckboxWithStrValue | Unset = UNSET
    host_summary: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_summary: Checkbox | CheckboxWithStrValue | Unset = UNSET
    host_title: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_title: Checkbox | CheckboxWithStrValue | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.ms_teams_explicit_webhook_url import MSTeamsExplicitWebhookUrl

        plugin_name = self.plugin_name

        webhook_url: dict[str, Any]
        if isinstance(self.webhook_url, MSTeamsExplicitWebhookUrl):
            webhook_url = self.webhook_url.to_dict()
        else:
            webhook_url = self.webhook_url.to_dict()

        affected_host_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affected_host_groups, Unset):
            affected_host_groups = self.affected_host_groups.to_dict()

        host_details: dict[str, Any] | Unset
        if isinstance(self.host_details, Unset):
            host_details = UNSET
        elif isinstance(self.host_details, Checkbox):
            host_details = self.host_details.to_dict()
        else:
            host_details = self.host_details.to_dict()

        service_details: dict[str, Any] | Unset
        if isinstance(self.service_details, Unset):
            service_details = UNSET
        elif isinstance(self.service_details, Checkbox):
            service_details = self.service_details.to_dict()
        else:
            service_details = self.service_details.to_dict()

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

        host_title: dict[str, Any] | Unset
        if isinstance(self.host_title, Unset):
            host_title = UNSET
        elif isinstance(self.host_title, Checkbox):
            host_title = self.host_title.to_dict()
        else:
            host_title = self.host_title.to_dict()

        service_title: dict[str, Any] | Unset
        if isinstance(self.service_title, Unset):
            service_title = UNSET
        elif isinstance(self.service_title, Checkbox):
            service_title = self.service_title.to_dict()
        else:
            service_title = self.service_title.to_dict()

        http_proxy: dict[str, Any] | Unset
        if isinstance(self.http_proxy, Unset):
            http_proxy = UNSET
        elif isinstance(self.http_proxy, Checkbox):
            http_proxy = self.http_proxy.to_dict()
        else:
            http_proxy = self.http_proxy.to_dict()

        url_prefix_for_links_to_checkmk: dict[str, Any] | Unset
        if isinstance(self.url_prefix_for_links_to_checkmk, Unset):
            url_prefix_for_links_to_checkmk = UNSET
        elif isinstance(self.url_prefix_for_links_to_checkmk, Checkbox):
            url_prefix_for_links_to_checkmk = (
                self.url_prefix_for_links_to_checkmk.to_dict()
            )
        else:
            url_prefix_for_links_to_checkmk = (
                self.url_prefix_for_links_to_checkmk.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
                "webhook_url": webhook_url,
            }
        )
        if affected_host_groups is not UNSET:
            field_dict["affected_host_groups"] = affected_host_groups
        if host_details is not UNSET:
            field_dict["host_details"] = host_details
        if service_details is not UNSET:
            field_dict["service_details"] = service_details
        if host_summary is not UNSET:
            field_dict["host_summary"] = host_summary
        if service_summary is not UNSET:
            field_dict["service_summary"] = service_summary
        if host_title is not UNSET:
            field_dict["host_title"] = host_title
        if service_title is not UNSET:
            field_dict["service_title"] = service_title
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy
        if url_prefix_for_links_to_checkmk is not UNSET:
            field_dict["url_prefix_for_links_to_checkmk"] = (
                url_prefix_for_links_to_checkmk
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.ms_teams_explicit_webhook_url import MSTeamsExplicitWebhookUrl
        from ..models.ms_teams_url_response import MSTeamsURLResponse

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_webhook_url(
            data: object,
        ) -> MSTeamsExplicitWebhookUrl | MSTeamsURLResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ms_teams_url_or_store_selector_type_0 = (
                    MSTeamsExplicitWebhookUrl.from_dict(data)
                )

                return componentsschemas_ms_teams_url_or_store_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ms_teams_url_or_store_selector_type_1 = (
                MSTeamsURLResponse.from_dict(data)
            )

            return componentsschemas_ms_teams_url_or_store_selector_type_1

        webhook_url = _parse_webhook_url(d.pop("webhook_url"))

        _affected_host_groups = d.pop("affected_host_groups", UNSET)
        affected_host_groups: Checkbox | Unset
        if isinstance(_affected_host_groups, Unset):
            affected_host_groups = UNSET
        else:
            affected_host_groups = Checkbox.from_dict(_affected_host_groups)

        def _parse_host_details(
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

        host_details = _parse_host_details(d.pop("host_details", UNSET))

        def _parse_service_details(
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

        service_details = _parse_service_details(d.pop("service_details", UNSET))

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

        def _parse_host_title(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        host_title = _parse_host_title(d.pop("host_title", UNSET))

        def _parse_service_title(
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

        service_title = _parse_service_title(d.pop("service_title", UNSET))

        def _parse_http_proxy(data: object) -> Checkbox | HttpProxyValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_http_proxy_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_http_proxy_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_http_proxy_one_of_type_1 = HttpProxyValue.from_dict(data)

            return componentsschemas_http_proxy_one_of_type_1

        http_proxy = _parse_http_proxy(d.pop("http_proxy", UNSET))

        def _parse_url_prefix_for_links_to_checkmk(
            data: object,
        ) -> Checkbox | CheckMKURLPrefixValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_url_prefix_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_url_prefix_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_url_prefix_one_of_type_1 = (
                CheckMKURLPrefixValue.from_dict(data)
            )

            return componentsschemas_url_prefix_one_of_type_1

        url_prefix_for_links_to_checkmk = _parse_url_prefix_for_links_to_checkmk(
            d.pop("url_prefix_for_links_to_checkmk", UNSET)
        )

        ms_teams_plugin_create = cls(
            plugin_name=plugin_name,
            webhook_url=webhook_url,
            affected_host_groups=affected_host_groups,
            host_details=host_details,
            service_details=service_details,
            host_summary=host_summary,
            service_summary=service_summary,
            host_title=host_title,
            service_title=service_title,
            http_proxy=http_proxy,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
        )

        ms_teams_plugin_create.additional_properties = d
        return ms_teams_plugin_create

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
