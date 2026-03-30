from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.host_or_service_condition_operator import HostOrServiceConditionOperator

T = TypeVar("T", bound="HostOrServiceCondition")


@_attrs_define
class HostOrServiceCondition:
    """
    Attributes:
        match_on (list[str]): A list of string matching regular expressions.
        operator (HostOrServiceConditionOperator): How the hosts or services should be matched.
             * one_of - will match if any of the hosts or services is matched
             * none_of - will match if none of the hosts are matched. In other words: will match all hosts or services which
            are not specified.
    """

    match_on: list[str]
    operator: HostOrServiceConditionOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_on = self.match_on

        operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match_on": match_on,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_on = cast(list[str], d.pop("match_on"))

        operator = HostOrServiceConditionOperator(d.pop("operator"))

        host_or_service_condition = cls(
            match_on=match_on,
            operator=operator,
        )

        host_or_service_condition.additional_properties = d
        return host_or_service_condition

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
