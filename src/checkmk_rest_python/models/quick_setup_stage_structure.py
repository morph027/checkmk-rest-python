from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action
    from ..models.quick_setup_button import QuickSetupButton
    from ..models.quick_setup_stage_structure_components_item import (
        QuickSetupStageStructureComponentsItem,
    )
    from ..models.quick_setup_stage_structure_prev_button_type_1_type_0 import (
        QuickSetupStageStructurePrevButtonType1Type0,
    )


T = TypeVar("T", bound="QuickSetupStageStructure")


@_attrs_define
class QuickSetupStageStructure:
    """
    Attributes:
        components (list[QuickSetupStageStructureComponentsItem] | Unset): A collection of stage components
        actions (list[Action] | Unset): A collection of stage actions
        prev_button (None | QuickSetupButton | QuickSetupStageStructurePrevButtonType1Type0 | Unset): Definition of the
            `go to previous stage` button Example: {'id': 'prev', 'label': 'Back'}.
    """

    components: list[QuickSetupStageStructureComponentsItem] | Unset = UNSET
    actions: list[Action] | Unset = UNSET
    prev_button: (
        None | QuickSetupButton | QuickSetupStageStructurePrevButtonType1Type0 | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.quick_setup_button import QuickSetupButton
        from ..models.quick_setup_stage_structure_prev_button_type_1_type_0 import (
            QuickSetupStageStructurePrevButtonType1Type0,
        )

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

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
        elif isinstance(self.prev_button, QuickSetupStageStructurePrevButtonType1Type0):
            prev_button = self.prev_button.to_dict()
        else:
            prev_button = self.prev_button

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if actions is not UNSET:
            field_dict["actions"] = actions
        if prev_button is not UNSET:
            field_dict["prev_button"] = prev_button

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action import Action
        from ..models.quick_setup_button import QuickSetupButton
        from ..models.quick_setup_stage_structure_components_item import (
            QuickSetupStageStructureComponentsItem,
        )
        from ..models.quick_setup_stage_structure_prev_button_type_1_type_0 import (
            QuickSetupStageStructurePrevButtonType1Type0,
        )

        d = dict(src_dict)
        _components = d.pop("components", UNSET)
        components: list[QuickSetupStageStructureComponentsItem] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = QuickSetupStageStructureComponentsItem.from_dict(
                    components_item_data
                )

                components.append(components_item)

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
            | QuickSetupStageStructurePrevButtonType1Type0
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
                    QuickSetupStageStructurePrevButtonType1Type0.from_dict(data)
                )

                return prev_button_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | QuickSetupButton
                | QuickSetupStageStructurePrevButtonType1Type0
                | Unset,
                data,
            )

        prev_button = _parse_prev_button(d.pop("prev_button", UNSET))

        quick_setup_stage_structure = cls(
            components=components,
            actions=actions,
            prev_button=prev_button,
        )

        quick_setup_stage_structure.additional_properties = d
        return quick_setup_stage_structure

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
