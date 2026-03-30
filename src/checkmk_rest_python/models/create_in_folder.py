from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_in_folder_option import CreateInFolderOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInFolder")


@_attrs_define
class CreateInFolder:
    r"""
    Attributes:
        option (CreateInFolderOption): Creation of gateway hosts option Example: no_gateway_hosts.
        folder (str): Folder location where the gateway hosts should be created

            Path delimiters can be either `~`, `/` or `\`. Please use the one most appropriate for your quoting/escaping
            needs. A good default choice is `~`. Example: /.
        hosts_alias (str | Unset): Alias for created gateway hosts Default: 'Created by parent scan'. Example: Created
            by parent scan.
    """

    option: CreateInFolderOption
    folder: str
    hosts_alias: str | Unset = "Created by parent scan"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        folder = self.folder

        hosts_alias = self.hosts_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "folder": folder,
            }
        )
        if hosts_alias is not UNSET:
            field_dict["hosts_alias"] = hosts_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = CreateInFolderOption(d.pop("option"))

        folder = d.pop("folder")

        hosts_alias = d.pop("hosts_alias", UNSET)

        create_in_folder = cls(
            option=option,
            folder=folder,
            hosts_alias=hosts_alias,
        )

        create_in_folder.additional_properties = d
        return create_in_folder

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
