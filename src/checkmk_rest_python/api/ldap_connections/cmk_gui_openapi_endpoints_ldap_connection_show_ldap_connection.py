from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_403_default_error import Api403DefaultError
from ...models.api_406_default_error import Api406DefaultError
from ...models.get_ldap_connection_404 import GETLdapConnection404
from ...types import Response


def _get_kwargs(
    ldap_connection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/objects/ldap_connection/{ldap_connection_id}".format(
            ldap_connection_id=quote(str(ldap_connection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Api403DefaultError | Api406DefaultError | GETLdapConnection404 | None:
    if response.status_code == 403:
        response_403 = Api403DefaultError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GETLdapConnection404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = Api406DefaultError.from_dict(response.json())

        return response_406

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Api403DefaultError | Api406DefaultError | GETLdapConnection404]:
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
) -> Response[Api403DefaultError | Api406DefaultError | GETLdapConnection404]:
    """Show an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError | GETLdapConnection404]
    """

    kwargs = _get_kwargs(
        ldap_connection_id=ldap_connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Api403DefaultError | Api406DefaultError | GETLdapConnection404 | None:
    """Show an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError | GETLdapConnection404
    """

    return sync_detailed(
        ldap_connection_id=ldap_connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Api403DefaultError | Api406DefaultError | GETLdapConnection404]:
    """Show an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Api403DefaultError | Api406DefaultError | GETLdapConnection404]
    """

    kwargs = _get_kwargs(
        ldap_connection_id=ldap_connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ldap_connection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Api403DefaultError | Api406DefaultError | GETLdapConnection404 | None:
    """Show an LDAP connection



    This endpoint requires the following permissions:
     * All of:
       * `wato.seeall`: When this permission is set then the user sees also such modules he has no
    explicit access to (see below).
       * `wato.users`: This permission is needed for the modules <b>Users</b>, <b>Roles</b> and
    <b>Contact groups</b>

    Args:
        ldap_connection_id (str):  Example: LDAP_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Api403DefaultError | Api406DefaultError | GETLdapConnection404
    """

    return (
        await asyncio_detailed(
            ldap_connection_id=ldap_connection_id,
            client=client,
        )
    ).parsed
