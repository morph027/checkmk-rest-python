from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_selection import ContactSelection
    from ..models.rule_conditions import RuleConditions
    from ..models.rule_notification_method import RuleNotificationMethod
    from ..models.rule_properties import RuleProperties


T = TypeVar("T", bound="RuleNotification")


@_attrs_define
class RuleNotification:
    """
    Attributes:
        rule_properties (RuleProperties):
        notification_method (RuleNotificationMethod):
        contact_selection (ContactSelection | Unset):
        conditions (RuleConditions | Unset):
    """

    rule_properties: RuleProperties
    notification_method: RuleNotificationMethod
    contact_selection: ContactSelection | Unset = UNSET
    conditions: RuleConditions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_properties = self.rule_properties.to_dict()

        notification_method = self.notification_method.to_dict()

        contact_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_selection, Unset):
            contact_selection = self.contact_selection.to_dict()

        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_properties": rule_properties,
                "notification_method": notification_method,
            }
        )
        if contact_selection is not UNSET:
            field_dict["contact_selection"] = contact_selection
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_selection import ContactSelection
        from ..models.rule_conditions import RuleConditions
        from ..models.rule_notification_method import RuleNotificationMethod
        from ..models.rule_properties import RuleProperties

        d = dict(src_dict)
        rule_properties = RuleProperties.from_dict(d.pop("rule_properties"))

        notification_method = RuleNotificationMethod.from_dict(
            d.pop("notification_method")
        )

        _contact_selection = d.pop("contact_selection", UNSET)
        contact_selection: ContactSelection | Unset
        if isinstance(_contact_selection, Unset):
            contact_selection = UNSET
        else:
            contact_selection = ContactSelection.from_dict(_contact_selection)

        _conditions = d.pop("conditions", UNSET)
        conditions: RuleConditions | Unset
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = RuleConditions.from_dict(_conditions)

        rule_notification = cls(
            rule_properties=rule_properties,
            notification_method=notification_method,
            contact_selection=contact_selection,
            conditions=conditions,
        )

        rule_notification.additional_properties = d
        return rule_notification

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
