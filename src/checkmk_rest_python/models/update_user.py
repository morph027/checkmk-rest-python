from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_user_language import UpdateUserLanguage
from ..models.update_user_temperature_unit import UpdateUserTemperatureUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_update_password import AuthUpdatePassword
    from ..models.auth_update_remove import AuthUpdateRemove
    from ..models.auth_update_secret import AuthUpdateSecret
    from ..models.disabled_notifications import DisabledNotifications
    from ..models.idle_option import IdleOption
    from ..models.user_contact_option import UserContactOption
    from ..models.user_interface_update_attributes import UserInterfaceUpdateAttributes


T = TypeVar("T", bound="UpdateUser")


@_attrs_define
class UpdateUser:
    """
    Attributes:
        fullname (str | Unset): The alias or full name of the user Example: Mathias Kettner.
        auth_option (AuthUpdatePassword | AuthUpdateRemove | AuthUpdateSecret | Unset):
        disable_login (bool | Unset): The user can be blocked from login but will remain part of the site. The disabling
            does not affect notification and alerts.
        contact_options (UserContactOption | Unset):
        pager_address (str | Unset):
        idle_timeout (IdleOption | Unset):
        roles (list[str] | Unset): The list of assigned roles to the user Example: ['user'].
        authorized_sites (list[str] | Unset): The names of the sites the user is authorized to handle. Specifying 'all'
            will grant the user access to all sites. Example: ['mysite'].
        contactgroups (list[str] | Unset): Assign the user to one or multiple contact groups. If no contact group is
            specified then no monitoring contact will be created for the user. Example: ['all'].
        disable_notifications (DisabledNotifications | Unset):
        language (UpdateUserLanguage | Unset): Configure the language to be used by the user in the user interface.
            Omitting this will configure the default language Example: en.
        temperature_unit (UpdateUserTemperatureUnit | Unset): Configure the temperature unit used for graphs and
            perfometers. Example: celsius.
        interface_options (UserInterfaceUpdateAttributes | Unset):
    """

    fullname: str | Unset = UNSET
    auth_option: AuthUpdatePassword | AuthUpdateRemove | AuthUpdateSecret | Unset = (
        UNSET
    )
    disable_login: bool | Unset = UNSET
    contact_options: UserContactOption | Unset = UNSET
    pager_address: str | Unset = UNSET
    idle_timeout: IdleOption | Unset = UNSET
    roles: list[str] | Unset = UNSET
    authorized_sites: list[str] | Unset = UNSET
    contactgroups: list[str] | Unset = UNSET
    disable_notifications: DisabledNotifications | Unset = UNSET
    language: UpdateUserLanguage | Unset = UNSET
    temperature_unit: UpdateUserTemperatureUnit | Unset = UNSET
    interface_options: UserInterfaceUpdateAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_update_password import AuthUpdatePassword
        from ..models.auth_update_secret import AuthUpdateSecret

        fullname = self.fullname

        auth_option: dict[str, Any] | Unset
        if isinstance(self.auth_option, Unset):
            auth_option = UNSET
        elif isinstance(self.auth_option, AuthUpdatePassword):
            auth_option = self.auth_option.to_dict()
        elif isinstance(self.auth_option, AuthUpdateSecret):
            auth_option = self.auth_option.to_dict()
        else:
            auth_option = self.auth_option.to_dict()

        disable_login = self.disable_login

        contact_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_options, Unset):
            contact_options = self.contact_options.to_dict()

        pager_address = self.pager_address

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

        disable_notifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disable_notifications, Unset):
            disable_notifications = self.disable_notifications.to_dict()

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        temperature_unit: str | Unset = UNSET
        if not isinstance(self.temperature_unit, Unset):
            temperature_unit = self.temperature_unit.value

        interface_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interface_options, Unset):
            interface_options = self.interface_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fullname is not UNSET:
            field_dict["fullname"] = fullname
        if auth_option is not UNSET:
            field_dict["auth_option"] = auth_option
        if disable_login is not UNSET:
            field_dict["disable_login"] = disable_login
        if contact_options is not UNSET:
            field_dict["contact_options"] = contact_options
        if pager_address is not UNSET:
            field_dict["pager_address"] = pager_address
        if idle_timeout is not UNSET:
            field_dict["idle_timeout"] = idle_timeout
        if roles is not UNSET:
            field_dict["roles"] = roles
        if authorized_sites is not UNSET:
            field_dict["authorized_sites"] = authorized_sites
        if contactgroups is not UNSET:
            field_dict["contactgroups"] = contactgroups
        if disable_notifications is not UNSET:
            field_dict["disable_notifications"] = disable_notifications
        if language is not UNSET:
            field_dict["language"] = language
        if temperature_unit is not UNSET:
            field_dict["temperature_unit"] = temperature_unit
        if interface_options is not UNSET:
            field_dict["interface_options"] = interface_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_update_password import AuthUpdatePassword
        from ..models.auth_update_remove import AuthUpdateRemove
        from ..models.auth_update_secret import AuthUpdateSecret
        from ..models.disabled_notifications import DisabledNotifications
        from ..models.idle_option import IdleOption
        from ..models.user_contact_option import UserContactOption
        from ..models.user_interface_update_attributes import (
            UserInterfaceUpdateAttributes,
        )

        d = dict(src_dict)
        fullname = d.pop("fullname", UNSET)

        def _parse_auth_option(
            data: object,
        ) -> AuthUpdatePassword | AuthUpdateRemove | AuthUpdateSecret | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_update_option_type_0 = (
                    AuthUpdatePassword.from_dict(data)
                )

                return componentsschemas_auth_update_option_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_auth_update_option_type_1 = (
                    AuthUpdateSecret.from_dict(data)
                )

                return componentsschemas_auth_update_option_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_auth_update_option_type_2 = AuthUpdateRemove.from_dict(
                data
            )

            return componentsschemas_auth_update_option_type_2

        auth_option = _parse_auth_option(d.pop("auth_option", UNSET))

        disable_login = d.pop("disable_login", UNSET)

        _contact_options = d.pop("contact_options", UNSET)
        contact_options: UserContactOption | Unset
        if isinstance(_contact_options, Unset):
            contact_options = UNSET
        else:
            contact_options = UserContactOption.from_dict(_contact_options)

        pager_address = d.pop("pager_address", UNSET)

        _idle_timeout = d.pop("idle_timeout", UNSET)
        idle_timeout: IdleOption | Unset
        if isinstance(_idle_timeout, Unset):
            idle_timeout = UNSET
        else:
            idle_timeout = IdleOption.from_dict(_idle_timeout)

        roles = cast(list[str], d.pop("roles", UNSET))

        authorized_sites = cast(list[str], d.pop("authorized_sites", UNSET))

        contactgroups = cast(list[str], d.pop("contactgroups", UNSET))

        _disable_notifications = d.pop("disable_notifications", UNSET)
        disable_notifications: DisabledNotifications | Unset
        if isinstance(_disable_notifications, Unset):
            disable_notifications = UNSET
        else:
            disable_notifications = DisabledNotifications.from_dict(
                _disable_notifications
            )

        _language = d.pop("language", UNSET)
        language: UpdateUserLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = UpdateUserLanguage(_language)

        _temperature_unit = d.pop("temperature_unit", UNSET)
        temperature_unit: UpdateUserTemperatureUnit | Unset
        if isinstance(_temperature_unit, Unset):
            temperature_unit = UNSET
        else:
            temperature_unit = UpdateUserTemperatureUnit(_temperature_unit)

        _interface_options = d.pop("interface_options", UNSET)
        interface_options: UserInterfaceUpdateAttributes | Unset
        if isinstance(_interface_options, Unset):
            interface_options = UNSET
        else:
            interface_options = UserInterfaceUpdateAttributes.from_dict(
                _interface_options
            )

        update_user = cls(
            fullname=fullname,
            auth_option=auth_option,
            disable_login=disable_login,
            contact_options=contact_options,
            pager_address=pager_address,
            idle_timeout=idle_timeout,
            roles=roles,
            authorized_sites=authorized_sites,
            contactgroups=contactgroups,
            disable_notifications=disable_notifications,
            language=language,
            temperature_unit=temperature_unit,
            interface_options=interface_options,
        )

        update_user.additional_properties = d
        return update_user

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
