from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.background_job_exception import BackgroundJobException
    from ..models.errors import Errors
    from ..models.quick_setup_complete_response_all_stage_errors_item_type_1_type_0 import (
        QuickSetupCompleteResponseAllStageErrorsItemType1Type0,
    )


T = TypeVar("T", bound="QuickSetupCompleteResponse")


@_attrs_define
class QuickSetupCompleteResponse:
    """
    Attributes:
        redirect_url (str | Unset): The url to redirect to after saving the quicksetup Example: http://save/url.
        all_stage_errors (list[Errors | None | QuickSetupCompleteResponseAllStageErrorsItemType1Type0] | Unset): A list
            of stage errors
        background_job_exception (BackgroundJobException | Unset):
    """

    redirect_url: str | Unset = UNSET
    all_stage_errors: (
        list[Errors | None | QuickSetupCompleteResponseAllStageErrorsItemType1Type0]
        | Unset
    ) = UNSET
    background_job_exception: BackgroundJobException | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.errors import Errors
        from ..models.quick_setup_complete_response_all_stage_errors_item_type_1_type_0 import (
            QuickSetupCompleteResponseAllStageErrorsItemType1Type0,
        )

        redirect_url = self.redirect_url

        all_stage_errors: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.all_stage_errors, Unset):
            all_stage_errors = []
            for all_stage_errors_item_data in self.all_stage_errors:
                all_stage_errors_item: dict[str, Any] | None
                if isinstance(all_stage_errors_item_data, Errors):
                    all_stage_errors_item = all_stage_errors_item_data.to_dict()
                elif isinstance(
                    all_stage_errors_item_data,
                    QuickSetupCompleteResponseAllStageErrorsItemType1Type0,
                ):
                    all_stage_errors_item = all_stage_errors_item_data.to_dict()
                else:
                    all_stage_errors_item = all_stage_errors_item_data
                all_stage_errors.append(all_stage_errors_item)

        background_job_exception: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_job_exception, Unset):
            background_job_exception = self.background_job_exception.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redirect_url is not UNSET:
            field_dict["redirect_url"] = redirect_url
        if all_stage_errors is not UNSET:
            field_dict["all_stage_errors"] = all_stage_errors
        if background_job_exception is not UNSET:
            field_dict["background_job_exception"] = background_job_exception

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.background_job_exception import BackgroundJobException
        from ..models.errors import Errors
        from ..models.quick_setup_complete_response_all_stage_errors_item_type_1_type_0 import (
            QuickSetupCompleteResponseAllStageErrorsItemType1Type0,
        )

        d = dict(src_dict)
        redirect_url = d.pop("redirect_url", UNSET)

        _all_stage_errors = d.pop("all_stage_errors", UNSET)
        all_stage_errors: (
            list[Errors | None | QuickSetupCompleteResponseAllStageErrorsItemType1Type0]
            | Unset
        ) = UNSET
        if _all_stage_errors is not UNSET:
            all_stage_errors = []
            for all_stage_errors_item_data in _all_stage_errors:

                def _parse_all_stage_errors_item(
                    data: object,
                ) -> (
                    Errors
                    | None
                    | QuickSetupCompleteResponseAllStageErrorsItemType1Type0
                ):
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        all_stage_errors_item_type_0 = Errors.from_dict(data)

                        return all_stage_errors_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        all_stage_errors_item_type_1_type_0 = QuickSetupCompleteResponseAllStageErrorsItemType1Type0.from_dict(
                            data
                        )

                        return all_stage_errors_item_type_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(
                        Errors
                        | None
                        | QuickSetupCompleteResponseAllStageErrorsItemType1Type0,
                        data,
                    )

                all_stage_errors_item = _parse_all_stage_errors_item(
                    all_stage_errors_item_data
                )

                all_stage_errors.append(all_stage_errors_item)

        _background_job_exception = d.pop("background_job_exception", UNSET)
        background_job_exception: BackgroundJobException | Unset
        if isinstance(_background_job_exception, Unset):
            background_job_exception = UNSET
        else:
            background_job_exception = BackgroundJobException.from_dict(
                _background_job_exception
            )

        quick_setup_complete_response = cls(
            redirect_url=redirect_url,
            all_stage_errors=all_stage_errors,
            background_job_exception=background_job_exception,
        )

        quick_setup_complete_response.additional_properties = d
        return quick_setup_complete_response

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
