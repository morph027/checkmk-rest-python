from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_management_type_state_case_values import (
        CheckboxWithManagementTypeStateCaseValues,
    )
    from ..models.checkbox_with_mgmt_type_priority_value import (
        CheckboxWithMgmtTypePriorityValue,
    )
    from ..models.checkbox_with_str_value import CheckboxWithStrValue


T = TypeVar("T", bound="CaseParams")


@_attrs_define
class CaseParams:
    """
    Attributes:
        host_description (Checkbox | CheckboxWithStrValue | Unset):
        service_description (Checkbox | CheckboxWithStrValue | Unset):
        host_short_description (Checkbox | CheckboxWithStrValue | Unset):
        service_short_description (Checkbox | CheckboxWithStrValue | Unset):
        priority (Checkbox | CheckboxWithMgmtTypePriorityValue | Unset):
        state_recovery (Checkbox | CheckboxWithManagementTypeStateCaseValues | Unset):
    """

    host_description: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_description: Checkbox | CheckboxWithStrValue | Unset = UNSET
    host_short_description: Checkbox | CheckboxWithStrValue | Unset = UNSET
    service_short_description: Checkbox | CheckboxWithStrValue | Unset = UNSET
    priority: Checkbox | CheckboxWithMgmtTypePriorityValue | Unset = UNSET
    state_recovery: Checkbox | CheckboxWithManagementTypeStateCaseValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        host_description: dict[str, Any] | Unset
        if isinstance(self.host_description, Unset):
            host_description = UNSET
        elif isinstance(self.host_description, Checkbox):
            host_description = self.host_description.to_dict()
        else:
            host_description = self.host_description.to_dict()

        service_description: dict[str, Any] | Unset
        if isinstance(self.service_description, Unset):
            service_description = UNSET
        elif isinstance(self.service_description, Checkbox):
            service_description = self.service_description.to_dict()
        else:
            service_description = self.service_description.to_dict()

        host_short_description: dict[str, Any] | Unset
        if isinstance(self.host_short_description, Unset):
            host_short_description = UNSET
        elif isinstance(self.host_short_description, Checkbox):
            host_short_description = self.host_short_description.to_dict()
        else:
            host_short_description = self.host_short_description.to_dict()

        service_short_description: dict[str, Any] | Unset
        if isinstance(self.service_short_description, Unset):
            service_short_description = UNSET
        elif isinstance(self.service_short_description, Checkbox):
            service_short_description = self.service_short_description.to_dict()
        else:
            service_short_description = self.service_short_description.to_dict()

        priority: dict[str, Any] | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, Checkbox):
            priority = self.priority.to_dict()
        else:
            priority = self.priority.to_dict()

        state_recovery: dict[str, Any] | Unset
        if isinstance(self.state_recovery, Unset):
            state_recovery = UNSET
        elif isinstance(self.state_recovery, Checkbox):
            state_recovery = self.state_recovery.to_dict()
        else:
            state_recovery = self.state_recovery.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_description is not UNSET:
            field_dict["host_description"] = host_description
        if service_description is not UNSET:
            field_dict["service_description"] = service_description
        if host_short_description is not UNSET:
            field_dict["host_short_description"] = host_short_description
        if service_short_description is not UNSET:
            field_dict["service_short_description"] = service_short_description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if state_recovery is not UNSET:
            field_dict["state_recovery"] = state_recovery

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_management_type_state_case_values import (
            CheckboxWithManagementTypeStateCaseValues,
        )
        from ..models.checkbox_with_mgmt_type_priority_value import (
            CheckboxWithMgmtTypePriorityValue,
        )
        from ..models.checkbox_with_str_value import CheckboxWithStrValue

        d = dict(src_dict)

        def _parse_host_description(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        host_description = _parse_host_description(d.pop("host_description", UNSET))

        def _parse_service_description(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        service_description = _parse_service_description(
            d.pop("service_description", UNSET)
        )

        def _parse_host_short_description(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        host_short_description = _parse_host_short_description(
            d.pop("host_short_description", UNSET)
        )

        def _parse_service_short_description(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        service_short_description = _parse_service_short_description(
            d.pop("service_short_description", UNSET)
        )

        def _parse_priority(
            data: object,
        ) -> Checkbox | CheckboxWithMgmtTypePriorityValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_priority_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_priority_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_priority_one_of_type_1 = (
                CheckboxWithMgmtTypePriorityValue.from_dict(data)
            )

            return componentsschemas_priority_one_of_type_1

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_state_recovery(
            data: object,
        ) -> Checkbox | CheckboxWithManagementTypeStateCaseValues | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_state_recovery_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_state_recovery_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_state_recovery_one_of_type_1 = (
                CheckboxWithManagementTypeStateCaseValues.from_dict(data)
            )

            return componentsschemas_state_recovery_one_of_type_1

        state_recovery = _parse_state_recovery(d.pop("state_recovery", UNSET))

        case_params = cls(
            host_description=host_description,
            service_description=service_description,
            host_short_description=host_short_description,
            service_short_description=service_short_description,
            priority=priority,
            state_recovery=state_recovery,
        )

        case_params.additional_properties = d
        return case_params

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
