from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.site_config_attributes_update import SiteConfigAttributesUpdate


T = TypeVar("T", bound="SiteConnectionRequestUpdate")


@_attrs_define
class SiteConnectionRequestUpdate:
    """
    Attributes:
        site_config (SiteConfigAttributesUpdate):
    """

    site_config: SiteConfigAttributesUpdate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_config = self.site_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site_config": site_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_config_attributes_update import SiteConfigAttributesUpdate

        d = dict(src_dict)
        site_config = SiteConfigAttributesUpdate.from_dict(d.pop("site_config"))

        site_connection_request_update = cls(
            site_config=site_config,
        )

        site_connection_request_update.additional_properties = d
        return site_connection_request_update

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
