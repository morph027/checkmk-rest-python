from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bi_all_hosts_choice import BIAllHostsChoice
    from ..models.bi_host_alias_regex_choice import BIHostAliasRegexChoice
    from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice
    from ..models.label_group_condition import LabelGroupCondition
    from ..models.service_conditions_host_tags import ServiceConditionsHostTags


T = TypeVar("T", bound="ServiceConditions")


@_attrs_define
class ServiceConditions:
    """
    Attributes:
        host_folder (str): Host folder. Example: servers/groupA.
        host_label_groups (list[LabelGroupCondition]): Host label conditions. Although all items in this list have a
            default operator value, the operator value for the the first item in the list does not have any effect. Example:
            [{'label_group': [{'operator': 'and', 'label': 'db:mssql'}]}, {'operator': 'and', 'label_group': [{'operator':
            'and', 'label': 'network/primary:yes'}]}].
        host_tags (ServiceConditionsHostTags): Host tags.
        host_choice (BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice):
        service_regex (str): Service name regex. Example: Filesystem.*.
        service_label_groups (list[LabelGroupCondition]): Service label conditions. Although all items in this list have
            a default operator value, the operator value for the the first item in the list does not have any effect.
            Example: [{'label_group': [{'operator': 'and', 'label': 'db:mssql'}]}, {'operator': 'and', 'label_group':
            [{'operator': 'and', 'label': 'network/primary:yes'}]}].
    """

    host_folder: str
    host_label_groups: list[LabelGroupCondition]
    host_tags: ServiceConditionsHostTags
    host_choice: BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice
    service_regex: str
    service_label_groups: list[LabelGroupCondition]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bi_all_hosts_choice import BIAllHostsChoice
        from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice

        host_folder = self.host_folder

        host_label_groups = []
        for host_label_groups_item_data in self.host_label_groups:
            host_label_groups_item = host_label_groups_item_data.to_dict()
            host_label_groups.append(host_label_groups_item)

        host_tags = self.host_tags.to_dict()

        host_choice: dict[str, Any]
        if isinstance(self.host_choice, BIAllHostsChoice):
            host_choice = self.host_choice.to_dict()
        elif isinstance(self.host_choice, BIHostNameRegexChoice):
            host_choice = self.host_choice.to_dict()
        else:
            host_choice = self.host_choice.to_dict()

        service_regex = self.service_regex

        service_label_groups = []
        for service_label_groups_item_data in self.service_label_groups:
            service_label_groups_item = service_label_groups_item_data.to_dict()
            service_label_groups.append(service_label_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host_folder": host_folder,
                "host_label_groups": host_label_groups,
                "host_tags": host_tags,
                "host_choice": host_choice,
                "service_regex": service_regex,
                "service_label_groups": service_label_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bi_all_hosts_choice import BIAllHostsChoice
        from ..models.bi_host_alias_regex_choice import BIHostAliasRegexChoice
        from ..models.bi_host_name_regex_choice import BIHostNameRegexChoice
        from ..models.label_group_condition import LabelGroupCondition
        from ..models.service_conditions_host_tags import ServiceConditionsHostTags

        d = dict(src_dict)
        host_folder = d.pop("host_folder")

        host_label_groups = []
        _host_label_groups = d.pop("host_label_groups")
        for host_label_groups_item_data in _host_label_groups:
            host_label_groups_item = LabelGroupCondition.from_dict(
                host_label_groups_item_data
            )

            host_label_groups.append(host_label_groups_item)

        host_tags = ServiceConditionsHostTags.from_dict(d.pop("host_tags"))

        def _parse_host_choice(
            data: object,
        ) -> BIAllHostsChoice | BIHostAliasRegexChoice | BIHostNameRegexChoice:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_host_choice_type_0 = BIAllHostsChoice.from_dict(
                    data
                )

                return componentsschemas_bi_host_choice_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bi_host_choice_type_1 = (
                    BIHostNameRegexChoice.from_dict(data)
                )

                return componentsschemas_bi_host_choice_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bi_host_choice_type_2 = BIHostAliasRegexChoice.from_dict(
                data
            )

            return componentsschemas_bi_host_choice_type_2

        host_choice = _parse_host_choice(d.pop("host_choice"))

        service_regex = d.pop("service_regex")

        service_label_groups = []
        _service_label_groups = d.pop("service_label_groups")
        for service_label_groups_item_data in _service_label_groups:
            service_label_groups_item = LabelGroupCondition.from_dict(
                service_label_groups_item_data
            )

            service_label_groups.append(service_label_groups_item)

        service_conditions = cls(
            host_folder=host_folder,
            host_label_groups=host_label_groups,
            host_tags=host_tags,
            host_choice=host_choice,
            service_regex=service_regex,
            service_label_groups=service_label_groups,
        )

        service_conditions.additional_properties = d
        return service_conditions

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
