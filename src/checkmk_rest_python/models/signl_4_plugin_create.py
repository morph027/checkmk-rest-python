from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
    from ..models.checkbox import Checkbox
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.sign_l4_team_secret import SignL4TeamSecret
    from ..models.sign_l4_team_secret_store_id import SignL4TeamSecretStoreID


T = TypeVar("T", bound="Signl4PluginCreate")


@_attrs_define
class Signl4PluginCreate:
    """
    Attributes:
        plugin_name (Any): The Signl4 plug-in. Default: 'signl4'. Example: signl4.
        team_secret (SignL4TeamSecret | SignL4TeamSecretStoreID):
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
        disable_ssl_cert_verification (Checkbox | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
    """

    team_secret: SignL4TeamSecret | SignL4TeamSecretStoreID
    plugin_name: Any = "signl4"
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.sign_l4_team_secret import SignL4TeamSecret

        plugin_name = self.plugin_name

        team_secret: dict[str, Any]
        if isinstance(self.team_secret, SignL4TeamSecret):
            team_secret = self.team_secret.to_dict()
        else:
            team_secret = self.team_secret.to_dict()

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

        disable_ssl_cert_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = self.disable_ssl_cert_verification.to_dict()

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
                "team_secret": team_secret,
            }
        )
        if url_prefix_for_links_to_checkmk is not UNSET:
            field_dict["url_prefix_for_links_to_checkmk"] = (
                url_prefix_for_links_to_checkmk
            )
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
        from ..models.checkbox import Checkbox
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.sign_l4_team_secret import SignL4TeamSecret
        from ..models.sign_l4_team_secret_store_id import SignL4TeamSecretStoreID

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_team_secret(
            data: object,
        ) -> SignL4TeamSecret | SignL4TeamSecretStoreID:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sign_l4_explicit_or_store_selector_type_0 = (
                    SignL4TeamSecret.from_dict(data)
                )

                return componentsschemas_sign_l4_explicit_or_store_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_sign_l4_explicit_or_store_selector_type_1 = (
                SignL4TeamSecretStoreID.from_dict(data)
            )

            return componentsschemas_sign_l4_explicit_or_store_selector_type_1

        team_secret = _parse_team_secret(d.pop("team_secret"))

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

        _disable_ssl_cert_verification = d.pop("disable_ssl_cert_verification", UNSET)
        disable_ssl_cert_verification: Checkbox | Unset
        if isinstance(_disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = UNSET
        else:
            disable_ssl_cert_verification = Checkbox.from_dict(
                _disable_ssl_cert_verification
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

        signl_4_plugin_create = cls(
            plugin_name=plugin_name,
            team_secret=team_secret,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            http_proxy=http_proxy,
        )

        signl_4_plugin_create.additional_properties = d
        return signl_4_plugin_create

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
