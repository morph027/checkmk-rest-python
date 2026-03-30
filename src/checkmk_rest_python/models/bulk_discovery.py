from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_discovery_options import BulkDiscoveryOptions


T = TypeVar("T", bound="BulkDiscovery")


@_attrs_define
class BulkDiscovery:
    """
    Attributes:
        hostnames (list[str]): A list of host names Example: ['example', 'sample'].
        options (BulkDiscoveryOptions):
        do_full_scan (bool | Unset): The option whether to perform a full scan or not. Default: True. Example: True.
        bulk_size (int | Unset): The number of hosts to be handled at once. Default: 10. Example: 10.
        ignore_errors (bool | Unset): The option whether to ignore errors in single check plug-ins. Default: True.
            Example: True.
    """

    hostnames: list[str]
    options: BulkDiscoveryOptions
    do_full_scan: bool | Unset = True
    bulk_size: int | Unset = 10
    ignore_errors: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostnames = self.hostnames

        options = self.options.to_dict()

        do_full_scan = self.do_full_scan

        bulk_size = self.bulk_size

        ignore_errors = self.ignore_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostnames": hostnames,
                "options": options,
            }
        )
        if do_full_scan is not UNSET:
            field_dict["do_full_scan"] = do_full_scan
        if bulk_size is not UNSET:
            field_dict["bulk_size"] = bulk_size
        if ignore_errors is not UNSET:
            field_dict["ignore_errors"] = ignore_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_discovery_options import BulkDiscoveryOptions

        d = dict(src_dict)
        hostnames = cast(list[str], d.pop("hostnames"))

        options = BulkDiscoveryOptions.from_dict(d.pop("options"))

        do_full_scan = d.pop("do_full_scan", UNSET)

        bulk_size = d.pop("bulk_size", UNSET)

        ignore_errors = d.pop("ignore_errors", UNSET)

        bulk_discovery = cls(
            hostnames=hostnames,
            options=options,
            do_full_scan=do_full_scan,
            bulk_size=bulk_size,
            ignore_errors=ignore_errors,
        )

        bulk_discovery.additional_properties = d
        return bulk_discovery

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
