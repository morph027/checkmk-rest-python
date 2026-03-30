from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_ops_genie_priority_value import CheckboxOpsGeniePriorityValue
    from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.http_proxy_value import HttpProxyValue
    from ..models.list_of_extra_properties import ListOfExtraProperties
    from ..models.ops_genie_explicit_key import OpsGenieExplicitKey
    from ..models.ops_genie_store_id import OpsGenieStoreID


T = TypeVar("T", bound="OpsGeniePluginCreate")


@_attrs_define
class OpsGeniePluginCreate:
    """
    Attributes:
        plugin_name (Any): The OpsGenie plug-in. Default: 'opsgenie_issues'. Example: opsgenie_issues.
        api_key (OpsGenieExplicitKey | OpsGenieStoreID):
        domain (Checkbox | CheckboxWithStrValue | Unset):
        disable_ssl_cert_verification (Checkbox | Unset):
        http_proxy (Checkbox | HttpProxyValue | Unset):
        owner (Checkbox | CheckboxWithStrValue | Unset):
        source (Checkbox | CheckboxWithStrValue | Unset):
        priority (Checkbox | CheckboxOpsGeniePriorityValue | Unset):
        note_while_creating (Checkbox | CheckboxWithStrValue | Unset):
        note_while_closing (Checkbox | CheckboxWithStrValue | Unset):
        desc_for_host_alerts (Checkbox | CheckboxWithStrValue | Unset):
        desc_for_service_alerts (Checkbox | CheckboxWithStrValue | Unset):
        message_for_host_alerts (Checkbox | CheckboxWithStrValue | Unset):
        message_for_service_alerts (Checkbox | CheckboxWithStrValue | Unset):
        responsible_teams (Checkbox | CheckboxWithListOfStr | Unset):
        actions (Checkbox | CheckboxWithListOfStr | Unset):
        tags (Checkbox | CheckboxWithListOfStr | Unset):
        entity (Checkbox | CheckboxWithStrValue | Unset):
        extra_properties (Checkbox | ListOfExtraProperties | Unset):
    """

    api_key: OpsGenieExplicitKey | OpsGenieStoreID
    plugin_name: Any = "opsgenie_issues"
    domain: Checkbox | CheckboxWithStrValue | Unset = UNSET
    disable_ssl_cert_verification: Checkbox | Unset = UNSET
    http_proxy: Checkbox | HttpProxyValue | Unset = UNSET
    owner: Checkbox | CheckboxWithStrValue | Unset = UNSET
    source: Checkbox | CheckboxWithStrValue | Unset = UNSET
    priority: Checkbox | CheckboxOpsGeniePriorityValue | Unset = UNSET
    note_while_creating: Checkbox | CheckboxWithStrValue | Unset = UNSET
    note_while_closing: Checkbox | CheckboxWithStrValue | Unset = UNSET
    desc_for_host_alerts: Checkbox | CheckboxWithStrValue | Unset = UNSET
    desc_for_service_alerts: Checkbox | CheckboxWithStrValue | Unset = UNSET
    message_for_host_alerts: Checkbox | CheckboxWithStrValue | Unset = UNSET
    message_for_service_alerts: Checkbox | CheckboxWithStrValue | Unset = UNSET
    responsible_teams: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    actions: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    tags: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    entity: Checkbox | CheckboxWithStrValue | Unset = UNSET
    extra_properties: Checkbox | ListOfExtraProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox
        from ..models.ops_genie_explicit_key import OpsGenieExplicitKey

        plugin_name = self.plugin_name

        api_key: dict[str, Any]
        if isinstance(self.api_key, OpsGenieExplicitKey):
            api_key = self.api_key.to_dict()
        else:
            api_key = self.api_key.to_dict()

        domain: dict[str, Any] | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        elif isinstance(self.domain, Checkbox):
            domain = self.domain.to_dict()
        else:
            domain = self.domain.to_dict()

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

        owner: dict[str, Any] | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        elif isinstance(self.owner, Checkbox):
            owner = self.owner.to_dict()
        else:
            owner = self.owner.to_dict()

        source: dict[str, Any] | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, Checkbox):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        priority: dict[str, Any] | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, Checkbox):
            priority = self.priority.to_dict()
        else:
            priority = self.priority.to_dict()

        note_while_creating: dict[str, Any] | Unset
        if isinstance(self.note_while_creating, Unset):
            note_while_creating = UNSET
        elif isinstance(self.note_while_creating, Checkbox):
            note_while_creating = self.note_while_creating.to_dict()
        else:
            note_while_creating = self.note_while_creating.to_dict()

        note_while_closing: dict[str, Any] | Unset
        if isinstance(self.note_while_closing, Unset):
            note_while_closing = UNSET
        elif isinstance(self.note_while_closing, Checkbox):
            note_while_closing = self.note_while_closing.to_dict()
        else:
            note_while_closing = self.note_while_closing.to_dict()

        desc_for_host_alerts: dict[str, Any] | Unset
        if isinstance(self.desc_for_host_alerts, Unset):
            desc_for_host_alerts = UNSET
        elif isinstance(self.desc_for_host_alerts, Checkbox):
            desc_for_host_alerts = self.desc_for_host_alerts.to_dict()
        else:
            desc_for_host_alerts = self.desc_for_host_alerts.to_dict()

        desc_for_service_alerts: dict[str, Any] | Unset
        if isinstance(self.desc_for_service_alerts, Unset):
            desc_for_service_alerts = UNSET
        elif isinstance(self.desc_for_service_alerts, Checkbox):
            desc_for_service_alerts = self.desc_for_service_alerts.to_dict()
        else:
            desc_for_service_alerts = self.desc_for_service_alerts.to_dict()

        message_for_host_alerts: dict[str, Any] | Unset
        if isinstance(self.message_for_host_alerts, Unset):
            message_for_host_alerts = UNSET
        elif isinstance(self.message_for_host_alerts, Checkbox):
            message_for_host_alerts = self.message_for_host_alerts.to_dict()
        else:
            message_for_host_alerts = self.message_for_host_alerts.to_dict()

        message_for_service_alerts: dict[str, Any] | Unset
        if isinstance(self.message_for_service_alerts, Unset):
            message_for_service_alerts = UNSET
        elif isinstance(self.message_for_service_alerts, Checkbox):
            message_for_service_alerts = self.message_for_service_alerts.to_dict()
        else:
            message_for_service_alerts = self.message_for_service_alerts.to_dict()

        responsible_teams: dict[str, Any] | Unset
        if isinstance(self.responsible_teams, Unset):
            responsible_teams = UNSET
        elif isinstance(self.responsible_teams, Checkbox):
            responsible_teams = self.responsible_teams.to_dict()
        else:
            responsible_teams = self.responsible_teams.to_dict()

        actions: dict[str, Any] | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, Checkbox):
            actions = self.actions.to_dict()
        else:
            actions = self.actions.to_dict()

        tags: dict[str, Any] | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, Checkbox):
            tags = self.tags.to_dict()
        else:
            tags = self.tags.to_dict()

        entity: dict[str, Any] | Unset
        if isinstance(self.entity, Unset):
            entity = UNSET
        elif isinstance(self.entity, Checkbox):
            entity = self.entity.to_dict()
        else:
            entity = self.entity.to_dict()

        extra_properties: dict[str, Any] | Unset
        if isinstance(self.extra_properties, Unset):
            extra_properties = UNSET
        elif isinstance(self.extra_properties, Checkbox):
            extra_properties = self.extra_properties.to_dict()
        else:
            extra_properties = self.extra_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
                "api_key": api_key,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if disable_ssl_cert_verification is not UNSET:
            field_dict["disable_ssl_cert_verification"] = disable_ssl_cert_verification
        if http_proxy is not UNSET:
            field_dict["http_proxy"] = http_proxy
        if owner is not UNSET:
            field_dict["owner"] = owner
        if source is not UNSET:
            field_dict["source"] = source
        if priority is not UNSET:
            field_dict["priority"] = priority
        if note_while_creating is not UNSET:
            field_dict["note_while_creating"] = note_while_creating
        if note_while_closing is not UNSET:
            field_dict["note_while_closing"] = note_while_closing
        if desc_for_host_alerts is not UNSET:
            field_dict["desc_for_host_alerts"] = desc_for_host_alerts
        if desc_for_service_alerts is not UNSET:
            field_dict["desc_for_service_alerts"] = desc_for_service_alerts
        if message_for_host_alerts is not UNSET:
            field_dict["message_for_host_alerts"] = message_for_host_alerts
        if message_for_service_alerts is not UNSET:
            field_dict["message_for_service_alerts"] = message_for_service_alerts
        if responsible_teams is not UNSET:
            field_dict["responsible_teams"] = responsible_teams
        if actions is not UNSET:
            field_dict["actions"] = actions
        if tags is not UNSET:
            field_dict["tags"] = tags
        if entity is not UNSET:
            field_dict["entity"] = entity
        if extra_properties is not UNSET:
            field_dict["extra_properties"] = extra_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.checkbox_ops_genie_priority_value import (
            CheckboxOpsGeniePriorityValue,
        )
        from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.http_proxy_value import HttpProxyValue
        from ..models.list_of_extra_properties import ListOfExtraProperties
        from ..models.ops_genie_explicit_key import OpsGenieExplicitKey
        from ..models.ops_genie_store_id import OpsGenieStoreID

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_api_key(data: object) -> OpsGenieExplicitKey | OpsGenieStoreID:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ops_genis_store_or_explicit_key_selector_type_0 = (
                    OpsGenieExplicitKey.from_dict(data)
                )

                return componentsschemas_ops_genis_store_or_explicit_key_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ops_genis_store_or_explicit_key_selector_type_1 = (
                OpsGenieStoreID.from_dict(data)
            )

            return componentsschemas_ops_genis_store_or_explicit_key_selector_type_1

        api_key = _parse_api_key(d.pop("api_key"))

        def _parse_domain(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        domain = _parse_domain(d.pop("domain", UNSET))

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

        def _parse_owner(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        owner = _parse_owner(d.pop("owner", UNSET))

        def _parse_source(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        source = _parse_source(d.pop("source", UNSET))

        def _parse_priority(
            data: object,
        ) -> Checkbox | CheckboxOpsGeniePriorityValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ops_genie_priority_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_ops_genie_priority_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_ops_genie_priority_one_of_type_1 = (
                CheckboxOpsGeniePriorityValue.from_dict(data)
            )

            return componentsschemas_ops_genie_priority_one_of_type_1

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_note_while_creating(
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

        note_while_creating = _parse_note_while_creating(
            d.pop("note_while_creating", UNSET)
        )

        def _parse_note_while_closing(
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

        note_while_closing = _parse_note_while_closing(
            d.pop("note_while_closing", UNSET)
        )

        def _parse_desc_for_host_alerts(
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

        desc_for_host_alerts = _parse_desc_for_host_alerts(
            d.pop("desc_for_host_alerts", UNSET)
        )

        def _parse_desc_for_service_alerts(
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

        desc_for_service_alerts = _parse_desc_for_service_alerts(
            d.pop("desc_for_service_alerts", UNSET)
        )

        def _parse_message_for_host_alerts(
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

        message_for_host_alerts = _parse_message_for_host_alerts(
            d.pop("message_for_host_alerts", UNSET)
        )

        def _parse_message_for_service_alerts(
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

        message_for_service_alerts = _parse_message_for_service_alerts(
            d.pop("message_for_service_alerts", UNSET)
        )

        def _parse_responsible_teams(
            data: object,
        ) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_str_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_list_of_str_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_str_one_of_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_list_of_str_one_of_type_1

        responsible_teams = _parse_responsible_teams(d.pop("responsible_teams", UNSET))

        def _parse_actions(data: object) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_str_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_list_of_str_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_str_one_of_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_list_of_str_one_of_type_1

        actions = _parse_actions(d.pop("actions", UNSET))

        def _parse_tags(data: object) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_str_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_list_of_str_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_str_one_of_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_list_of_str_one_of_type_1

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_entity(data: object) -> Checkbox | CheckboxWithStrValue | Unset:
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

        entity = _parse_entity(d.pop("entity", UNSET))

        def _parse_extra_properties(
            data: object,
        ) -> Checkbox | ListOfExtraProperties | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_extra_properties_one_of_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_list_of_extra_properties_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_extra_properties_one_of_type_1 = (
                ListOfExtraProperties.from_dict(data)
            )

            return componentsschemas_list_of_extra_properties_one_of_type_1

        extra_properties = _parse_extra_properties(d.pop("extra_properties", UNSET))

        ops_genie_plugin_create = cls(
            plugin_name=plugin_name,
            api_key=api_key,
            domain=domain,
            disable_ssl_cert_verification=disable_ssl_cert_verification,
            http_proxy=http_proxy,
            owner=owner,
            source=source,
            priority=priority,
            note_while_creating=note_while_creating,
            note_while_closing=note_while_closing,
            desc_for_host_alerts=desc_for_host_alerts,
            desc_for_service_alerts=desc_for_service_alerts,
            message_for_host_alerts=message_for_host_alerts,
            message_for_service_alerts=message_for_service_alerts,
            responsible_teams=responsible_teams,
            actions=actions,
            tags=tags,
            entity=entity,
            extra_properties=extra_properties,
        )

        ops_genie_plugin_create.additional_properties = d
        return ops_genie_plugin_create

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
