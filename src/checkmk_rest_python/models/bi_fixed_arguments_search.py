from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_fixed_arguments_search_token import BIFixedArgumentsSearchToken


T = TypeVar("T", bound="BIFixedArgumentsSearch")


@_attrs_define
class BIFixedArgumentsSearch:
    """
    Attributes:
        type_ (Any): Fixed search arguments. Default: 'fixed_arguments'.
        arguments (list[BIFixedArgumentsSearchToken]): Search arguments.
    """

    arguments: list[BIFixedArgumentsSearchToken]
    type_: Any = "fixed_arguments"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        arguments = []
        for arguments_item_data in self.arguments:
            arguments_item = arguments_item_data.to_dict()
            arguments.append(arguments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_fixed_arguments_search_token import BIFixedArgumentsSearchToken

        d = dict(src_dict)
        type_ = d.pop("type")

        arguments = []
        _arguments = d.pop("arguments")
        for arguments_item_data in _arguments:
            arguments_item = BIFixedArgumentsSearchToken.from_dict(arguments_item_data)

            arguments.append(arguments_item)

        bi_fixed_arguments_search = cls(
            type_=type_,
            arguments=arguments,
        )

        bi_fixed_arguments_search.additional_properties = d
        return bi_fixed_arguments_search

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
