from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mgmnt_type_incident_params_option import MgmntTypeIncidentParamsOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_params import IncidentParams


T = TypeVar("T", bound="MgmntTypeIncidentParams")


@_attrs_define
class MgmntTypeIncidentParams:
    """
    Attributes:
        option (MgmntTypeIncidentParamsOption):  Example: case.
        params (IncidentParams | Unset):
    """

    option: MgmntTypeIncidentParamsOption
    params: IncidentParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_params import IncidentParams

        d = dict(src_dict)
        option = MgmntTypeIncidentParamsOption(d.pop("option"))

        _params = d.pop("params", UNSET)
        params: IncidentParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = IncidentParams.from_dict(_params)

        mgmnt_type_incident_params = cls(
            option=option,
            params=params,
        )

        mgmnt_type_incident_params.additional_properties = d
        return mgmnt_type_incident_params

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
