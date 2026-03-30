from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discover_services_mode import DiscoverServicesMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoverServices")


@_attrs_define
class DiscoverServices:
    """
    Attributes:
        host_name (str): The host of the service which shall be updated. Example: example.com.
        mode (DiscoverServicesMode | Unset): The mode of the discovery action. The 'refresh' mode starts a new service
                    discovery which will contact the host and identify undecided and vanished services and host
                    labels. Those services and host labels can be added or removed accordingly with the
                    'fix_all' mode. The 'tabula_rasa' mode combines these two procedures. The 'new', 'remove',
                    'only_host_labels' and 'only_service_labels' modes give you more granular control. Both the
                    'tabula_rasa' and 'refresh' modes will start a background job and the endpoint will return
                    a redirect to the 'wait-for-completion' endpoint. All other modes will return an immediate
                    result instead. Keep in mind that the non background job modes only work with scanned data,
                    so you may need to run "refresh" first. The corresponding user interface option for each
                    discovery mode is shown below.

             * `new` - Monitor undecided services
             * `remove` - Remove vanished services
             * `fix_all` - Accept all
             * `tabula_rasa` - Remove all and find new
             * `refresh` - Rescan
             * `only_host_labels` - Update host labels
             * `only_service_labels` - Update service labels
                 Default: DiscoverServicesMode.FIX_ALL. Example: refresh.
    """

    host_name: str
    mode: DiscoverServicesMode | Unset = DiscoverServicesMode.FIX_ALL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host_name = self.host_name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_name": host_name,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_name = d.pop("host_name")

        _mode = d.pop("mode", UNSET)
        mode: DiscoverServicesMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = DiscoverServicesMode(_mode)

        discover_services = cls(
            host_name=host_name,
            mode=mode,
        )

        discover_services.additional_properties = d
        return discover_services

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
