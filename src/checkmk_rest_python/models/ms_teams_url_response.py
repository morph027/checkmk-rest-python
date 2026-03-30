from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ms_teams_url_response_option import MSTeamsURLResponseOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="MSTeamsURLResponse")


@_attrs_define
class MSTeamsURLResponse:
    """
    Attributes:
        option (MSTeamsURLResponseOption):  Example: store.
        store_id (str): A password store ID Example: stored_password_1.
        url (str | Unset):  Example: http://example_webhook_url.com.
    """

    option: MSTeamsURLResponseOption
    store_id: str
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option = self.option.value

        store_id = self.store_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "option": option,
                "store_id": store_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option = MSTeamsURLResponseOption(d.pop("option"))

        store_id = d.pop("store_id")

        url = d.pop("url", UNSET)

        ms_teams_url_response = cls(
            option=option,
            store_id=store_id,
            url=url,
        )

        ms_teams_url_response.additional_properties = d
        return ms_teams_url_response

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
