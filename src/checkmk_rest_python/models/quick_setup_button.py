from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_setup_button_icon import QuickSetupButtonIcon
    from ..models.quick_setup_button_icon_type_1_type_0 import (
        QuickSetupButtonIconType1Type0,
    )


T = TypeVar("T", bound="QuickSetupButton")


@_attrs_define
class QuickSetupButton:
    """
    Attributes:
        id (None | str | Unset): The button id Example: next.
        label (str | Unset): The label of the button Example: Next.
        icon (None | QuickSetupButtonIcon | QuickSetupButtonIconType1Type0 | Unset): Definition of the button icon
            Example: {'name': 'save-to-service', 'rotate': 0}.
        aria_label (None | str | Unset): The aria label of the button Example: Next.
    """

    id: None | str | Unset = UNSET
    label: str | Unset = UNSET
    icon: None | QuickSetupButtonIcon | QuickSetupButtonIconType1Type0 | Unset = UNSET
    aria_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_setup_button_icon import QuickSetupButtonIcon
        from ..models.quick_setup_button_icon_type_1_type_0 import (
            QuickSetupButtonIconType1Type0,
        )

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        label = self.label

        icon: dict[str, Any] | None | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        elif isinstance(self.icon, QuickSetupButtonIcon):
            icon = self.icon.to_dict()
        elif isinstance(self.icon, QuickSetupButtonIconType1Type0):
            icon = self.icon.to_dict()
        else:
            icon = self.icon

        aria_label: None | str | Unset
        if isinstance(self.aria_label, Unset):
            aria_label = UNSET
        else:
            aria_label = self.aria_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if icon is not UNSET:
            field_dict["icon"] = icon
        if aria_label is not UNSET:
            field_dict["aria_label"] = aria_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_setup_button_icon import QuickSetupButtonIcon
        from ..models.quick_setup_button_icon_type_1_type_0 import (
            QuickSetupButtonIconType1Type0,
        )

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        label = d.pop("label", UNSET)

        def _parse_icon(
            data: object,
        ) -> None | QuickSetupButtonIcon | QuickSetupButtonIconType1Type0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icon_type_0 = QuickSetupButtonIcon.from_dict(data)

                return icon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                icon_type_1_type_0 = QuickSetupButtonIconType1Type0.from_dict(data)

                return icon_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | QuickSetupButtonIcon | QuickSetupButtonIconType1Type0 | Unset,
                data,
            )

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_aria_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aria_label = _parse_aria_label(d.pop("aria_label", UNSET))

        quick_setup_button = cls(
            id=id,
            label=label,
            icon=icon,
            aria_label=aria_label,
        )

        quick_setup_button.additional_properties = d
        return quick_setup_button

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
