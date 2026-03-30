from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BIAggregationComputationOptions")


@_attrs_define
class BIAggregationComputationOptions:
    """
    Attributes:
        disabled (bool): Enable or disable this computation option.
        use_hard_states (bool): Bases state computation only on hard states instead of hard and soft states.
        escalate_downtimes_as_warn (bool): Escalates downtimes based on aggregated WARN state instead of CRIT state.
        freeze_aggregations (bool | Unset): Generates the aggregations initially, then doesn't update them
            automatically.
    """

    disabled: bool
    use_hard_states: bool
    escalate_downtimes_as_warn: bool
    freeze_aggregations: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled

        use_hard_states = self.use_hard_states

        escalate_downtimes_as_warn = self.escalate_downtimes_as_warn

        freeze_aggregations = self.freeze_aggregations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disabled": disabled,
                "use_hard_states": use_hard_states,
                "escalate_downtimes_as_warn": escalate_downtimes_as_warn,
            }
        )
        if freeze_aggregations is not UNSET:
            field_dict["freeze_aggregations"] = freeze_aggregations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = d.pop("disabled")

        use_hard_states = d.pop("use_hard_states")

        escalate_downtimes_as_warn = d.pop("escalate_downtimes_as_warn")

        freeze_aggregations = d.pop("freeze_aggregations", UNSET)

        bi_aggregation_computation_options = cls(
            disabled=disabled,
            use_hard_states=use_hard_states,
            escalate_downtimes_as_warn=escalate_downtimes_as_warn,
            freeze_aggregations=freeze_aggregations,
        )

        bi_aggregation_computation_options.additional_properties = d
        return bi_aggregation_computation_options

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
