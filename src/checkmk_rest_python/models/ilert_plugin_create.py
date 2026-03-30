from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ilert_plugin_create_notification_priority import (
    IlertPluginCreateNotificationPriority,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
    from ..models.checkbox import Checkbox
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.ilert_api_key import IlertAPIKey
    from ..models.ilert_password_store_id import IlertPasswordStoreID


T = TypeVar("T", bound="IlertPluginCreate")


@_attrs_define
class IlertPluginCreate:
    """
    Attributes:
        plugin_name (Any): The Ilert plug-in. Default: 'ilert'. Example: ilert.
        notification_priority (IlertPluginCreateNotificationPriority): HIGH - with escalation, LOW - without escalation
            Example: HIGH.
        custom_summary_for_host_alerts (str): A custom summary for host alerts Example: $NOTIFICATIONTYPE$ Host Alert:
            $HOSTNAME$ is $HOSTSTATE$ - $HOSTOUTPUT$.
        custom_summary_for_service_alerts (str): A custom summary for service alerts Example: $NOTIFICATIONTYPE$ Service
            Alert: $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$ - $SERVICEOUTPUT$.
        api_key (IlertAPIKey | IlertPasswordStoreID):
        disable_ssl_cert_verification (Checkbox | Unset):
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
    """

    notification_priority: IlertPluginCreateNotificationPriority
    custom_summary_for_host_alerts: str
    custom_summary_for_service_alerts: str
    api_key: IlertAPIKey | IlertPasswordStoreID
    plugin_name: Any = "ilert"
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.ilert_api_key import IlertAPIKey

        plugin_name = self.plugin_name

        notification_priority = self.notification_priority.value

        custom_summary_for_host_alerts = self.custom_summary_for_host_alerts

        custom_summary_for_service_alerts = self.custom_summary_for_service_alerts

        api_key: dict[str, Any]
        if isinstance(self.api_key, IlertAPIKey):
            api_key = self.api_key.to_dict()
        else:
            api_key = self.api_key.to_dict()

        disable_ssl_cert_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = self.disable_ssl_cert_verification.to_dict()

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
                "notification_priority": notification_priority,
                "custom_summary_for_host_alerts": custom_summary_for_host_alerts,
                "custom_summary_for_service_alerts": custom_summary_for_service_alerts,
                "api_key": api_key,
            }
        )
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
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
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.ilert_api_key import IlertAPIKey
        from ..models.ilert_password_store_id import IlertPasswordStoreID

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        notification_priority = IlertPluginCreateNotificationPriority(
            d.pop("notification_priority")
        )

        custom_summary_for_host_alerts = d.pop("custom_summary_for_host_alerts")

        custom_summary_for_service_alerts = d.pop("custom_summary_for_service_alerts")

        def _parse_api_key(data: object) -> IlertAPIKey | IlertPasswordStoreID:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ilert_key_or_store_selector_type_0 = (
                    IlertAPIKey.from_dict(data)
                )

                return componentsschemas_ilert_key_or_store_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ilert_key_or_store_selector_type_1 = (
                IlertPasswordStoreID.from_dict(data)
            )

            return componentsschemas_ilert_key_or_store_selector_type_1

        api_key = _parse_api_key(d.pop("api_key"))

        _disable_ssl_cert_verification = d.pop("disable_ssl_cert_verification", UNSET)
        disable_ssl_cert_verification: Checkbox | Unset
        if isinstance(_disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = UNSET
        else:
            disable_ssl_cert_verification = Checkbox.from_dict(
                _disable_ssl_cert_verification
            )

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

        ilert_plugin_create = cls(
            plugin_name=plugin_name,
            notification_priority=notification_priority,
            custom_summary_for_host_alerts=custom_summary_for_host_alerts,
            custom_summary_for_service_alerts=custom_summary_for_service_alerts,
            api_key=api_key,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
            http_proxy=http_proxy,
        )

        ilert_plugin_create.additional_properties = d
        return ilert_plugin_create

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
