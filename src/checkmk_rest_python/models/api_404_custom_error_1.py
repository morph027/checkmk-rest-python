from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_404_custom_error_1_ext import Api404CustomError1Ext
    from ..models.api_404_custom_error_1_fields import Api404CustomError1Fields


T = TypeVar("T", bound="Api404CustomError1")


@_attrs_define
class Api404CustomError1:
    """
    Attributes:
        status (int | Unset): The HTTP status code. Example: 404.
        detail (str | Unset): Detailed information on what exactly went wrong. Example: There is no running activation
            with this activation_id..
        title (str | Unset): A summary of the problem. Example: Not Found.
        fields (Api404CustomError1Fields | Unset): Detailed error messages on all fields failing validation.
        ext (Api404CustomError1Ext | Unset): Additional information about the error.
    """

    status: int | Unset = UNSET
    detail: str | Unset = UNSET
    title: str | Unset = UNSET
    fields: Api404CustomError1Fields | Unset = UNSET
    ext: Api404CustomError1Ext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        detail = self.detail

        title = self.title

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        ext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ext, Unset):
            ext = self.ext.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if title is not UNSET:
            field_dict["title"] = title
        if fields is not UNSET:
            field_dict["fields"] = fields
        if ext is not UNSET:
            field_dict["ext"] = ext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_404_custom_error_1_ext import Api404CustomError1Ext
        from ..models.api_404_custom_error_1_fields import Api404CustomError1Fields

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        title = d.pop("title", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: Api404CustomError1Fields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = Api404CustomError1Fields.from_dict(_fields)

        _ext = d.pop("ext", UNSET)
        ext: Api404CustomError1Ext | Unset
        if isinstance(_ext, Unset):
            ext = UNSET
        else:
            ext = Api404CustomError1Ext.from_dict(_ext)

        api_404_custom_error_1 = cls(
            status=status,
            detail=detail,
            title=title,
            fields=fields,
            ext=ext,
        )

        api_404_custom_error_1.additional_properties = d
        return api_404_custom_error_1

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
