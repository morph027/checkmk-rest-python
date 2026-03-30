from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox_output import CheckboxOutput
    from ..models.checkbox_with_list_of_str_output import CheckboxWithListOfStrOutput
    from ..models.match_custom_macros_output import MatchCustomMacrosOutput


T = TypeVar("T", bound="ContactSelectionAttributes")


@_attrs_define
class ContactSelectionAttributes:
    """
    Attributes:
        all_contacts_of_the_notified_object (CheckboxOutput | Unset):
        all_users (CheckboxOutput | Unset):
        all_users_with_an_email_address (CheckboxOutput | Unset):
        the_following_users (CheckboxWithListOfStrOutput | Unset):
        members_of_contact_groups (CheckboxWithListOfStrOutput | Unset):
        explicit_email_addresses (CheckboxWithListOfStrOutput | Unset):
        restrict_by_custom_macros (MatchCustomMacrosOutput | Unset):
        restrict_by_contact_groups (CheckboxWithListOfStrOutput | Unset):
    """

    all_contacts_of_the_notified_object: CheckboxOutput | Unset = UNSET
    all_users: CheckboxOutput | Unset = UNSET
    all_users_with_an_email_address: CheckboxOutput | Unset = UNSET
    the_following_users: CheckboxWithListOfStrOutput | Unset = UNSET
    members_of_contact_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    explicit_email_addresses: CheckboxWithListOfStrOutput | Unset = UNSET
    restrict_by_custom_macros: MatchCustomMacrosOutput | Unset = UNSET
    restrict_by_contact_groups: CheckboxWithListOfStrOutput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        the_following_users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.the_following_users, Unset):
            the_following_users = self.the_following_users.to_dict()

        members_of_contact_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members_of_contact_groups, Unset):
            members_of_contact_groups = self.members_of_contact_groups.to_dict()

        explicit_email_addresses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.explicit_email_addresses, Unset):
            explicit_email_addresses = self.explicit_email_addresses.to_dict()

        restrict_by_custom_macros: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrict_by_custom_macros, Unset):
            restrict_by_custom_macros = self.restrict_by_custom_macros.to_dict()

        restrict_by_contact_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrict_by_contact_groups, Unset):
            restrict_by_contact_groups = self.restrict_by_contact_groups.to_dict()

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
        if restrict_by_custom_macros is not UNSET:
            field_dict["restrict_by_custom_macros"] = restrict_by_custom_macros
        if restrict_by_contact_groups is not UNSET:
            field_dict["restrict_by_contact_groups"] = restrict_by_contact_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox_output import CheckboxOutput
        from ..models.checkbox_with_list_of_str_output import (
            CheckboxWithListOfStrOutput,
        )
        from ..models.match_custom_macros_output import MatchCustomMacrosOutput

        d = dict(src_dict)
        _all_contacts_of_the_notified_object = d.pop(
            "all_contacts_of_the_notified_object", UNSET
        )
        all_contacts_of_the_notified_object: CheckboxOutput | Unset
        if isinstance(_all_contacts_of_the_notified_object, Unset):
            all_contacts_of_the_notified_object = UNSET
        else:
            all_contacts_of_the_notified_object = CheckboxOutput.from_dict(
                _all_contacts_of_the_notified_object
            )

        _all_users = d.pop("all_users", UNSET)
        all_users: CheckboxOutput | Unset
        if isinstance(_all_users, Unset):
            all_users = UNSET
        else:
            all_users = CheckboxOutput.from_dict(_all_users)

        _all_users_with_an_email_address = d.pop(
            "all_users_with_an_email_address", UNSET
        )
        all_users_with_an_email_address: CheckboxOutput | Unset
        if isinstance(_all_users_with_an_email_address, Unset):
            all_users_with_an_email_address = UNSET
        else:
            all_users_with_an_email_address = CheckboxOutput.from_dict(
                _all_users_with_an_email_address
            )

        _the_following_users = d.pop("the_following_users", UNSET)
        the_following_users: CheckboxWithListOfStrOutput | Unset
        if isinstance(_the_following_users, Unset):
            the_following_users = UNSET
        else:
            the_following_users = CheckboxWithListOfStrOutput.from_dict(
                _the_following_users
            )

        _members_of_contact_groups = d.pop("members_of_contact_groups", UNSET)
        members_of_contact_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_members_of_contact_groups, Unset):
            members_of_contact_groups = UNSET
        else:
            members_of_contact_groups = CheckboxWithListOfStrOutput.from_dict(
                _members_of_contact_groups
            )

        _explicit_email_addresses = d.pop("explicit_email_addresses", UNSET)
        explicit_email_addresses: CheckboxWithListOfStrOutput | Unset
        if isinstance(_explicit_email_addresses, Unset):
            explicit_email_addresses = UNSET
        else:
            explicit_email_addresses = CheckboxWithListOfStrOutput.from_dict(
                _explicit_email_addresses
            )

        _restrict_by_custom_macros = d.pop("restrict_by_custom_macros", UNSET)
        restrict_by_custom_macros: MatchCustomMacrosOutput | Unset
        if isinstance(_restrict_by_custom_macros, Unset):
            restrict_by_custom_macros = UNSET
        else:
            restrict_by_custom_macros = MatchCustomMacrosOutput.from_dict(
                _restrict_by_custom_macros
            )

        _restrict_by_contact_groups = d.pop("restrict_by_contact_groups", UNSET)
        restrict_by_contact_groups: CheckboxWithListOfStrOutput | Unset
        if isinstance(_restrict_by_contact_groups, Unset):
            restrict_by_contact_groups = UNSET
        else:
            restrict_by_contact_groups = CheckboxWithListOfStrOutput.from_dict(
                _restrict_by_contact_groups
            )

        contact_selection_attributes = cls(
            all_contacts_of_the_notified_object=all_contacts_of_the_notified_object,
            all_users=all_users,
            all_users_with_an_email_address=all_users_with_an_email_address,
            the_following_users=the_following_users,
            members_of_contact_groups=members_of_contact_groups,
            explicit_email_addresses=explicit_email_addresses,
            restrict_by_custom_macros=restrict_by_custom_macros,
            restrict_by_contact_groups=restrict_by_contact_groups,
        )

        contact_selection_attributes.additional_properties = d
        return contact_selection_attributes

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
