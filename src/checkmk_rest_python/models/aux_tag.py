from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aux_tag_operator import AuxTagOperator
from ..models.aux_tag_tag_type import AuxTagTagType

T = TypeVar("T", bound="AuxTag")


@_attrs_define
class AuxTag:
    """
    Attributes:
        tag_type (AuxTagTagType):  Example: aux_tag.
        operator (AuxTagOperator):  Example: is_set.
        tag_id (None | str): Tag ids are available via the aux tag endpoint. Example: snmp.
    """

    tag_type: AuxTagTagType
    operator: AuxTagOperator
    tag_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_type = self.tag_type.value

        operator = self.operator.value

        tag_id: None | str
        tag_id = self.tag_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_type": tag_type,
                "operator": operator,
                "tag_id": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tag_type = AuxTagTagType(d.pop("tag_type"))

        operator = AuxTagOperator(d.pop("operator"))

        def _parse_tag_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tag_id = _parse_tag_id(d.pop("tag_id"))

        aux_tag = cls(
            tag_type=tag_type,
            operator=operator,
            tag_id=tag_id,
        )

        aux_tag.additional_properties = d
        return aux_tag

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
