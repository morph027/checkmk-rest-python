from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_address_range import IPAddressRange
    from ..models.ip_addresses import IPAddresses
    from ..models.ip_network import IPNetwork
    from ..models.ip_regexp import IPRegexp
    from ..models.time_allowed_range import TimeAllowedRange
    from ..models.translate_names import TranslateNames


T = TypeVar("T", bound="NetworkScan")


@_attrs_define
class NetworkScan:
    """
    Attributes:
        addresses (list[IPAddresses | IPAddressRange | IPNetwork | IPRegexp]): IPv4 addresses to include.
        time_allowed (list[TimeAllowedRange]): Only execute the discovery during this time range each day..
        exclude_addresses (list[IPAddresses | IPAddressRange | IPNetwork | IPRegexp] | Unset): IPv4 addresses to
            exclude.
        scan_interval (int | Unset): Scan interval in seconds. Default is 1 day, minimum is 1 hour. Default: 86400.
        set_ip_address (bool | Unset): When set, the found IPv4 address is set on the discovered host. Default: True.
        max_parallel_pings (int | Unset): Set the maximum number of concurrent pings sent to target IP addresses.
            Default: 100.
        run_as (str | Unset): Execute the network scan in the Checkmk user context of the chosen user. This user needs
            the permission to add new hosts to this folder.
        tag_criticality (str | Unset): Specify which criticality tag to set on the host created by the network scan.
            This field is required if the criticality tag group exists, otherwise it as to be omitted.
        translate_names (TranslateNames | Unset):
    """

    addresses: list[IPAddresses | IPAddressRange | IPNetwork | IPRegexp]
    time_allowed: list[TimeAllowedRange]
    exclude_addresses: (
        list[IPAddresses | IPAddressRange | IPNetwork | IPRegexp] | Unset
    ) = UNSET
    scan_interval: int | Unset = 86400
    set_ip_address: bool | Unset = True
    max_parallel_pings: int | Unset = 100
    run_as: str | Unset = UNSET
    tag_criticality: str | Unset = UNSET
    translate_names: TranslateNames | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_address_range import IPAddressRange
        from ..models.ip_addresses import IPAddresses
        from ..models.ip_network import IPNetwork

        addresses = []
        for addresses_item_data in self.addresses:
            addresses_item: dict[str, Any]
            if isinstance(addresses_item_data, IPAddressRange):
                addresses_item = addresses_item_data.to_dict()
            elif isinstance(addresses_item_data, IPNetwork):
                addresses_item = addresses_item_data.to_dict()
            elif isinstance(addresses_item_data, IPAddresses):
                addresses_item = addresses_item_data.to_dict()
            else:
                addresses_item = addresses_item_data.to_dict()

            addresses.append(addresses_item)

        time_allowed = []
        for time_allowed_item_data in self.time_allowed:
            time_allowed_item = time_allowed_item_data.to_dict()
            time_allowed.append(time_allowed_item)

        exclude_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclude_addresses, Unset):
            exclude_addresses = []
            for exclude_addresses_item_data in self.exclude_addresses:
                exclude_addresses_item: dict[str, Any]
                if isinstance(exclude_addresses_item_data, IPAddressRange):
                    exclude_addresses_item = exclude_addresses_item_data.to_dict()
                elif isinstance(exclude_addresses_item_data, IPNetwork):
                    exclude_addresses_item = exclude_addresses_item_data.to_dict()
                elif isinstance(exclude_addresses_item_data, IPAddresses):
                    exclude_addresses_item = exclude_addresses_item_data.to_dict()
                else:
                    exclude_addresses_item = exclude_addresses_item_data.to_dict()

                exclude_addresses.append(exclude_addresses_item)

        scan_interval = self.scan_interval

        set_ip_address = self.set_ip_address

        max_parallel_pings = self.max_parallel_pings

        run_as = self.run_as

        tag_criticality = self.tag_criticality

        translate_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translate_names, Unset):
            translate_names = self.translate_names.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addresses": addresses,
                "time_allowed": time_allowed,
            }
        )
        if exclude_addresses is not UNSET:
            field_dict["exclude_addresses"] = exclude_addresses
        if scan_interval is not UNSET:
            field_dict["scan_interval"] = scan_interval
        if set_ip_address is not UNSET:
            field_dict["set_ip_address"] = set_ip_address
        if max_parallel_pings is not UNSET:
            field_dict["max_parallel_pings"] = max_parallel_pings
        if run_as is not UNSET:
            field_dict["run_as"] = run_as
        if tag_criticality is not UNSET:
            field_dict["tag_criticality"] = tag_criticality
        if translate_names is not UNSET:
            field_dict["translate_names"] = translate_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_range import IPAddressRange
        from ..models.ip_addresses import IPAddresses
        from ..models.ip_network import IPNetwork
        from ..models.ip_regexp import IPRegexp
        from ..models.time_allowed_range import TimeAllowedRange
        from ..models.translate_names import TranslateNames

        d = dict(src_dict)
        addresses = []
        _addresses = d.pop("addresses")
        for addresses_item_data in _addresses:

            def _parse_addresses_item(
                data: object,
            ) -> IPAddresses | IPAddressRange | IPNetwork | IPRegexp:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ip_range_with_regexp_type_0 = (
                        IPAddressRange.from_dict(data)
                    )

                    return componentsschemas_ip_range_with_regexp_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ip_range_with_regexp_type_1 = IPNetwork.from_dict(
                        data
                    )

                    return componentsschemas_ip_range_with_regexp_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ip_range_with_regexp_type_2 = (
                        IPAddresses.from_dict(data)
                    )

                    return componentsschemas_ip_range_with_regexp_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_ip_range_with_regexp_type_3 = IPRegexp.from_dict(data)

                return componentsschemas_ip_range_with_regexp_type_3

            addresses_item = _parse_addresses_item(addresses_item_data)

            addresses.append(addresses_item)

        time_allowed = []
        _time_allowed = d.pop("time_allowed")
        for time_allowed_item_data in _time_allowed:
            time_allowed_item = TimeAllowedRange.from_dict(time_allowed_item_data)

            time_allowed.append(time_allowed_item)

        _exclude_addresses = d.pop("exclude_addresses", UNSET)
        exclude_addresses: (
            list[IPAddresses | IPAddressRange | IPNetwork | IPRegexp] | Unset
        ) = UNSET
        if _exclude_addresses is not UNSET:
            exclude_addresses = []
            for exclude_addresses_item_data in _exclude_addresses:

                def _parse_exclude_addresses_item(
                    data: object,
                ) -> IPAddresses | IPAddressRange | IPNetwork | IPRegexp:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_ip_range_with_regexp_type_0 = (
                            IPAddressRange.from_dict(data)
                        )

                        return componentsschemas_ip_range_with_regexp_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_ip_range_with_regexp_type_1 = (
                            IPNetwork.from_dict(data)
                        )

                        return componentsschemas_ip_range_with_regexp_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_ip_range_with_regexp_type_2 = (
                            IPAddresses.from_dict(data)
                        )

                        return componentsschemas_ip_range_with_regexp_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_ip_range_with_regexp_type_3 = IPRegexp.from_dict(
                        data
                    )

                    return componentsschemas_ip_range_with_regexp_type_3

                exclude_addresses_item = _parse_exclude_addresses_item(
                    exclude_addresses_item_data
                )

                exclude_addresses.append(exclude_addresses_item)

        scan_interval = d.pop("scan_interval", UNSET)

        set_ip_address = d.pop("set_ip_address", UNSET)

        max_parallel_pings = d.pop("max_parallel_pings", UNSET)

        run_as = d.pop("run_as", UNSET)

        tag_criticality = d.pop("tag_criticality", UNSET)

        _translate_names = d.pop("translate_names", UNSET)
        translate_names: TranslateNames | Unset
        if isinstance(_translate_names, Unset):
            translate_names = UNSET
        else:
            translate_names = TranslateNames.from_dict(_translate_names)

        network_scan = cls(
            addresses=addresses,
            time_allowed=time_allowed,
            exclude_addresses=exclude_addresses,
            scan_interval=scan_interval,
            set_ip_address=set_ip_address,
            max_parallel_pings=max_parallel_pings,
            run_as=run_as,
            tag_criticality=tag_criticality,
            translate_names=translate_names,
        )

        network_scan.additional_properties = d
        return network_scan

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
