from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.folder_view_attribute_management_protocol import (
    FolderViewAttributeManagementProtocol,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_view_attribute_labels import FolderViewAttributeLabels
    from ..models.folder_view_attribute_management_ipmi_credentials_type_1_type_0 import (
        FolderViewAttributeManagementIpmiCredentialsType1Type0,
    )
    from ..models.folder_view_attribute_management_snmp_community_type_1_type_0 import (
        FolderViewAttributeManagementSnmpCommunityType1Type0,
    )
    from ..models.host_contact_group import HostContactGroup
    from ..models.ipmi_parameters import IPMIParameters
    from ..models.meta_data import MetaData
    from ..models.network_scan import NetworkScan
    from ..models.network_scan_result import NetworkScanResult
    from ..models.snm_pv_3_auth_no_privacy import SNMPv3AuthNoPrivacy
    from ..models.snm_pv_3_auth_privacy import SNMPv3AuthPrivacy
    from ..models.snm_pv_3_no_auth_no_privacy import SNMPv3NoAuthNoPrivacy
    from ..models.snmp_community import SNMPCommunity


T = TypeVar("T", bound="FolderViewAttribute")


@_attrs_define
class FolderViewAttribute:
    """
    Attributes:
        site (str | Unset): The site that should monitor this host.
        contactgroups (HostContactGroup | Unset):
        parents (list[str] | Unset): A list of parents of this host.
        tag_address_family (str | Unset):
        tag_agent (str | Unset):
        tag_snmp_ds (str | Unset):
        snmp_community (SNMPCommunity | SNMPv3AuthNoPrivacy | SNMPv3AuthPrivacy | SNMPv3NoAuthNoPrivacy | Unset):
        tag_piggyback (str | Unset): By default, each host has a piggyback data source.<br><br><b>Use piggyback data
            from other hosts if present:</b><br>If selected, the <tt>Check_MK</tt> service of this host will process the
            piggyback data, but will not warn if no piggyback data is available. The associated discovered services would
            become stale.<br><br><b>Always use and expect piggyback data:</b><br>The host will expect piggyback data, and
            the <tt>Check_MK</tt> service of this host will warn if no piggyback data is available.<br><br><b>Never use
            piggyback data:</b><br>The <tt>Check_MK</tt> service does not process piggybacking data at all, and will ignore
            it if it's available.
        tag_criticality (str | Unset):
        tag_networking (str | Unset):
        labels (FolderViewAttributeLabels | Unset): Labels allow you to flexibly group your hosts in order to refer to
            them later at other places in Checkmk, e.g. in rule chains.<br><b>Label format:</b> key:value<br><br>Neither the
            key nor the value can contain ‘:’. Checkmk does not perform any other validation on the labels you use.
        network_scan (NetworkScan | Unset):
        network_scan_result (NetworkScanResult | Unset):
        management_protocol (FolderViewAttributeManagementProtocol | Unset): The protocol used to connect to the
            management board.

            Valid options are:

             * `none` - No management board
             * `snmp` - Connect using SNMP
             * `ipmi` - Connect using IPMI
        management_snmp_community (FolderViewAttributeManagementSnmpCommunityType1Type0 | None | SNMPCommunity |
            SNMPv3AuthNoPrivacy | SNMPv3AuthPrivacy | SNMPv3NoAuthNoPrivacy | Unset): SNMP credentials
        management_ipmi_credentials (FolderViewAttributeManagementIpmiCredentialsType1Type0 | IPMIParameters | None |
            Unset): IPMI credentials
        meta_data (MetaData | Unset):
    """

    site: str | Unset = UNSET
    contactgroups: HostContactGroup | Unset = UNSET
    parents: list[str] | Unset = UNSET
    tag_address_family: str | Unset = UNSET
    tag_agent: str | Unset = UNSET
    tag_snmp_ds: str | Unset = UNSET
    snmp_community: (
        SNMPCommunity
        | SNMPv3AuthNoPrivacy
        | SNMPv3AuthPrivacy
        | SNMPv3NoAuthNoPrivacy
        | Unset
    ) = UNSET
    tag_piggyback: str | Unset = UNSET
    tag_criticality: str | Unset = UNSET
    tag_networking: str | Unset = UNSET
    labels: FolderViewAttributeLabels | Unset = UNSET
    network_scan: NetworkScan | Unset = UNSET
    network_scan_result: NetworkScanResult | Unset = UNSET
    management_protocol: FolderViewAttributeManagementProtocol | Unset = UNSET
    management_snmp_community: (
        FolderViewAttributeManagementSnmpCommunityType1Type0
        | None
        | SNMPCommunity
        | SNMPv3AuthNoPrivacy
        | SNMPv3AuthPrivacy
        | SNMPv3NoAuthNoPrivacy
        | Unset
    ) = UNSET
    management_ipmi_credentials: (
        FolderViewAttributeManagementIpmiCredentialsType1Type0
        | IPMIParameters
        | None
        | Unset
    ) = UNSET
    meta_data: MetaData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.folder_view_attribute_management_ipmi_credentials_type_1_type_0 import (
            FolderViewAttributeManagementIpmiCredentialsType1Type0,
        )
        from ..models.folder_view_attribute_management_snmp_community_type_1_type_0 import (
            FolderViewAttributeManagementSnmpCommunityType1Type0,
        )
        from ..models.ipmi_parameters import IPMIParameters
        from ..models.snm_pv_3_auth_no_privacy import SNMPv3AuthNoPrivacy
        from ..models.snm_pv_3_auth_privacy import SNMPv3AuthPrivacy
        from ..models.snm_pv_3_no_auth_no_privacy import SNMPv3NoAuthNoPrivacy
        from ..models.snmp_community import SNMPCommunity

        site = self.site

        contactgroups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contactgroups, Unset):
            contactgroups = self.contactgroups.to_dict()

        parents: list[str] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = self.parents

        tag_address_family = self.tag_address_family

        tag_agent = self.tag_agent

        tag_snmp_ds = self.tag_snmp_ds

        snmp_community: dict[str, Any] | Unset
        if isinstance(self.snmp_community, Unset):
            snmp_community = UNSET
        elif isinstance(self.snmp_community, SNMPCommunity):
            snmp_community = self.snmp_community.to_dict()
        elif isinstance(self.snmp_community, SNMPv3NoAuthNoPrivacy):
            snmp_community = self.snmp_community.to_dict()
        elif isinstance(self.snmp_community, SNMPv3AuthNoPrivacy):
            snmp_community = self.snmp_community.to_dict()
        else:
            snmp_community = self.snmp_community.to_dict()

        tag_piggyback = self.tag_piggyback

        tag_criticality = self.tag_criticality

        tag_networking = self.tag_networking

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        network_scan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_scan, Unset):
            network_scan = self.network_scan.to_dict()

        network_scan_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network_scan_result, Unset):
            network_scan_result = self.network_scan_result.to_dict()

        management_protocol: str | Unset = UNSET
        if not isinstance(self.management_protocol, Unset):
            management_protocol = self.management_protocol.value

        management_snmp_community: dict[str, Any] | None | Unset
        if isinstance(self.management_snmp_community, Unset):
            management_snmp_community = UNSET
        elif isinstance(self.management_snmp_community, SNMPCommunity):
            management_snmp_community = self.management_snmp_community.to_dict()
        elif isinstance(self.management_snmp_community, SNMPv3NoAuthNoPrivacy):
            management_snmp_community = self.management_snmp_community.to_dict()
        elif isinstance(self.management_snmp_community, SNMPv3AuthNoPrivacy):
            management_snmp_community = self.management_snmp_community.to_dict()
        elif isinstance(self.management_snmp_community, SNMPv3AuthPrivacy):
            management_snmp_community = self.management_snmp_community.to_dict()
        elif isinstance(
            self.management_snmp_community,
            FolderViewAttributeManagementSnmpCommunityType1Type0,
        ):
            management_snmp_community = self.management_snmp_community.to_dict()
        else:
            management_snmp_community = self.management_snmp_community

        management_ipmi_credentials: dict[str, Any] | None | Unset
        if isinstance(self.management_ipmi_credentials, Unset):
            management_ipmi_credentials = UNSET
        elif isinstance(self.management_ipmi_credentials, IPMIParameters):
            management_ipmi_credentials = self.management_ipmi_credentials.to_dict()
        elif isinstance(
            self.management_ipmi_credentials,
            FolderViewAttributeManagementIpmiCredentialsType1Type0,
        ):
            management_ipmi_credentials = self.management_ipmi_credentials.to_dict()
        else:
            management_ipmi_credentials = self.management_ipmi_credentials

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if contactgroups is not UNSET:
            field_dict["contactgroups"] = contactgroups
        if parents is not UNSET:
            field_dict["parents"] = parents
        if tag_address_family is not UNSET:
            field_dict["tag_address_family"] = tag_address_family
        if tag_agent is not UNSET:
            field_dict["tag_agent"] = tag_agent
        if tag_snmp_ds is not UNSET:
            field_dict["tag_snmp_ds"] = tag_snmp_ds
        if snmp_community is not UNSET:
            field_dict["snmp_community"] = snmp_community
        if tag_piggyback is not UNSET:
            field_dict["tag_piggyback"] = tag_piggyback
        if tag_criticality is not UNSET:
            field_dict["tag_criticality"] = tag_criticality
        if tag_networking is not UNSET:
            field_dict["tag_networking"] = tag_networking
        if labels is not UNSET:
            field_dict["labels"] = labels
        if network_scan is not UNSET:
            field_dict["network_scan"] = network_scan
        if network_scan_result is not UNSET:
            field_dict["network_scan_result"] = network_scan_result
        if management_protocol is not UNSET:
            field_dict["management_protocol"] = management_protocol
        if management_snmp_community is not UNSET:
            field_dict["management_snmp_community"] = management_snmp_community
        if management_ipmi_credentials is not UNSET:
            field_dict["management_ipmi_credentials"] = management_ipmi_credentials
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_view_attribute_labels import FolderViewAttributeLabels
        from ..models.folder_view_attribute_management_ipmi_credentials_type_1_type_0 import (
            FolderViewAttributeManagementIpmiCredentialsType1Type0,
        )
        from ..models.folder_view_attribute_management_snmp_community_type_1_type_0 import (
            FolderViewAttributeManagementSnmpCommunityType1Type0,
        )
        from ..models.host_contact_group import HostContactGroup
        from ..models.ipmi_parameters import IPMIParameters
        from ..models.meta_data import MetaData
        from ..models.network_scan import NetworkScan
        from ..models.network_scan_result import NetworkScanResult
        from ..models.snm_pv_3_auth_no_privacy import SNMPv3AuthNoPrivacy
        from ..models.snm_pv_3_auth_privacy import SNMPv3AuthPrivacy
        from ..models.snm_pv_3_no_auth_no_privacy import SNMPv3NoAuthNoPrivacy
        from ..models.snmp_community import SNMPCommunity

        d = dict(src_dict)
        site = d.pop("site", UNSET)

        _contactgroups = d.pop("contactgroups", UNSET)
        contactgroups: HostContactGroup | Unset
        if isinstance(_contactgroups, Unset):
            contactgroups = UNSET
        else:
            contactgroups = HostContactGroup.from_dict(_contactgroups)

        parents = cast(list[str], d.pop("parents", UNSET))

        tag_address_family = d.pop("tag_address_family", UNSET)

        tag_agent = d.pop("tag_agent", UNSET)

        tag_snmp_ds = d.pop("tag_snmp_ds", UNSET)

        def _parse_snmp_community(
            data: object,
        ) -> (
            SNMPCommunity
            | SNMPv3AuthNoPrivacy
            | SNMPv3AuthPrivacy
            | SNMPv3NoAuthNoPrivacy
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_0 = SNMPCommunity.from_dict(
                    data
                )

                return componentsschemas_snmp_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_1 = (
                    SNMPv3NoAuthNoPrivacy.from_dict(data)
                )

                return componentsschemas_snmp_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_2 = (
                    SNMPv3AuthNoPrivacy.from_dict(data)
                )

                return componentsschemas_snmp_credentials_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_snmp_credentials_type_3 = SNMPv3AuthPrivacy.from_dict(
                data
            )

            return componentsschemas_snmp_credentials_type_3

        snmp_community = _parse_snmp_community(d.pop("snmp_community", UNSET))

        tag_piggyback = d.pop("tag_piggyback", UNSET)

        tag_criticality = d.pop("tag_criticality", UNSET)

        tag_networking = d.pop("tag_networking", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: FolderViewAttributeLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = FolderViewAttributeLabels.from_dict(_labels)

        _network_scan = d.pop("network_scan", UNSET)
        network_scan: NetworkScan | Unset
        if isinstance(_network_scan, Unset):
            network_scan = UNSET
        else:
            network_scan = NetworkScan.from_dict(_network_scan)

        _network_scan_result = d.pop("network_scan_result", UNSET)
        network_scan_result: NetworkScanResult | Unset
        if isinstance(_network_scan_result, Unset):
            network_scan_result = UNSET
        else:
            network_scan_result = NetworkScanResult.from_dict(_network_scan_result)

        _management_protocol = d.pop("management_protocol", UNSET)
        management_protocol: FolderViewAttributeManagementProtocol | Unset
        if isinstance(_management_protocol, Unset):
            management_protocol = UNSET
        else:
            management_protocol = FolderViewAttributeManagementProtocol(
                _management_protocol
            )

        def _parse_management_snmp_community(
            data: object,
        ) -> (
            FolderViewAttributeManagementSnmpCommunityType1Type0
            | None
            | SNMPCommunity
            | SNMPv3AuthNoPrivacy
            | SNMPv3AuthPrivacy
            | SNMPv3NoAuthNoPrivacy
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_0 = SNMPCommunity.from_dict(
                    data
                )

                return componentsschemas_snmp_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_1 = (
                    SNMPv3NoAuthNoPrivacy.from_dict(data)
                )

                return componentsschemas_snmp_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_2 = (
                    SNMPv3AuthNoPrivacy.from_dict(data)
                )

                return componentsschemas_snmp_credentials_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_snmp_credentials_type_3 = SNMPv3AuthPrivacy.from_dict(
                    data
                )

                return componentsschemas_snmp_credentials_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                management_snmp_community_type_1_type_0 = (
                    FolderViewAttributeManagementSnmpCommunityType1Type0.from_dict(data)
                )

                return management_snmp_community_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FolderViewAttributeManagementSnmpCommunityType1Type0
                | None
                | SNMPCommunity
                | SNMPv3AuthNoPrivacy
                | SNMPv3AuthPrivacy
                | SNMPv3NoAuthNoPrivacy
                | Unset,
                data,
            )

        management_snmp_community = _parse_management_snmp_community(
            d.pop("management_snmp_community", UNSET)
        )

        def _parse_management_ipmi_credentials(
            data: object,
        ) -> (
            FolderViewAttributeManagementIpmiCredentialsType1Type0
            | IPMIParameters
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                management_ipmi_credentials_type_0 = IPMIParameters.from_dict(data)

                return management_ipmi_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                management_ipmi_credentials_type_1_type_0 = (
                    FolderViewAttributeManagementIpmiCredentialsType1Type0.from_dict(
                        data
                    )
                )

                return management_ipmi_credentials_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                FolderViewAttributeManagementIpmiCredentialsType1Type0
                | IPMIParameters
                | None
                | Unset,
                data,
            )

        management_ipmi_credentials = _parse_management_ipmi_credentials(
            d.pop("management_ipmi_credentials", UNSET)
        )

        _meta_data = d.pop("meta_data", UNSET)
        meta_data: MetaData | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = MetaData.from_dict(_meta_data)

        folder_view_attribute = cls(
            site=site,
            contactgroups=contactgroups,
            parents=parents,
            tag_address_family=tag_address_family,
            tag_agent=tag_agent,
            tag_snmp_ds=tag_snmp_ds,
            snmp_community=snmp_community,
            tag_piggyback=tag_piggyback,
            tag_criticality=tag_criticality,
            tag_networking=tag_networking,
            labels=labels,
            network_scan=network_scan,
            network_scan_result=network_scan_result,
            management_protocol=management_protocol,
            management_snmp_community=management_snmp_community,
            management_ipmi_credentials=management_ipmi_credentials,
            meta_data=meta_data,
        )

        folder_view_attribute.additional_properties = d
        return folder_view_attribute

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
