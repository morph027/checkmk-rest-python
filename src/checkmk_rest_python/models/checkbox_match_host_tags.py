from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkbox_match_host_tags_state import CheckboxMatchHostTagsState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aux_tag import AuxTag
    from ..models.tag_group_is_not_or_is import TagGroupIsNotOrIs
    from ..models.tag_group_none_of_or_oneof import TagGroupNoneOfOrOneof


T = TypeVar("T", bound="CheckboxMatchHostTags")


@_attrs_define
class CheckboxMatchHostTags:
    """
    Attributes:
        value (list[AuxTag | TagGroupIsNotOrIs | TagGroupNoneOfOrOneof]): A list of tag groups or aux tags with
            conditions Example: [{'tag_type': 'tag_group', 'tag_group_id': 'agent', 'operator': 'is', 'tag_id': 'checkmk-
            agent'}, {'tag_type': 'aux_tag', 'operator': 'is_set', 'tag_id': 'snmp'}].
        state (CheckboxMatchHostTagsState | Unset): To enable or disable this field Example: enabled.
    """

    value: list[AuxTag | TagGroupIsNotOrIs | TagGroupNoneOfOrOneof]
    state: CheckboxMatchHostTagsState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aux_tag import AuxTag
        from ..models.tag_group_none_of_or_oneof import TagGroupNoneOfOrOneof

        value = []
        for value_item_data in self.value:
            value_item: dict[str, Any]
            if isinstance(value_item_data, AuxTag):
                value_item = value_item_data.to_dict()
            elif isinstance(value_item_data, TagGroupNoneOfOrOneof):
                value_item = value_item_data.to_dict()
            else:
                value_item = value_item_data.to_dict()

            value.append(value_item)

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
        from ..models.aux_tag import AuxTag
        from ..models.tag_group_is_not_or_is import TagGroupIsNotOrIs
        from ..models.tag_group_none_of_or_oneof import TagGroupNoneOfOrOneof

        d = dict(src_dict)
        value = []
        _value = d.pop("value")
        for value_item_data in _value:

            def _parse_value_item(
                data: object,
            ) -> AuxTag | TagGroupIsNotOrIs | TagGroupNoneOfOrOneof:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tag_type_selector_type_0 = AuxTag.from_dict(data)

                    return componentsschemas_tag_type_selector_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tag_group_selector_type_0 = (
                        TagGroupNoneOfOrOneof.from_dict(data)
                    )

                    return componentsschemas_tag_group_selector_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tag_group_selector_type_2 = (
                    TagGroupIsNotOrIs.from_dict(data)
                )

                return componentsschemas_tag_group_selector_type_2

            value_item = _parse_value_item(value_item_data)

            value.append(value_item)

        _state = d.pop("state", UNSET)
        state: CheckboxMatchHostTagsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckboxMatchHostTagsState(_state)

        checkbox_match_host_tags = cls(
            value=value,
            state=state,
        )

        checkbox_match_host_tags.additional_properties = d
        return checkbox_match_host_tags

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
