from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ec_event_attributes_facility import ECEventAttributesFacility
from ..models.ec_event_attributes_phase import ECEventAttributesPhase
from ..models.ec_event_attributes_priority import ECEventAttributesPriority
from ..models.ec_event_attributes_service_level import ECEventAttributesServiceLevel
from ..models.ec_event_attributes_state import ECEventAttributesState

T = TypeVar("T", bound="ECEventAttributes")


@_attrs_define
class ECEventAttributes:
    """
    Attributes:
        site_id (str): The site id of the EC event. Example: mysite.
        state (ECEventAttributesState): The state Example: ok.
        service_level (ECEventAttributesServiceLevel): The service level for this event. Example: gold.
        host (str): The host name. No exception is raised when the specified host name does not exist Example: host_1.
        rule_id (str): The ID of the rule. Example: rule_1.
        application (str): The syslog tag/application this event originated from. Example: app_1.
        comment (str): The event comment. Example: Example comment.
        contact (str): The event contact information. Example: Mr Monitor.
        ipaddress (str): The IP address where the event originated. Example: 127.0.0.1.
        facility (ECEventAttributesFacility): The syslog facility. Example: kern.
        priority (ECEventAttributesPriority): The syslog priority. Example: warning.
        phase (ECEventAttributesPhase): The event phase, open or ack Example: open.
        last (datetime.datetime):  Example: 2017-11-09T17:32:28Z.
        first (datetime.datetime):  Example: 2022-11-09T16:12:12Z.
        count (int): The number of occurrences of this event within a period. Example: 1.
        text (str): The event message text Example: Sample message text.
    """

    site_id: str
    state: ECEventAttributesState
    service_level: ECEventAttributesServiceLevel
    host: str
    rule_id: str
    application: str
    comment: str
    contact: str
    ipaddress: str
    facility: ECEventAttributesFacility
    priority: ECEventAttributesPriority
    phase: ECEventAttributesPhase
    last: datetime.datetime
    first: datetime.datetime
    count: int
    text: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        state = self.state.value

        service_level = self.service_level.value

        host = self.host

        rule_id = self.rule_id

        application = self.application

        comment = self.comment

        contact = self.contact

        ipaddress = self.ipaddress

        facility = self.facility.value

        priority = self.priority.value

        phase = self.phase.value

        last = self.last.isoformat()

        first = self.first.isoformat()

        count = self.count

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_id": site_id,
                "state": state,
                "service_level": service_level,
                "host": host,
                "rule_id": rule_id,
                "application": application,
                "comment": comment,
                "contact": contact,
                "ipaddress": ipaddress,
                "facility": facility,
                "priority": priority,
                "phase": phase,
                "last": last,
                "first": first,
                "count": count,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        site_id = d.pop("site_id")

        state = ECEventAttributesState(d.pop("state"))

        service_level = ECEventAttributesServiceLevel(d.pop("service_level"))

        host = d.pop("host")

        rule_id = d.pop("rule_id")

        application = d.pop("application")

        comment = d.pop("comment")

        contact = d.pop("contact")

        ipaddress = d.pop("ipaddress")

        facility = ECEventAttributesFacility(d.pop("facility"))

        priority = ECEventAttributesPriority(d.pop("priority"))

        phase = ECEventAttributesPhase(d.pop("phase"))

        last = isoparse(d.pop("last"))

        first = isoparse(d.pop("first"))

        count = d.pop("count")

        text = d.pop("text")

        ec_event_attributes = cls(
            site_id=site_id,
            state=state,
            service_level=service_level,
            host=host,
            rule_id=rule_id,
            application=application,
            comment=comment,
            contact=contact,
            ipaddress=ipaddress,
            facility=facility,
            priority=priority,
            phase=phase,
            last=last,
            first=first,
            count=count,
            text=text,
        )

        ec_event_attributes.additional_properties = d
        return ec_event_attributes

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
