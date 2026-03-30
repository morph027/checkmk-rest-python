from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.modify_end_time_by_delta_modify_type import ModifyEndTimeByDeltaModifyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyEndTimeByDelta")


@_attrs_define
class ModifyEndTimeByDelta:
    """
    Attributes:
        value (int): A positive or negative number representing the amount of minutes to be added to or substracted from
            the current end time. The value must be non-zero Example: 60.
        modify_type (ModifyEndTimeByDeltaModifyType | Unset): How to modify the end time of a downtime. Example:
            absolute.
    """

    value: int
    modify_type: ModifyEndTimeByDeltaModifyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        modify_type: str | Unset = UNSET
        if not isinstance(self.modify_type, Unset):
            modify_type = self.modify_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if modify_type is not UNSET:
            field_dict["modify_type"] = modify_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        _modify_type = d.pop("modify_type", UNSET)
        modify_type: ModifyEndTimeByDeltaModifyType | Unset
        if isinstance(_modify_type, Unset):
            modify_type = UNSET
        else:
            modify_type = ModifyEndTimeByDeltaModifyType(_modify_type)

        modify_end_time_by_delta = cls(
            value=value,
            modify_type=modify_type,
        )

        modify_end_time_by_delta.additional_properties = d
        return modify_end_time_by_delta

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
