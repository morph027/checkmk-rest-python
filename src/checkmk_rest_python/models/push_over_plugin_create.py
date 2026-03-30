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
    from ..models.push_over_priority import PushOverPriority
    from ..models.sounds import Sounds


T = TypeVar("T", bound="PushOverPluginCreate")


@_attrs_define
class PushOverPluginCreate:
    """
    Attributes:
        plugin_name (Any): The Pushover plug-in. Default: 'pushover'. Example: pushover.
        api_key (str): You need to provide a valid API key to be able to send push notifications using Pushover.
            Register and login to Pushover, thn create your Check_MK installation as application and obtain your API key
            Example: azGDORePK8gMaC0QOYAMyEEuzJnyUi.
        user_group_key (str): Configure the user or group to receive the notifications by providing the user or group
            key here. The key can be obtained from the Pushover website. Example: azGDORePK8gMaC0QOYAMyEEuzJnyUi.
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
        priority (Checkbox | PushOverPriority | Unset):
        sound (Checkbox | Sounds | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
    """

    api_key: str
    user_group_key: str
    plugin_name: Any = "pushover"
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    priority: Checkbox | PushOverPriority | Unset = UNSET
    sound: Checkbox | Sounds | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        plugin_name = self.plugin_name

        api_key = self.api_key

        user_group_key = self.user_group_key

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

        priority: dict[str, Any] | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, Checkbox):
            priority = self.priority.to_dict()
        else:
            priority = self.priority.to_dict()

        sound: dict[str, Any] | Unset
        if isinstance(self.sound, Unset):
            sound = UNSET
        elif isinstance(self.sound, Checkbox):
            sound = self.sound.to_dict()
        else:
            sound = self.sound.to_dict()

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
                "api_key": api_key,
                "user_group_key": user_group_key,
            }
        )
        if url_prefix_for_links_to_checkmk is not UNSET:
            field_dict["url_prefix_for_links_to_checkmk"] = (
                url_prefix_for_links_to_checkmk
            )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if sound is not UNSET:
            field_dict["sound"] = sound
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
        from ..models.checkbox import Checkbox
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.push_over_priority import PushOverPriority
        from ..models.sounds import Sounds

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        api_key = d.pop("api_key")

        user_group_key = d.pop("user_group_key")

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

        def _parse_priority(data: object) -> Checkbox | PushOverPriority | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_push_over_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_push_over_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_push_over_one_of_type_1 = PushOverPriority.from_dict(data)

            return componentsschemas_push_over_one_of_type_1

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_sound(data: object) -> Checkbox | Sounds | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sounds_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_sounds_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_sounds_one_of_type_1 = Sounds.from_dict(data)

            return componentsschemas_sounds_one_of_type_1

        sound = _parse_sound(d.pop("sound", UNSET))

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

        push_over_plugin_create = cls(
            plugin_name=plugin_name,
            api_key=api_key,
            user_group_key=user_group_key,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
            priority=priority,
            sound=sound,
            http_proxy=http_proxy,
        )

        push_over_plugin_create.additional_properties = d
        return push_over_plugin_create

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
