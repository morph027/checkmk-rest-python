from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.directory_type_manual_request_type import DirectoryTypeManualRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectoryTypeManualRequest")


@_attrs_define
class DirectoryTypeManualRequest:
    """
    Attributes:
        type_ (DirectoryTypeManualRequestType): Select the software the LDAP directory is based on. Example:
            active_directory_manual.
        ldap_server (str): Set the host address of the LDAP server. Might be an IP address or resolvable host name.
            Example: your_ldap_server.example.com.
        failover_servers (list[str] | Unset): When the connection to the first server fails with connect specific errors
            like timeouts or some other network related problems, the connect mechanism will try to use this server instead
            of the server configured above. If you use persistent connections (default), the connection is being used until
            the LDAP is not reachable or the local webserver is restarted. You may paste a text from your clipboard which
            contains several parts separated by ';' characters into the last input field. The text will then be split by
            these separators and the single parts are added into dedicated input fields. Example: ['192.168.5.2',
            '195.65.2.8'].
    """

    type_: DirectoryTypeManualRequestType
    ldap_server: str
    failover_servers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        ldap_server = self.ldap_server

        failover_servers: list[str] | Unset = UNSET
        if not isinstance(self.failover_servers, Unset):
            failover_servers = self.failover_servers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "ldap_server": ldap_server,
            }
        )
        if failover_servers is not UNSET:
            field_dict["failover_servers"] = failover_servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = DirectoryTypeManualRequestType(d.pop("type"))

        ldap_server = d.pop("ldap_server")

        failover_servers = cast(list[str], d.pop("failover_servers", UNSET))

        directory_type_manual_request = cls(
            type_=type_,
            ldap_server=ldap_server,
            failover_servers=failover_servers,
        )

        directory_type_manual_request.additional_properties = d
        return directory_type_manual_request

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
