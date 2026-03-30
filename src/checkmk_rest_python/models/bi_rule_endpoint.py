from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_aggregation_function_best import BIAggregationFunctionBest
    from ..models.bi_aggregation_function_count_ok import BIAggregationFunctionCountOK
    from ..models.bi_aggregation_function_worst import BIAggregationFunctionWorst
    from ..models.bi_node_generator import BINodeGenerator
    from ..models.bi_node_vis_block_style import BINodeVisBlockStyle
    from ..models.bi_node_vis_force_style import BINodeVisForceStyle
    from ..models.bi_node_vis_hierarchy_style import BINodeVisHierarchyStyle
    from ..models.bi_node_vis_none_style import BINodeVisNoneStyle
    from ..models.bi_node_vis_radial_style import BINodeVisRadialStyle
    from ..models.bi_params import BIParams
    from ..models.bi_rule_computation_options import BIRuleComputationOptions
    from ..models.bi_rule_properties import BIRuleProperties


T = TypeVar("T", bound="BIRuleEndpoint")


@_attrs_define
class BIRuleEndpoint:
    """
    Attributes:
        id (str): The unique rule id Example: rule1.
        nodes (list[BINodeGenerator]): A list of nodes for for this rule
        params (BIParams):
        node_visualization (BINodeVisBlockStyle | BINodeVisForceStyle | BINodeVisHierarchyStyle | BINodeVisNoneStyle |
            BINodeVisRadialStyle):
        properties (BIRuleProperties):
        aggregation_function (BIAggregationFunctionBest | BIAggregationFunctionCountOK | BIAggregationFunctionWorst):
        computation_options (BIRuleComputationOptions):
        pack_id (str): The identifier of the BI pack. Example: pack1.
    """

    id: str
    nodes: list[BINodeGenerator]
    params: BIParams
    node_visualization: (
        BINodeVisBlockStyle
        | BINodeVisForceStyle
        | BINodeVisHierarchyStyle
        | BINodeVisNoneStyle
        | BINodeVisRadialStyle
    )
    properties: BIRuleProperties
    aggregation_function: (
        BIAggregationFunctionBest
        | BIAggregationFunctionCountOK
        | BIAggregationFunctionWorst
    )
    computation_options: BIRuleComputationOptions
    pack_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bi_aggregation_function_best import BIAggregationFunctionBest
        from ..models.bi_aggregation_function_worst import BIAggregationFunctionWorst
        from ..models.bi_node_vis_block_style import BINodeVisBlockStyle
        from ..models.bi_node_vis_hierarchy_style import BINodeVisHierarchyStyle
        from ..models.bi_node_vis_none_style import BINodeVisNoneStyle
        from ..models.bi_node_vis_radial_style import BINodeVisRadialStyle

        id = self.id

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        params = self.params.to_dict()

        node_visualization: dict[str, Any]
        if isinstance(self.node_visualization, BINodeVisNoneStyle):
            node_visualization = self.node_visualization.to_dict()
        elif isinstance(self.node_visualization, BINodeVisBlockStyle):
            node_visualization = self.node_visualization.to_dict()
        elif isinstance(self.node_visualization, BINodeVisHierarchyStyle):
            node_visualization = self.node_visualization.to_dict()
        elif isinstance(self.node_visualization, BINodeVisRadialStyle):
            node_visualization = self.node_visualization.to_dict()
        else:
            node_visualization = self.node_visualization.to_dict()

        properties = self.properties.to_dict()

        aggregation_function: dict[str, Any]
        if isinstance(self.aggregation_function, BIAggregationFunctionBest):
            aggregation_function = self.aggregation_function.to_dict()
        elif isinstance(self.aggregation_function, BIAggregationFunctionWorst):
            aggregation_function = self.aggregation_function.to_dict()
        else:
            aggregation_function = self.aggregation_function.to_dict()

        computation_options = self.computation_options.to_dict()

        pack_id = self.pack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "nodes": nodes,
                "params": params,
                "node_visualization": node_visualization,
                "properties": properties,
                "aggregation_function": aggregation_function,
                "computation_options": computation_options,
                "pack_id": pack_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_aggregation_function_best import BIAggregationFunctionBest
        from ..models.bi_aggregation_function_count_ok import (
            BIAggregationFunctionCountOK,
        )
        from ..models.bi_aggregation_function_worst import BIAggregationFunctionWorst
        from ..models.bi_node_generator import BINodeGenerator
        from ..models.bi_node_vis_block_style import BINodeVisBlockStyle
        from ..models.bi_node_vis_force_style import BINodeVisForceStyle
        from ..models.bi_node_vis_hierarchy_style import BINodeVisHierarchyStyle
        from ..models.bi_node_vis_none_style import BINodeVisNoneStyle
        from ..models.bi_node_vis_radial_style import BINodeVisRadialStyle
        from ..models.bi_params import BIParams
        from ..models.bi_rule_computation_options import BIRuleComputationOptions
        from ..models.bi_rule_properties import BIRuleProperties

        d = dict(src_dict)
        id = d.pop("id")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = BINodeGenerator.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        params = BIParams.from_dict(d.pop("params"))

        def _parse_node_visualization(
            data: object,
        ) -> (
            BINodeVisBlockStyle
            | BINodeVisForceStyle
            | BINodeVisHierarchyStyle
            | BINodeVisNoneStyle
            | BINodeVisRadialStyle
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_node_vis_layout_style_type_0 = (
                    BINodeVisNoneStyle.from_dict(data)
                )

                return componentsschemas_bi_node_vis_layout_style_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_node_vis_layout_style_type_1 = (
                    BINodeVisBlockStyle.from_dict(data)
                )

                return componentsschemas_bi_node_vis_layout_style_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_node_vis_layout_style_type_2 = (
                    BINodeVisHierarchyStyle.from_dict(data)
                )

                return componentsschemas_bi_node_vis_layout_style_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_node_vis_layout_style_type_3 = (
                    BINodeVisRadialStyle.from_dict(data)
                )

                return componentsschemas_bi_node_vis_layout_style_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_node_vis_layout_style_type_4 = (
                BINodeVisForceStyle.from_dict(data)
            )

            return componentsschemas_bi_node_vis_layout_style_type_4

        node_visualization = _parse_node_visualization(d.pop("node_visualization"))

        properties = BIRuleProperties.from_dict(d.pop("properties"))

        def _parse_aggregation_function(
            data: object,
        ) -> (
            BIAggregationFunctionBest
            | BIAggregationFunctionCountOK
            | BIAggregationFunctionWorst
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_aggregation_function_type_0 = (
                    BIAggregationFunctionBest.from_dict(data)
                )

                return componentsschemas_bi_aggregation_function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_aggregation_function_type_1 = (
                    BIAggregationFunctionWorst.from_dict(data)
                )

                return componentsschemas_bi_aggregation_function_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_aggregation_function_type_2 = (
                BIAggregationFunctionCountOK.from_dict(data)
            )

            return componentsschemas_bi_aggregation_function_type_2

        aggregation_function = _parse_aggregation_function(
            d.pop("aggregation_function")
        )

        computation_options = BIRuleComputationOptions.from_dict(
            d.pop("computation_options")
        )

        pack_id = d.pop("pack_id")

        bi_rule_endpoint = cls(
            id=id,
            nodes=nodes,
            params=params,
            node_visualization=node_visualization,
            properties=properties,
            aggregation_function=aggregation_function,
            computation_options=computation_options,
            pack_id=pack_id,
        )

        bi_rule_endpoint.additional_properties = d
        return bi_rule_endpoint

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
