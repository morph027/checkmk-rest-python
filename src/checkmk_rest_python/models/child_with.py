from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_all_hosts_choice import BIAllHostsChoice
    from ..models.bi_host_alias_regex_choice import BIHostAliasRegexChoice
    from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice
    from ..models.host_conditions import HostConditions


T = TypeVar("T", bound="ChildWith")


@_attrs_define
class ChildWith:
    """
    Attributes:
        type_ (Any): Create nodes for all the children of matched hosts that also match other conditions. Default:
            'child_with'.
        conditions (HostConditions):
        host_choice (BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice):
    """

    conditions: HostConditions
    host_choice: BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice
    type_: Any = "child_with"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bi_all_hosts_choice import BIAllHostsChoice
        from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice

        type_ = self.type_

        conditions = self.conditions.to_dict()

        host_choice: dict[str, Any]
        if isinstance(self.host_choice, BIAllHostsChoice):
            host_choice = self.host_choice.to_dict()
        elif isinstance(self.host_choice, BIHostNameRegexChoice):
            host_choice = self.host_choice.to_dict()
        else:
            host_choice = self.host_choice.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "conditions": conditions,
                "host_choice": host_choice,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_all_hosts_choice import BIAllHostsChoice
        from ..models.bi_host_alias_regex_choice import BIHostAliasRegexChoice
        from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice
        from ..models.host_conditions import HostConditions

        d = dict(src_dict)
        type_ = d.pop("type")

        conditions = HostConditions.from_dict(d.pop("conditions"))

        def _parse_host_choice(
            data: object,
        ) -> BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_host_choice_type_0 = BIAllHostsChoice.from_dict(
                    data
                )

                return componentsschemas_bi_host_choice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_host_choice_type_1 = (
                    BIHostNameRegexChoice.from_dict(data)
                )

                return componentsschemas_bi_host_choice_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_host_choice_type_2 = BIHostAliasRegexChoice.from_dict(
                data
            )

            return componentsschemas_bi_host_choice_type_2

        host_choice = _parse_host_choice(d.pop("host_choice"))

        child_with = cls(
            type_=type_,
            conditions=conditions,
            host_choice=host_choice,
        )

        child_with.additional_properties = d
        return child_with

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
