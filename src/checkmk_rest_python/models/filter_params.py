from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_params_phase import FilterParamsPhase
from ..models.filter_params_state import FilterParamsState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterParams")


@_attrs_define
class FilterParams:
    """
    Attributes:
        state (FilterParamsState | Unset): The state Example: ok.
        host (str | Unset): The host name. No exception is raised when the specified host name does not exist Example:
            host_1.
        phase (FilterParamsPhase | Unset): The event phase, open or ack Example: open.
        application (str | Unset): Show events that originated from this app. Example: app_1.
    """

    state: FilterParamsState | Unset = UNSET
    host: str | Unset = UNSET
    phase: FilterParamsPhase | Unset = UNSET
    application: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        host = self.host

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        application = self.application

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if host is not UNSET:
            field_dict["host"] = host
        if phase is not UNSET:
            field_dict["phase"] = phase
        if application is not UNSET:
            field_dict["application"] = application

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: FilterParamsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = FilterParamsState(_state)

        host = d.pop("host", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: FilterParamsPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = FilterParamsPhase(_phase)

        application = d.pop("application", UNSET)

        filter_params = cls(
            state=state,
            host=host,
            phase=phase,
            application=application,
        )

        filter_params.additional_properties = d
        return filter_params

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
