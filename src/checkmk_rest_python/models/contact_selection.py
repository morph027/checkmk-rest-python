from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_with_list_of_contact_groups import (
        CheckboxWithListOfContactGroups,
    )
    from ..models.checkbox_with_list_of_email_addresses import (
        CheckboxWithListOfEmailAddresses,
    )
    from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
    from ..models.match_custom_macros import MatchCustomMacros


T = TypeVar("T", bound="ContactSelection")


@_attrs_define
class ContactSelection:
    """
    Attributes:
        all_contacts_of_the_notified_object (Checkbox | Unset):
        all_users (Checkbox | Unset):
        all_users_with_an_email_address (Checkbox | Unset):
        the_following_users (Checkbox | CheckboxWithListOfStr | Unset):
        members_of_contact_groups (Checkbox | CheckboxWithListOfContactGroups | Unset):
        explicit_email_addresses (Checkbox | CheckboxWithListOfEmailAddresses | Unset):
        restrict_by_contact_groups (Checkbox | CheckboxWithListOfContactGroups | Unset):
        restrict_by_custom_macros (Checkbox | MatchCustomMacros | Unset):
    """

    all_contacts_of_the_notified_object: Checkbox | Unset = UNSET
    all_users: Checkbox | Unset = UNSET
    all_users_with_an_email_address: Checkbox | Unset = UNSET
    the_following_users: Checkbox | CheckboxWithListOfStr | Unset = UNSET
    members_of_contact_groups: Checkbox | CheckboxWithListOfContactGroups | Unset = (
        UNSET
    )
    explicit_email_addresses: Checkbox | CheckboxWithListOfEmailAddresses | Unset = (
        UNSET
    )
    restrict_by_contact_groups: Checkbox | CheckboxWithListOfContactGroups | Unset = (
        UNSET
    )
    restrict_by_custom_macros: Checkbox | MatchCustomMacros | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        all_contacts_of_the_notified_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_contacts_of_the_notified_object, Unset):
            all_contacts_of_the_notified_object = (
                self.all_contacts_of_the_notified_object.to_dict()
            )

        all_users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_users, Unset):
            all_users = self.all_users.to_dict()

        all_users_with_an_email_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_users_with_an_email_address, Unset):
            all_users_with_an_email_address = (
                self.all_users_with_an_email_address.to_dict()
            )

        the_following_users: dict[str, Any] | Unset
        if isinstance(self.the_following_users, Unset):
            the_following_users = UNSET
        elif isinstance(self.the_following_users, Checkbox):
            the_following_users = self.the_following_users.to_dict()
        else:
            the_following_users = self.the_following_users.to_dict()

        members_of_contact_groups: dict[str, Any] | Unset
        if isinstance(self.members_of_contact_groups, Unset):
            members_of_contact_groups = UNSET
        elif isinstance(self.members_of_contact_groups, Checkbox):
            members_of_contact_groups = self.members_of_contact_groups.to_dict()
        else:
            members_of_contact_groups = self.members_of_contact_groups.to_dict()

        explicit_email_addresses: dict[str, Any] | Unset
        if isinstance(self.explicit_email_addresses, Unset):
            explicit_email_addresses = UNSET
        elif isinstance(self.explicit_email_addresses, Checkbox):
            explicit_email_addresses = self.explicit_email_addresses.to_dict()
        else:
            explicit_email_addresses = self.explicit_email_addresses.to_dict()

        restrict_by_contact_groups: dict[str, Any] | Unset
        if isinstance(self.restrict_by_contact_groups, Unset):
            restrict_by_contact_groups = UNSET
        elif isinstance(self.restrict_by_contact_groups, Checkbox):
            restrict_by_contact_groups = self.restrict_by_contact_groups.to_dict()
        else:
            restrict_by_contact_groups = self.restrict_by_contact_groups.to_dict()

        restrict_by_custom_macros: dict[str, Any] | Unset
        if isinstance(self.restrict_by_custom_macros, Unset):
            restrict_by_custom_macros = UNSET
        elif isinstance(self.restrict_by_custom_macros, Checkbox):
            restrict_by_custom_macros = self.restrict_by_custom_macros.to_dict()
        else:
            restrict_by_custom_macros = self.restrict_by_custom_macros.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_contacts_of_the_notified_object is not UNSET:
            field_dict["all_contacts_of_the_notified_object"] = (
                all_contacts_of_the_notified_object
            )
        if all_users is not UNSET:
            field_dict["all_users"] = all_users
        if all_users_with_an_email_address is not UNSET:
            field_dict["all_users_with_an_email_address"] = (
                all_users_with_an_email_address
            )
        if the_following_users is not UNSET:
            field_dict["the_following_users"] = the_following_users
        if members_of_contact_groups is not UNSET:
            field_dict["members_of_contact_groups"] = members_of_contact_groups
        if explicit_email_addresses is not UNSET:
            field_dict["explicit_email_addresses"] = explicit_email_addresses
        if restrict_by_contact_groups is not UNSET:
            field_dict["restrict_by_contact_groups"] = restrict_by_contact_groups
        if restrict_by_custom_macros is not UNSET:
            field_dict["restrict_by_custom_macros"] = restrict_by_custom_macros

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.checkbox_with_list_of_contact_groups import (
            CheckboxWithListOfContactGroups,
        )
        from ..models.checkbox_with_list_of_email_addresses import (
            CheckboxWithListOfEmailAddresses,
        )
        from ..models.checkbox_with_list_of_str import CheckboxWithListOfStr
        from ..models.match_custom_macros import MatchCustomMacros

        d = dict(src_dict)
        _all_contacts_of_the_notified_object = d.pop(
            "all_contacts_of_the_notified_object", UNSET
        )
        all_contacts_of_the_notified_object: Checkbox | Unset
        if isinstance(_all_contacts_of_the_notified_object, Unset):
            all_contacts_of_the_notified_object = UNSET
        else:
            all_contacts_of_the_notified_object = Checkbox.from_dict(
                _all_contacts_of_the_notified_object
            )

        _all_users = d.pop("all_users", UNSET)
        all_users: Checkbox | Unset
        if isinstance(_all_users, Unset):
            all_users = UNSET
        else:
            all_users = Checkbox.from_dict(_all_users)

        _all_users_with_an_email_address = d.pop(
            "all_users_with_an_email_address", UNSET
        )
        all_users_with_an_email_address: Checkbox | Unset
        if isinstance(_all_users_with_an_email_address, Unset):
            all_users_with_an_email_address = UNSET
        else:
            all_users_with_an_email_address = Checkbox.from_dict(
                _all_users_with_an_email_address
            )

        def _parse_the_following_users(
            data: object,
        ) -> Checkbox | CheckboxWithListOfStr | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_the_following_users_type_0 = Checkbox.from_dict(data)

                return componentsschemas_the_following_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_the_following_users_type_1 = (
                CheckboxWithListOfStr.from_dict(data)
            )

            return componentsschemas_the_following_users_type_1

        the_following_users = _parse_the_following_users(
            d.pop("the_following_users", UNSET)
        )

        def _parse_members_of_contact_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfContactGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_contact_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_list_of_contact_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_contact_groups_checkbox_type_1 = (
                CheckboxWithListOfContactGroups.from_dict(data)
            )

            return componentsschemas_list_of_contact_groups_checkbox_type_1

        members_of_contact_groups = _parse_members_of_contact_groups(
            d.pop("members_of_contact_groups", UNSET)
        )

        def _parse_explicit_email_addresses(
            data: object,
        ) -> Checkbox | CheckboxWithListOfEmailAddresses | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_explicit_email_addresses_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_explicit_email_addresses_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_explicit_email_addresses_checkbox_type_1 = (
                CheckboxWithListOfEmailAddresses.from_dict(data)
            )

            return componentsschemas_explicit_email_addresses_checkbox_type_1

        explicit_email_addresses = _parse_explicit_email_addresses(
            d.pop("explicit_email_addresses", UNSET)
        )

        def _parse_restrict_by_contact_groups(
            data: object,
        ) -> Checkbox | CheckboxWithListOfContactGroups | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_list_of_contact_groups_checkbox_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_list_of_contact_groups_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_list_of_contact_groups_checkbox_type_1 = (
                CheckboxWithListOfContactGroups.from_dict(data)
            )

            return componentsschemas_list_of_contact_groups_checkbox_type_1

        restrict_by_contact_groups = _parse_restrict_by_contact_groups(
            d.pop("restrict_by_contact_groups", UNSET)
        )

        def _parse_restrict_by_custom_macros(
            data: object,
        ) -> Checkbox | MatchCustomMacros | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_custom_macros_checkbox_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_custom_macros_checkbox_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_custom_macros_checkbox_type_1 = (
                MatchCustomMacros.from_dict(data)
            )

            return componentsschemas_custom_macros_checkbox_type_1

        restrict_by_custom_macros = _parse_restrict_by_custom_macros(
            d.pop("restrict_by_custom_macros", UNSET)
        )

        contact_selection = cls(
            all_contacts_of_the_notified_object=all_contacts_of_the_notified_object,
            all_users=all_users,
            all_users_with_an_email_address=all_users_with_an_email_address,
            the_following_users=the_following_users,
            members_of_contact_groups=members_of_contact_groups,
            explicit_email_addresses=explicit_email_addresses,
            restrict_by_contact_groups=restrict_by_contact_groups,
            restrict_by_custom_macros=restrict_by_custom_macros,
        )

        contact_selection.additional_properties = d
        return contact_selection

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
