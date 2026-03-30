from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.modify_downtime_by_service_group_modify_type import (
    ModifyDowntimeByServiceGroupModifyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_end_time_by_datetime import ModifyEndTimeByDatetime
    from ..models.modify_end_time_by_delta import ModifyEndTimeByDelta


T = TypeVar("T", bound="ModifyDowntimeByServiceGroup")


@_attrs_define
class ModifyDowntimeByServiceGroup:
    """
    Attributes:
        modify_type (ModifyDowntimeByServiceGroupModifyType): The option of how to select the downtimes to be targeted
            by the modification. Example: params.
        servicegroup_name (str): Name of a valid servicegroup, all current downtimes for services in this group will be
            modified. Example: windows.
        end_time (ModifyEndTimeByDatetime | ModifyEndTimeByDelta | Unset):
        comment (str | Unset): The comment for the downtime. Example: Security updates.
    """

    modify_type: ModifyDowntimeByServiceGroupModifyType
    servicegroup_name: str
    end_time: ModifyEndTimeByDatetime | ModifyEndTimeByDelta | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.modify_end_time_by_datetime import ModifyEndTimeByDatetime

        modify_type = self.modify_type.value

        servicegroup_name = self.servicegroup_name

        end_time: dict[str, Any] | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, ModifyEndTimeByDatetime):
            end_time = self.end_time.to_dict()
        else:
            end_time = self.end_time.to_dict()

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modify_type": modify_type,
                "servicegroup_name": servicegroup_name,
            }
        )
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_end_time_by_datetime import ModifyEndTimeByDatetime
        from ..models.modify_end_time_by_delta import ModifyEndTimeByDelta

        d = dict(src_dict)
        modify_type = ModifyDowntimeByServiceGroupModifyType(d.pop("modify_type"))

        servicegroup_name = d.pop("servicegroup_name")

        def _parse_end_time(
            data: object,
        ) -> ModifyEndTimeByDatetime | ModifyEndTimeByDelta | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_modify_end_time_type_type_0 = (
                    ModifyEndTimeByDatetime.from_dict(data)
                )

                return componentsschemas_modify_end_time_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_modify_end_time_type_type_1 = (
                ModifyEndTimeByDelta.from_dict(data)
            )

            return componentsschemas_modify_end_time_type_type_1

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        comment = d.pop("comment", UNSET)

        modify_downtime_by_service_group = cls(
            modify_type=modify_type,
            servicegroup_name=servicegroup_name,
            end_time=end_time,
            comment=comment,
        )

        modify_downtime_by_service_group.additional_properties = d
        return modify_downtime_by_service_group

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
