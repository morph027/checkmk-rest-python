from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_formspec_errors import ErrorsFormspecErrors


T = TypeVar("T", bound="Errors")


@_attrs_define
class Errors:
    """
    Attributes:
        stage_index (int | None | Unset): Index of the stage containing errors.
        formspec_errors (ErrorsFormspecErrors | Unset): A mapping of formspec ids to formspec validation errors
        stage_errors (list[str] | Unset): A collection of general stage errors
    """

    stage_index: int | None | Unset = UNSET
    formspec_errors: ErrorsFormspecErrors | Unset = UNSET
    stage_errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_index: int | None | Unset
        if isinstance(self.stage_index, Unset):
            stage_index = UNSET
        else:
            stage_index = self.stage_index

        formspec_errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.formspec_errors, Unset):
            formspec_errors = self.formspec_errors.to_dict()

        stage_errors: list[str] | Unset = UNSET
        if not isinstance(self.stage_errors, Unset):
            stage_errors = self.stage_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_index is not UNSET:
            field_dict["stage_index"] = stage_index
        if formspec_errors is not UNSET:
            field_dict["formspec_errors"] = formspec_errors
        if stage_errors is not UNSET:
            field_dict["stage_errors"] = stage_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.errors_formspec_errors import ErrorsFormspecErrors

        d = dict(src_dict)

        def _parse_stage_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stage_index = _parse_stage_index(d.pop("stage_index", UNSET))

        _formspec_errors = d.pop("formspec_errors", UNSET)
        formspec_errors: ErrorsFormspecErrors | Unset
        if isinstance(_formspec_errors, Unset):
            formspec_errors = UNSET
        else:
            formspec_errors = ErrorsFormspecErrors.from_dict(_formspec_errors)

        stage_errors = cast(list[str], d.pop("stage_errors", UNSET))

        errors = cls(
            stage_index=stage_index,
            formspec_errors=formspec_errors,
            stage_errors=stage_errors,
        )

        errors.additional_properties = d
        return errors

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
