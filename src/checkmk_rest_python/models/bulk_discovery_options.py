from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkDiscoveryOptions")


@_attrs_define
class BulkDiscoveryOptions:
    """
    Attributes:
        monitor_undecided_services (bool | Unset): The option whether to monitor undecided services or not. Default:
            False. Example: True.
        remove_vanished_services (bool | Unset): The option whether to remove vanished services or not. Default: False.
            Example: True.
        update_service_labels (bool | Unset): The option whether to update service labels or not. Default: False.
            Example: True.
        update_service_parameters (bool | Unset): The option whether to update discovered service parameters or not.
            Default: False. Example: True.
        update_host_labels (bool | Unset): The option whether to update host labels or not. Default: False. Example:
            True.
    """

    monitor_undecided_services: bool | Unset = False
    remove_vanished_services: bool | Unset = False
    update_service_labels: bool | Unset = False
    update_service_parameters: bool | Unset = False
    update_host_labels: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_undecided_services = self.monitor_undecided_services

        remove_vanished_services = self.remove_vanished_services

        update_service_labels = self.update_service_labels

        update_service_parameters = self.update_service_parameters

        update_host_labels = self.update_host_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor_undecided_services is not UNSET:
            field_dict["monitor_undecided_services"] = monitor_undecided_services
        if remove_vanished_services is not UNSET:
            field_dict["remove_vanished_services"] = remove_vanished_services
        if update_service_labels is not UNSET:
            field_dict["update_service_labels"] = update_service_labels
        if update_service_parameters is not UNSET:
            field_dict["update_service_parameters"] = update_service_parameters
        if update_host_labels is not UNSET:
            field_dict["update_host_labels"] = update_host_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_undecided_services = d.pop("monitor_undecided_services", UNSET)

        remove_vanished_services = d.pop("remove_vanished_services", UNSET)

        update_service_labels = d.pop("update_service_labels", UNSET)

        update_service_parameters = d.pop("update_service_parameters", UNSET)

        update_host_labels = d.pop("update_host_labels", UNSET)

        bulk_discovery_options = cls(
            monitor_undecided_services=monitor_undecided_services,
            remove_vanished_services=remove_vanished_services,
            update_service_labels=update_service_labels,
            update_service_parameters=update_service_parameters,
            update_host_labels=update_host_labels,
        )

        bulk_discovery_options.additional_properties = d
        return bulk_discovery_options

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
