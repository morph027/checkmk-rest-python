from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_notifications_with_graphs import BulkNotificationsWithGraphs
    from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
    from ..models.checkbox import Checkbox
    from ..models.checkbox_sort_order_value import CheckboxSortOrderValue
    from ..models.checkbox_with_list_of_email_info_strs import (
        CheckboxWithListOfEmailInfoStrs,
    )
    from ..models.enable_synchronous_delivery_via_smtp_value import (
        EnableSynchronousDeliveryViaSMTPValue,
    )
    from ..models.from_email_and_name_checkbox import FromEmailAndNameCheckbox
    from ..models.graphs_per_notification import GraphsPerNotification
    from ..models.html_section_between_body_and_table_checkbox import (
        HtmlSectionBetweenBodyAndTableCheckbox,
    )
    from ..models.subject_for_host_notifications_checkbox import (
        SubjectForHostNotificationsCheckbox,
    )
    from ..models.subject_for_service_notifications_checkbox import (
        SubjectForServiceNotificationsCheckbox,
    )
    from ..models.to_email_and_name_checkbox import ToEmailAndNameCheckbox


T = TypeVar("T", bound="HTMLMailPluginCreate")


@_attrs_define
class HTMLMailPluginCreate:
    """
    Attributes:
        plugin_name (Any): The HTML mail plug-in. Default: 'mail'. Example: mail.
        from_details (Checkbox | FromEmailAndNameCheckbox | Unset):
        reply_to (Checkbox | ToEmailAndNameCheckbox | Unset):
        subject_for_host_notifications (Checkbox | SubjectForHostNotificationsCheckbox | Unset):
        subject_for_service_notifications (Checkbox | SubjectForServiceNotificationsCheckbox | Unset):
        send_separate_notification_to_every_recipient (Checkbox | Unset):
        sort_order_for_bulk_notifications (Checkbox | CheckboxSortOrderValue | Unset):
        info_to_be_displayed_in_the_email_body (Checkbox | CheckboxWithListOfEmailInfoStrs | Unset):
        insert_html_section_between_body_and_table (Checkbox | HtmlSectionBetweenBodyAndTableCheckbox | Unset):
        url_prefix_for_links_to_checkmk (Checkbox | CheckMKURLPrefixValue | Unset):
        display_graphs_among_each_other (Checkbox | Unset):
        enable_sync_smtp (Checkbox | EnableSynchronousDeliveryViaSMTPValue | Unset):
        graphs_per_notification (Checkbox | GraphsPerNotification | Unset):
        bulk_notifications_with_graphs (BulkNotificationsWithGraphs | Checkbox | Unset):
    """

    plugin_name: Any = "mail"
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
    info_to_be_displayed_in_the_email_body: (
        Checkbox | CheckboxWithListOfEmailInfoStrs | Unset
    ) = UNSET
    insert_html_section_between_body_and_table: (
        Checkbox | HtmlSectionBetweenBodyAndTableCheckbox | Unset
    ) = UNSET
    url_prefix_for_links_to_checkmk: Checkbox | CheckMKURLPrefixValue | Unset = UNSET
    display_graphs_among_each_other: Checkbox | Unset = UNSET
    enable_sync_smtp: Checkbox | EnableSynchronousDeliveryViaSMTPValue | Unset = UNSET
    graphs_per_notification: Checkbox | GraphsPerNotification | Unset = UNSET
    bulk_notifications_with_graphs: BulkNotificationsWithGraphs | Checkbox | Unset = (
        UNSET
    )
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

        info_to_be_displayed_in_the_email_body: dict[str, Any] | Unset
        if isinstance(self.info_to_be_displayed_in_the_email_body, Unset):
            info_to_be_displayed_in_the_email_body = UNSET
        elif isinstance(self.info_to_be_displayed_in_the_email_body, Checkbox):
            info_to_be_displayed_in_the_email_body = (
                self.info_to_be_displayed_in_the_email_body.to_dict()
            )
        else:
            info_to_be_displayed_in_the_email_body = (
                self.info_to_be_displayed_in_the_email_body.to_dict()
            )

        insert_html_section_between_body_and_table: dict[str, Any] | Unset
        if isinstance(self.insert_html_section_between_body_and_table, Unset):
            insert_html_section_between_body_and_table = UNSET
        elif isinstance(self.insert_html_section_between_body_and_table, Checkbox):
            insert_html_section_between_body_and_table = (
                self.insert_html_section_between_body_and_table.to_dict()
            )
        else:
            insert_html_section_between_body_and_table = (
                self.insert_html_section_between_body_and_table.to_dict()
            )

        url_prefix_for_links_to_checkmk: dict[str, Any] | Unset
        if isinstance(self.url_prefix_for_links_to_checkmk, Unset):
            url_prefix_for_links_to_checkmk = UNSET
        elif isinstance(self.url_prefix_for_links_to_checkmk, Checkbox):
            url_prefix_for_links_to_checkmk = (
                self.url_prefix_for_links_to_checkmk.to_dict()
            )
        else:
            url_prefix_for_links_to_checkmk = (
                self.url_prefix_for_links_to_checkmk.to_dict()
            )

        display_graphs_among_each_other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_graphs_among_each_other, Unset):
            display_graphs_among_each_other = (
                self.display_graphs_among_each_other.to_dict()
            )

        enable_sync_smtp: dict[str, Any] | Unset
        if isinstance(self.enable_sync_smtp, Unset):
            enable_sync_smtp = UNSET
        elif isinstance(self.enable_sync_smtp, Checkbox):
            enable_sync_smtp = self.enable_sync_smtp.to_dict()
        else:
            enable_sync_smtp = self.enable_sync_smtp.to_dict()

        graphs_per_notification: dict[str, Any] | Unset
        if isinstance(self.graphs_per_notification, Unset):
            graphs_per_notification = UNSET
        elif isinstance(self.graphs_per_notification, Checkbox):
            graphs_per_notification = self.graphs_per_notification.to_dict()
        else:
            graphs_per_notification = self.graphs_per_notification.to_dict()

        bulk_notifications_with_graphs: dict[str, Any] | Unset
        if isinstance(self.bulk_notifications_with_graphs, Unset):
            bulk_notifications_with_graphs = UNSET
        elif isinstance(self.bulk_notifications_with_graphs, Checkbox):
            bulk_notifications_with_graphs = (
                self.bulk_notifications_with_graphs.to_dict()
            )
        else:
            bulk_notifications_with_graphs = (
                self.bulk_notifications_with_graphs.to_dict()
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
        if info_to_be_displayed_in_the_email_body is not UNSET:
            field_dict["info_to_be_displayed_in_the_email_body"] = (
                info_to_be_displayed_in_the_email_body
            )
        if insert_html_section_between_body_and_table is not UNSET:
            field_dict["insert_html_section_between_body_and_table"] = (
                insert_html_section_between_body_and_table
            )
        if url_prefix_for_links_to_checkmk is not UNSET:
            field_dict["url_prefix_for_links_to_checkmk"] = (
                url_prefix_for_links_to_checkmk
            )
        if display_graphs_among_each_other is not UNSET:
            field_dict["display_graphs_among_each_other"] = (
                display_graphs_among_each_other
            )
        if enable_sync_smtp is not UNSET:
            field_dict["enable_sync_smtp"] = enable_sync_smtp
        if graphs_per_notification is not UNSET:
            field_dict["graphs_per_notification"] = graphs_per_notification
        if bulk_notifications_with_graphs is not UNSET:
            field_dict["bulk_notifications_with_graphs"] = (
                bulk_notifications_with_graphs
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_notifications_with_graphs import BulkNotificationsWithGraphs
        from ..models.check_mkurl_prefix_value import CheckMKURLPrefixValue
        from ..models.checkbox import Checkbox
        from ..models.checkbox_sort_order_value import CheckboxSortOrderValue
        from ..models.checkbox_with_list_of_email_info_strs import (
            CheckboxWithListOfEmailInfoStrs,
        )
        from ..models.enable_synchronous_delivery_via_smtp_value import (
            EnableSynchronousDeliveryViaSMTPValue,
        )
        from ..models.from_email_and_name_checkbox import FromEmailAndNameCheckbox
        from ..models.graphs_per_notification import GraphsPerNotification
        from ..models.html_section_between_body_and_table_checkbox import (
            HtmlSectionBetweenBodyAndTableCheckbox,
        )
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

        def _parse_info_to_be_displayed_in_the_email_body(
            data: object,
        ) -> Checkbox | CheckboxWithListOfEmailInfoStrs | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_email_info_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_email_info_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_email_info_one_of_type_1 = (
                CheckboxWithListOfEmailInfoStrs.from_dict(data)
            )

            return componentsschemas_email_info_one_of_type_1

        info_to_be_displayed_in_the_email_body = (
            _parse_info_to_be_displayed_in_the_email_body(
                d.pop("info_to_be_displayed_in_the_email_body", UNSET)
            )
        )

        def _parse_insert_html_section_between_body_and_table(
            data: object,
        ) -> Checkbox | HtmlSectionBetweenBodyAndTableCheckbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_insert_html_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_insert_html_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_insert_html_one_of_type_1 = (
                HtmlSectionBetweenBodyAndTableCheckbox.from_dict(data)
            )

            return componentsschemas_insert_html_one_of_type_1

        insert_html_section_between_body_and_table = (
            _parse_insert_html_section_between_body_and_table(
                d.pop("insert_html_section_between_body_and_table", UNSET)
            )
        )

        def _parse_url_prefix_for_links_to_checkmk(
            data: object,
        ) -> Checkbox | CheckMKURLPrefixValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_url_prefix_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_url_prefix_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_url_prefix_one_of_type_1 = (
                CheckMKURLPrefixValue.from_dict(data)
            )

            return componentsschemas_url_prefix_one_of_type_1

        url_prefix_for_links_to_checkmk = _parse_url_prefix_for_links_to_checkmk(
            d.pop("url_prefix_for_links_to_checkmk", UNSET)
        )

        _display_graphs_among_each_other = d.pop(
            "display_graphs_among_each_other", UNSET
        )
        display_graphs_among_each_other: Checkbox | Unset
        if isinstance(_display_graphs_among_each_other, Unset):
            display_graphs_among_each_other = UNSET
        else:
            display_graphs_among_each_other = Checkbox.from_dict(
                _display_graphs_among_each_other
            )

        def _parse_enable_sync_smtp(
            data: object,
        ) -> Checkbox | EnableSynchronousDeliveryViaSMTPValue | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_enable_sync_one_of_type_0 = Checkbox.from_dict(data)

                return componentsschemas_enable_sync_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_enable_sync_one_of_type_1 = (
                EnableSynchronousDeliveryViaSMTPValue.from_dict(data)
            )

            return componentsschemas_enable_sync_one_of_type_1

        enable_sync_smtp = _parse_enable_sync_smtp(d.pop("enable_sync_smtp", UNSET))

        def _parse_graphs_per_notification(
            data: object,
        ) -> Checkbox | GraphsPerNotification | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_graphs_per_notification_one_of_type_0 = (
                    Checkbox.from_dict(data)
                )

                return componentsschemas_graphs_per_notification_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_graphs_per_notification_one_of_type_1 = (
                GraphsPerNotification.from_dict(data)
            )

            return componentsschemas_graphs_per_notification_one_of_type_1

        graphs_per_notification = _parse_graphs_per_notification(
            d.pop("graphs_per_notification", UNSET)
        )

        def _parse_bulk_notifications_with_graphs(
            data: object,
        ) -> BulkNotificationsWithGraphs | Checkbox | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_bulk_notifications_one_of_type_0 = Checkbox.from_dict(
                    data
                )

                return componentsschemas_bulk_notifications_one_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_bulk_notifications_one_of_type_1 = (
                BulkNotificationsWithGraphs.from_dict(data)
            )

            return componentsschemas_bulk_notifications_one_of_type_1

        bulk_notifications_with_graphs = _parse_bulk_notifications_with_graphs(
            d.pop("bulk_notifications_with_graphs", UNSET)
        )

        html_mail_plugin_create = cls(
            plugin_name=plugin_name,
            from_details=from_details,
            reply_to=reply_to,
            subject_for_host_notifications=subject_for_host_notifications,
            subject_for_service_notifications=subject_for_service_notifications,
            send_separate_notification_to_every_recipient=send_separate_notification_to_every_recipient,
            sort_order_for_bulk_notifications=sort_order_for_bulk_notifications,
            info_to_be_displayed_in_the_email_body=info_to_be_displayed_in_the_email_body,
            insert_html_section_between_body_and_table=insert_html_section_between_body_and_table,
            url_prefix_for_links_to_checkmk=url_prefix_for_links_to_checkmk,
            display_graphs_among_each_other=display_graphs_among_each_other,
            enable_sync_smtp=enable_sync_smtp,
            graphs_per_notification=graphs_per_notification,
            bulk_notifications_with_graphs=bulk_notifications_with_graphs,
        )

        html_mail_plugin_create.additional_properties = d
        return html_mail_plugin_create

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
