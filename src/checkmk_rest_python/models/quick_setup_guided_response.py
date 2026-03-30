from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.quick_setup_button import QuickSetupButton
    from ..models.quick_setup_guided_response_prev_button_type_1_type_0 import (
        QuickSetupGuidedResponsePrevButtonType1Type0,
    )
    from ..models.quick_setup_stage_overview_response import (
        QuickSetupStageOverviewResponse,
    )
    from ..models.quick_setup_stage_structure import QuickSetupStageStructure


T = TypeVar("T", bound="QuickSetupGuidedResponse")


@_attrs_define
class QuickSetupGuidedResponse:
    """
    Attributes:
        quick_setup_id (str | Unset): The quicksetup id Example: aws_quicksetup.
        actions (list[Action] | Unset): A list of all complete actions Example: [{'id': 'save', 'label': 'Save
            configuration'}].
        prev_button (None | QuickSetupButton | QuickSetupGuidedResponsePrevButtonType1Type0 | Unset): Definition of the
            `go to previous stage` button Example: {'id': 'prev', 'label': 'Back', 'aria_label': 'Back'}.
        guided_mode_string (str | Unset): The string for the guided mode label Example: Guided mode.
        overview_mode_string (str | Unset): The string for the overview mode label Example: Overview mode.
        overviews (list[QuickSetupStageOverviewResponse] | Unset): The overview of the quicksetup stages
        stage (QuickSetupStageStructure | Unset):
    """

    quick_setup_id: str | Unset = UNSET
    actions: list[Action] | Unset = UNSET
    prev_button: (
        None | QuickSetupButton | QuickSetupGuidedResponsePrevButtonType1Type0 | Unset
    ) = UNSET
    guided_mode_string: str | Unset = UNSET
    overview_mode_string: str | Unset = UNSET
    overviews: list[QuickSetupStageOverviewResponse] | Unset = UNSET
    stage: QuickSetupStageStructure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_setup_button import QuickSetupButton
        from ..models.quick_setup_guided_response_prev_button_type_1_type_0 import (
            QuickSetupGuidedResponsePrevButtonType1Type0,
        )

        quick_setup_id = self.quick_setup_id

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        prev_button: dict[str, Any] | None | Unset
        if isinstance(self.prev_button, Unset):
            prev_button = UNSET
        elif isinstance(self.prev_button, QuickSetupButton):
            prev_button = self.prev_button.to_dict()
        elif isinstance(self.prev_button, QuickSetupGuidedResponsePrevButtonType1Type0):
            prev_button = self.prev_button.to_dict()
        else:
            prev_button = self.prev_button

        guided_mode_string = self.guided_mode_string

        overview_mode_string = self.overview_mode_string

        overviews: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overviews, Unset):
            overviews = []
            for overviews_item_data in self.overviews:
                overviews_item = overviews_item_data.to_dict()
                overviews.append(overviews_item)

        stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quick_setup_id is not UNSET:
            field_dict["quick_setup_id"] = quick_setup_id
        if actions is not UNSET:
            field_dict["actions"] = actions
        if prev_button is not UNSET:
            field_dict["prev_button"] = prev_button
        if guided_mode_string is not UNSET:
            field_dict["guided_mode_string"] = guided_mode_string
        if overview_mode_string is not UNSET:
            field_dict["overview_mode_string"] = overview_mode_string
        if overviews is not UNSET:
            field_dict["overviews"] = overviews
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action
        from ..models.quick_setup_button import QuickSetupButton
        from ..models.quick_setup_guided_response_prev_button_type_1_type_0 import (
            QuickSetupGuidedResponsePrevButtonType1Type0,
        )
        from ..models.quick_setup_stage_overview_response import (
            QuickSetupStageOverviewResponse,
        )
        from ..models.quick_setup_stage_structure import QuickSetupStageStructure

        d = dict(src_dict)
        quick_setup_id = d.pop("quick_setup_id", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[Action] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = Action.from_dict(actions_item_data)

                actions.append(actions_item)

        def _parse_prev_button(
            data: object,
        ) -> (
            None
            | QuickSetupButton
            | QuickSetupGuidedResponsePrevButtonType1Type0
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prev_button_type_0 = QuickSetupButton.from_dict(data)

                return prev_button_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prev_button_type_1_type_0 = (
                    QuickSetupGuidedResponsePrevButtonType1Type0.from_dict(data)
                )

                return prev_button_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | QuickSetupButton
                | QuickSetupGuidedResponsePrevButtonType1Type0
                | Unset,
                data,
            )

        prev_button = _parse_prev_button(d.pop("prev_button", UNSET))

        guided_mode_string = d.pop("guided_mode_string", UNSET)

        overview_mode_string = d.pop("overview_mode_string", UNSET)

        _overviews = d.pop("overviews", UNSET)
        overviews: list[QuickSetupStageOverviewResponse] | Unset = UNSET
        if _overviews is not UNSET:
            overviews = []
            for overviews_item_data in _overviews:
                overviews_item = QuickSetupStageOverviewResponse.from_dict(
                    overviews_item_data
                )

                overviews.append(overviews_item)

        _stage = d.pop("stage", UNSET)
        stage: QuickSetupStageStructure | Unset
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = QuickSetupStageStructure.from_dict(_stage)

        quick_setup_guided_response = cls(
            quick_setup_id=quick_setup_id,
            actions=actions,
            prev_button=prev_button,
            guided_mode_string=guided_mode_string,
            overview_mode_string=overview_mode_string,
            overviews=overviews,
            stage=stage,
        )

        quick_setup_guided_response.additional_properties = d
        return quick_setup_guided_response

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
