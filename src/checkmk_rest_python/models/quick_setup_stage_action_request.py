from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quick_setup_stage_request import QuickSetupStageRequest


T = TypeVar("T", bound="QuickSetupStageActionRequest")


@_attrs_define
class QuickSetupStageActionRequest:
    """
    Attributes:
        stage_action_id (str): The id of the stage action to be performed Example: test_connection.
        stages (list[QuickSetupStageRequest] | Unset): A list of stages Example: [{'form_data': {}}, {'form_data': {}}].
    """

    stage_action_id: str
    stages: list[QuickSetupStageRequest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_action_id = self.stage_action_id

        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_action_id": stage_action_id,
            }
        )
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_setup_stage_request import QuickSetupStageRequest

        d = dict(src_dict)
        stage_action_id = d.pop("stage_action_id")

        _stages = d.pop("stages", UNSET)
        stages: list[QuickSetupStageRequest] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = QuickSetupStageRequest.from_dict(stages_item_data)

                stages.append(stages_item)

        quick_setup_stage_action_request = cls(
            stage_action_id=stage_action_id,
            stages=stages,
        )

        quick_setup_stage_action_request.additional_properties = d
        return quick_setup_stage_action_request

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
