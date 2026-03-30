from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bi_aggregation_computation_options import (
        BIAggregationComputationOptions,
    )
    from ..models.bi_aggregation_groups import BIAggregationGroups
    from ..models.bi_aggregation_visualization import BIAggregationVisualization
    from ..models.bi_node_generator import BINodeGenerator


T = TypeVar("T", bound="BIAggregationEndpoint")


@_attrs_define
class BIAggregationEndpoint:
    """
    Attributes:
        id (str): The unique aggregation id Example: aggr1.
        groups (BIAggregationGroups):
        node (BINodeGenerator):
        aggregation_visualization (BIAggregationVisualization):
        computation_options (BIAggregationComputationOptions):
        pack_id (str): The identifier of the BI pack. Example: pack1.
        comment (None | str | Unset): An optional comment that may be used to explain the purpose of this object.
            Example: Rule comment.
        customer (None | str | Unset): CME Edition only: The customer id for this aggregation. Example: customer1.
    """

    id: str
    groups: BIAggregationGroups
    node: BINodeGenerator
    aggregation_visualization: BIAggregationVisualization
    computation_options: BIAggregationComputationOptions
    pack_id: str
    comment: None | str | Unset = UNSET
    customer: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        groups = self.groups.to_dict()

        node = self.node.to_dict()

        aggregation_visualization = self.aggregation_visualization.to_dict()

        computation_options = self.computation_options.to_dict()

        pack_id = self.pack_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        customer: None | str | Unset
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "groups": groups,
                "node": node,
                "aggregation_visualization": aggregation_visualization,
                "computation_options": computation_options,
                "pack_id": pack_id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_aggregation_computation_options import (
            BIAggregationComputationOptions,
        )
        from ..models.bi_aggregation_groups import BIAggregationGroups
        from ..models.bi_aggregation_visualization import BIAggregationVisualization
        from ..models.bi_node_generator import BINodeGenerator

        d = dict(src_dict)
        id = d.pop("id")

        groups = BIAggregationGroups.from_dict(d.pop("groups"))

        node = BINodeGenerator.from_dict(d.pop("node"))

        aggregation_visualization = BIAggregationVisualization.from_dict(
            d.pop("aggregation_visualization")
        )

        computation_options = BIAggregationComputationOptions.from_dict(
            d.pop("computation_options")
        )

        pack_id = d.pop("pack_id")

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_customer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer = _parse_customer(d.pop("customer", UNSET))

        bi_aggregation_endpoint = cls(
            id=id,
            groups=groups,
            node=node,
            aggregation_visualization=aggregation_visualization,
            computation_options=computation_options,
            pack_id=pack_id,
            comment=comment,
            customer=customer,
        )

        bi_aggregation_endpoint.additional_properties = d
        return bi_aggregation_endpoint

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
