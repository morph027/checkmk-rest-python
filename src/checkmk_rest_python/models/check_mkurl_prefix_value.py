from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_mkurl_prefix_value_state import CheckMKURLPrefixValueState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_mkurl_prefix_auto import CheckMKURLPrefixAuto
    from ..models.check_mkurl_prefix_manual import CheckMKURLPrefixManual


T = TypeVar("T", bound="CheckMKURLPrefixValue")


@_attrs_define
class CheckMKURLPrefixValue:
    """
    Attributes:
        state (CheckMKURLPrefixValueState | Unset): To enable or disable this field Example: enabled.
        value (CheckMKURLPrefixAuto | CheckMKURLPrefixManual | Unset):
    """

    state: CheckMKURLPrefixValueState | Unset = UNSET
    value: CheckMKURLPrefixAuto | CheckMKURLPrefixManual | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.check_mkurl_prefix_auto import CheckMKURLPrefixAuto

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        value: dict[str, Any] | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, CheckMKURLPrefixAuto):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_mkurl_prefix_auto import CheckMKURLPrefixAuto
        from ..models.check_mkurl_prefix_manual import CheckMKURLPrefixManual

        d = dict(src_dict)
        _state = d.pop("state", UNSET)
        state: CheckMKURLPrefixValueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CheckMKURLPrefixValueState(_state)

        def _parse_value(
            data: object,
        ) -> CheckMKURLPrefixAuto | CheckMKURLPrefixManual | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_manual_or_automatic_selector_type_0 = (
                    CheckMKURLPrefixAuto.from_dict(data)
                )

                return componentsschemas_manual_or_automatic_selector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_manual_or_automatic_selector_type_1 = (
                CheckMKURLPrefixManual.from_dict(data)
            )

            return componentsschemas_manual_or_automatic_selector_type_1

        value = _parse_value(d.pop("value", UNSET))

        check_mkurl_prefix_value = cls(
            state=state,
            value=value,
        )

        check_mkurl_prefix_value.additional_properties = d
        return check_mkurl_prefix_value

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
