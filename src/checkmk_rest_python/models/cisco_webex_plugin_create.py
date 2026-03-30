from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
    from ..models.checkbox import Checkbox
    from ..models.cisco_explicit_webhook_url import CiscoExplicitWebhookUrl
    from ..models.cisco_password_store import CiscoPasswordStore
    from ..models.http_proxy_value import HttpProxyValue


T = TypeVar("T", bound="CiscoWebexPluginCreate")


@_attrs_define
class CiscoWebexPluginCreate:
    """
    Attributes:
        plugin_name (Any): The Cisco plug-in. Default: 'cisco_webex_teams'. Example: cisco_webex_teams.
        disable_ssl_cert_verification (Checkbox | Unset):
        webhook_url (CiscoExplicitWebhookUrl | CiscoPasswordStore | Unset):
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
    """

    plugin_name: Any = "cisco_webex_teams"
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    webhook_url: CiscoExplicitWebhookUrl | CiscoPasswordStore | Unset = UNSET
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.cisco_explicit_webhook_url import CiscoExplicitWebhookUrl

        plugin_name = self.plugin_name

        disable_ssl_cert_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = self.disable_ssl_cert_verification.to_dict()

        webhook_url: dict[str, Any] | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        elif isinstance(self.webhook_url, CiscoExplicitWebhookUrl):
            webhook_url = self.webhook_url.to_dict()
        else:
            webhook_url = self.webhook_url.to_dict()

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

        http_proxy: dict[str, Any] | Unset
        if isinstance(self.http_proxy, Unset):
            http_proxy = UNSET
        elif isinstance(self.http_proxy, Checkbox):
            http_proxy = self.http_proxy.to_dict()
        else:
            http_proxy = self.http_proxy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
            }
        )
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if url_prefix_for_links_to_checkmk is not UNSET:
            field_dict["url_prefix_for_links_to_checkmk"] = (
                url_prefix_for_links_to_checkmk
            )
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
        from ..models.checkbox import Checkbox
        from ..models.cisco_explicit_webhook_url import CiscoExplicitWebhookUrl
        from ..models.cisco_password_store import CiscoPasswordStore
        from ..models.http_proxy_value import HttpProxyValue

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        _disable_ssl_cert_verification = d.pop("disable_ssl_cert_verification", UNSET)
        disable_ssl_cert_verification: Checkbox | Unset
        if isinstance(_disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = UNSET
        else:
            disable_ssl_cert_verification = Checkbox.from_dict(
                _disable_ssl_cert_verification
            )

        def _parse_webhook_url(
            data: object,
        ) -> CiscoExplicitWebhookUrl | CiscoPasswordStore | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_cisco_url_or_store_selector_type_0 = (
                    CiscoExplicitWebhookUrl.from_dict(data)
                )

                return componentsschemas_cisco_url_or_store_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_cisco_url_or_store_selector_type_1 = (
                CiscoPasswordStore.from_dict(data)
            )

            return componentsschemas_cisco_url_or_store_selector_type_1

        webhook_url = _parse_webhook_url(d.pop("webhook_url", UNSET))

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

        cisco_webex_plugin_create = cls(
            plugin_name=plugin_name,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            webhook_url=webhook_url,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
            http_proxy=http_proxy,
        )

        cisco_webex_plugin_create.additional_properties = d
        return cisco_webex_plugin_create

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
