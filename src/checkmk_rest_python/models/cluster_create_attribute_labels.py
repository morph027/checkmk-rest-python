from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClusterCreateAttributeLabels")


@_attrs_define
class ClusterCreateAttributeLabels:
    """Labels allow you to flexibly group your hosts in order to refer to them later at other places in Checkmk, e.g. in
    rule chains.<br><b>Label format:</b> key:value<br><br>Neither the key nor the value can contain ‘:’. Checkmk does
    not perform any other validation on the labels you use.

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_create_attribute_labels = cls()

        cluster_create_attribute_labels.additional_properties = d
        return cluster_create_attribute_labels

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
