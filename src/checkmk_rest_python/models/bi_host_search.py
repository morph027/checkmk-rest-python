from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.child import Child
    from ..models.child_with import ChildWith
    from ..models.host import Host
    from ..models.host_conditions import HostConditions
    from ..models.parent import Parent


T = TypeVar("T", bound="BIHostSearch")


@_attrs_define
class BIHostSearch:
    """
    Attributes:
        type_ (Any): Host search. Default: 'host_search'.
        conditions (HostConditions):
        refer_to (Child | ChildWith | Host | Parent):
    """

    conditions: HostConditions
    refer_to: Child | ChildWith | Host | Parent
    type_: Any = "host_search"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.child import Child
        from ..models.host import Host
        from ..models.parent import Parent

        type_ = self.type_

        conditions = self.conditions.to_dict()

        refer_to: dict[str, Any]
        if isinstance(self.refer_to, Host):
            refer_to = self.refer_to.to_dict()
        elif isinstance(self.refer_to, Parent):
            refer_to = self.refer_to.to_dict()
        elif isinstance(self.refer_to, Child):
            refer_to = self.refer_to.to_dict()
        else:
            refer_to = self.refer_to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "conditions": conditions,
                "refer_to": refer_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.child import Child
        from ..models.child_with import ChildWith
        from ..models.host import Host
        from ..models.host_conditions import HostConditions
        from ..models.parent import Parent

        d = dict(src_dict)
        type_ = d.pop("type")

        conditions = HostConditions.from_dict(d.pop("conditions"))

        def _parse_refer_to(data: object) -> Child | ChildWith | Host | Parent:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_refer_to_type_0 = Host.from_dict(data)

                return componentsschemas_refer_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_refer_to_type_1 = Parent.from_dict(data)

                return componentsschemas_refer_to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_refer_to_type_2 = Child.from_dict(data)

                return componentsschemas_refer_to_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_refer_to_type_3 = ChildWith.from_dict(data)

            return componentsschemas_refer_to_type_3

        refer_to = _parse_refer_to(d.pop("refer_to"))

        bi_host_search = cls(
            type_=type_,
            conditions=conditions,
            refer_to=refer_to,
        )

        bi_host_search.additional_properties = d
        return bi_host_search

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
