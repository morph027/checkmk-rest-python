from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_extension import AuditLogExtension


T = TypeVar("T", bound="AuditLogEntry")


@_attrs_define
class AuditLogEntry:
    """
    Attributes:
        title (str | Unset): A human readable title of this object. Can be used for user interfaces.
        extensions (AuditLogExtension | Unset):
    """

    title: str | Unset = UNSET
    extensions: AuditLogExtension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log_extension import AuditLogExtension

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: AuditLogExtension | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = AuditLogExtension.from_dict(_extensions)

        audit_log_entry = cls(
            title=title,
            extensions=extensions,
        )

        audit_log_entry.additional_properties = d
        return audit_log_entry

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
