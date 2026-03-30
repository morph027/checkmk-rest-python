from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Params")


@_attrs_define
class Params:
    """
    Attributes:
        strict (Any | Unset): Whether to use strict matching Example: True.
        group_type (str | Unset): The group type Example: host.
        group_id (str | Unset): The group id Example: my_group.
        world (str | Unset): World field Example: Earth.
        presentation (str | Unset): Presentation field Example: lines.
        mode (str | Unset): Mode field Example: template.
        datasource (str | Unset): Datasource field Example: services.
        single_infos (list[str] | Unset): Single infos field Example: ['my_info'].
    """

    strict: Any | Unset = UNSET
    group_type: str | Unset = UNSET
    group_id: str | Unset = UNSET
    world: str | Unset = UNSET
    presentation: str | Unset = UNSET
    mode: str | Unset = UNSET
    datasource: str | Unset = UNSET
    single_infos: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strict = self.strict

        group_type = self.group_type

        group_id = self.group_id

        world = self.world

        presentation = self.presentation

        mode = self.mode

        datasource = self.datasource

        single_infos: list[str] | Unset = UNSET
        if not isinstance(self.single_infos, Unset):
            single_infos = self.single_infos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if strict is not UNSET:
            field_dict["strict"] = strict
        if group_type is not UNSET:
            field_dict["group_type"] = group_type
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if world is not UNSET:
            field_dict["world"] = world
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if mode is not UNSET:
            field_dict["mode"] = mode
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if single_infos is not UNSET:
            field_dict["single_infos"] = single_infos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strict = d.pop("strict", UNSET)

        group_type = d.pop("group_type", UNSET)

        group_id = d.pop("group_id", UNSET)

        world = d.pop("world", UNSET)

        presentation = d.pop("presentation", UNSET)

        mode = d.pop("mode", UNSET)

        datasource = d.pop("datasource", UNSET)

        single_infos = cast(list[str], d.pop("single_infos", UNSET))

        params = cls(
            strict=strict,
            group_type=group_type,
            group_id=group_id,
            world=world,
            presentation=presentation,
            mode=mode,
            datasource=datasource,
            single_infos=single_infos,
        )

        params.additional_properties = d
        return params

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
