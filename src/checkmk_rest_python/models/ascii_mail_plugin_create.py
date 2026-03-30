from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkbox import Checkbox
    from ..models.checkbox_sort_order_value import CheckboxSortOrderValue
    from ..models.checkbox_with_str_value import CheckboxWithStrValue
    from ..models.from_email_and_name_checkbox import FromEmailAndNameCheckbox
    from ..models.subject_for_host_notifications_checkbox import (
        SubjectForHostNotificationsCheckbox,
    )
    from ..models.subject_for_service_notifications_checkbox import (
        SubjectForServiceNotificationsCheckbox,
    )
    from ..models.to_email_and_name_checkbox import ToEmailAndNameCheckbox


T = TypeVar("T", bound="AsciiMailPluginCreate")


@_attrs_define
class AsciiMailPluginCreate:
    """
    Attributes:
        plugin_name (Any): The ASCII Mail plug-in. Default: 'asciimail'. Example: asciimail.
        from_details (Checkbox | FromEmailAndNameCheckbox | Unset):
        reply_to (Checkbox | ToEmailAndNameCheckbox | Unset):
        subject_for_host_notifications (Checkbox | SubjectForHostNotificationsCheckbox | Unset):
        subject_for_service_notifications (Checkbox | SubjectForServiceNotificationsCheckbox | Unset):
        send_separate_notification_to_every_recipient (Checkbox | Unset):
        sort_order_for_bulk_notifications (Checkbox | CheckboxSortOrderValue | Unset):
        body_head_for_both_host_and_service_notifications (Checkbox | CheckboxWithStrValue | Unset):
        body_tail_for_host_notifications (Checkbox | CheckboxWithStrValue | Unset):
        body_tail_for_service_notifications (Checkbox | CheckboxWithStrValue | Unset):
    """

    plugin_name: Any = "asciimail"
    from_details: Checkbox | FromEmailAndNameCheckbox | Unset = UNSET
    reply_to: Checkbox | ToEmailAndNameCheckbox | Unset = UNSET
    subject_for_host_notifications: (
        Checkbox | SubjectForHostNotificationsCheckbox | Unset
    ) = UNSET
    subject_for_service_notifications: (
        Checkbox | SubjectForServiceNotificationsCheckbox | Unset
    ) = UNSET
    send_separate_notification_to_every_recipient: Checkbox | Unset = UNSET
    sort_order_for_bulk_notifications: Checkbox | CheckboxSortOrderValue | Unset = UNSET
    body_head_for_both_host_and_service_notifications: (
        Checkbox | CheckboxWithStrValue | Unset
    ) = UNSET
    body_tail_for_host_notifications: Checkbox | CheckboxWithStrValue | Unset = UNSET
    body_tail_for_service_notifications: Checkbox | CheckboxWithStrValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.checkbox import Checkbox

        plugin_name = self.plugin_name

        from_details: dict[str, Any] | Unset
        if isinstance(self.from_details, Unset):
            from_details = UNSET
        elif isinstance(self.from_details, Checkbox):
            from_details = self.from_details.to_dict()
        else:
            from_details = self.from_details.to_dict()

        reply_to: dict[str, Any] | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        elif isinstance(self.reply_to, Checkbox):
            reply_to = self.reply_to.to_dict()
        else:
            reply_to = self.reply_to.to_dict()

        subject_for_host_notifications: dict[str, Any] | Unset
        if isinstance(self.subject_for_host_notifications, Unset):
            subject_for_host_notifications = UNSET
        elif isinstance(self.subject_for_host_notifications, Checkbox):
            subject_for_host_notifications = (
                self.subject_for_host_notifications.to_dict()
            )
        else:
            subject_for_host_notifications = (
                self.subject_for_host_notifications.to_dict()
            )

        subject_for_service_notifications: dict[str, Any] | Unset
        if isinstance(self.subject_for_service_notifications, Unset):
            subject_for_service_notifications = UNSET
        elif isinstance(self.subject_for_service_notifications, Checkbox):
            subject_for_service_notifications = (
                self.subject_for_service_notifications.to_dict()
            )
        else:
            subject_for_service_notifications = (
                self.subject_for_service_notifications.to_dict()
            )

        send_separate_notification_to_every_recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_separate_notification_to_every_recipient, Unset):
            send_separate_notification_to_every_recipient = (
                self.send_separate_notification_to_every_recipient.to_dict()
            )

        sort_order_for_bulk_notifications: dict[str, Any] | Unset
        if isinstance(self.sort_order_for_bulk_notifications, Unset):
            sort_order_for_bulk_notifications = UNSET
        elif isinstance(self.sort_order_for_bulk_notifications, Checkbox):
            sort_order_for_bulk_notifications = (
                self.sort_order_for_bulk_notifications.to_dict()
            )
        else:
            sort_order_for_bulk_notifications = (
                self.sort_order_for_bulk_notifications.to_dict()
            )

        body_head_for_both_host_and_service_notifications: dict[str, Any] | Unset
        if isinstance(self.body_head_for_both_host_and_service_notifications, Unset):
            body_head_for_both_host_and_service_notifications = UNSET
        elif isinstance(
            self.body_head_for_both_host_and_service_notifications, Checkbox
        ):
            body_head_for_both_host_and_service_notifications = (
                self.body_head_for_both_host_and_service_notifications.to_dict()
            )
        else:
            body_head_for_both_host_and_service_notifications = (
                self.body_head_for_both_host_and_service_notifications.to_dict()
            )

        body_tail_for_host_notifications: dict[str, Any] | Unset
        if isinstance(self.body_tail_for_host_notifications, Unset):
            body_tail_for_host_notifications = UNSET
        elif isinstance(self.body_tail_for_host_notifications, Checkbox):
            body_tail_for_host_notifications = (
                self.body_tail_for_host_notifications.to_dict()
            )
        else:
            body_tail_for_host_notifications = (
                self.body_tail_for_host_notifications.to_dict()
            )

        body_tail_for_service_notifications: dict[str, Any] | Unset
        if isinstance(self.body_tail_for_service_notifications, Unset):
            body_tail_for_service_notifications = UNSET
        elif isinstance(self.body_tail_for_service_notifications, Checkbox):
            body_tail_for_service_notifications = (
                self.body_tail_for_service_notifications.to_dict()
            )
        else:
            body_tail_for_service_notifications = (
                self.body_tail_for_service_notifications.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plugin_name": plugin_name,
            }
        )
        if from_details is not UNSET:
            field_dict["from_details"] = from_details
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if subject_for_host_notifications is not UNSET:
            field_dict["subject_for_host_notifications"] = (
                subject_for_host_notifications
            )
        if subject_for_service_notifications is not UNSET:
            field_dict["subject_for_service_notifications"] = (
                subject_for_service_notifications
            )
        if send_separate_notification_to_every_recipient is not UNSET:
            field_dict["send_separate_notification_to_every_recipient"] = (
                send_separate_notification_to_every_recipient
            )
        if sort_order_for_bulk_notifications is not UNSET:
            field_dict["sort_order_for_bulk_notifications"] = (
                sort_order_for_bulk_notifications
            )
        if body_head_for_both_host_and_service_notifications is not UNSET:
            field_dict["body_head_for_both_host_and_service_notifications"] = (
                body_head_for_both_host_and_service_notifications
            )
        if body_tail_for_host_notifications is not UNSET:
            field_dict["body_tail_for_host_notifications"] = (
                body_tail_for_host_notifications
            )
        if body_tail_for_service_notifications is not UNSET:
            field_dict["body_tail_for_service_notifications"] = (
                body_tail_for_service_notifications
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkbox import Checkbox
        from ..models.checkbox_sort_order_value import CheckboxSortOrderValue
        from ..models.checkbox_with_str_value import CheckboxWithStrValue
        from ..models.from_email_and_name_checkbox import FromEmailAndNameCheckbox
        from ..models.subject_for_host_notifications_checkbox import (
            SubjectForHostNotificationsCheckbox,
        )
        from ..models.subject_for_service_notifications_checkbox import (
            SubjectForServiceNotificationsCheckbox,
        )
        from ..models.to_email_and_name_checkbox import ToEmailAndNameCheckbox

        d = dict(src_dict)
        plugin_name = d.pop("plugin_name")

        def _parse_from_details(
            data: object,
        ) -> Checkbox | FromEmailAndNameCheckbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_from_details_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_from_details_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_from_details_one_of_type_1 = (
                FromEmailAndNameCheckbox.from_dict(data)
            )

            return componentsschemas_from_details_one_of_type_1

        from_details = _parse_from_details(d.pop("from_details", UNSET))

        def _parse_reply_to(data: object) -> Checkbox | ToEmailAndNameCheckbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reply_to_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_reply_to_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_reply_to_one_of_type_1 = ToEmailAndNameCheckbox.from_dict(
                data
            )

            return componentsschemas_reply_to_one_of_type_1

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        def _parse_subject_for_host_notifications(
            data: object,
        ) -> Checkbox | SubjectForHostNotificationsCheckbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subject_host_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_subject_host_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_subject_host_one_of_type_1 = (
                SubjectForHostNotificationsCheckbox.from_dict(data)
            )

            return componentsschemas_subject_host_one_of_type_1

        subject_for_host_notifications = _parse_subject_for_host_notifications(
            d.pop("subject_for_host_notifications", UNSET)
        )

        def _parse_subject_for_service_notifications(
            data: object,
        ) -> Checkbox | SubjectForServiceNotificationsCheckbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subject_service_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_subject_service_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_subject_service_one_of_type_1 = (
                SubjectForServiceNotificationsCheckbox.from_dict(data)
            )

            return componentsschemas_subject_service_one_of_type_1

        subject_for_service_notifications = _parse_subject_for_service_notifications(
            d.pop("subject_for_service_notifications", UNSET)
        )

        _send_separate_notification_to_every_recipient = d.pop(
            "send_separate_notification_to_every_recipient", UNSET
        )
        send_separate_notification_to_every_recipient: Checkbox | Unset
        if isinstance(_send_separate_notification_to_every_recipient, Unset):
            send_separate_notification_to_every_recipient = UNSET
        else:
            send_separate_notification_to_every_recipient = Checkbox.from_dict(
                _send_separate_notification_to_every_recipient
            )

        def _parse_sort_order_for_bulk_notifications(
            data: object,
        ) -> Checkbox | CheckboxSortOrderValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sort_order_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_sort_order_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_sort_order_one_of_type_1 = (
                CheckboxSortOrderValue.from_dict(data)
            )

            return componentsschemas_sort_order_one_of_type_1

        sort_order_for_bulk_notifications = _parse_sort_order_for_bulk_notifications(
            d.pop("sort_order_for_bulk_notifications", UNSET)
        )

        def _parse_body_head_for_both_host_and_service_notifications(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        body_head_for_both_host_and_service_notifications = (
            _parse_body_head_for_both_host_and_service_notifications(
                d.pop("body_head_for_both_host_and_service_notifications", UNSET)
            )
        )

        def _parse_body_tail_for_host_notifications(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        body_tail_for_host_notifications = _parse_body_tail_for_host_notifications(
            d.pop("body_tail_for_host_notifications", UNSET)
        )

        def _parse_body_tail_for_service_notifications(
            data: object,
        ) -> Checkbox | CheckboxWithStrValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_str_value_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_str_value_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_str_value_one_of_type_1 = CheckboxWithStrValue.from_dict(
                data
            )

            return componentsschemas_str_value_one_of_type_1

        body_tail_for_service_notifications = (
            _parse_body_tail_for_service_notifications(
                d.pop("body_tail_for_service_notifications", UNSET)
            )
        )

        ascii_mail_plugin_create = cls(
            plugin_name=plugin_name,
            from_details=from_details,
            reply_to=reply_to,
            subject_for_host_notifications=subject_for_host_notifications,
            subject_for_service_notifications=subject_for_service_notifications,
            send_separate_notification_to_every_recipient=send_separate_notification_to_every_recipient,
            sort_order_for_bulk_notifications=sort_order_for_bulk_notifications,
            body_head_for_both_host_and_service_notifications=body_head_for_both_host_and_service_notifications,
            body_tail_for_host_notifications=body_tail_for_host_notifications,
            body_tail_for_service_notifications=body_tail_for_service_notifications,
        )

        ascii_mail_plugin_create.additional_properties = d
        return ascii_mail_plugin_create

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
