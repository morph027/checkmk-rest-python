from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.push_over_priority_state import PushOverPriorityState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_over_priority_base import PushOverPriorityBase
    from ..models.push_over_priority_emergency import PushOverPriorityEmergency


T = TypeVar("T", bound="PushOverPriority")


@_attrs_define
class PushOverPriority:
    """
    Attributes:
        value (PushOverPriorityBase | PushOverPriorityEmergency):
        state (PushOverPriorityState | Unset): To enable or disable this field Example: enabled.
    """

    value: PushOverPriorityBase | PushOverPriorityEmergency
    state: PushOverPriorityState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.push_over_priority_base import PushOverPriorityBase

        value: dict[str, Any]
        if isinstance(self.value, PushOverPriorityBase):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_over_priority_base import PushOverPriorityBase
        from ..models.push_over_priority_emergency import PushOverPriorityEmergency

        d = dict(src_dict)

        def _parse_value(
            data: object,
        ) -> PushOverPriorityBase | PushOverPriorityEmergency:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_push_over_priority_selector_type_0 = (
                    PushOverPriorityBase.from_dict(data)
                )

                return componentsschemas_push_over_priority_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_push_over_priority_selector_type_4 = (
                PushOverPriorityEmergency.from_dict(data)
            )

            return componentsschemas_push_over_priority_selector_type_4

        value = _parse_value(d.pop("value"))

        _state = d.pop("state", UNSET)
        state: PushOverPriorityState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PushOverPriorityState(_state)

        push_over_priority = cls(
            value=value,
            state=state,
        )

        push_over_priority.additional_properties = d
        return push_over_priority

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
