from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_400_default_error import Api400DefaultError
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.notification_rule_request import NotificationRuleRequest
from ...types import Response


def _get_kwargs(
    rule_id: str,
    *,
    body: NotificationRuleRequest,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/notification_rule/{rule_id}".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    if response.status_code == 400:
        response_400 = Api400DefaultError.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Api404DefaultError.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationRuleRequest,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update a notification rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * `general.edit_notifications`: This allows a user to edit his personal notification settings.
    You also need the permission <i>Edit the user profile</i> in order to do this.

    Args:
        rule_id (str):  Example: 5425d554-5741-4bbf-b907-1a391dfab5bb.
        content_type (str):  Example: application/json.
        body (NotificationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationRuleRequest,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update a notification rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * `general.edit_notifications`: This allows a user to edit his personal notification settings.
    You also need the permission <i>Edit the user profile</i> in order to do this.

    Args:
        rule_id (str):  Example: 5425d554-5741-4bbf-b907-1a391dfab5bb.
        content_type (str):  Example: application/json.
        body (NotificationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationRuleRequest,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
]:
    """Update a notification rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * `general.edit_notifications`: This allows a user to edit his personal notification settings.
    You also need the permission <i>Edit the user profile</i> in order to do this.

    Args:
        rule_id (str):  Example: 5425d554-5741-4bbf-b907-1a391dfab5bb.
        content_type (str):  Example: application/json.
        body (NotificationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NotificationRuleRequest,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api415DefaultError
    | None
):
    """Update a notification rule



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.see_all_folders`: Users without this permissions can only see folders with a contact
    group they are in.
       * `general.edit_notifications`: This allows a user to edit his personal notification settings.
    You also need the permission <i>Edit the user profile</i> in order to do this.

    Args:
        rule_id (str):  Example: 5425d554-5741-4bbf-b907-1a391dfab5bb.
        content_type (str):  Example: application/json.
        body (NotificationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api415DefaultError
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
