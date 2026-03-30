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
    from ..models.check_box_use_site_id_prefix import CheckBoxUseSiteIDPrefix
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.explicit_token import ExplicitToken
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.mgmnt_type_case_params import MgmntTypeCaseParams
    from ..models.mgmnt_type_incident_params import MgmntTypeIncidentParams


T = TypeVar("T", bound="ServiceNowPluginCreate")


@_attrs_define
class ServiceNowPluginCreate:
    """
    Attributes:
        plugin_name (Any): The ServiceNow plug-in. Default: 'servicenow'. Example: servicenow.
        servicenow_url (str): Configure your ServiceNow URL here Example: https://myservicenow.com.
        auth (AuthStoreToken | BasicAuthExplicit | BasicAuthStorePassword | ExplicitToken):
        http_proxy (Checkbox | HttpProxyValue | Unset):
        use_site_id_prefix (Checkbox | CheckBoxUseSiteIDPrefix | Unset):
        optional_timeout (Checkbox | CheckboxWithStrValue | Unset):
        management_type (MgmntTypeCaseParams | MgmntTypeIncidentParams | Unset):
    """

    servicenow_url: str
    auth: AuthStoreToken | BasicAuthExplicit | BasicAuthStorePassword | ExplicitToken
    plugin_name: Any = "servicenow"
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    use_site_id_prefix: Checkbox | CheckBoxUseSiteIDPrefix | Unset = UNSET
    optional_timeout: Checkbox | CheckboxWithStrValue | Unset = UNSET
    management_type: MgmntTypeCaseParams | MgmntTypeIncidentParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_auth_explicit import BasicAuthExplicit
        from ..models.basic_auth_store_password import BasicAuthStorePassword
        from ..models.checkbox import Checkbox
        from ..models.explicit_token import ExplicitToken
        from ..models.mgmnt_type_case_params import MgmntTypeCaseParams

        plugin_name = self.plugin_name

        servicenow_url = self.servicenow_url

        auth: dict[str, Any]
        if isinstance(self.auth, BasicAuthStorePassword):
            auth = self.auth.to_dict()
        elif isinstance(self.auth, BasicAuthExplicit):
            auth = self.auth.to_dict()
        elif isinstance(self.auth, ExplicitToken):
            auth = self.auth.to_dict()
        else:
            auth = self.auth.to_dict()

        http_proxy: dict[str, Any] | Unset
        if isinstance(self.http_proxy, Unset):
            http_proxy = UNSET
        elif isinstance(self.http_proxy, Checkbox):
            http_proxy = self.http_proxy.to_dict()
        else:
            http_proxy = self.http_proxy.to_dict()

        use_site_id_prefix: dict[str, Any] | Unset
        if isinstance(self.use_site_id_prefix, Unset):
            use_site_id_prefix = UNSET
        elif isinstance(self.use_site_id_prefix, Checkbox):
            use_site_id_prefix = self.use_site_id_prefix.to_dict()
        else:
            use_site_id_prefix = self.use_site_id_prefix.to_dict()

        optional_timeout: dict[str, Any] | Unset
        if isinstance(self.optional_timeout, Unset):
            optional_timeout = UNSET
        elif isinstance(self.optional_timeout, Checkbox):
            optional_timeout = self.optional_timeout.to_dict()
        else:
            optional_timeout = self.optional_timeout.to_dict()

        management_type: dict[str, Any] | Unset
        if isinstance(self.management_type, Unset):
            management_type = UNSET
        elif isinstance(self.management_type, MgmntTypeCaseParams):
            management_type = self.management_type.to_dict()
        else:
            management_type = self.management_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
                "servicenow_url": servicenow_url,
                "auth": auth,
            }
        )
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy
        if use_site_id_prefix is not UNSET:
            field_dict["use_site_id_prefix"] = use_site_id_prefix
        if optional_timeout is not UNSET:
            field_dict["optional_timeout"] = optional_timeout
        if management_type is not UNSET:
            field_dict["management_type"] = management_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_store_token import AuthStoreToken
        from ..models.basic_auth_explicit import BasicAuthExplicit
        from ..models.basic_auth_store_password import BasicAuthStorePassword
        from ..models.check_box_use_site_id_prefix import CheckBoxUseSiteIDPrefix
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.explicit_token import ExplicitToken
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.mgmnt_type_case_params import MgmntTypeCaseParams
        from ..models.mgmnt_type_incident_params import MgmntTypeIncidentParams

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        servicenow_url = d.pop("servicenow_url")

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

        def _parse_use_site_id_prefix(
            data: object,
        ) -> Checkbox | CheckBoxUseSiteIDPrefix | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_site_id_prefix_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_site_id_prefix_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_site_id_prefix_one_of_type_1 = (
                CheckBoxUseSiteIDPrefix.from_dict(data)
            )

            return componentsschemas_site_id_prefix_one_of_type_1

        use_site_id_prefix = _parse_use_site_id_prefix(
            d.pop("use_site_id_prefix", UNSET)
        )

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

        def _parse_management_type(
            data: object,
        ) -> MgmntTypeCaseParams | MgmntTypeIncidentParams | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_mgmnt_type_selector_type_0 = (
                    MgmntTypeCaseParams.from_dict(data)
                )

                return componentsschemas_mgmnt_type_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_mgmnt_type_selector_type_1 = (
                MgmntTypeIncidentParams.from_dict(data)
            )

            return componentsschemas_mgmnt_type_selector_type_1

        management_type = _parse_management_type(d.pop("management_type", UNSET))

        service_now_plugin_create = cls(
            plugin_name=plugin_name,
            servicenow_url=servicenow_url,
            auth=auth,
            http_proxy=http_proxy,
            use_site_id_prefix=use_site_id_prefix,
            optional_timeout=optional_timeout,
            management_type=management_type,
        )

        service_now_plugin_create.additional_properties = d
        return service_now_plugin_create

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
