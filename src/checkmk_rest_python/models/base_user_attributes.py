from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_option_output import AuthOptionOutput
    from ..models.concrete_disabled_notifications import ConcreteDisabledNotifications
    from ..models.concrete_user_contact_option import ConcreteUserContactOption
    from ..models.concrete_user_interface_attributes import (
        ConcreteUserInterfaceAttributes,
    )
    from ..models.user_idle_option import UserIdleOption


T = TypeVar("T", bound="BaseUserAttributes")


@_attrs_define
class BaseUserAttributes:
    """
    Attributes:
        fullname (str): The alias or full name of the user.
        disable_login (bool | Unset): This field indicates if the user is allowed to login to the monitoring.
        contact_options (ConcreteUserContactOption | Unset):
        idle_timeout (UserIdleOption | Unset):
        roles (list[str] | Unset): The list of assigned roles to the user
        authorized_sites (list[str] | Unset): The names of the sites that this user is authorized to handle
        contactgroups (list[str] | Unset): The contact groups that this user is a member of
        pager_address (str | Unset):
        disable_notifications (ConcreteDisabledNotifications | Unset):
        language (str | Unset): The language used by the user in the user interface
        temperature_unit (str | Unset): The temperature unit used for graphs and perfometers.
        auth_option (AuthOptionOutput | Unset):
        interface_options (ConcreteUserInterfaceAttributes | Unset):
    """

    fullname: str
    disable_login: bool | Unset = UNSET
    contact_options: ConcreteUserContactOption | Unset = UNSET
    idle_timeout: UserIdleOption | Unset = UNSET
    roles: list[str] | Unset = UNSET
    authorized_sites: list[str] | Unset = UNSET
    contactgroups: list[str] | Unset = UNSET
    pager_address: str | Unset = UNSET
    disable_notifications: ConcreteDisabledNotifications | Unset = UNSET
    language: str | Unset = UNSET
    temperature_unit: str | Unset = UNSET
    auth_option: AuthOptionOutput | Unset = UNSET
    interface_options: ConcreteUserInterfaceAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fullname = self.fullname

        disable_login = self.disable_login

        contact_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_options, Unset):
            contact_options = self.contact_options.to_dict()

        idle_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.idle_timeout, Unset):
            idle_timeout = self.idle_timeout.to_dict()

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        authorized_sites: list[str] | Unset = UNSET
        if not isinstance(self.authorized_sites, Unset):
            authorized_sites = self.authorized_sites

        contactgroups: list[str] | Unset = UNSET
        if not isinstance(self.contactgroups, Unset):
            contactgroups = self.contactgroups

        pager_address = self.pager_address

        disable_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_notifications, Unset):
            disable_notifications = self.disable_notifications.to_dict()

        language = self.language

        temperature_unit = self.temperature_unit

        auth_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_option, Unset):
            auth_option = self.auth_option.to_dict()

        interface_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = self.interface_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fullname": fullname,
            }
        )
        if disable_login is not UNSET:
            field_dict["disable_login"] = disable_login
        if contact_options is not UNSET:
            field_dict["contact_options"] = contact_options
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout
        if roles is not UNSET:
            field_dict["roles"] = roles
        if authorized_sites is not UNSET:
            field_dict["authorized_sites"] = authorized_sites
        if contactgroups is not UNSET:
            field_dict["contactgroups"] = contactgroups
        if pager_address is not UNSET:
            field_dict["pager_address"] = pager_address
        if disable_notifications is not UNSET:
            field_dict["disable_notifications"] = disable_notifications
        if language is not UNSET:
            field_dict["language"] = language
        if temperature_unit is not UNSET:
            field_dict["temperature_unit"] = temperature_unit
        if auth_option is not UNSET:
            field_dict["auth_option"] = auth_option
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_option_output import AuthOptionOutput
        from ..models.concrete_disabled_notifications import (
            ConcreteDisabledNotifications,
        )
        from ..models.concrete_user_contact_option import ConcreteUserContactOption
        from ..models.concrete_user_interface_attributes import (
            ConcreteUserInterfaceAttributes,
        )
        from ..models.user_idle_option import UserIdleOption

        d = dict(src_dict)
        fullname = d.pop("fullname")

        disable_login = d.pop("disable_login", UNSET)

        _contact_options = d.pop("contact_options", UNSET)
        contact_options: ConcreteUserContactOption | Unset
        if isinstance(_contact_options, Unset):
            contact_options = UNSET
        else:
            contact_options = ConcreteUserContactOption.from_dict(_contact_options)

        _idle_timeout = d.pop("idle_timeout", UNSET)
        idle_timeout: UserIdleOption | Unset
        if isinstance(_idle_timeout, Unset):
            idle_timeout = UNSET
        else:
            idle_timeout = UserIdleOption.from_dict(_idle_timeout)

        roles = cast(list[str], d.pop("roles", UNSET))

        authorized_sites = cast(list[str], d.pop("authorized_sites", UNSET))

        contactgroups = cast(list[str], d.pop("contactgroups", UNSET))

        pager_address = d.pop("pager_address", UNSET)

        _disable_notifications = d.pop("disable_notifications", UNSET)
        disable_notifications: ConcreteDisabledNotifications | Unset
        if isinstance(_disable_notifications, Unset):
            disable_notifications = UNSET
        else:
            disable_notifications = ConcreteDisabledNotifications.from_dict(
                _disable_notifications
            )

        language = d.pop("language", UNSET)

        temperature_unit = d.pop("temperature_unit", UNSET)

        _auth_option = d.pop("auth_option", UNSET)
        auth_option: AuthOptionOutput | Unset
        if isinstance(_auth_option, Unset):
            auth_option = UNSET
        else:
            auth_option = AuthOptionOutput.from_dict(_auth_option)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: ConcreteUserInterfaceAttributes | Unset
        if isinstance(_interface_options, Unset):
            interface_options = UNSET
        else:
            interface_options = ConcreteUserInterfaceAttributes.from_dict(
                _interface_options
            )

        base_user_attributes = cls(
            fullname=fullname,
            disable_login=disable_login,
            contact_options=contact_options,
            idle_timeout=idle_timeout,
            roles=roles,
            authorized_sites=authorized_sites,
            contactgroups=contactgroups,
            pager_address=pager_address,
            disable_notifications=disable_notifications,
            language=language,
            temperature_unit=temperature_unit,
            auth_option=auth_option,
            interface_options=interface_options,
        )

        base_user_attributes.additional_properties = d
        return base_user_attributes

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
