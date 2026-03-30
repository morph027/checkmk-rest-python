from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.smsapi_plugin_create_modem_type import SMSAPIPluginCreateModemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.smsapi_explicit_password import SMSAPIExplicitPassword
    from ..models.smsapip_store_id import SMSAPIPStoreID


T = TypeVar("T", bound="SMSAPIPluginCreate")


@_attrs_define
class SMSAPIPluginCreate:
    """
    Attributes:
        plugin_name (Any): The SMS API plug-in. Default: 'sms_api'. Example: sms_api.
        modem_url (str): Configure your modem URL here Example: https://mymodem.mydomain.example.
        username (str): Configure the user name here Example: username_a.
        user_password (SMSAPIExplicitPassword | SMSAPIPStoreID):
        modem_type (SMSAPIPluginCreateModemType | Unset): Choose what modem is used. Currently supported is only
            Teltonika-TRB140. Default: SMSAPIPluginCreateModemType.TRB140. Example: trb140.
        disable_ssl_cert_verification (Checkbox | Unset):
        timeout (str | Unset): Here you can configure timeout settings Default: '10'. Example: 10.
        http_proxy (Checkbox | HttpProxyValue | Unset):
    """

    modem_url: str
    username: str
    user_password: SMSAPIExplicitPassword | SMSAPIPStoreID
    plugin_name: Any = "sms_api"
    modem_type: SMSAPIPluginCreateModemType | Unset = SMSAPIPluginCreateModemType.TRB140
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    timeout: str | Unset = "10"
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.smsapi_explicit_password import SMSAPIExplicitPassword

        plugin_name = self.plugin_name

        modem_url = self.modem_url

        username = self.username

        user_password: dict[str, Any]
        if isinstance(self.user_password, SMSAPIExplicitPassword):
            user_password = self.user_password.to_dict()
        else:
            user_password = self.user_password.to_dict()

        modem_type: str | Unset = UNSET
        if not isinstance(self.modem_type, Unset):
            modem_type = self.modem_type.value

        disable_ssl_cert_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = self.disable_ssl_cert_verification.to_dict()

        timeout = self.timeout

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
                "modem_url": modem_url,
                "username": username,
                "user_password": user_password,
            }
        )
        if modem_type is not UNSET:
            field_dict["modem_type"] = modem_type
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.smsapi_explicit_password import SMSAPIExplicitPassword
        from ..models.smsapip_store_id import SMSAPIPStoreID

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        modem_url = d.pop("modem_url")

        username = d.pop("username")

        def _parse_user_password(
            data: object,
        ) -> SMSAPIExplicitPassword | SMSAPIPStoreID:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_smsapi_password_selector_type_0 = (
                    SMSAPIExplicitPassword.from_dict(data)
                )

                return componentsschemas_smsapi_password_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_smsapi_password_selector_type_1 = (
                SMSAPIPStoreID.from_dict(data)
            )

            return componentsschemas_smsapi_password_selector_type_1

        user_password = _parse_user_password(d.pop("user_password"))

        _modem_type = d.pop("modem_type", UNSET)
        modem_type: SMSAPIPluginCreateModemType | Unset
        if isinstance(_modem_type, Unset):
            modem_type = UNSET
        else:
            modem_type = SMSAPIPluginCreateModemType(_modem_type)

        _disable_ssl_cert_verification = d.pop("disable_ssl_cert_verification", UNSET)
        disable_ssl_cert_verification: Checkbox | Unset
        if isinstance(_disable_ssl_cert_verification, Unset):
            disable_ssl_cert_verification = UNSET
        else:
            disable_ssl_cert_verification = Checkbox.from_dict(
                _disable_ssl_cert_verification
            )

        timeout = d.pop("timeout", UNSET)

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

        smsapi_plugin_create = cls(
            plugin_name=plugin_name,
            modem_url=modem_url,
            username=username,
            user_password=user_password,
            modem_type=modem_type,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            timeout=timeout,
            http_proxy=http_proxy,
        )

        smsapi_plugin_create.additional_properties = d
        return smsapi_plugin_create

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
