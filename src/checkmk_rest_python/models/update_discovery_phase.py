from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_discovery_phase_target_phase import UpdateDiscoveryPhaseTargetPhase

T = TypeVar("T", bound="UpdateDiscoveryPhase")


@_attrs_define
class UpdateDiscoveryPhase:
    """
    Attributes:
        check_type (str): The name of the check which this service uses. Example: df.
        service_item (None | str): The value uniquely identifying the service on a given host. Example: /home.
        target_phase (UpdateDiscoveryPhaseTargetPhase): The target phase of the service. Example: monitored.
    """

    check_type: str
    service_item: None | str
    target_phase: UpdateDiscoveryPhaseTargetPhase
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_type = self.check_type

        service_item: None | str
        service_item = self.service_item

        target_phase = self.target_phase.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "check_type": check_type,
                "service_item": service_item,
                "target_phase": target_phase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_type = d.pop("check_type")

        def _parse_service_item(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        service_item = _parse_service_item(d.pop("service_item"))

        target_phase = UpdateDiscoveryPhaseTargetPhase(d.pop("target_phase"))

        update_discovery_phase = cls(
            check_type=check_type,
            service_item=service_item,
            target_phase=target_phase,
        )

        update_discovery_phase.additional_properties = d
        return update_discovery_phase

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
