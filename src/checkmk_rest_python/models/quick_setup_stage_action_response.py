from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.background_job_exception import BackgroundJobException
    from ..models.errors import Errors
    from ..models.quick_setup_stage_action_response_stage_recap_item import (
        QuickSetupStageActionResponseStageRecapItem,
    )
    from ..models.quick_setup_stage_action_response_validation_errors_type_1_type_0 import (
        QuickSetupStageActionResponseValidationErrorsType1Type0,
    )


T = TypeVar("T", bound="QuickSetupStageActionResponse")


@_attrs_define
class QuickSetupStageActionResponse:
    """
    Attributes:
        stage_recap (list[QuickSetupStageActionResponseStageRecapItem] | Unset): A collection of widget recaps
        validation_errors (Errors | None | QuickSetupStageActionResponseValidationErrorsType1Type0 | Unset): All
            formspec errors and general stage errors
        background_job_exception (BackgroundJobException | Unset):
    """

    stage_recap: list[QuickSetupStageActionResponseStageRecapItem] | Unset = UNSET
    validation_errors: (
        Errors | None | QuickSetupStageActionResponseValidationErrorsType1Type0 | Unset
    ) = UNSET
    background_job_exception: BackgroundJobException | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.errors import Errors
        from ..models.quick_setup_stage_action_response_validation_errors_type_1_type_0 import (
            QuickSetupStageActionResponseValidationErrorsType1Type0,
        )

        stage_recap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stage_recap, Unset):
            stage_recap = []
            for stage_recap_item_data in self.stage_recap:
                stage_recap_item = stage_recap_item_data.to_dict()
                stage_recap.append(stage_recap_item)

        validation_errors: dict[str, Any] | None | Unset
        if isinstance(self.validation_errors, Unset):
            validation_errors = UNSET
        elif isinstance(self.validation_errors, Errors):
            validation_errors = self.validation_errors.to_dict()
        elif isinstance(
            self.validation_errors,
            QuickSetupStageActionResponseValidationErrorsType1Type0,
        ):
            validation_errors = self.validation_errors.to_dict()
        else:
            validation_errors = self.validation_errors

        background_job_exception: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_job_exception, Unset):
            background_job_exception = self.background_job_exception.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_recap is not UNSET:
            field_dict["stage_recap"] = stage_recap
        if validation_errors is not UNSET:
            field_dict["validation_errors"] = validation_errors
        if background_job_exception is not UNSET:
            field_dict["background_job_exception"] = background_job_exception

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.background_job_exception import BackgroundJobException
        from ..models.errors import Errors
        from ..models.quick_setup_stage_action_response_stage_recap_item import (
            QuickSetupStageActionResponseStageRecapItem,
        )
        from ..models.quick_setup_stage_action_response_validation_errors_type_1_type_0 import (
            QuickSetupStageActionResponseValidationErrorsType1Type0,
        )

        d = dict(src_dict)
        _stage_recap = d.pop("stage_recap", UNSET)
        stage_recap: list[QuickSetupStageActionResponseStageRecapItem] | Unset = UNSET
        if _stage_recap is not UNSET:
            stage_recap = []
            for stage_recap_item_data in _stage_recap:
                stage_recap_item = (
                    QuickSetupStageActionResponseStageRecapItem.from_dict(
                        stage_recap_item_data
                    )
                )

                stage_recap.append(stage_recap_item)

        def _parse_validation_errors(
            data: object,
        ) -> (
            Errors
            | None
            | QuickSetupStageActionResponseValidationErrorsType1Type0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                validation_errors_type_0 = Errors.from_dict(data)

                return validation_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                validation_errors_type_1_type_0 = (
                    QuickSetupStageActionResponseValidationErrorsType1Type0.from_dict(
                        data
                    )
                )

                return validation_errors_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                Errors
                | None
                | QuickSetupStageActionResponseValidationErrorsType1Type0
                | Unset,
                data,
            )

        validation_errors = _parse_validation_errors(d.pop("validation_errors", UNSET))

        _background_job_exception = d.pop("background_job_exception", UNSET)
        background_job_exception: BackgroundJobException | Unset
        if isinstance(_background_job_exception, Unset):
            background_job_exception = UNSET
        else:
            background_job_exception = BackgroundJobException.from_dict(
                _background_job_exception
            )

        quick_setup_stage_action_response = cls(
            stage_recap=stage_recap,
            validation_errors=validation_errors,
            background_job_exception=background_job_exception,
        )

        quick_setup_stage_action_response.additional_properties = d
        return quick_setup_stage_action_response

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
