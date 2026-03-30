from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.acknowledge_service_query_problem_acknowledge_type import (
    AcknowledgeServiceQueryProblemAcknowledgeType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.binary_expr import BinaryExpr
    from ..models.logical_expr import LogicalExpr
    from ..models.not_expr import NotExpr


T = TypeVar("T", bound="AcknowledgeServiceQueryProblem")


@_attrs_define
class AcknowledgeServiceQueryProblem:
    """
    Attributes:
        comment (str): Comment to be stored alongside the acknowledgement. Example: This was expected..
        acknowledge_type (AcknowledgeServiceQueryProblemAcknowledgeType): Select services with a query. Example:
            service_by_query.
        query (BinaryExpr | LogicalExpr | NotExpr):
        sticky (bool | Unset): If set, only a state-change to the UP/OK state will discard the acknowledgement.
            Otherwise, it will be discarded on any state-change. Default: True.
        persistent (bool | Unset): If set, the comment will persist a restart. Default: False.
        notify (bool | Unset): If set, notifications will be sent out to the configured contacts. Default: True.
        expire_on (datetime.datetime | Unset): If set, the acknowledgement will expire at this time. The timezone will
            default to UTC. Example: 2025-05-20T07:30:00Z.
    """

    comment: str
    acknowledge_type: AcknowledgeServiceQueryProblemAcknowledgeType
    query: BinaryExpr | LogicalExpr | NotExpr
    sticky: bool | Unset = True
    persistent: bool | Unset = False
    notify: bool | Unset = True
    expire_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        comment = self.comment

        acknowledge_type = self.acknowledge_type.value

        query: dict[str, Any]
        if isinstance(self.query, LogicalExpr):
            query = self.query.to_dict()
        elif isinstance(self.query, NotExpr):
            query = self.query.to_dict()
        else:
            query = self.query.to_dict()

        sticky = self.sticky

        persistent = self.persistent

        notify = self.notify

        expire_on: str | Unset = UNSET
        if not isinstance(self.expire_on, Unset):
            expire_on = self.expire_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "acknowledge_type": acknowledge_type,
                "query": query,
            }
        )
        if sticky is not UNSET:
            field_dict["sticky"] = sticky
        if persistent is not UNSET:
            field_dict["persistent"] = persistent
        if notify is not UNSET:
            field_dict["notify"] = notify
        if expire_on is not UNSET:
            field_dict["expire_on"] = expire_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.binary_expr import BinaryExpr
        from ..models.logical_expr import LogicalExpr
        from ..models.not_expr import NotExpr

        d = dict(src_dict)
        comment = d.pop("comment")

        acknowledge_type = AcknowledgeServiceQueryProblemAcknowledgeType(
            d.pop("acknowledge_type")
        )

        def _parse_query(data: object) -> BinaryExpr | LogicalExpr | NotExpr:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_0 = LogicalExpr.from_dict(data)

                return componentsschemas_expr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_expr_type_2 = NotExpr.from_dict(data)

                return componentsschemas_expr_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_expr_type_3 = BinaryExpr.from_dict(data)

            return componentsschemas_expr_type_3

        query = _parse_query(d.pop("query"))

        sticky = d.pop("sticky", UNSET)

        persistent = d.pop("persistent", UNSET)

        notify = d.pop("notify", UNSET)

        _expire_on = d.pop("expire_on", UNSET)
        expire_on: datetime.datetime | Unset
        if isinstance(_expire_on, Unset):
            expire_on = UNSET
        else:
            expire_on = isoparse(_expire_on)

        acknowledge_service_query_problem = cls(
            comment=comment,
            acknowledge_type=acknowledge_type,
            query=query,
            sticky=sticky,
            persistent=persistent,
            notify=notify,
            expire_on=expire_on,
        )

        acknowledge_service_query_problem.additional_properties = d
        return acknowledge_service_query_problem

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
