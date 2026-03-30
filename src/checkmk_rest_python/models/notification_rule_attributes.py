from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conditions_attributes import ConditionsAttributes
    from ..models.contact_selection_attributes import ContactSelectionAttributes
    from ..models.notification_plugin import NotificationPlugin
    from ..models.rule_properties_attributes import RulePropertiesAttributes


T = TypeVar("T", bound="NotificationRuleAttributes")


@_attrs_define
class NotificationRuleAttributes:
    """
    Attributes:
        rule_properties (RulePropertiesAttributes | Unset):
        notification_method (NotificationPlugin | Unset):
        contact_selection (ContactSelectionAttributes | Unset):
        conditions (ConditionsAttributes | Unset):
    """

    rule_properties: RulePropertiesAttributes | Unset = UNSET
    notification_method: NotificationPlugin | Unset = UNSET
    contact_selection: ContactSelectionAttributes | Unset = UNSET
    conditions: ConditionsAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule_properties, Unset):
            rule_properties = self.rule_properties.to_dict()

        notification_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_method, Unset):
            notification_method = self.notification_method.to_dict()

        contact_selection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_selection, Unset):
            contact_selection = self.contact_selection.to_dict()

        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_properties is not UNSET:
            field_dict["rule_properties"] = rule_properties
        if notification_method is not UNSET:
            field_dict["notification_method"] = notification_method
        if contact_selection is not UNSET:
            field_dict["contact_selection"] = contact_selection
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conditions_attributes import ConditionsAttributes
        from ..models.contact_selection_attributes import ContactSelectionAttributes
        from ..models.notification_plugin import NotificationPlugin
        from ..models.rule_properties_attributes import RulePropertiesAttributes

        d = dict(src_dict)
        _rule_properties = d.pop("rule_properties", UNSET)
        rule_properties: RulePropertiesAttributes | Unset
        if isinstance(_rule_properties, Unset):
            rule_properties = UNSET
        else:
            rule_properties = RulePropertiesAttributes.from_dict(_rule_properties)

        _notification_method = d.pop("notification_method", UNSET)
        notification_method: NotificationPlugin | Unset
        if isinstance(_notification_method, Unset):
            notification_method = UNSET
        else:
            notification_method = NotificationPlugin.from_dict(_notification_method)

        _contact_selection = d.pop("contact_selection", UNSET)
        contact_selection: ContactSelectionAttributes | Unset
        if isinstance(_contact_selection, Unset):
            contact_selection = UNSET
        else:
            contact_selection = ContactSelectionAttributes.from_dict(_contact_selection)

        _conditions = d.pop("conditions", UNSET)
        conditions: ConditionsAttributes | Unset
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = ConditionsAttributes.from_dict(_conditions)

        notification_rule_attributes = cls(
            rule_properties=rule_properties,
            notification_method=notification_method,
            contact_selection=contact_selection,
            conditions=conditions,
        )

        notification_rule_attributes.additional_properties = d
        return notification_rule_attributes

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
