from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.configuration import Configuration
    from ..models.create_in_folder import CreateInFolder
    from ..models.create_in_host_location import CreateInHostLocation
    from ..models.no_gateway_hosts import NoGatewayHosts
    from ..models.performance_settings import PerformanceSettings


T = TypeVar("T", bound="ParentScan")


@_attrs_define
class ParentScan:
    """
    Attributes:
        host_names (list[str]): Targeted hosts for parent scan. Example: ['host1', 'host2'].
        performance (PerformanceSettings):
        configuration (Configuration):
        gateway_hosts (CreateInFolder | CreateInHostLocation | NoGatewayHosts):
    """

    host_names: list[str]
    performance: PerformanceSettings
    configuration: Configuration
    gateway_hosts: CreateInFolder | CreateInHostLocation | NoGatewayHosts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_in_folder import CreateInFolder
        from ..models.no_gateway_hosts import NoGatewayHosts

        host_names = self.host_names

        performance = self.performance.to_dict()

        configuration = self.configuration.to_dict()

        gateway_hosts: dict[str, Any]
        if isinstance(self.gateway_hosts, NoGatewayHosts):
            gateway_hosts = self.gateway_hosts.to_dict()
        elif isinstance(self.gateway_hosts, CreateInFolder):
            gateway_hosts = self.gateway_hosts.to_dict()
        else:
            gateway_hosts = self.gateway_hosts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_names": host_names,
                "performance": performance,
                "configuration": configuration,
                "gateway_hosts": gateway_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration import Configuration
        from ..models.create_in_folder import CreateInFolder
        from ..models.create_in_host_location import CreateInHostLocation
        from ..models.no_gateway_hosts import NoGatewayHosts
        from ..models.performance_settings import PerformanceSettings

        d = dict(src_dict)
        host_names = cast(list[str], d.pop("host_names"))

        performance = PerformanceSettings.from_dict(d.pop("performance"))

        configuration = Configuration.from_dict(d.pop("configuration"))

        def _parse_gateway_hosts(
            data: object,
        ) -> CreateInFolder | CreateInHostLocation | NoGatewayHosts:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_gateway_hosts_type_0 = NoGatewayHosts.from_dict(data)

                return componentsschemas_gateway_hosts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_gateway_hosts_type_1 = CreateInFolder.from_dict(data)

                return componentsschemas_gateway_hosts_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_gateway_hosts_type_2 = CreateInHostLocation.from_dict(
                data
            )

            return componentsschemas_gateway_hosts_type_2

        gateway_hosts = _parse_gateway_hosts(d.pop("gateway_hosts"))

        parent_scan = cls(
            host_names=host_names,
            performance=performance,
            configuration=configuration,
            gateway_hosts=gateway_hosts,
        )

        parent_scan.additional_properties = d
        return parent_scan

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
