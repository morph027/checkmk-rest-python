from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_downtime_by_id_delete_type import DeleteDowntimeByIdDeleteType

T = TypeVar("T", bound="DeleteDowntimeById")


@_attrs_define
class DeleteDowntimeById:
    """
    Attributes:
        delete_type (DeleteDowntimeByIdDeleteType): The option how to delete a downtime. Example: params.
        site_id (str): The site from which you want to delete a downtime. Example: mysite.
        downtime_id (str): The id of the downtime Example: 54.
    """

    delete_type: DeleteDowntimeByIdDeleteType
    site_id: str
    downtime_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_type = self.delete_type.value

        site_id = self.site_id

        downtime_id = self.downtime_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete_type": delete_type,
                "site_id": site_id,
                "downtime_id": downtime_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_type = DeleteDowntimeByIdDeleteType(d.pop("delete_type"))

        site_id = d.pop("site_id")

        downtime_id = d.pop("downtime_id")

        delete_downtime_by_id = cls(
            delete_type=delete_type,
            site_id=site_id,
            downtime_id=downtime_id,
        )

        delete_downtime_by_id.additional_properties = d
        return delete_downtime_by_id

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
