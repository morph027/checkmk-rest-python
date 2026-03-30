from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="X509ReqPEMUUID")


@_attrs_define
class X509ReqPEMUUID:
    """
    Attributes:
        csr (str): PEM-encoded X.509 CSR. The CN must a valid version-4 UUID. Example: -----BEGIN CERTIFICATE
            REQUEST-----
            ...
            -----END CERTIFICATE REQUEST-----
            .
    """

    csr: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csr = self.csr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "csr": csr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csr = d.pop("csr")

        x509_req_pemuuid = cls(
            csr=csr,
        )

        x509_req_pemuuid.additional_properties = d
        return x509_req_pemuuid

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
