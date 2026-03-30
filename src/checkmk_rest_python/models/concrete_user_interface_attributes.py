from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.concrete_user_interface_attributes_contextual_help_icon import (
    ConcreteUserInterfaceAttributesContextualHelpIcon,
)
from ..models.concrete_user_interface_attributes_interface_theme import (
    ConcreteUserInterfaceAttributesInterfaceTheme,
)
from ..models.concrete_user_interface_attributes_mega_menu_icons import (
    ConcreteUserInterfaceAttributesMegaMenuIcons,
)
from ..models.concrete_user_interface_attributes_navigation_bar_icons import (
    ConcreteUserInterfaceAttributesNavigationBarIcons,
)
from ..models.concrete_user_interface_attributes_show_mode import (
    ConcreteUserInterfaceAttributesShowMode,
)
from ..models.concrete_user_interface_attributes_sidebar_position import (
    ConcreteUserInterfaceAttributesSidebarPosition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConcreteUserInterfaceAttributes")


@_attrs_define
class ConcreteUserInterfaceAttributes:
    """
    Attributes:
        interface_theme (ConcreteUserInterfaceAttributesInterfaceTheme | Unset): The theme of the interface Example:
            default.
        sidebar_position (ConcreteUserInterfaceAttributesSidebarPosition | Unset): The position of the sidebar Example:
            right.
        navigation_bar_icons (ConcreteUserInterfaceAttributesNavigationBarIcons | Unset): This option decides if icons
            in the navigation bar should show/hide the respective titles Example: hide.
        mega_menu_icons (ConcreteUserInterfaceAttributesMegaMenuIcons | Unset): This option decides if colored icon
            should be shown foe every entry in the mega menus or alternatively only for the headlines (the 'topics')
            Example: topic.
        show_mode (ConcreteUserInterfaceAttributesShowMode | Unset): This option decides what show mode should be used
            for unvisited menus. Alternatively, this option can also be used to enforce show more removing the three dots
            for all menus. Example: default.
        contextual_help_icon (ConcreteUserInterfaceAttributesContextualHelpIcon | Unset): Whether or not to show the
            contextual icon in the UI for this user. Default: ConcreteUserInterfaceAttributesContextualHelpIcon.SHOW_ICON.
            Example: show_icon.
    """

    interface_theme: ConcreteUserInterfaceAttributesInterfaceTheme | Unset = UNSET
    sidebar_position: ConcreteUserInterfaceAttributesSidebarPosition | Unset = UNSET
    navigation_bar_icons: ConcreteUserInterfaceAttributesNavigationBarIcons | Unset = (
        UNSET
    )
    mega_menu_icons: ConcreteUserInterfaceAttributesMegaMenuIcons | Unset = UNSET
    show_mode: ConcreteUserInterfaceAttributesShowMode | Unset = UNSET
    contextual_help_icon: ConcreteUserInterfaceAttributesContextualHelpIcon | Unset = (
        ConcreteUserInterfaceAttributesContextualHelpIcon.SHOW_ICON
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_theme: str | Unset = UNSET
        if not isinstance(self.interface_theme, Unset):
            interface_theme = self.interface_theme.value

        sidebar_position: str | Unset = UNSET
        if not isinstance(self.sidebar_position, Unset):
            sidebar_position = self.sidebar_position.value

        navigation_bar_icons: str | Unset = UNSET
        if not isinstance(self.navigation_bar_icons, Unset):
            navigation_bar_icons = self.navigation_bar_icons.value

        mega_menu_icons: str | Unset = UNSET
        if not isinstance(self.mega_menu_icons, Unset):
            mega_menu_icons = self.mega_menu_icons.value

        show_mode: str | Unset = UNSET
        if not isinstance(self.show_mode, Unset):
            show_mode = self.show_mode.value

        contextual_help_icon: str | Unset = UNSET
        if not isinstance(self.contextual_help_icon, Unset):
            contextual_help_icon = self.contextual_help_icon.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_theme is not UNSET:
            field_dict["interface_theme"] = interface_theme
        if sidebar_position is not UNSET:
            field_dict["sidebar_position"] = sidebar_position
        if navigation_bar_icons is not UNSET:
            field_dict["navigation_bar_icons"] = navigation_bar_icons
        if mega_menu_icons is not UNSET:
            field_dict["mega_menu_icons"] = mega_menu_icons
        if show_mode is not UNSET:
            field_dict["show_mode"] = show_mode
        if contextual_help_icon is not UNSET:
            field_dict["contextual_help_icon"] = contextual_help_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _interface_theme = d.pop("interface_theme", UNSET)
        interface_theme: ConcreteUserInterfaceAttributesInterfaceTheme | Unset
        if isinstance(_interface_theme, Unset):
            interface_theme = UNSET
        else:
            interface_theme = ConcreteUserInterfaceAttributesInterfaceTheme(
                _interface_theme
            )

        _sidebar_position = d.pop("sidebar_position", UNSET)
        sidebar_position: ConcreteUserInterfaceAttributesSidebarPosition | Unset
        if isinstance(_sidebar_position, Unset):
            sidebar_position = UNSET
        else:
            sidebar_position = ConcreteUserInterfaceAttributesSidebarPosition(
                _sidebar_position
            )

        _navigation_bar_icons = d.pop("navigation_bar_icons", UNSET)
        navigation_bar_icons: ConcreteUserInterfaceAttributesNavigationBarIcons | Unset
        if isinstance(_navigation_bar_icons, Unset):
            navigation_bar_icons = UNSET
        else:
            navigation_bar_icons = ConcreteUserInterfaceAttributesNavigationBarIcons(
                _navigation_bar_icons
            )

        _mega_menu_icons = d.pop("mega_menu_icons", UNSET)
        mega_menu_icons: ConcreteUserInterfaceAttributesMegaMenuIcons | Unset
        if isinstance(_mega_menu_icons, Unset):
            mega_menu_icons = UNSET
        else:
            mega_menu_icons = ConcreteUserInterfaceAttributesMegaMenuIcons(
                _mega_menu_icons
            )

        _show_mode = d.pop("show_mode", UNSET)
        show_mode: ConcreteUserInterfaceAttributesShowMode | Unset
        if isinstance(_show_mode, Unset):
            show_mode = UNSET
        else:
            show_mode = ConcreteUserInterfaceAttributesShowMode(_show_mode)

        _contextual_help_icon = d.pop("contextual_help_icon", UNSET)
        contextual_help_icon: ConcreteUserInterfaceAttributesContextualHelpIcon | Unset
        if isinstance(_contextual_help_icon, Unset):
            contextual_help_icon = UNSET
        else:
            contextual_help_icon = ConcreteUserInterfaceAttributesContextualHelpIcon(
                _contextual_help_icon
            )

        concrete_user_interface_attributes = cls(
            interface_theme=interface_theme,
            sidebar_position=sidebar_position,
            navigation_bar_icons=navigation_bar_icons,
            mega_menu_icons=mega_menu_icons,
            show_mode=show_mode,
            contextual_help_icon=contextual_help_icon,
        )

        concrete_user_interface_attributes.additional_properties = d
        return concrete_user_interface_attributes

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
