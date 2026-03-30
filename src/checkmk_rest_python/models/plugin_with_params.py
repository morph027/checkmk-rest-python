from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ascii_mail_plugin_create import AsciiMailPluginCreate
    from ..models.cisco_webex_plugin_create import CiscoWebexPluginCreate
    from ..models.html_mail_plugin_create import HTMLMailPluginCreate
    from ..models.ilert_plugin_create import IlertPluginCreate
    from ..models.jira_plugin_create import JiraPluginCreate
    from ..models.mk_event_d_plugin_create import MkEventDPluginCreate
    from ..models.ms_teams_plugin_create import MSTeamsPluginCreate
    from ..models.ops_genie_plugin_create import OpsGeniePluginCreate
    from ..models.pager_duty_plugin_create import PagerDutyPluginCreate
    from ..models.push_over_plugin_create import PushOverPluginCreate
    from ..models.service_now_plugin_create import ServiceNowPluginCreate
    from ..models.signl_4_plugin_create import Signl4PluginCreate
    from ..models.slack_plugin_create import SlackPluginCreate
    from ..models.sms_plugin_base import SMSPluginBase
    from ..models.smsapi_plugin_create import SMSAPIPluginCreate
    from ..models.spectrum_plugin_base import SpectrumPluginBase
    from ..models.victorops_plugin_create import VictoropsPluginCreate


T = TypeVar("T", bound="PluginWithParams")


@_attrs_define
class PluginWithParams:
    """
    Attributes:
        plugin_params (AsciiMailPluginCreate | CiscoWebexPluginCreate | HTMLMailPluginCreate | IlertPluginCreate |
            JiraPluginCreate | MkEventDPluginCreate | MSTeamsPluginCreate | OpsGeniePluginCreate | PagerDutyPluginCreate |
            PushOverPluginCreate | ServiceNowPluginCreate | Signl4PluginCreate | SlackPluginCreate | SMSAPIPluginCreate |
            SMSPluginBase | SpectrumPluginBase | VictoropsPluginCreate):
        option (Any | Unset): Create notifications with parameters Default:
            'create_notification_with_the_following_parameters'. Example: create_notification_with_the_following_parameters.
    """

    plugin_params: (
        AsciiMailPluginCreate
        | CiscoWebexPluginCreate
        | HTMLMailPluginCreate
        | IlertPluginCreate
        | JiraPluginCreate
        | MkEventDPluginCreate
        | MSTeamsPluginCreate
        | OpsGeniePluginCreate
        | PagerDutyPluginCreate
        | PushOverPluginCreate
        | ServiceNowPluginCreate
        | Signl4PluginCreate
        | SlackPluginCreate
        | SMSAPIPluginCreate
        | SMSPluginBase
        | SpectrumPluginBase
        | VictoropsPluginCreate
    )
    option: Any | Unset = "create_notification_with_the_following_parameters"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ascii_mail_plugin_create import AsciiMailPluginCreate
        from ..models.cisco_webex_plugin_create import CiscoWebexPluginCreate
        from ..models.html_mail_plugin_create import HTMLMailPluginCreate
        from ..models.ilert_plugin_create import IlertPluginCreate
        from ..models.jira_plugin_create import JiraPluginCreate
        from ..models.mk_event_d_plugin_create import MkEventDPluginCreate
        from ..models.ops_genie_plugin_create import OpsGeniePluginCreate
        from ..models.pager_duty_plugin_create import PagerDutyPluginCreate
        from ..models.push_over_plugin_create import PushOverPluginCreate
        from ..models.service_now_plugin_create import ServiceNowPluginCreate
        from ..models.signl_4_plugin_create import Signl4PluginCreate
        from ..models.slack_plugin_create import SlackPluginCreate
        from ..models.sms_plugin_base import SMSPluginBase
        from ..models.smsapi_plugin_create import SMSAPIPluginCreate
        from ..models.spectrum_plugin_base import SpectrumPluginBase
        from ..models.victorops_plugin_create import VictoropsPluginCreate

        plugin_params: dict[str, Any]
        if isinstance(self.plugin_params, AsciiMailPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, HTMLMailPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, CiscoWebexPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, MkEventDPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, IlertPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, JiraPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, OpsGeniePluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, PagerDutyPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, PushOverPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, ServiceNowPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, Signl4PluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, SlackPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, SMSAPIPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, SMSPluginBase):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, SpectrumPluginBase):
            plugin_params = self.plugin_params.to_dict()
        elif isinstance(self.plugin_params, VictoropsPluginCreate):
            plugin_params = self.plugin_params.to_dict()
        else:
            plugin_params = self.plugin_params.to_dict()

        option = self.option

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_params": plugin_params,
            }
        )
        if option is not UNSET:
            field_dict["option"] = option

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ascii_mail_plugin_create import AsciiMailPluginCreate
        from ..models.cisco_webex_plugin_create import CiscoWebexPluginCreate
        from ..models.html_mail_plugin_create import HTMLMailPluginCreate
        from ..models.ilert_plugin_create import IlertPluginCreate
        from ..models.jira_plugin_create import JiraPluginCreate
        from ..models.mk_event_d_plugin_create import MkEventDPluginCreate
        from ..models.ms_teams_plugin_create import MSTeamsPluginCreate
        from ..models.ops_genie_plugin_create import OpsGeniePluginCreate
        from ..models.pager_duty_plugin_create import PagerDutyPluginCreate
        from ..models.push_over_plugin_create import PushOverPluginCreate
        from ..models.service_now_plugin_create import ServiceNowPluginCreate
        from ..models.signl_4_plugin_create import Signl4PluginCreate
        from ..models.slack_plugin_create import SlackPluginCreate
        from ..models.sms_plugin_base import SMSPluginBase
        from ..models.smsapi_plugin_create import SMSAPIPluginCreate
        from ..models.spectrum_plugin_base import SpectrumPluginBase
        from ..models.victorops_plugin_create import VictoropsPluginCreate

        d = dict(src_dict)

        def _parse_plugin_params(
            data: object,
        ) -> (
            AsciiMailPluginCreate
            | CiscoWebexPluginCreate
            | HTMLMailPluginCreate
            | IlertPluginCreate
            | JiraPluginCreate
            | MkEventDPluginCreate
            | MSTeamsPluginCreate
            | OpsGeniePluginCreate
            | PagerDutyPluginCreate
            | PushOverPluginCreate
            | ServiceNowPluginCreate
            | Signl4PluginCreate
            | SlackPluginCreate
            | SMSAPIPluginCreate
            | SMSPluginBase
            | SpectrumPluginBase
            | VictoropsPluginCreate
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_0 = (
                    AsciiMailPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_1 = (
                    HTMLMailPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_2 = (
                    CiscoWebexPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_3 = (
                    MkEventDPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_4 = IlertPluginCreate.from_dict(
                    data
                )

                return componentsschemas_plugin_selector_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_5 = JiraPluginCreate.from_dict(
                    data
                )

                return componentsschemas_plugin_selector_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_6 = (
                    OpsGeniePluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_7 = (
                    PagerDutyPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_8 = (
                    PushOverPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_9 = (
                    ServiceNowPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_10 = (
                    Signl4PluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_11 = SlackPluginCreate.from_dict(
                    data
                )

                return componentsschemas_plugin_selector_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_12 = (
                    SMSAPIPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_13 = SMSPluginBase.from_dict(
                    data
                )

                return componentsschemas_plugin_selector_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_14 = (
                    SpectrumPluginBase.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_selector_type_15 = (
                    VictoropsPluginCreate.from_dict(data)
                )

                return componentsschemas_plugin_selector_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_selector_type_16 = MSTeamsPluginCreate.from_dict(
                data
            )

            return componentsschemas_plugin_selector_type_16

        plugin_params = _parse_plugin_params(d.pop("plugin_params"))

        option = d.pop("option", UNSET)

        plugin_with_params = cls(
            plugin_params=plugin_params,
            option=option,
        )

        plugin_with_params.additional_properties = d
        return plugin_with_params

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
