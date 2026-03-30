from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bi_aggregation_state_response_aggregations import (
        BIAggregationStateResponseAggregations,
    )


T = TypeVar("T", bound="BIAggregationStateResponse")


@_attrs_define
class BIAggregationStateResponse:
    """
    Attributes:
        aggregations (BIAggregationStateResponseAggregations | Unset): The Aggregation state
        missing_sites (list[str] | Unset): The missing sites Example: ['beta', 'mysite'].
        missing_aggr (list[str] | Unset): the missing aggregations Example: ['Host central'].
    """

    aggregations: BIAggregationStateResponseAggregations | Unset = UNSET
    missing_sites: list[str] | Unset = UNSET
    missing_aggr: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregations, Unset):
            aggregations = self.aggregations.to_dict()

        missing_sites: list[str] | Unset = UNSET
        if not isinstance(self.missing_sites, Unset):
            missing_sites = self.missing_sites

        missing_aggr: list[str] | Unset = UNSET
        if not isinstance(self.missing_aggr, Unset):
            missing_aggr = self.missing_aggr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregations is not UNSET:
            field_dict["aggregations"] = aggregations
        if missing_sites is not UNSET:
            field_dict["missing_sites"] = missing_sites
        if missing_aggr is not UNSET:
            field_dict["missing_aggr"] = missing_aggr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_aggregation_state_response_aggregations import (
            BIAggregationStateResponseAggregations,
        )

        d = dict(src_dict)
        _aggregations = d.pop("aggregations", UNSET)
        aggregations: BIAggregationStateResponseAggregations | Unset
        if isinstance(_aggregations, Unset):
            aggregations = UNSET
        else:
            aggregations = BIAggregationStateResponseAggregations.from_dict(
                _aggregations
            )

        missing_sites = cast(list[str], d.pop("missing_sites", UNSET))

        missing_aggr = cast(list[str], d.pop("missing_aggr", UNSET))

        bi_aggregation_state_response = cls(
            aggregations=aggregations,
            missing_sites=missing_sites,
            missing_aggr=missing_aggr,
        )

        bi_aggregation_state_response.additional_properties = d
        return bi_aggregation_state_response

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
