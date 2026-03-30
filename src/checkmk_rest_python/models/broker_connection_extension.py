from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_site_attributes import ConnectedSiteAttributes


T = TypeVar("T", bound="BrokerConnectionExtension")


@_attrs_define
class BrokerConnectionExtension:
    """
    Attributes:
        id (str | Unset): The unique identifier of the connection.
        connecter (ConnectedSiteAttributes | Unset):
        connectee (ConnectedSiteAttributes | Unset):
    """

    id: str | Unset = UNSET
    connecter: ConnectedSiteAttributes | Unset = UNSET
    connectee: ConnectedSiteAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        connecter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connecter, Unset):
            connecter = self.connecter.to_dict()

        connectee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connectee, Unset):
            connectee = self.connectee.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if connecter is not UNSET:
            field_dict["connecter"] = connecter
        if connectee is not UNSET:
            field_dict["connectee"] = connectee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_site_attributes import ConnectedSiteAttributes

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _connecter = d.pop("connecter", UNSET)
        connecter: ConnectedSiteAttributes | Unset
        if isinstance(_connecter, Unset):
            connecter = UNSET
        else:
            connecter = ConnectedSiteAttributes.from_dict(_connecter)

        _connectee = d.pop("connectee", UNSET)
        connectee: ConnectedSiteAttributes | Unset
        if isinstance(_connectee, Unset):
            connectee = UNSET
        else:
            connectee = ConnectedSiteAttributes.from_dict(_connectee)

        broker_connection_extension = cls(
            id=id,
            connecter=connecter,
            connectee=connectee,
        )

        broker_connection_extension.additional_properties = d
        return broker_connection_extension

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
