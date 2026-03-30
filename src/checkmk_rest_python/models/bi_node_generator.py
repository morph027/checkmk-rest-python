from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_call_a_rule_action import BICallARuleAction
    from ..models.bi_empty_search import BIEmptySearch
    from ..models.bi_fixed_arguments_search import BIFixedArgumentsSearch
    from ..models.bi_host_search import BIHostSearch
    from ..models.bi_service_search import BIServiceSearch
    from ..models.bi_state_of_host_action import BIStateOfHostAction
    from ..models.bi_state_of_remaining_services_action import (
        BIStateOfRemainingServicesAction,
    )
    from ..models.bi_state_of_service_action import BIStateOfServiceAction


T = TypeVar("T", bound="BINodeGenerator")


@_attrs_define
class BINodeGenerator:
    """
    Attributes:
        search (BIEmptySearch | BIFixedArgumentsSearch | BIHostSearch | BIServiceSearch):
        action (BICallARuleAction | BIStateOfHostAction | BIStateOfRemainingServicesAction | BIStateOfServiceAction):
    """

    search: BIEmptySearch | BIFixedArgumentsSearch | BIHostSearch | BIServiceSearch
    action: (
        BICallARuleAction
        | BIStateOfHostAction
        | BIStateOfRemainingServicesAction
        | BIStateOfServiceAction
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bi_call_a_rule_action import BICallARuleAction
        from ..models.bi_empty_search import BIEmptySearch
        from ..models.bi_host_search import BIHostSearch
        from ..models.bi_service_search import BIServiceSearch
        from ..models.bi_state_of_host_action import BIStateOfHostAction
        from ..models.bi_state_of_service_action import BIStateOfServiceAction

        search: dict[str, Any]
        if isinstance(self.search, BIEmptySearch):
            search = self.search.to_dict()
        elif isinstance(self.search, BIHostSearch):
            search = self.search.to_dict()
        elif isinstance(self.search, BIServiceSearch):
            search = self.search.to_dict()
        else:
            search = self.search.to_dict()

        action: dict[str, Any]
        if isinstance(self.action, BICallARuleAction):
            action = self.action.to_dict()
        elif isinstance(self.action, BIStateOfHostAction):
            action = self.action.to_dict()
        elif isinstance(self.action, BIStateOfServiceAction):
            action = self.action.to_dict()
        else:
            action = self.action.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "search": search,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_call_a_rule_action import BICallARuleAction
        from ..models.bi_empty_search import BIEmptySearch
        from ..models.bi_fixed_arguments_search import BIFixedArgumentsSearch
        from ..models.bi_host_search import BIHostSearch
        from ..models.bi_service_search import BIServiceSearch
        from ..models.bi_state_of_host_action import BIStateOfHostAction
        from ..models.bi_state_of_remaining_services_action import (
            BIStateOfRemainingServicesAction,
        )
        from ..models.bi_state_of_service_action import BIStateOfServiceAction

        d = dict(src_dict)

        def _parse_search(
            data: object,
        ) -> BIEmptySearch | BIFixedArgumentsSearch | BIHostSearch | BIServiceSearch:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_search_type_0 = BIEmptySearch.from_dict(data)

                return componentsschemas_bi_search_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_search_type_1 = BIHostSearch.from_dict(data)

                return componentsschemas_bi_search_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_search_type_2 = BIServiceSearch.from_dict(data)

                return componentsschemas_bi_search_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_search_type_3 = BIFixedArgumentsSearch.from_dict(data)

            return componentsschemas_bi_search_type_3

        search = _parse_search(d.pop("search"))

        def _parse_action(
            data: object,
        ) -> (
            BICallARuleAction
            | BIStateOfHostAction
            | BIStateOfRemainingServicesAction
            | BIStateOfServiceAction
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_action_type_0 = BICallARuleAction.from_dict(data)

                return componentsschemas_bi_action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_action_type_1 = BIStateOfHostAction.from_dict(data)

                return componentsschemas_bi_action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_action_type_2 = BIStateOfServiceAction.from_dict(
                    data
                )

                return componentsschemas_bi_action_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_action_type_3 = (
                BIStateOfRemainingServicesAction.from_dict(data)
            )

            return componentsschemas_bi_action_type_3

        action = _parse_action(d.pop("action"))

        bi_node_generator = cls(
            search=search,
            action=action,
        )

        bi_node_generator.additional_properties = d
        return bi_node_generator

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
