from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_params import BIParams


T = TypeVar("T", bound="BICallARuleAction")


@_attrs_define
class BICallARuleAction:
    """
    Attributes:
        type_ (Any): Call a BI rule to create nodes. Default: 'call_a_rule'.
        rule_id (str): ID of the rule. Example: test_rule_1.
        params (BIParams):
    """

    rule_id: str
    params: BIParams
    type_: Any = "call_a_rule"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        rule_id = self.rule_id

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "rule_id": rule_id,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_params import BIParams

        d = dict(src_dict)
        type_ = d.pop("type")

        rule_id = d.pop("rule_id")

        params = BIParams.from_dict(d.pop("params"))

        bi_call_a_rule_action = cls(
            type_=type_,
            rule_id=rule_id,
            params=params,
        )

        bi_call_a_rule_action.additional_properties = d
        return bi_call_a_rule_action

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
