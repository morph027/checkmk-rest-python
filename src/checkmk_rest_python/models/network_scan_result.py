from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.network_scan_result_state import NetworkScanResultState
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkScanResult")


@_attrs_define
class NetworkScanResult:
    """
    Attributes:
        start (datetime.datetime | None | Unset): When the scan started
        end (datetime.datetime | None | Unset): When the scan finished. Will be Null if not yet run.
        state (NetworkScanResultState | Unset): Last scan result
        output (str | Unset): Short human readable description of what is happening.
    """

    start: datetime.datetime | None | Unset = UNSET
    end: datetime.datetime | None | Unset = UNSET
    state: NetworkScanResultState | Unset = UNSET
    output: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start: None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        elif isinstance(self.start, datetime.datetime):
            start = self.start.isoformat()
        else:
            start = self.start

        end: None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, datetime.datetime):
            end = self.end.isoformat()
        else:
            end = self.end

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        output = self.output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if state is not UNSET:
            field_dict["state"] = state
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_0 = isoparse(data)

                return start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start = _parse_start(d.pop("start", UNSET))

        def _parse_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = isoparse(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))

        _state = d.pop("state", UNSET)
        state: NetworkScanResultState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = NetworkScanResultState(_state)

        output = d.pop("output", UNSET)

        network_scan_result = cls(
            start=start,
            end=end,
            state=state,
            output=output,
        )

        network_scan_result.additional_properties = d
        return network_scan_result

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
