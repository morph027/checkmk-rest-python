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
from ...models.api_412_default_error import Api412DefaultError
from ...models.api_415_default_error import Api415DefaultError
from ...models.api_428_default_error import Api428DefaultError
from ...models.update_user import UpdateUser
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    body: UpdateUser,
    if_match: str,
    content_type: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/objects/user_config/{username}".format(
            username=quote(str(username), safe=""),
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
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
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

    if response.status_code == 412:
        response_412 = Api412DefaultError.from_dict(response.json())

        return response_412

    if response.status_code == 415:
        response_415 = Api415DefaultError.from_dict(response.json())

        return response_415

    if response.status_code == 428:
        response_428 = Api428DefaultError.from_dict(response.json())

        return response_428

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
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateUser,
    if_match: str,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    """Edit a user

     You can pass custom attributes you defined directly in the top level JSON object of the request.This
    endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        username (str):  Example: cmkuser.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (UpdateUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateUser,
    if_match: str,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
    | None
):
    """Edit a user

     You can pass custom attributes you defined directly in the top level JSON object of the request.This
    endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        username (str):  Example: cmkuser.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (UpdateUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
        if_match=if_match,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateUser,
    if_match: str,
    content_type: str,
) -> Response[
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
]:
    """Edit a user

     You can pass custom attributes you defined directly in the top level JSON object of the request.This
    endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        username (str):  Example: cmkuser.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (UpdateUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
        if_match=if_match,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateUser,
    if_match: str,
    content_type: str,
) -> (
    Api400DefaultError
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api415DefaultError
    | Api428DefaultError
    | None
):
    """Edit a user

     You can pass custom attributes you defined directly in the top level JSON object of the request.This
    endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        username (str):  Example: cmkuser.
        if_match (str):  Example: "a20ceacf346041dc".
        content_type (str):  Example: application/json.
        body (UpdateUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api400DefaultError | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api415DefaultError | Api428DefaultError
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
            if_match=if_match,
            content_type=content_type,
        )
    ).parsed
