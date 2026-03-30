from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/domain-types/user_config/collections/all",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api403DefaultError | Api406DefaultError | None:
    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api403DefaultError | Api406DefaultError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api403DefaultError | Api406DefaultError]:
    """Show all users



    This endpoint requires the following permissions:
     * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and <b>Contact
    groups</b>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Api403DefaultError | Api406DefaultError | None:
    """Show all users



    This endpoint requires the following permissions:
     * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and <b>Contact
    groups</b>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api403DefaultError | Api406DefaultError]:
    """Show all users



    This endpoint requires the following permissions:
     * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and <b>Contact
    groups</b>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Api403DefaultError | Api406DefaultError | None:
    """Show all users



    This endpoint requires the following permissions:
     * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and <b>Contact
    groups</b>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
