from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_dismiss_warning_warning import UserDismissWarningWarning

T = TypeVar("T", bound="UserDismissWarning")


@_attrs_define
class UserDismissWarning:
    """
    Attributes:
        warning (UserDismissWarningWarning): The warning to be dismissed. Example: notification_fallback.
    """

    warning: UserDismissWarningWarning
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warning = self.warning.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warning": warning,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warning = UserDismissWarningWarning(d.pop("warning"))

        user_dismiss_warning = cls(
            warning=warning,
        )

        user_dismiss_warning.additional_properties = d
        return user_dismiss_warning

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
