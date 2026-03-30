from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentControllerCertificateSettings")


@_attrs_define
class AgentControllerCertificateSettings:
    """
    Attributes:
        lifetime_in_months (int): Lifetime of agent controller certificates in months Example: 60.
    """

    lifetime_in_months: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lifetime_in_months = self.lifetime_in_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lifetime_in_months": lifetime_in_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lifetime_in_months = d.pop("lifetime_in_months")

        agent_controller_certificate_settings = cls(
            lifetime_in_months=lifetime_in_months,
        )

        agent_controller_certificate_settings.additional_properties = d
        return agent_controller_certificate_settings

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
