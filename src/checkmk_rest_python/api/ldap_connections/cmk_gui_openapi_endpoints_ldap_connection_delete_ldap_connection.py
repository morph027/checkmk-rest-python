from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_404_default_error import Api404DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.api_412_default_error import Api412DefaultError
from ...models.api_428_default_error import Api428DefaultError
from ...types import Response


def _get_kwargs(
    ldap_connection_id: str,
    *,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/objects/ldap_connection/{ldap_connection_id}".format(
            ldap_connection_id=quote(str(ldap_connection_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_match: str,
) -> Response[
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
]:
    """Delete an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * All of:
         * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
         * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.
        if_match (str):  Example: "a20ceacf346041dc".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        ldap_connection_id=ldap_connection_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_match: str,
) -> (
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
    | None
):
    """Delete an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * All of:
         * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
         * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.
        if_match (str):  Example: "a20ceacf346041dc".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api428DefaultError
    """

    return sync_detailed(
        ldap_connection_id=ldap_connection_id,
        client=client,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_match: str,
) -> Response[
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
]:
    """Delete an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * All of:
         * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
         * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.
        if_match (str):  Example: "a20ceacf346041dc".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api428DefaultError]
    """

    kwargs = _get_kwargs(
        ldap_connection_id=ldap_connection_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_match: str,
) -> (
    Any
    | Api403DefaultError
    | Api404DefaultError
    | Api406DefaultError
    | Api412DefaultError
    | Api428DefaultError
    | None
):
    """Delete an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.edit`: This permission is needed in order to make any changes or perform any actions at
    all. Without this permission, the user is only able to view data, and that only in modules he has
    explicit permissions for.
       * All of:
         * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
         * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.
        if_match (str):  Example: "a20ceacf346041dc".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Api403DefaultError | Api404DefaultError | Api406DefaultError | Api412DefaultError | Api428DefaultError
    """

    return (
        await asyncio_detailed(
            ldap_connection_id=ldap_connection_id,
            client=client,
            if_match=if_match,
        )
    ).parsed
