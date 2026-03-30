from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_or_service_condition import HostOrServiceCondition
    from ..models.label_condition_2 import LabelCondition2
    from ..models.label_group_condition_1 import LabelGroupCondition1
    from ..models.tag_condition_condition_schema_base import (
        TagConditionConditionSchemaBase,
    )
    from ..models.tag_condition_scalar_schema_base import TagConditionScalarSchemaBase


T = TypeVar("T", bound="InputConditions")


@_attrs_define
class InputConditions:
    """
    Attributes:
        host_name (HostOrServiceCondition | Unset):
        host_tags (list[TagConditionConditionSchemaBase | TagConditionScalarSchemaBase] | Unset): The rule will only be
            applied to hosts fulfilling all the host tag conditions listed here, even if they appear in the list of explicit
            host names. Example: [{'key': 'criticality', 'operator': 'is', 'value': 'prod'}].
        host_label_groups (list[LabelGroupCondition1] | Unset): Further restrict this rule by applying host label
            conditions. Although all items in this list have a default operator value, the operator value for the the first
            item in the list does not have any effect. Example: [{'label_group': [{'operator': 'and', 'label':
            'db:mssql'}]}, {'operator': 'and', 'label_group': [{'operator': 'and', 'label': 'os:windows'}]}].
        service_label_groups (list[LabelGroupCondition1] | Unset): Restrict the application of the rule, by checking
            against service label conditions. Although all items in this list have a default operator value, the operator
            value for the the first item in the list does not have any effect. Example: [{'label_group': [{'operator':
            'and', 'label': 'db:mssql'}]}, {'operator': 'and', 'label_group': [{'operator': 'and', 'label':
            'os:windows'}]}].
        service_description (HostOrServiceCondition | Unset):
        host_labels (list[LabelCondition2] | Unset): Further restrict this rule by applying host label conditions. -
            Deprecated: Use `host_label_groups` instead. Example: [{'key': 'os', 'operator': 'is', 'value': 'windows'}].
        service_labels (list[LabelCondition2] | Unset): Restrict the application of the rule, by checking against
            service label conditions. - Deprecated: Use `service_label_groups` instead. Example: [{'key': 'os', 'operator':
            'is', 'value': 'windows'}].
    """

    host_name: HostOrServiceCondition | Unset = UNSET
    host_tags: (
        list[TagConditionConditionSchemaBase | TagConditionScalarSchemaBase] | Unset
    ) = UNSET
    host_label_groups: list[LabelGroupCondition1] | Unset = UNSET
    service_label_groups: list[LabelGroupCondition1] | Unset = UNSET
    service_description: HostOrServiceCondition | Unset = UNSET
    host_labels: list[LabelCondition2] | Unset = UNSET
    service_labels: list[LabelCondition2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tag_condition_scalar_schema_base import (
            TagConditionScalarSchemaBase,
        )

        host_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host_name, Unset):
            host_name = self.host_name.to_dict()

        host_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.host_tags, Unset):
            host_tags = []
            for host_tags_item_data in self.host_tags:
                host_tags_item: dict[str, Any]
                if isinstance(host_tags_item_data, TagConditionScalarSchemaBase):
                    host_tags_item = host_tags_item_data.to_dict()
                else:
                    host_tags_item = host_tags_item_data.to_dict()

                host_tags.append(host_tags_item)

        host_label_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.host_label_groups, Unset):
            host_label_groups = []
            for host_label_groups_item_data in self.host_label_groups:
                host_label_groups_item = host_label_groups_item_data.to_dict()
                host_label_groups.append(host_label_groups_item)

        service_label_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_label_groups, Unset):
            service_label_groups = []
            for service_label_groups_item_data in self.service_label_groups:
                service_label_groups_item = service_label_groups_item_data.to_dict()
                service_label_groups.append(service_label_groups_item)

        service_description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_description, Unset):
            service_description = self.service_description.to_dict()

        host_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.host_labels, Unset):
            host_labels = []
            for host_labels_item_data in self.host_labels:
                host_labels_item = host_labels_item_data.to_dict()
                host_labels.append(host_labels_item)

        service_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_labels, Unset):
            service_labels = []
            for service_labels_item_data in self.service_labels:
                service_labels_item = service_labels_item_data.to_dict()
                service_labels.append(service_labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if host_tags is not UNSET:
            field_dict["host_tags"] = host_tags
        if host_label_groups is not UNSET:
            field_dict["host_label_groups"] = host_label_groups
        if service_label_groups is not UNSET:
            field_dict["service_label_groups"] = service_label_groups
        if service_description is not UNSET:
            field_dict["service_description"] = service_description
        if host_labels is not UNSET:
            field_dict["host_labels"] = host_labels
        if service_labels is not UNSET:
            field_dict["service_labels"] = service_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_or_service_condition import HostOrServiceCondition
        from ..models.label_condition_2 import LabelCondition2
        from ..models.label_group_condition_1 import LabelGroupCondition1
        from ..models.tag_condition_condition_schema_base import (
            TagConditionConditionSchemaBase,
        )
        from ..models.tag_condition_scalar_schema_base import (
            TagConditionScalarSchemaBase,
        )

        d = dict(src_dict)
        _host_name = d.pop("host_name", UNSET)
        host_name: HostOrServiceCondition | Unset
        if isinstance(_host_name, Unset):
            host_name = UNSET
        else:
            host_name = HostOrServiceCondition.from_dict(_host_name)

        _host_tags = d.pop("host_tags", UNSET)
        host_tags: (
            list[TagConditionConditionSchemaBase | TagConditionScalarSchemaBase] | Unset
        ) = UNSET
        if _host_tags is not UNSET:
            host_tags = []
            for host_tags_item_data in _host_tags:

                def _parse_host_tags_item(
                    data: object,
                ) -> TagConditionConditionSchemaBase | TagConditionScalarSchemaBase:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_tag_condition_type_0 = (
                            TagConditionScalarSchemaBase.from_dict(data)
                        )

                        return componentsschemas_tag_condition_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tag_condition_type_2 = (
                        TagConditionConditionSchemaBase.from_dict(data)
                    )

                    return componentsschemas_tag_condition_type_2

                host_tags_item = _parse_host_tags_item(host_tags_item_data)

                host_tags.append(host_tags_item)

        _host_label_groups = d.pop("host_label_groups", UNSET)
        host_label_groups: list[LabelGroupCondition1] | Unset = UNSET
        if _host_label_groups is not UNSET:
            host_label_groups = []
            for host_label_groups_item_data in _host_label_groups:
                host_label_groups_item = LabelGroupCondition1.from_dict(
                    host_label_groups_item_data
                )

                host_label_groups.append(host_label_groups_item)

        _service_label_groups = d.pop("service_label_groups", UNSET)
        service_label_groups: list[LabelGroupCondition1] | Unset = UNSET
        if _service_label_groups is not UNSET:
            service_label_groups = []
            for service_label_groups_item_data in _service_label_groups:
                service_label_groups_item = LabelGroupCondition1.from_dict(
                    service_label_groups_item_data
                )

                service_label_groups.append(service_label_groups_item)

        _service_description = d.pop("service_description", UNSET)
        service_description: HostOrServiceCondition | Unset
        if isinstance(_service_description, Unset):
            service_description = UNSET
        else:
            service_description = HostOrServiceCondition.from_dict(_service_description)

        _host_labels = d.pop("host_labels", UNSET)
        host_labels: list[LabelCondition2] | Unset = UNSET
        if _host_labels is not UNSET:
            host_labels = []
            for host_labels_item_data in _host_labels:
                host_labels_item = LabelCondition2.from_dict(host_labels_item_data)

                host_labels.append(host_labels_item)

        _service_labels = d.pop("service_labels", UNSET)
        service_labels: list[LabelCondition2] | Unset = UNSET
        if _service_labels is not UNSET:
            service_labels = []
            for service_labels_item_data in _service_labels:
                service_labels_item = LabelCondition2.from_dict(
                    service_labels_item_data
                )

                service_labels.append(service_labels_item)

        input_conditions = cls(
            host_name=host_name,
            host_tags=host_tags,
            host_label_groups=host_label_groups,
            service_label_groups=service_label_groups,
            service_description=service_description,
            host_labels=host_labels,
            service_labels=service_labels,
        )

        input_conditions.additional_properties = d
        return input_conditions

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
