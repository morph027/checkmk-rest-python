from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_webhook_url_option import SlackWebhookURLOption

T = TypeVar("T", bound="SlackWebhookURL")


@_attrs_define
class SlackWebhookURL:
    """
    Attributes:
        option (SlackWebhookURLOption):  Example: store.
        url (str): Configure your Slack or Mattermost Webhook URL here. Slack Webhooks must use HTTPS Example:
            https://example_webhook_url.com.
    """

    option: SlackWebhookURLOption
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = SlackWebhookURLOption(d.pop("option"))

        url = d.pop("url")

        slack_webhook_url = cls(
            option=option,
            url=url,
        )

        slack_webhook_url.additional_properties = d
        return slack_webhook_url

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
