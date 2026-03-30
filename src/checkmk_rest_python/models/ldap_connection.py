from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ldap_connection_ssl_encryption import LDAPConnectionSslEncryption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_bind_credentials import LDAPBindCredentials
    from ..models.ldap_connect_timeout import LDAPConnectTimeout
    from ..models.ldap_connection_suffix import LDAPConnectionSuffix
    from ..models.ldap_directory_type_connection import LDAPDirectoryTypeConnection
    from ..models.ldap_page_size import LDAPPageSize
    from ..models.ldap_response_timeout import LDAPResponseTimeout
    from ..models.ldap_version import LDAPVersion
    from ..models.ldaptcp_port import LDAPTCPPort


T = TypeVar("T", bound="LDAPConnection")


@_attrs_define
class LDAPConnection:
    """
    Attributes:
        directory_type (LDAPDirectoryTypeConnection | Unset):
        bind_credentials (LDAPBindCredentials | Unset):
        tcp_port (LDAPTCPPort | Unset):
        ssl_encryption (LDAPConnectionSslEncryption | Unset): Connect to the LDAP server with a SSL encrypted
            connection. The trusted certificates authorities configured in Checkmk will be used to validate the certificate
            provided by the LDAP server. Example: enable_ssl.
        connect_timeout (LDAPConnectTimeout | Unset):
        ldap_version (LDAPVersion | Unset):
        page_size (LDAPPageSize | Unset):
        response_timeout (LDAPResponseTimeout | Unset):
        connection_suffix (LDAPConnectionSuffix | Unset):
    """

    directory_type: LDAPDirectoryTypeConnection | Unset = UNSET
    bind_credentials: LDAPBindCredentials | Unset = UNSET
    tcp_port: LDAPTCPPort | Unset = UNSET
    ssl_encryption: LDAPConnectionSslEncryption | Unset = UNSET
    connect_timeout: LDAPConnectTimeout | Unset = UNSET
    ldap_version: LDAPVersion | Unset = UNSET
    page_size: LDAPPageSize | Unset = UNSET
    response_timeout: LDAPResponseTimeout | Unset = UNSET
    connection_suffix: LDAPConnectionSuffix | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.directory_type, Unset):
            directory_type = self.directory_type.to_dict()

        bind_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bind_credentials, Unset):
            bind_credentials = self.bind_credentials.to_dict()

        tcp_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcp_port, Unset):
            tcp_port = self.tcp_port.to_dict()

        ssl_encryption: str | Unset = UNSET
        if not isinstance(self.ssl_encryption, Unset):
            ssl_encryption = self.ssl_encryption.value

        connect_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connect_timeout, Unset):
            connect_timeout = self.connect_timeout.to_dict()

        ldap_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_version, Unset):
            ldap_version = self.ldap_version.to_dict()

        page_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_size, Unset):
            page_size = self.page_size.to_dict()

        response_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_timeout, Unset):
            response_timeout = self.response_timeout.to_dict()

        connection_suffix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connection_suffix, Unset):
            connection_suffix = self.connection_suffix.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if directory_type is not UNSET:
            field_dict["directory_type"] = directory_type
        if bind_credentials is not UNSET:
            field_dict["bind_credentials"] = bind_credentials
        if tcp_port is not UNSET:
            field_dict["tcp_port"] = tcp_port
        if ssl_encryption is not UNSET:
            field_dict["ssl_encryption"] = ssl_encryption
        if connect_timeout is not UNSET:
            field_dict["connect_timeout"] = connect_timeout
        if ldap_version is not UNSET:
            field_dict["ldap_version"] = ldap_version
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if response_timeout is not UNSET:
            field_dict["response_timeout"] = response_timeout
        if connection_suffix is not UNSET:
            field_dict["connection_suffix"] = connection_suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_bind_credentials import LDAPBindCredentials
        from ..models.ldap_connect_timeout import LDAPConnectTimeout
        from ..models.ldap_connection_suffix import LDAPConnectionSuffix
        from ..models.ldap_directory_type_connection import LDAPDirectoryTypeConnection
        from ..models.ldap_page_size import LDAPPageSize
        from ..models.ldap_response_timeout import LDAPResponseTimeout
        from ..models.ldap_version import LDAPVersion
        from ..models.ldaptcp_port import LDAPTCPPort

        d = dict(src_dict)
        _directory_type = d.pop("directory_type", UNSET)
        directory_type: LDAPDirectoryTypeConnection | Unset
        if isinstance(_directory_type, Unset):
            directory_type = UNSET
        else:
            directory_type = LDAPDirectoryTypeConnection.from_dict(_directory_type)

        _bind_credentials = d.pop("bind_credentials", UNSET)
        bind_credentials: LDAPBindCredentials | Unset
        if isinstance(_bind_credentials, Unset):
            bind_credentials = UNSET
        else:
            bind_credentials = LDAPBindCredentials.from_dict(_bind_credentials)

        _tcp_port = d.pop("tcp_port", UNSET)
        tcp_port: LDAPTCPPort | Unset
        if isinstance(_tcp_port, Unset):
            tcp_port = UNSET
        else:
            tcp_port = LDAPTCPPort.from_dict(_tcp_port)

        _ssl_encryption = d.pop("ssl_encryption", UNSET)
        ssl_encryption: LDAPConnectionSslEncryption | Unset
        if isinstance(_ssl_encryption, Unset):
            ssl_encryption = UNSET
        else:
            ssl_encryption = LDAPConnectionSslEncryption(_ssl_encryption)

        _connect_timeout = d.pop("connect_timeout", UNSET)
        connect_timeout: LDAPConnectTimeout | Unset
        if isinstance(_connect_timeout, Unset):
            connect_timeout = UNSET
        else:
            connect_timeout = LDAPConnectTimeout.from_dict(_connect_timeout)

        _ldap_version = d.pop("ldap_version", UNSET)
        ldap_version: LDAPVersion | Unset
        if isinstance(_ldap_version, Unset):
            ldap_version = UNSET
        else:
            ldap_version = LDAPVersion.from_dict(_ldap_version)

        _page_size = d.pop("page_size", UNSET)
        page_size: LDAPPageSize | Unset
        if isinstance(_page_size, Unset):
            page_size = UNSET
        else:
            page_size = LDAPPageSize.from_dict(_page_size)

        _response_timeout = d.pop("response_timeout", UNSET)
        response_timeout: LDAPResponseTimeout | Unset
        if isinstance(_response_timeout, Unset):
            response_timeout = UNSET
        else:
            response_timeout = LDAPResponseTimeout.from_dict(_response_timeout)

        _connection_suffix = d.pop("connection_suffix", UNSET)
        connection_suffix: LDAPConnectionSuffix | Unset
        if isinstance(_connection_suffix, Unset):
            connection_suffix = UNSET
        else:
            connection_suffix = LDAPConnectionSuffix.from_dict(_connection_suffix)

        ldap_connection = cls(
            directory_type=directory_type,
            bind_credentials=bind_credentials,
            tcp_port=tcp_port,
            ssl_encryption=ssl_encryption,
            connect_timeout=connect_timeout,
            ldap_version=ldap_version,
            page_size=page_size,
            response_timeout=response_timeout,
            connection_suffix=connection_suffix,
        )

        ldap_connection.additional_properties = d
        return ldap_connection

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
