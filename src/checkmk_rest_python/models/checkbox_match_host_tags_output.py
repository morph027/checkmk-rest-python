from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_match_host_tags_output_state import (
    CheckboxMatchHostTagsOutputState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aux_tag_output import AuxTagOutput
    from ..models.tag_group_is_not_or_is_output import TagGroupIsNotOrIsOutput
    from ..models.tag_group_none_of_or_one_of_output import TagGroupNoneOfOrOneOfOutput


T = TypeVar("T", bound="CheckboxMatchHostTagsOutput")


@_attrs_define
class CheckboxMatchHostTagsOutput:
    """
    Attributes:
        state (CheckboxMatchHostTagsOutputState | Unset): To enable or disable this field Example: enabled.
        value (list[AuxTagOutput | TagGroupIsNotOrIsOutput | TagGroupNoneOfOrOneOfOutput] | Unset): A list of tag groups
            or aux tags with conditions Example: [{'tag_type': 'tag_group', 'tag_group_id': 'agent', 'operator': 'is',
            'tag_id': 'checkmk-agent'}, {'tag_type': 'aux_tag', 'operator': 'is_set', 'tag_id': 'snmp'}].
    """

    state: CheckboxMatchHostTagsOutputState | Unset = UNSET
    value: (
        list[AuxTagOutput | TagGroupIsNotOrIsOutput | TagGroupNoneOfOrOneOfOutput]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aux_tag_output import AuxTagOutput
        from ..models.tag_group_none_of_or_one_of_output import (
            TagGroupNoneOfOrOneOfOutput,
        )

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item: dict[str, Any]
                if isinstance(value_item_data, AuxTagOutput):
                    value_item = value_item_data.to_dict()
                elif isinstance(value_item_data, TagGroupNoneOfOrOneOfOutput):
                    value_item = value_item_data.to_dict()
                else:
                    value_item = value_item_data.to_dict()

                value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aux_tag_output import AuxTagOutput
        from ..models.tag_group_is_not_or_is_output import TagGroupIsNotOrIsOutput
        from ..models.tag_group_none_of_or_one_of_output import (
            TagGroupNoneOfOrOneOfOutput,
        )

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckboxMatchHostTagsOutputState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxMatchHostTagsOutputState(_state)

        _value = d.pop("value", UNSET)
        value: (
            list[AuxTagOutput | TagGroupIsNotOrIsOutput | TagGroupNoneOfOrOneOfOutput]
            | Unset
        ) = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:

                def _parse_value_item(
                    data: object,
                ) -> (
                    AuxTagOutput | TagGroupIsNotOrIsOutput | TagGroupNoneOfOrOneOfOutput
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_tag_type_selector_output_type_0 = (
                            AuxTagOutput.from_dict(data)
                        )

                        return componentsschemas_tag_type_selector_output_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_tag_group_selector_output_type_0 = (
                            TagGroupNoneOfOrOneOfOutput.from_dict(data)
                        )

                        return componentsschemas_tag_group_selector_output_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tag_group_selector_output_type_2 = (
                        TagGroupIsNotOrIsOutput.from_dict(data)
                    )

                    return componentsschemas_tag_group_selector_output_type_2

                value_item = _parse_value_item(value_item_data)

                value.append(value_item)

        checkbox_match_host_tags_output = cls(
            state=state,
            value=value,
        )

        checkbox_match_host_tags_output.additional_properties = d
        return checkbox_match_host_tags_output

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
